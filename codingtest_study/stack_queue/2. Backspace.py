def solution(s):
    stack = list(s)
    answer = []
    for st in stack:
        if st == '#':
            if len(answer) > 0:
                answer.pop()
        else:
            answer.append(st)

    answer = "".join(answer)
    
    return answer
            
          
print(solution("abc##ec#ab"))
print(solution("kefd#ef##s##"))
print(solution("teac#cher##er"))
print(solution("englitk##shabcde##ff##ef##ashe####"))
print(solution("itistime####gold"))
