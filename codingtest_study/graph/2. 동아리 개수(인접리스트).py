def solution(n, edges):
    # 인접 리스트
    graph = [[] for _ in range(n + 1)]
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # print(graph)

    visited = [False] * (n + 1)
    answer = 0
    for student in range(1, n + 1):
        if not visited[student]: # 1번째, 2번째, 3번째
            lst = [student] # 방문 안되있는(연결 안되있는 것만 확인)
            visited[student] = True
            
            while lst: # 리스트 빌 때까지 하기()
                cur = lst.pop(0) # 앞에 있는거 꺼내기
                # 연결된 친구들 확인
                for friend in graph[cur]: # 예를 들어 첫번째는 2,4,5
                    if not visited[friend]: # visited[2], visited[4], visited[5]
                        visited[friend] = True # 방문처리 안되있으면 방문처리하고
                        lst.append(friend) # 리스트에 넣어 주기
            answer += 1

    return answer


print(solution(10, [[1, 2], [2, 3], [1, 4], [1, 5], [6, 8], [7, 8], [9, 10]]))
print(solution(20, [[1, 2], [2, 5], [5, 7], [9, 7], [5, 13], [15, 13], [3, 4], [4, 6], [6, 8], [8, 10], [11, 12], [14, 16], [16, 17], [17, 18], [19, 20]]))
print(solution(7, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
print(solution(30, [[5, 6], [6, 7]]))

