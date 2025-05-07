from collections import deque
# deque의 rotet 함수 사용?

def solution(nums, k):
    answer = nums[k:] + nums[0:k]
    return answer  

print(solution([3, 7, 1, 5, 9, 2, 8], 3))
print(solution([2, 12, 2, 1, 3, 3, 9], 2))
print(solution([1, 2, 5, 4, 6, 7, 9], 6))
print(solution([1, 3, 6, 8, 14, 2, 1, 7], 5))