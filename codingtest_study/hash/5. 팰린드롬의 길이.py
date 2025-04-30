from collections import Counter
def solution(s):
    s = Counter(list(s))
    s = dict(sorted(s.items(), reverse = True))
    
    oddlen = 0
    oddcnt = 0
    evenlen = 0
    for k, v in s.items():
        # print(k ,v)
        if v%2 != 0: # 홀수일 때
            oddcnt += 1
            if oddcnt >= 2:
                oddlen += (v - 1)
            else:
                oddlen += v
        else: # 짝수일 때
            evenlen += v
        # print(oddlen, evenlen)
    
    answer = evenlen + oddlen
    return answer
    
                   
print(solution("abcbbbccaaeee"))
print(solution("aabbccddee"))
print(solution("fgfgabtetaaaetytceefcecekefefkccckbsgaafffg"))
print(solution("aabcefagcefbcabbcc"))
print(solution("abcbbbccaa"))
