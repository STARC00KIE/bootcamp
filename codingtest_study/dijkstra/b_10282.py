import sys
import heapq

n = int(sys.stdin.readline()) 
for _ in range(n): # 테스트 케이스의 개수
    n, d, c = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b].append((a, s))
    
    dist = [float('inf')] * (n + 1)
    dist[c] = 0
    H = [(0, c)]

    while H:
        time, node = heapq.heappop(H)
        if dist[node] < time:
            continue
        for next_node, cost in graph[node]:
            new_time = time + cost
            if dist[next_node] > new_time:
                dist[next_node] = new_time
                heapq.heappush(H, (new_time, next_node))
    result = dist # 

    infected = [time for time in result if time != float('inf')] # 감염된 컴퓨터의 개수
    print(len(infected), max(infected)) # 출력은 감염된 컴퓨터의 개수, 걸리는 시간
