#! -*- coding:utf-8 -*-

import turtle


class TurtlePortal(object):
    @staticmethod
    def draw_colorful_lines(loops):
        colors = ["red", "purple", "blue", "green", "yellow", "orange"]

        turtle.hideturtle()
        turtle.screensize(800, 800, "black")

        for i in range(loops):
            turtle.pencolor(colors[i % 6])
            turtle.pensize(i//300 + 1)
            turtle.forward(i)
            turtle.right(59)

        turtle.exitonclick()


if __name__ == "__main__":
    tp = TurtlePortal
    tp.draw_colorful_lines(360)