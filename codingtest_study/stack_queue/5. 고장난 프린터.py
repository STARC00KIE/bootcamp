from collections import deque
def solution(nums):
    queue = deque(nums)

    while queue:
        if len(queue) > 3: # 3개 초과일 때
            queue.popleft()
            queue.popleft()
            tmp = queue.popleft()
            queue.append(tmp)
        # 3개 일 때
        elif len(queue) == 3:
            queue.popleft()
            queue.popleft()
            return queue[0]
        # 3개 미만일 때
        else:
            queue.popleft()
            return queue[0]

print(solution([3, 1, 4, 5, 2, 6, 7]))
print(solution([10, 8, 3, 1, 4, 5, 2, 6, 7, 9]))
print(solution([10, 8, 3, 11, 12, 1, 4, 5, 2, 6, 7, 9]))
print(solution([10, 8, 3, 1, 4, 5, 2, 11, 13, 6, 7, 12, 9, 14]))
print(solution([1, 8, 6, 10, 4, 7, 2, 5, 3, 9]))
