def solution(s):
    lst_s = list(s)
    cnt = [0, 0]

    if s[0] == '0':
        cnt[0] += 1
    else:
        cnt[1] += 1

    for i in range(len(lst_s)-1):
        if lst_s[i] == lst_s[i+1]:
            pass
        else:
            if s[i+1] == '0':
                cnt[0] += 1
            else:
                cnt[1] += 1
    
    if (cnt[0] == 1 and cnt[1] == 0) or (cnt[0] == 0 and cnt[1] == 1):
        return 0
    else:
        return min(cnt)


print(solution("0001100")) # 1
print(solution('11111')) # 0
print(solution('00000001')) # 1
print(solution('11001100110011000001')) # 4
print(solution('11101101')) # 2