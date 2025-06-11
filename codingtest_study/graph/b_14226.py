from collections import deque

E = int(input())  # 목표 이모티콘 수

# (화면 이모티콘 수, 클립보드 이모티콘 수, 시간)
queue = deque()
queue.append((1, 0, 0))  # 시작: 화면 1개, 클립보드 0개, 시간 0

visited = [[False] * (E + 1) for _ in range(E + 1)] # 2차원 배열 [화면 임티 수][클립보드 임티 수]
visited[1][0] = True #

while queue:
    sc, cl, ti = queue.popleft()
    if sc == E:
        print(ti)
        break

    # 1. 복사
    if not visited[sc][sc]:
        visited[sc][sc] = True
        queue.append((sc, sc, ti + 1))

    # 2. 붙여넣기
    if cl > 0 and sc + cl <= E and not visited[sc + cl][cl]:
        visited[sc + cl][cl] = True
        queue.append((sc + cl, cl, ti + 1))

    # 3. 삭제
    if sc > 0 and not visited[sc - 1][cl]:
        visited[sc - 1][cl] = True
        queue.append((sc - 1, cl, ti + 1))