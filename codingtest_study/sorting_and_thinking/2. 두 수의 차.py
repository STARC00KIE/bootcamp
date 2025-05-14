
def solution(nums):
    nums = sorted(nums)
    answer = []
    min_num = float("inf")

    for idx, i in enumerate(nums[:-1]):
        for j in nums[idx+1:]:
            if min_num < abs(i-j):
                pass
            elif min_num > abs(i-j):
                min_num = abs(i-j)
                answer = [[i, j]]
            else:
                answer.append([i, j])
    
    return answer
print(solution([3, 8, 1, 5, 12]))
print(solution([2, 1, 3, 5, 4]))
print(solution([5, 10, 15, 20, 25, 11]))
print(solution([2, 4, 3, 1, 5, 7, 8, 12, 13, 15, 23]))
print(solution([100, 200, 300, 400, 120, 130, 135, 132, 121]))
