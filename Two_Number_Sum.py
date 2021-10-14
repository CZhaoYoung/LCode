
def Solution2(array, targetSum):
    nums = {}
    for num in array:
        secondSum = targetSum - num
        if secondSum in nums:
            return [secondSum, num]
        else:
            nums[num] = True
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
    print(twoNumberSum(array, targetSum))