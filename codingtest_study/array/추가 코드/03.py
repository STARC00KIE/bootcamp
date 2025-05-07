def solution(numbers):
  answer = []
  for idx, i in enumerate(numbers[:-1]):
    for j in numbers[idx+1:]:
      answer.append(i+j)
  answer = sorted(list(set(answer)))
  return answer
#TEST 코드입니다. 주석을 풀어서 확인해보세요
print(solution([2, 1, 3, 4, 1])) # 반환값 : [2, 3, 4, 5, 6, 7]
print(solution([5, 0, 2, 7])) # 반환값 : [2, 5, 7, 9, 12]
