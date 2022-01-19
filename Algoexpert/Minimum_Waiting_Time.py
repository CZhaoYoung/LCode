def minimumWaitingTime(queries):
    queries.sort()
    totalWaitingTime = 0
    for idx, duration in enumerate(queries):
        count = len(queries) - (idx+1)
        totalWaitingTime += duration * count

    return totalWaitingTime

def solution2(queries):
    queries.sort(reverse=True)
    totalWaitingTime = 0
    for idx in range(len(queries)):
        duration = queries[idx]
        totalWaitingTime += duration * idx
    return totalWaitingTime



if __name__ == '__main__':
    queries = [3, 2, 1, 2, 6]
    print(solution2(queries))
