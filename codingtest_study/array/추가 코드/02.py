def solution(lst):
  answer = sorted(list(set(lst)), reverse = True)
  return answer
# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
print(solution([4, 2, 2, 1, 3, 4])) # 반환값 : [4, 3, 2, 1]
print(solution([2, 1, 1, 3, 2, 5, 4])) # 반환값 : [5, 4, 3, 2, 1]
