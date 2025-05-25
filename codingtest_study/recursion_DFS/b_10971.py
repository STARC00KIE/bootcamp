# 도시의 개수 입력 받기
n = int(input())

# 비용 행렬 입력 받기 (2차원 리스트)
W = [list(map(int, input().split())) for _ in range(n)]

# 각 도시 방문 여부를 저장할 리스트
visited = [False] * n

# 최소 비용을 저장할 변수 (처음엔 아주 큰 수로 설정)
min_cost = int(1e9)

# 깊이 우선 탐색 함수 정의
# city: 현재 도시
# count: 방문한 도시 수
# cost: 지금까지 사용한 비용
def DFS(city, count, cost):
    global min_cost

    # 모든 도시를 방문한 경우
    if count == n:
        # 출발 도시(0번)로 돌아갈 수 있는 경우만 고려
        if W[city][0] != 0:
            # 최소 비용 갱신
            min_cost = min(min_cost, cost + W[city][0])
        return

    # 다음 도시를 하나씩 탐색
    for next_city in range(n):
        # 아직 방문하지 않았고, 현재 도시에서 갈 수 있는 도시인 경우
        if not visited[next_city] and W[city][next_city] != 0:
            visited[next_city] = True  # 방문 표시
            # 다음 도시로 이동 (도시 수 +1, 비용 추가)
            DFS(next_city, count + 1, cost + W[city][next_city])
            visited[next_city] = False  # 다시 돌아왔을 때 방문 해제

# 0번 도시부터 시작
visited[0] = True  # 시작 도시 방문 표시
DFS(0, 1, 0)       # 도시 0에서 출발, 방문 수 1, 비용 0

# 최소 비용 출력
print(min_cost)