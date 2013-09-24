class BinaryPlusOne(object):
    @staticmethod
    def add_one(num):
        """Pass in an array representing an array of bits."""        
        bitIndex = len(num) - 1
        
        while (True):
            if (num[bitIndex] == 0):
                num[bitIndex] = 1
                break
            else:
                num[bitIndex] = 0

            bitIndex -= 1
