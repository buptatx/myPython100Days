import heapq

def small_large():
    portfolio = [ {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65} ]
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
    print(cheap)
    print(expensive)

    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(min(nums))
    print(max(nums))

    heap_list = list(nums)
    heapq.heapify(heap_list)
    print(heap_list)
    print(heapq.heappop(list(heap_list)))
    #list pop
    print(heap_list.pop())
    print(heap_list)
    print(heap_list.pop(-2))


class Priority():
    def __init__(self):
        self.queue = []
        self.index = 0

    def push(self, item, priority):
        heapq.heappush(self.queue, (-priority, self.index, item))
        self.index += 1
        print(self.queue)

    def pop(self):
        return heapq.heappop(self.queue)[-1]


class Item():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item{!r}".format(self.name)


def test_heap_priority():
    q = Priority()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)

    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())

if __name__ == "__main__":
    small_large()
    test_heap_priority()