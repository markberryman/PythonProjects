class QuickSort(object):
    @staticmethod
    def swap_data(data, idx1, idx2):
        """Swap two elements."""
        temp = data[idx1]
        data[idx1] = data[idx2]
        data[idx2] = temp

    @staticmethod
    def partition(data, leftIdx, rightIdx, pIdx):
        """Partitions block of data around a pivot. When
        done, data to left of pivot is less than pivot
        and data to the right is greater."""
        storeIdx = leftIdx  # tracks idx of value
                            # larger than the pivot

        if (len(data) >= 2):
            pivotVal = data[pIdx]

            # push pivot to end
            QuickSort.swap_data(data, pIdx, rightIdx)

            # look at all values starting at left up to end - 1
            # note, we don't minus 1 though b/c range needs to
            # +1 to be inclusive
            for i in range(leftIdx, rightIdx):
                if (data[i] < pivotVal):
                    # upon finding a value less than the pivot
                    # we can swap that w/ the first value we
                    # found that was greater than the pivot
                    QuickSort.swap_data(data, i, storeIdx)

                    storeIdx += 1
                    
            # finally, replace the pivot w/ the first value
            # we found to be larger than it
            QuickSort.swap_data(data, storeIdx, rightIdx)

        # return the storeIdx so we know where the pivot landed
        return storeIdx

    @staticmethod
    def sort(data, leftIdx, rightIdx):
        # terminating case
        if (rightIdx <= leftIdx):
            return

        # bit more complicated pIdx calc here to prevent
        # integer overflow scenario
        pIdx = int((rightIdx - leftIdx) / 2) + leftIdx
        # partition the data around a pivot
        pIdx = QuickSort.partition(data, leftIdx, rightIdx, pIdx)
        # sort the data left of the pivot
        QuickSort.sort(data, leftIdx, pIdx  - 1)
        # sort the data right of the pivot
        QuickSort.sort(data, pIdx + 1, rightIdx)
