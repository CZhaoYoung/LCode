
# comments on solution 2
# nums is an empty dic at first. The first num in the result will be mismatched.
# And then the second on will be matched
def Solution2(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []

# comments
# preprocess the input may reduce the time complexity
# sth like the union find in MST. Sorting the edge in advance will reduce Kruskal algorithm to O(nlog(n))
def Solution3(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right += 1
    return []


def twoNumberSum(array, targetSum):
    # O(n^2)time | O(1) space
    for i in range(len(array)-1):
        firstSum = array[i]
        for j in range(i+1, len(array)):
            secondSum = array[j]
            if firstSum + secondSum == targetSum:
                return [firstSum, secondSum]

    # else return empty set
    return []


if __name__ == '__main__':
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10
    print(Solution3(array, targetSum))
    print(2)