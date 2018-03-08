'''
https://leetcode.com/problems/course-schedule/discuss/58586/Python-20-lines-DFS-solution-sharing-with-explanation
'''


def canFinish(n, pres):
    from collections import deque
    ind = [[] for _ in range(n)]  # indegree
    oud = [0] * n  # outdegree
    for p in pres:
        oud[p[0]] += 1
        ind[p[1]].append(p[0])
    dq = deque()
    for i in range(n):
        if oud[i] == 0:
            dq.append(i)
    k = 0

    print('indeg: ' + str(ind))
    print('outdeg: ' + str(oud))
    while dq:
        x = dq.popleft()
        k += 1
        for i in ind[x]:
            oud[i] -= 1
            if oud[i] == 0:
                dq.append(i)
    return k == n

if __name__ == "__main__":
    print(canFinish(2, [[1,0]]))
    print(canFinish(2, [[1,0],[0,1]]))