class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def majority(low, high):
            """
                low: 인덱스 첫번째 (처음은 무조건 0)
                how: 인덱스 마지막 (개수 - 1)
                
                과반수는 전체에 하나만 존재
                분할된 각각의 구간도 전체의 일부
            """
            if low == high:  # base case: 한 원소만 있으면 그것이 과반수
                return nums[low]

            mid = (low + high) // 2 # 중간값 표시
            left = majority(low, mid) # 재귀를 반복해서 결국에는 low == mid(high)가 되는 지점에 도달함(base case)
            right = majority(mid + 1, high) # 재귀를 반복해서 결국에선 (mid + 1) == high가 되는 지점에 도달함(base case)

            if left == right:
                return right

            left_cnt = 0 # left와 같은 값 개수 초기화
            right_cnt = 0 # right와 같은 값 개수 초기화

            for i in range(low, high + 1): # 인덱스 low부터 high까지 반복
                if nums[i] == left: # 현재 값이 left와 같으면
                    left_cnt += 1 # 개수 증가

            for i in range(low, high + 1): # 인덱스 low부터 high까지 반복
                if nums[i] == right: # 현재 값이 right와 같으면
                    right_cnt += 1 # 개수 증가

            if left_cnt > right_cnt:
                return left
            else:
                return right

        return majority(0, len(nums) - 1) # 인덱스 번호