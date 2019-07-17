#! -*- coding:utf-8 -*-

class SearchTest(object):
    @staticmethod
    def seq_search(items, key):
        #遍历列表元素，如果相同则返回索引
        #enumerate将列表调整为 （索引，元素）的列表
        for index, item in enumerate(items):
            if item == key:
                return index
        else:
            return -1

    @staticmethod
    def binary_search_exists(items, key):
        #迭代
        #分而治之 如果中位数比要校验的元素小，则用右侧列表元素继续对比
        #如果中位数比要校验的元素大，则使用左侧列表元素对比
        #需要考虑列表是否已经为空
        #返回True 如果命中元素 返回False未命中元素
        if len(items) < 1:
            return False

        low, high = 0, len(items)-1
        mid = (low+high)//2

        if items[mid] == key:
            return True
        elif items[mid] < key:
            return SearchTest.binary_search_exists(items[mid+1:], key)
        elif items[mid] > key:
            return SearchTest.binary_search_exists(items[:mid], key)

    @staticmethod
    def binary_search_position(items, key):
        #中位元素与要校验的元素做对比
        #如果中位元素大 则将high改为中位索引-1
        #如果中位元素小 则将low改为中位索引+1
        #循环条件low<=high
        low, high = 0, len(items)-1
        mid = (low + high)//2

        while low <= high:
            if items[mid] == key:
                return mid
            elif items[mid] < key:
                low = mid + 1
            else:
                high = mid - 1

            mid = (low + high)//2

        return -1


if __name__ == "__main__":
    test_data = [1, 4, 3, 2, 7, 9, 8, 21, 11]
    print(SearchTest.seq_search(test_data, 88))
    print(SearchTest.seq_search(test_data, 8))

    test_data = [1, 3, 4, 7, 8, 12, 14, 20, 88]
    print(SearchTest.binary_search_exists(test_data, 88))
    print(SearchTest.binary_search_exists(test_data, 7))
    print(SearchTest.binary_search_exists(test_data, 1))
    print(SearchTest.binary_search_exists(test_data, 13))

    print(SearchTest.binary_search_position(test_data, 88))
    print(SearchTest.binary_search_position(test_data, 7))
    print(SearchTest.binary_search_position(test_data, 1))
    print(SearchTest.binary_search_position(test_data, 13))