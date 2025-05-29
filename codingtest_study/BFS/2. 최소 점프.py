# continue: 이번 반복만 건너뛰고 넘어감

from collections import deque
def BFS(home): # +1 -1 +5
    Q = deque()
    Q.append(0)
    visited = set()
    visited.add(0)
    L = 0
    while Q:
        n = len(Q)
        # print(n)
        for _ in range(n):
            v = Q.popleft()

            for nv in (v-1, v+1, v+5): 
                if nv < 0 or nv > 10000:
                    continue
                if nv == home:
                    return L + 1
                if nv not in visited:
                    visited.add(nv)
                    Q.append(nv)
                
        # print(Q)
        L += 1

print(BFS(10))
print(BFS(14))
print(BFS(25))
print(BFS(24))
print(BFS(345))