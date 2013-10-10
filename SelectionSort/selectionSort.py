class SelectionSort(object):
    @staticmethod
    def sort(data):
        for i in range(len(data)):
            smallestValueIdx = i

            for j in range(i, len(data)):
                # find smallest value
                if (data[j] < data[smallestValueIdx]):
                    smallestValueIdx = j
                
            # swap
            temp = data[i]
            data[i] = data[smallestValueIdx]
            data[smallestValueIdx] = temp
