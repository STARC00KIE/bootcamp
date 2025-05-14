"""
푸는것보다 문제 이해하는게 더 어려운 문제
"""
def solution(box, limit):
    box = sorted(box, key= lambda x: x[1], reverse=True)
    answer = 0
    cnt = 0
    
    for b in range(len(box)):
        for _ in range(box[b][0]):
            if limit <= cnt:
                return answer
            answer += box[b][1]
            cnt += 1
            
print(solution([[2, 20], [2, 10], [3, 15], [2, 30]], 5)) # 115
print(solution([[1, 50], [2, 20], [3, 30], [2, 31], [5, 25]], 10)) # 302
print(solution([[3, 40], [5, 20], [5, 70], [1, 80], [5, 30], [3, 35]], 15)) # 745
print(solution([[2, 70], [5, 100], [3, 90], [1, 95]], 8)) # 775
print(solution([[80, 20], [50, 10], [70, 15], [70, 30], [80, 70], [90, 88], [70, 75]], 500)) # 23920