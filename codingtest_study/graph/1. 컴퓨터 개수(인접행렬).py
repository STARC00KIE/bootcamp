def solution(n, edges):
    lst = [1]

    graph = [[0] * (n+1) for _ in range(n+1)]
    for a, b in edges:
        graph[a][b] = 1
        graph[b][a] = 1
    print(graph)

    visited = [False] * (n + 1)
    visited[1] = True

    while lst:
        cur = lst.pop(0)
        for l in range(1, n + 1):  # 노드 번호를 직접 순회
            if graph[cur][l] == 1 and not visited[l]: # 방문 안했고, 1과 연결되 있으면
                visited[l] = True
                lst.append(l)

    return visited.count(False) - 1  # 0번 인덱스 제외


print(solution(11, [[1, 2], [1, 4], [2, 3], [4, 5], [5, 6], [7, 8], [7, 10], [8, 9], [10, 11]]))
print(solution(12, [[1, 2], [1, 7], [1, 8], [1, 6], [8, 11], [11, 12]]))
print(solution(14, [[1, 6], [1, 5], [6, 7], [7, 8], [9, 8], [3, 4], [4, 14]]))
print(solution(15, [[1, 4], [1, 5], [9, 5], [9, 6], [7, 9], [7, 14]]))