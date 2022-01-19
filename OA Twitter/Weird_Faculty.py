# https://leetcode.com/discuss/interview-question/374440/Twitter-or-OA-2019-or-Weird-Faculty

# Easy

def Weird_Faculty(v):
    n = len(v)
    # Convert all the zeros to -1 as
    # the zero gives us the negative score of -1
    for i in range(n):
        if not v[i]:
            v[i] = -1

    # Find the total sum

    totalSum = sum(v)
    currSum = 0

    # Find the point where current sum is
    # greater than the total sum

    for i in range(n):
        if currSum > totalSum:
            return i
        currSum += v[i]
        totalSum -= v[i]
    return n

if __name__ == '__main__':
    case1 = [1, 0, 0, 1, 0]
    print(Weird_Faculty(case1))