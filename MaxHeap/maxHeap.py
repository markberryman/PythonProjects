class MaxHeap(object):
    """Binary max-heap."""
    def __init__(self, data=[]):
        """Data is an array of unordered integers."""
        self.__data = data

    @property
    def data(self):
        return self.__data

    def add_data(self, item):
        """Add a new item to the heap and re-orders node
        to satisfy max-heap property."""
        self.__data.append(item)

        parentIdx = MaxHeap.get_parentIdx(len(self.__data))

        # repeat until we hit the root
        while (parentIdx != 0):
            self.max_heapify(parentIdx)
            parentIdx = MaxHeap.get_parentIdx(parentIdx)

    @staticmethod
    def get_parentIdx(i):
        """Gets parent index of "i" element. "i" is 1-based."""
        return int(i / 2)

    @staticmethod
    def get_childIdx(i, dir):
        """Returns array index of child of "i" element. "i" is 1 based.
        Dir 0 means left. 1 means right."""
        if (dir == 0):
            return 2 * i
        else:
            return (2 * i) + 1

    def max_heapify(self, i):
        """Orders the data to satisfy the max-heap property:
        Value of parent node >= value of child nodes.
        Once we've done this, we can employ heap sort.
        Parameter 'i' is the starting index ot begin the "heapfication"."""
        lChildIdx = MaxHeap.get_childIdx(i, 0)
        rChildIdx = MaxHeap.get_childIdx(i, 1)
        largestIdx = i

        # for element at 'i', see if either "child" is greater (i.e., voilates
        # the max-heap property)

        # index check is to prevent us from going out of bounds
        # w/ the array and will cause largestIdx == i when we
        # do which means we won't recurse
        if ((lChildIdx <= len(self.data)) and 
            (self.__data[lChildIdx - 1] > self.__data[i - 1])):
            largestIdx = lChildIdx
        else:
            largestIdx = i

        if ((rChildIdx <= len(self.data)) and 
            (self.__data[rChildIdx - 1] > self.__data[largestIdx - 1])):
            largestIdx = rChildIdx

        # need to swap values?
        if (largestIdx != i):
            temp = self.__data[i - 1]
            self.__data[i - 1] = self.__data[largestIdx - 1]
            self.__data[largestIdx - 1] = temp

            # we need to max_heapify the child element we swapped
            self.max_heapify(largestIdx)

    def heap_sort(self):
        """Heap sort!"""
        sortedArray = []
        lastSortedIdx = len(self.__data)

        print("Initial  heap: {}".format(self.__data))

        # build sorted array by whacking elements from
        # the end of the heap
        while (len(self.__data) > 0):
            # place largest element (root) in sorted array
            # swap last element in heap w/ root
            sortedArray.append(self.__data[0])
            self.__data[0] = self.__data[len(self.__data) - 1]
            # delete the last element in the heap which is
            # now in the sorted array
            self.__data.pop()

            # max-heapify at the root; ensures largest # is at root
            # 1 based indexing
            self.max_heapify(1)

            print("Heap: {}".format(self.__data))
            print("Sorted array: {}".format(sortedArray))

        sortedArray.reverse()

        return sortedArray
