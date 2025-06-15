n, m = map(int, input().split())  # n: 숫자의 범위, m: 뽑을 개수

used = [False] * (n + 1)  # 숫자를 썼는지 표시 (1부터 n까지)
result = []  # 현재 고른 숫자들

def solution():
    if len(result) == m:  # 숫자를 m개 고르면 출력
        print(' '.join(map(str, result)))
        return

    for i in range(1, n + 1):
        if not used[i]:         # 안 쓴 숫자만 고르기
            used[i] = True      # 숫자 사용 표시
            result.append(i)    # 숫자 고르기
            solution()              # 다음 숫자 고르러 가기 (재귀)
            result.pop()        # 숫자 다시 빼기 (되돌리기)
            used[i] = False     # 사용 표시 풀기

solution()