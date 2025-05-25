def solution(board):
    n = len(board)  # 보드의 크기 (5x5라면 n = 5)

    # 각 위치의 방문 여부를 저장하는 2차원 리스트
    visited = [[False] * n for _ in range(n)]

    # DFS 함수: (x, y) 위치에서 상하좌우로 연결된 1들을 모두 방문
    def DFS(x, y):
        # 범위를 벗어났다면 종료
        if x < 0 or x >= n or y < 0 or y >= n:
            return
        # 흰색(0)이거나 이미 방문한 칸이면 종료
        if board[x][y] == 0 or visited[x][y]:
            return

        visited[x][y] = True  # 현재 위치 방문 처리

        # 상하좌우로 DFS 수행 (연결된 검정색 영역 탐색)
        DFS(x-1, y)  # 위쪽
        DFS(x+1, y)  # 아래쪽
        DFS(x, y-1)  # 왼쪽
        DFS(x, y+1)  # 오른쪽

    count = 0  # 검정색 영역 개수

    # 보드 전체를 순회하면서 DFS 시작
    for i in range(n):
        for j in range(n):
            # 방문하지 않은 검정색(1)을 찾으면 새 영역 탐색 시작
            if board[i][j] == 1 and not visited[i][j]:
                DFS(i, j)      # 연결된 모든 1을 방문
                count += 1    # 영역 개수 1 증가

    return count  # 전체 영역 수 반환

            
print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))

