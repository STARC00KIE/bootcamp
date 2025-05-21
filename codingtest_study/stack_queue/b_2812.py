N, K = map(int, input().split())
str_num = input()

stack = [] #  결과 저장할 스택
to_remove = K # 제거 개수

# 숫자 문자열의 각 자릿수를 순회
for num in str_num:
    # 스택이 비어 있지 않고, 아직 제거할 수 있으며,
    # 현재 숫자가 스택의 마지막 숫자보다 크다면 (작은 수 제거)
    while stack and (to_remove > 0) and (stack[-1] < num):
        stack.pop()       # 스택에서 마지막 숫자 제거
        to_remove -= 1    # 제거 횟수 감소
    stack.append(num)     # 현재 숫자를 스택에 추가

# 만약 아직 제거하지 못한 숫자가 남아 있다면,
# 뒤에서부터 잘라내어 총 N - K 자릿수로 만들어줌
result = ''.join(stack[:N - K]) # 스택에 순대로 값이 들어가면 오류가 생기므로 그것 방지
# result = ''.join(stack)
# 최종 결과 출력
print(result)
"""
# 시간초과 O(n*m)
# 초기설정
N, K = map(int, input().split())
str_num = input()
answer = ""

num_list = list(str(str_num))
num_list = list(map(int, num_list))

for _ in range(K):
    num_list.remove(min(num_list))

answer = ""
for num in num_list:
    answer += str(num)
print(int(answer))
"""