def solution(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop() 
        else:
            stack.append(char)
    
    answer = "".join(stack)
    return answer

print(solution("acbbcaa"))
print(solution("bacccaba"))
print(solution("aabaababbaa"))
print(solution("bcaacccbaabccabbaa"))
print(solution("cacaabbc"))
