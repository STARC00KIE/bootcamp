def solution(moves):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_idx = 1  # 시작 방향은 3시(→) 방향

    x, y = 0, 0  # 시작 위치

    for move in moves:
        if move == 'G':
            dx, dy = directions[dir_idx]
            nx, ny = x + dx, y + dy

            # 격자판 범위 확인 (100x100)
            if 0 <= nx < 100 and 0 <= ny < 100:
                x, y = nx, ny
        elif move == 'R':
            dir_idx = (dir_idx + 1) % 4  # 시계방향 90도
        elif move == 'L':
            dir_idx = (dir_idx - 1) % 4  # 반시계방향 90도

    return [x, y]

                      
print(solution('GGGRGGG'))
print(solution('GGRGGG'))
print(solution('GGGGGGGRGGGRGGRGGGLGGG'))
print(solution('GGLLLGLGGG'))
