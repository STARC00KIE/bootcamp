from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic_tasks = Counter(tasks)
        max_values = max(dic_tasks.values())
        max_count = list(dic_tasks.values()).count(max_values) # 최댓값 공통된거 있는지 세숨
        
        # 기본 공식
        # n + 1 : 값 + idle 차지하는 개수
        # max_values - 1 : 마지막은 idle 필요 없음
        # - 1 부분은 max_count에 존재함
        # max_count 에 최댓값 개수만큼 뒤에 붙임, 최소 1 이상
        answer = (max_values - 1) * (n + 1) + max_count
        
        # 실제 작업이 더 많으면 그 수가 정답
        return max(answer, len(tasks))