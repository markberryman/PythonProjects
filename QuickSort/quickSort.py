class QuickSort(object):
    @staticmethod
    def swap_data(data, idx1, idx2):
        """Swap two elements."""
        temp = data[idx1]
        data[idx1] = data[idx2]
        data[idx2] = temp

    @staticmethod
    def partition(data, left, right, pIdx):
        """Partitions block of data around a pivot. When
        done 
        Takes data and a pivot index and returns the data
        such that all values to the left of the pivot index
        are less than or equal to the pivot and all values
        to the right are greater than the pivot."""
        if (len(data) >= 2):
            pivotVal = data[pIdx]

            # push pivot to end
            QuickSort.swap_data(data, pIdx, len(data) - 1)

            storeIdx = left # idx tracking the first value
                            # that's larger than the pivot
                            # in the data

            # look at all values starting at left up to end - 1
            # note, we don't minus 1 though b/c range needs to
            # +1 to be inclusive
            for i in range(left, right):
                if (data[i] < pivotVal):
                    # upon finding a value less than the pivot
                    # we can swap that w/ the first value we
                    # found that was greater than the pivot
                    QuickSort.swap_data(data, i, storeIdx)

                    storeIdx += 1
                    
            # finally, replace the pivot w/ the last value
            # we found to be larger than it
            QuickSort.swap_data(data, storeIdx, len(data) - 1)


    @staticmethod
    def sort():
        pass