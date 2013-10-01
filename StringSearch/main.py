import rabinKarp
import time


algo = rabinKarp.RabinKarp()
s1 = "ABC"
s2 = "1234567890ABC"
numIters = 100000

time.clock()

for x in range(numIters):
    algo.contains_string(s1, s2)

timeRK = time.clock()

#for x in range(numIters):
#    s1 in s2

#timeBuiltInStringSearch = time.clock() - timeRK

#print("RK time: " + str(timeRK))
#print("Built-in algo time: " + str(timeBuiltInStringSearch))
#print()
#print("Comparison (RK / Built-in): " + str((timeRK / timeBuiltInStringSearch)))

#input("Done")
