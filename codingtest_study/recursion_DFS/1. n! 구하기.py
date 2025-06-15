def DFS(n):
    if n == 0:
        return 1
    else:
        return n * DFS(n-1)

print(DFS(5))             
print(DFS(6))

"""재귀 흐름 예씨
DFS(5)
→ 5 * DFS(4)
→ 5 * (4 * DFS(3))
→ 5 * (4 * (3 * DFS(2)))
→ 5 * (4 * (3 * (2 * DFS(1))))
→ 5 * (4 * (3 * (2 * (1 * DFS(0)))))
→ 5 * 4 * 3 * 2 * 1 * 1 = 120
"""