# 시간복잡도 O(N)

def solution(nums):
    length = 0 # 최소 길이
    cnt = 0 # 연속된 1 개수 카운트
    for n in nums:
        if n == 1:
            cnt += 1
        else:
            if cnt > length:
                length = cnt
            cnt = 0
    if cnt > length:
        length = cnt
    return length

print(solution([1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]))
print(solution([0, 0, 1, 0, 1, 0, 0]))
print(solution([1, 1, 1, 1, 1]))
print(solution([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]))
