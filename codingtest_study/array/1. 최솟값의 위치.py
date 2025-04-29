"""
# 한 줄로 코드 작성 가능
def solution(nums):
    answer = nums.index(min(nums))
    
    return answer
"""

# 여러 줄로 코드 표현, 시간복잡도 O(n)
def solution(nums):
    cnt = 0 # 인덱스 카운트
    ind = 0 # 최솟값 index
    min = nums[0] # 최솟값

    for num in nums:
        if num < min:
            min = num
            ind = cnt
        cnt += 1
    return ind
print(solution([7, 10, 5, 3, 2, 15, 19]))
print(solution([-12, 12, 30, -15, -5, 3, 9, -11, 14]))
print(solution([17, 11, 5, 8, 23, 29, 19, 12, 25, 16, 2]))
print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21]))