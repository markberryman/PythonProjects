import sorter


class MergeSortSorter(sorter.Sorter):
    """Sorter using merge sort algorithm.
    Note - merge sort is not an in-place sort.
    It returns a sorted list."""
    def sort_words(self, wordTuples):
        # base case to return is list of size one
        if (len(wordTuples) == 1):
            return wordTuples
        else:
            splitIdx = len(wordTuples) // 2
            firstHalf = wordTuples[:splitIdx]
            secondHalf = wordTuples[splitIdx:]
            l1 = self.sort_words(firstHalf)
            l2 = self.sort_words(secondHalf)
            return self.merge(l1, l2)
        
    def merge(self, list1, list2):
        list1Idx = 0
        list2Idx = 0
        result = []

        while ((list1Idx < len(list1)) and
               (list2Idx < len(list2))):
            if (list1[list1Idx] < list2[list2Idx]):
                result.append(list1[list1Idx])
                list1Idx += 1
            else:
                result.append(list2[list2Idx])
                list2Idx += 1

        # at this point, at least one of the lists
        # has been fully traversed; append the
        # remaining elements of the other list
        if (list1Idx == len(list1)):
            result.extend(list2[list2Idx:])
        else:
            result.extend(list1[list1Idx:])

        return result

#def mergeSort(list):
#    if (len(list) == 1):
#        return list

#    splitIndex = len(list) // 2
#    list1 = list[:splitIndex]
#    list2 = list[splitIndex:]

#    return mergeSortSorter(mergeSort(list1), mergeSort(list2))

#def mergeSortSorter(list1, list2):
#    list1Index = 0
#    list2Index = 0

#    newList = []

#    lengthList1 = len(list1)
#    lengthList2 = len(list2)

#    while ((list1Index < lengthList1) and (list2Index < lengthList2)):
#        if (list1[list1Index][0] < list2[list2Index][0]):
#            newList.append(list1[list1Index])
#            list1Index += 1
#        else:
#            newList.append(list2[list2Index])
#            list2Index += 1
            
#    if (list1Index < lengthList1):
#        newList.extend(list1[list1Index:])
#    else:
#        newList.extend(list2[list2Index:])

#    return newList
