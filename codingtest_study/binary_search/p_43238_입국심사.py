# https://school.programmers.co.kr/learn/courses/30/lessons/43238?language=python3

### 해결한 문제

def cnt_people(t, times, n): # 사람 세는 알고리즘, 목표로 하는 시간보다 같거나 적게 걸리면 True 반환
    people = 0
    for time in times:
        people += t // time
    return people >= n

def solution(n, times):
    # 초기 설정
    left = 1 # 최소 걸리는 시간
    right = max(times) * n # 최대 걸리는 시간, 제일 많이 걸리는 사람
    answer = right # 최대 걸리는 시간이 정답이므로 초기값은 right
    
    # 이분탐색
    while left <= right:
        mid = (left + right) // 2 # 목표로 하는 값
    
        if cnt_people(mid, times, n): # 목표로 하는 사람수 보다 많은 사람을 확인할 수 있으면
            right = mid - 1 # 반으로 줄여보기
            answer = mid
        else: # 목표로 하는 사람수 보다 적은 사람을 확인할 수 있으면
            left = mid + 1
    return answer

"""
# 시간 초과
def solution(n, times):
    # 각 심사관이 처리한 사람의 수를 저장하는 배열 초기화
    done = [0] * len(times)  
    # 경과 시간을 추적하는 변수
    time = 0

    # 모든 사람이 심사를 받을 때까지 반복
    while n > 0:
        # 시간을 1씩 증가
        time += 1
        # 각 심사관에 대해 확인
        for i in range(len(times)):
            # 현재 시간이 심사관의 심사 시간의 배수인 경우
            # (즉, 심사관이 한 명의 심사를 마친 경우)
            if time % times[i] == 0:
                # 해당 심사관이 처리한 사람 수 증가
                done[i] += 1
                # 남은 사람 수 감소
                n -= 1
                # 모든 사람이 심사를 받았다면 현재 시간 반환
                if n == 0:
                    return time
"""

