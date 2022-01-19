# https://leetcode.com/discuss/interview-question/374446/twitter-oa-2019-efficient-job-processing-service

# dynamic programming

# medium

def maximumTotalWeight(tasks, weights, runningtime):
    items = [[tasks[i] * 2, weights[i]] for i in range(len(tasks))]

    res = [[0 for _ in range(runningtime + 1)] for _ in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        duration, value = items[i - 1]
        for d in range(1, runningtime + 1):
            if duration > d:
                res[i][d] = res[i - 1][d]
            else:
                # 用之前的task + 现在的task weight
                res[i][d] = max(res[i - 1][d], res[i-1][d-duration]+value)
    return res


if __name__ == '__main__':
    runningtime = 9
    weights = [3, 2, 2]
    tasks = [3, 2, 2]
    output= maximumTotalWeight(tasks, weights, runningtime)
