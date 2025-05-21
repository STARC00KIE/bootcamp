def solution(s):
    stack = list(s)
    check = 0

    for i in stack:
        if i == '(':
            check += 1
        else:
            check -= 1

    if stack[0] == ')' or stack[-1] == '(':
        return "NO"

    if check == 0:
        return "YES"
    else:
        return "NO"


print(solution("((()))()"))
print(solution("(()(()"))
print(solution("()())"))
print(solution("())("))
print(solution("((())))()("))
