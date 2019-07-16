#! -*- coding:utf-8 -*-

from PIL import Image, ImageFilter
import os

class PilTest(object):
    def __init__(self, filename):
        if os.path.exists(filename):
            self._image = Image.open(filename)
        else:
            print("%s not exist" % filename)

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, filename):
        if os.path.exists(filename):
            self._image = Image.open(filename)
        else:
            print("%s not exist" % filename)

    def test_pillow_size(self):
        #打印图片格式 jpeg jpg png
        print(self._image.format)
        #打印图片大小 长*宽
        print(self._image.size)
        #打印图片 颜色模式 RGB
        print(self._image.mode)

    def test_cut(self):
        #image.show()展示图片
        #image.crop()裁剪
        rect = 80, 20, 310, 360
        self._image.crop(rect).show()

    def test_thumbnail(self):
        #生成缩略图
        size = 70, 47
        self._image.thumbnail(size)
        self._image.show()

    def test_rotate(self):
        #旋转图片
        self._image.rotate(180).show()

    def test_transpose(self):
        #镜像
        self._image.show()
        #左右镜像
        self._image.transpose(Image.FLIP_LEFT_RIGHT).show()
        #上下镜像
        self._image.transpose(Image.FLIP_TOP_BOTTOM).show()

    def test_filter(self):
        self._image.filter(ImageFilter.CONTOUR).show()


if __name__ == "__main__":
    pt = PilTest("../data/ban.jpeg")
    pt.test_pillow_size()
    #pt.test_thumbnail()
    pt.test_cut()
    pt.test_rotate()
    pt.test_transpose()
    pt.test_filter()