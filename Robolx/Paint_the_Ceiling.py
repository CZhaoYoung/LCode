# https://leetcode.com/discuss/interview-question/892579/paint-the-ceiling-swe-hackerrank-test


def get_pair(n, s0, k, b, m, a):
    s = [s0, ]

    for i in range(1, n):
        x = ((k * s[i - 1] + b) % m) + 1 + s[i - 1]
        s.append(x)

    start = 0
    end = n - 1
    count = 0
    while start < end:
        if s[start] * s[end] <= a:
            count += (end - start) * 2
            start += 1
        else:
            end -= 1

    for i in range(n):
        if s[i] * s[i] <= a:
            count += 1
        else:
            break

    return count