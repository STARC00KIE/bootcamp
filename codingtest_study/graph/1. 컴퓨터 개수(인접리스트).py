def solution(n, edges):
    lst = [1]
    
    graph = [[] for _ in range(n+1)]
    for [a, b] in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # 방문여부 확인할 수 있는 
    visited = [False] * (n + 1)
    lst.append(1) # 1번 -> 컴퓨터부터 시작해서 연결되어 있는 노드들 다 체크
    # 방문처리
    visited[1] = True
    
    while lst:
        cur = lst.pop(0)
        for l in graph[cur]:
            if not visited[l]:
                visited[l] = True
                lst.append(l)
    
    return visited.count(False) - 1  # 0번 인덱스 제외
                    

print(solution(11, [[1, 2], [1, 4], [2, 3], [4, 5], [5, 6], [7, 8], [7, 10], [8, 9], [10, 11]]))
print(solution(12, [[1, 2], [1, 7], [1, 8], [1, 6], [8, 11], [11, 12]]))
print(solution(14, [[1, 6], [1, 5], [6, 7], [7, 8], [9, 8], [3, 4], [4, 14]]))
print(solution(15, [[1, 4], [1, 5], [9, 5], [9, 6], [7, 9], [7, 14]]))

