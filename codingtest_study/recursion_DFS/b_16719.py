# 입력 문자열 받기
s = input()
# 각 문자의 사용 여부를 나타내는 리스트
used = [False] * len(s)

def solution(s, used, result):
    # 모든 문자를 다 사용했으면 종료
    if all(used):
        return

    min_str = None      # 사전 순으로 가장 앞서는 문자열
    min_idx = -1        # 그 문자열을 만들기 위해 고른 문자 위치

    # 아직 사용하지 않은 문자들 중 하나씩 시도
    for i in range(len(s)):
        if not used[i]:
            temp = ""
            # 현재까지 보여준 문자 + i번째 문자를 포함한 문자열 만들기
            for j in range(len(s)):
                # 이미 사용했거나, 이번에 선택한 i번째 문자면 포함
                if used[j] or j == i:
                    temp += s[j]

            # 지금까지 본 것 중 사전순으로 가장 앞이라면 갱신
            if min_str is None or temp < min_str:
                min_str = temp
                min_idx = i

    # 고른 문자 사용 표시
    used[min_idx] = True

    # 결과 출력
    print(min_str)

    # 다음 문자를 선택하기 위해 재귀 호출
    solution(s, used, min_str)

# 재귀 함수 호출 시작 (초기 result는 빈 문자열)
solution(s, used, "")
