# https://leetcode.com/discuss/interview-question/406638/Twitter-or-OA-2019-or-Balanced-Sales-Array

# easy


def balancedSum(sales):
    ls = 0
    l_arr = []
    r_arr = []

    ts = sum(sales)

    for i in range(len(sales)):
        ls = ls + sales[i]
        l_arr.append(ls - sales[i])
        r_arr.append(ts - l_arr[i] - sales[i])

    for i in range(len(sales)):
        if l_arr[i] == r_arr[i]:
            return i
            break