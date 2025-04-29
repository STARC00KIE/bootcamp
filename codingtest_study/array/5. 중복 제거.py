from collections import deque
def solution(nums):
    nums = sorted(nums, reverse=True) # 입력된 리스트 내림차순으로 정렬
    answer = [nums[0]]

    for num in nums[1:]:
        if answer[-1] == num: 
            pass
        else:
            answer.append(num)

    return answer
# deque는 정렬하는 방법이 따로 없음, 따라서 que를 정렬하여 리스트에 넣어 줘야 함

print(solution([0, 1, 1, 1, 2, 2, 2, 3]))
print(solution([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5]))
print(solution([0, 0, 0, 3, 3, 3, 5, 7, 7, 7]))
print(solution([1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9]))
