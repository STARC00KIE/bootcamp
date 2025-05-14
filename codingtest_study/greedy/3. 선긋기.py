from collections import defaultdict

def solution(m, nums):
    line_dic = defaultdict(list)
    mn, mx = 0, 0
    cnt = 0
    for num in nums:
        line_dic[num[0]].append(num[1])
    line_dic = dict(sorted(line_dic.items()))
    
    while mx < m:
        tmp = []
        keys_to_delete = []  # 삭제할 키를 저장할 리스트
        for key, value in line_dic.items():
            if key == 0:
                mx = max(value)
                keys_to_delete.append(key)  # 삭제할 키 추가
                cnt += 1
            elif mn <= key <= mx:
                tmp += value
                keys_to_delete.append(key)  # 삭제할 키 추가
        # 반복문이 끝난 후 삭제
        for key in keys_to_delete:
            del line_dic[key]
        mx = max(tmp)
        cnt += 1
    return cnt

print(solution(12, [[5, 10], [1, 8], [0, 2], [0, 3], [2, 5], [2, 6], [10, 12], [7, 12]]))
print(solution(15, [[1, 10], [0, 8], [0, 7], [0, 10], [12, 5], [0, 12], [8, 15], [5, 14]]))
print(solution(20, [[3, 7], [5, 8], [15, 20], [0, 5], [7, 14], [3, 10], [0, 8], [13, 18], [5, 9]]))
print(solution(30, [[5, 7], [3, 9], [2, 7], [0, 1], [0, 2], [0, 3], [19, 30], [8, 15], [7, 12], [13, 20]]))
print(solution(25, [[10, 15], [15, 20], [5, 15], [3, 16], [0, 5], [0, 3], [12, 25]]))