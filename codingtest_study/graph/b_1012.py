from collections import deque

T = int(input())  # 테스트 케이스 수

for _ in range(T):
    M, N, K = map(int, input().split())  # 가로 M, 세로 N, 배추 수 K
    field = [[0] * M for _ in range(N)]  # 배추밭
    visited = [[False] * M for _ in range(N)]  # 방문 여부

    for _ in range(K):
        y, x = map(int, input().split())
        field[x][y] = 1

    dx = (0, 0, -1, 1)
    dy = (-1, 1, 0, 0)

    count = 0  # 필요한 지렁이 수

    for i in range(N):  # 세로
        for j in range(M):  # 가로
            if field[i][j] == 1 and not visited[i][j]:
                Q = deque()
                Q.append((i, j))
                visited[i][j] = True

                while Q:
                    cx, cy = Q.popleft()
                    for d in range(4):
                        nx = cx + dx[d]
                        ny = cy + dy[d]
                        if 0 <= nx < N and 0 <= ny < M:
                            if field[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                Q.append((nx, ny))

                count += 1  # 군집 하나 끝날 때마다 +1

    print(count)
