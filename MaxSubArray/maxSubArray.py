class MaxSubArray(object):
    """Return the max sub-array value for an array of integers."""
    @staticmethod
    def calc(data):
        # track the max sub-array values and
        # the max sub-array ending at a specific location
        maxEndingHere = 0
        maxValue = 0
        # track the indices corresponding to the
        # sub-array; basically resets whenever the max value
        # for a specific location is set to 0 (i.e., it's zero or
        # less than zero)
        maxValueStartIdx = None
        maxValueEndIdx = None
        tempMaxValueStartIdx = None
        tempMaxValueEndIdx = None

        for i in range(len(data)):
            tempMaxEndingHere = maxEndingHere + data[i]

            if (tempMaxEndingHere > 0):
                maxEndingHere = tempMaxEndingHere

                if (tempMaxValueStartIdx is None):
                    tempMaxValueStartIdx = i
                    
                tempMaxValueEndIdx = i
            else:
                maxEndingHere = 0
                # reset tracking indices; bounced on a zero value
                tempMaxValueStartIdx = None
                # might not need the following statement
                tempMaxValueEndIdx = None

            if (maxEndingHere > maxValue):
                maxValue = maxEndingHere

                maxValueStartIdx = tempMaxValueStartIdx
                maxValueEndIdx = tempMaxValueEndIdx

        print("Index range is {} to {}".format(maxValueStartIdx, maxValueEndIdx))

        return maxValue

print(MaxSubArray.calc([-3,4,-1,2,1,-5,4,-100,100]))

input("Enter to exit")