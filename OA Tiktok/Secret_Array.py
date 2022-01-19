# https://leetcode.com/discuss/interview-question/1332322/amazon-online-assessment-july-2021-secret-array

# Medium

def countAnalogousArrays(consecutiveDifference , lowerBound , upperBound):

    maxdiff = float('-inf')
    mindiff = float('inf')
    runningsum = 0
    if len(consecutiveDifference) == 0:
        return 0

    if upperBound < lowerBound :
        return 0

    for diff in consecutiveDifference:
        runningsum+=diff
        if runningsum > maxdiff:
            maxdiff = runningsum

        if runningsum < mindiff:
            mindiff = runningsum

    maxvalidupperbound = upperBound + mindiff if upperBound+mindiff < upperBound else upperBound
    minvalidlowerbound = lowerBound + maxdiff if lowerBound + maxdiff > lowerBound else lowerBound

    if maxvalidupperbound >= minvalidlowerbound:
        return maxvalidupperbound - minvalidlowerbound + 1
    else:
        return 0