class InsertionSort(object):
    @staticmethod
    def find_insert_index(data, item):
        i = 0

        while ((i < len(data)) and 
               (item > data[i])):
            i += 1

        return i

    @staticmethod
    def insert(data, item):
        """Inserts item in ordered list, preserving order."""
        idxToPlace = InsertionSort.find_insert_index(data, item)

        # grow data by 1 element
        data.append(0)

        i = len(data) - 1

        while (i > idxToPlace):
            data[i] = data[i - 1]
            i -= 1

        data[idxToPlace] = item


    @staticmethod
    def sort(data):
        newData = []

        # start w/ the first element going into newData
        newData.append(data[0])

        # look at each item in data
        # place at correct location in newData
        # bumping elements up as needed
        for dataIdx in range(1, len(data)):
            valToInsert = data[dataIdx]

            InsertionSort.insert(newData, valToInsert)

        return newData
