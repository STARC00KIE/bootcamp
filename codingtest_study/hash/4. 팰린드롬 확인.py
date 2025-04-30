from collections import Counter
def solution(s):
    s = Counter(list(s))
    s = dict(sorted(s.items(), reverse = True))
    
    oddcnt = 0
    for k, v in s.items():
        # print(k ,v)
        if v%2 != 0: # 홀수일 때
            oddcnt += 1
        if oddcnt >= 2:
            return False
    return True
        
print(solution("abacbaa"))
print(solution("abaaceeffkckbaa"))
print(solution("abcabbcc"))
print(solution("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))
print(solution("aabcefagcefbcabbcc"))