# https://leetcode.com/problems/jump-game/submissions/


# Medium


class Solution:
    def canJump(self, A):
        n = len(A)
        last = n-1
        for i  in range(n-2)[::-1]:
            if (i+A[i] >= last):
                last = i
        return last<=0


if __name__ == '__main__':
    n = 10
    for i  in range(n-2)[::-1]:
        print (i)

