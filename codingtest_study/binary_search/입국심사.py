# https://school.programmers.co.kr/learn/courses/30/lessons/43238?language=python3

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

def solution(n, times):
    # 이진 탐색의 시작점과 끝점 설정
    left = 1  # 최소 시간 (1분)
    right = max(times) * n  # 최악의 경우 (가장 느린 심사관이 모든 사람을 처리할 때)
    answer = right  # 최소 시간을 저장할 변수 초기화

    # 이진 탐색 수행
    while left <= right:
        mid = (left + right) // 2  # 중간 시간 계산
        people = 0  # mid 시간 동안 처리할 수 있는 총 사람 수

        # 각 심사관이 mid 시간 동안 처리할 수 있는 사람 수 계산
        for time in times:
            people += mid // time  # 각 심사관은 mid 시간 동안 (mid // time) 명의 사람을 처리할 수 있음

        # 처리할 수 있는 사람 수가 목표 인원(n)보다 크거나 같은 경우
        if people >= n:
            answer = mid  # 현재 시간을 정답으로 저장
            right = mid - 1  # 더 작은 시간으로 탐색 (최소 시간을 찾기 위해)
        else:
            left = mid + 1  # 더 큰 시간으로 탐색 (현재 시간으로는 모든 사람을 처리할 수 없음)

    return answer

