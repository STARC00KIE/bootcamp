import sys

N, D = map(int, sys.stdin.readline().split()) # 지름길의 개수, 고속도로의 길이
inf = float('inf')

graph = [[] for _ in range(D+1)] # 그래프 초기화, 거리는 무조건 양의 정수수
distance = [inf] * (D+1) # 다익스트라의 시작 0 ~150
for i in range(D): # 만약 D가 150이면
    # 그래프 리스트 구조: 그래프[시작점] = [(목적지, 가중치)]
    graph[i].append((i+1, 1)) # 1부터 150까지 graph[i]에 append

for _ in range(N):
    # 줄 읽어와서 split, int
    # 시작, 목적지, 가중치(지름길의 길이)
    start, end, length = map(int, sys.stdin.readline().split())

    # 만약 목적지보다 시작점이 작으면 graph 리스트에 추가함
    # 반대면 추가하지 않음
    if end <= D:
        graph[start].append((end, length))

# 우선순위 큐
# 다익스트라 알고리즘 시작
Q = []
heapq.heappush(Q, (0, 0)) # 시작점은 0, 거리는 0
distance[0] = 0 # 시작점 0, 거리 0

while Q: # 큐가 빌 때까지 반복
    d1, u = heapq.heappop(Q) # 처음에는 시작점 0, 거리 0부터 시작

    # graph[0]은 (1,1) 이렇게 되어있음음
    for v, d2 in graph[u]: # 현재 노드 u에서 갈 수 있는 모든 노드 v와 거리 d2, 처음에는 그래프 0에서 가져옴
        cost = distance[u] + d2  # 거리 더해서
        if cost < distance[v]: # 만약 거리가 더 작으면
            distance[v] = cost # 거리 업데이트
            heapq.heappush(Q, (cost, v)) # 큐에 추가

print(distance[D]) # 150까지 가는 최단 거리 출력