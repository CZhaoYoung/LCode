# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

# Medium

# 比较简单，记录每个字母出现的次数，然后比较
import collections

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = collections.Counter(s)
        res = 0
        for c in t:
            if count[c] > 0:
                count[c] -= 1
            else:
                res += 1
        return res

