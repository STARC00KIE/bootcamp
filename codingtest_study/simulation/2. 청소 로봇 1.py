def solution(moves):
    # 시작 위치
    x, y = 0, 0

    # 이동 방향 정의: U, R, L, D
    move_dict = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    for move in moves:
        dx, dy = move_dict[move]
        x += dx
        y += dy

    return [x, y]

                            
print(solution('RRRDDDLU'))
print(solution('DDDRRRDDLL'))
print(solution('RRRRRRDDDDDDUULLL'))
print(solution('RRRRDDDRRDDLLUU'))
