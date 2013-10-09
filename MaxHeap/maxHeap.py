# todo - write code to build heap
# todo - implement heapsort

class MaxHeap(object):
    """Binary max-heap."""
    def __init__(self, data=[]):
        """Data is an array of unordered integers."""
        self.__data = data

    @property
    def data(self):
        return self.__data

    def add_data(self, item):
        """Add a new item to the heap."""
        # item goes on end of data array
        self.__data.append(item)
        # max-heapify the parent of this new item
        # recurse until we hit the root

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
