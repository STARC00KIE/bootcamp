def solution(n, moves):
    x, y = 0, 0

    move_dict = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }

    for move in moves:
        dx, dy = move_dict[move]
        nx, ny = x + dx, y + dy

        # 격자 범위 안이면 이동
        if 0 <= nx < n and 0 <= ny < n:
            x, y = nx, ny

    return [x, y]
 
                
                      
print(solution(5, 'RRRDDDUUUUUUL'))
print(solution(7, 'DDDRRRDDLL'))
print(solution(5, 'RRRRRDDDDDU'))
print(solution(6, 'RRRRDDDRRDDLLUU'))

