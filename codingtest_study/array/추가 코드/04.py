def solution(answers):
  p1 = [1,2,3,4,5] 
  p2 = [2,1,2,3,2,4,2,5]
  p3 = [3,3,1,1,2,2,4,4,5,5]

  p1_cnt, p2_cnt, p3_cnt = 0, 0, 0
  answer = []
  
  for idx, an in enumerate(answers):
    if p1[idx % len(p1)] == an:
      p1_cnt += 1
    if p2[idx % len(p2)] == an:
      p2_cnt += 1
    if p3[idx % len(p3)] == an:
      p3_cnt += 1

  # p1, p2, p3 중에서 제일 큰 값 구하기
  maxcnt = max([p1_cnt, p2_cnt, p3_cnt])

  # 최댓값
  if maxcnt == p1_cnt:
    answer.append(1)
  if maxcnt == p2_cnt:
    answer.append(2)
  if maxcnt == p3_cnt:
    answer.append(3)

  answer = sorted(answer)
  return answer

print(solution([1, 2, 3, 4, 5])) # 반환값 : [1]
print(solution([1, 3, 2, 4, 2])) # 반환값 : [1, 2, 3]