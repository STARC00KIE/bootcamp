def count_black_areas_with_size(board):
    n = len(board)  # 보드의 크기 (5x5이면 n=5)

    # 방문 여부를 저장할 2차원 리스트 초기화
    visited = [[False] * n for _ in range(n)]

    # 결과를 저장할 리스트: 각 영역의 (행, 열, 픽셀 수)를 담음
    results = []

    # DFS 함수 정의: 현재 위치 (x, y)에서 연결된 모든 검정색(1) 픽셀 탐색
    def dfs(x, y):
        # 아래 변수들은 바깥 함수의 변수인데, dfs 내부에서 수정해야 하므로 nonlocal로 선언
        nonlocal size, min_row, min_col

        # 1. 범위를 벗어난 경우 종료
        if x < 0 or x >= n or y < 0 or y >= n:
            return
        # 2. 흰색(0)이거나 이미 방문한 칸은 무시
        if board[x][y] == 0 or visited[x][y]:
            return

        # 3. 현재 위치 방문 처리
        visited[x][y] = True
        size += 1  # 현재 영역의 픽셀 수 1 증가

        # 4. 현재 위치가 영역 내 가장 왼쪽 위 픽셀인지 확인 (정렬 기준용)
        if x < min_row or (x == min_row and y < min_col):
            min_row, min_col = x, y

        # 5. 상하좌우로 연결된 칸 재귀 탐색
        dfs(x-1, y)  # 위
        dfs(x+1, y)  # 아래
        dfs(x, y-1)  # 왼쪽
        dfs(x, y+1)  # 오른쪽

    # 보드 전체를 순회하면서 DFS 시작
    for i in range(n):
        for j in range(n):
            # 방문하지 않은 검정색 픽셀을 발견하면 새로운 영역 시작
            if board[i][j] == 1 and not visited[i][j]:
                size = 0  # 현재 영역의 픽셀 수
                min_row, min_col = i, j  # 현재 영역의 기준 좌표

                dfs(i, j)  # 현재 위치에서 DFS 시작

                # 해당 영역의 기준 위치 및 픽셀 수 저장
                results.append((min_row, min_col, size))

    # 영역 기준 (행, 열 순서)로 정렬
    results.sort()

    # 영역별 픽셀 수만 리스트로 추출해서 반환
    return [size for _, _, size in results]

print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))