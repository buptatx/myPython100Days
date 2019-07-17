#! -*- coding:utf-8 -*-

class SortTest(object):
    @staticmethod
    def select_sorted(origin_items, comp= lambda x,y:x<y):
        #选择排序 时间复杂度 O(n**2)
        items = origin_items[:]
        for i in range(len(items) - 1):
            #设置游标 当前元素
            min_index = i
            #遍历当前元素的下一个元素到最后一个元素
            #一轮遍历，筛选出列表中最小的元素 和 当前的游标指向的元素交换
            for j in range(i+1, len(items)):
                #如果下一个元素比当前元素小，则重新赋值min_index
                if comp(items[j], items[min_index]):
                    min_index = j

            items[i], items[min_index] = items[min_index], items[i]

        return items

    @staticmethod
    def bubble_sorted(origin_items, comp=lambda x,y:x<y):
        items = origin_items[:]
        size = len(items)
        for i in range(size):
            #当前元素 与 它之后的其他元素对比
            #如果它后面的元素比它大，则互换
            #每次遍历会筛选出剩余元素中最大的
            #结果列表为从大到小的降序排列
            for j in range(i+1, size):
                if comp(items[i], items[j]):
                    items[i], items[j] = items[j], items[i]

        return items

    @staticmethod
    def merge_sorted(items, cmp=lambda x,y:x<=y):
        if len(items) < 2:
            return items[:]
        mid = len(items)//2
        left = SortTest.merge_sorted(items[:mid], cmp)
        right = SortTest.merge_sorted(items[mid:], cmp)
        return SortTest.merge(left, right, cmp)

    @staticmethod
    def merge(items1, items2, cmp):
        items = []
        idx1, idx2 = 0, 0
        while idx1<len(items1) and idx2<len(items2):
            if cmp(items1[idx1], items2[idx2]):
                items.append(items1[idx1])
                idx1 += 1
            else:
                items.append(items2[idx2])
                idx2 += 1
        items += items1[idx1:]
        items += items2[idx2:]
        return items

if __name__ == "__main__":
    test_data = [1, 4, 3, 2, 7, 9, 8, 21, 11]
    res = SortTest.bubble_sorted(test_data)
    print(res)
    res = SortTest.merge_sorted(test_data)
    print(res)