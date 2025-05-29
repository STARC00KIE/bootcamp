from collections import deque

def solution(board):
    n = len(board)
    visited = [[False] * n for _ in range(n)]

    def BFS(x, y):
        Q = deque() # 덱
        Q.append((x, y)) # 현재 위치 추가
        visited[x][y] = True # 방문 처리

        # 네 방향 이동 (상, 하, 좌, 우)
        dx = (-1, 1, 0, 0)
        dy = (0, 0, -1, 1)

        while Q: # 결국에 방문할 데 없어지면 Q가 popleft만 하고 append를 안하므로 while문을 벗어나게 된다. 
            cx, cy = Q.popleft() # 현재 위치 cx, cy

            for idx in range(4): # 0(-1, 0), 1(1, 0), 2(0, -1), 3(0, 1)
                nx = cx + dx[idx]
                ny = cy + dy[idx]

                # 범위 체크 및 방문 조건
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] == 1 and not visited[nx][ny]: # 검은색이고 아직 방문 안했으면
                        visited[nx][ny] = True # 방문처리
                        Q.append((nx, ny)) # 추가

    # 진짜 시작
    count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1 and not visited[i][j]: # 검정이고 아직 방문 안하면
                BFS(i, j) # BFS 실행
                count += 1 # 그러면 개수 한개 추가

    return count # 훨씬나은듯

print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))