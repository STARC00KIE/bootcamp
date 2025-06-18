class Solution:
    # 다이나믹 프로그래밍 해보기
    def maxSubArray(self, nums: List[int]) -> int:
        def binery_search(low, high):
            """
                무조건 3가지 케이스 밖에 없을 수 있음
                최대값이 low ~ mid나 mid+1 ~ high 사이일 때
                마지막으로 mid에 걸쳐 있을 때
                mid에 걸쳐 있을 때는 a ~ mid, mid ~ b 값을 채택할 수 있음
                low, mid, high ?? -> divide and conquer 사용할 수 있을 듯?
            """
            # base case: 원소가 하나뿐일 때: 그 값 자체가 부분합임
            if low == high:
                return nums[low]

            # 이진 탐색
            mid = (low + high) // 2
            # 1. 왼쪽 절반 최대 부분합 탐색
            left = binery_search(low, mid)
            # 2. 오른쪽 절반 최대 부분합 탐색
            right = binery_search(mid + 1, high)
            
            # 3. 중간을 걸치는 최대 부분합: 무조건 mid가 들어가야 하기 때문에 역순으로 진행
            # 3-1 mid에서 왼쪽으로 확장
            left_mid, tmp = float('-inf'), 0
            for i in range(mid, low - 1, -1):
                tmp += nums[i]
                if left_mid > tmp:
                    pass
                else:
                    left_mid = tmp

            # 3-2 mid에서 오른쪽으로 확장
            mid_right, tmp = float('-inf'), 0
            for i in range(mid + 1, high + 1):
                tmp += nums[i]
                if mid_right > tmp:
                    pass
                else:
                    mid_right = tmp                

            # 3. 증간을 걸치는 최대 부분합
            left_mid_right = left_mid + mid_right

            # 결과는 셋 중 최댓값
            answer = max(left, left_mid_right, right)
            return answer
        return binery_search(0, len(nums) - 1)