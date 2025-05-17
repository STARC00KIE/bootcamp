"""
nums에  오름차순으로  정렬된  정수  배열이  주어지고,  target에  nums배열에서  찾고자  하는  값이 주어지면  nums배열에서 target의 인덱스 번호를 찾아  반환하는 프로그램을 작성하세요. 인덱스 번호는 0번부터 시작합니다.
target값이 nums에 존재하지 않을 경우 -1를 반환합니다.
"""

"""
리스트 전체 길이의 1/2 지점부터 탐색하여 문제 해결하면 됨
"""

# next(iterator, default) 함수 설명:
# 1. iterator: 이터레이터 객체 (여기서는 제너레이터 표현식)
# 2. default: 이터레이터가 소진되었을 때 반환할 기본값 (-1)
# 
# 제너레이터 표현식 (idx for idx, i in enumerate(nums) if i == target):
# - enumerate(nums): 인덱스와 값을 순회
# - if i == target: target과 일치하는 값 찾기
# - idx: 일치하는 값의 인덱스 반환
# 
# 작동 방식:
# 1. target과 일치하는 첫 번째 값을 찾으면 해당 인덱스 반환
# 2. 일치하는 값이 없으면 기본값 -1 반환

# 이진 탐색 문제 풀이 공식
# 최솟값, 최댓값 정하기(LEFT, RIGHT)
# 중간값(mid)을 계산결과에 따라 늘리고 줄이면서 최적의 값 탐색하기
# LEFT = mid -1 , RIGHT = mid + 1 -> 이런 식으로
# 1/2씩 줄여 나가므로 log함수이고, 한번 리스트 순회를 진행하므로 시간복잡도는 nlogn

def solution(nums, target): return next((idx for idx, i in enumerate(nums) if i == target), -1)

def solution(nums, target):
    # num 순회하여 같으면 인덱스 반환
    for idx, i in enumerate(nums): 
        if i == target:
            return idx
    return -1                                         
print(solution([2, 5, 7, 8, 10, 15, 20, 24, 25, 30], 8))
print(solution([-3, 0, 2, 5, 8, 9, 12, 15], 0))
print(solution([-5, -2, -1, 3, 8, 9, 12, 17, 23], 2))
print(solution([3, 6, 9, 12, 17, 29, 33], 3))
print(solution([1, 2, 3, 4, 5, 7, 9, 11, 12, 15, 16, 17, 18], 18))
