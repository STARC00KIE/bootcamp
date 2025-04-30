def solution(nums):
    # 정렬하기
    # 빈도수 세서 key - value 쌍으로 딕셔너리에 저장하기
    # key: 빈도 수, value: 리스트 형태로 만들기
    # key가 1인 value 중 가장 큰 수 반환하기
    dic = {}
    cnt = 0 # 숫자 개수
    nums.sort() # 정렬
    tmp = nums[0] # 처음 비교할 숫자
    # print(nums) # print

    for num in nums:
        # tmp랑 num이랑 다를 때
        # print(f"dic: {dic}\ntmp: {tmp}\nnum: {num}\ncnt: {cnt}\n") # print
        if tmp != num:
            # 딕셔너리에 (tmp, 숫자 저장)
            # 딕셔너리에 key(cnt) 없을 때
            if cnt not in dic:
                dic[cnt] = [tmp]
            # key 존재하면 append 함수 사용
            else: # 
                dic[cnt].append(tmp)
            tmp = num
            cnt = 1
        
        # tmp랑 num이랑 같을 때
        else:
            cnt += 1

    # 마지막 글자 딕셔너리에 추가
    if cnt not in dic:
        dic[cnt] = [tmp]
        # key 존재하면 append 함수 사용
    else: # 
        dic[cnt].append(tmp)

    # key에 1일 있을 때 최대값 반환
    # 없을 때 -1 반환
    if 1 in dic.keys():
        return max(list(dic[1]))
    else:
        return -1           
                
print(solution([3, 9, 2, 12, 9, 12, 8, 7, 9, 12]))
print(solution([2, 1, 3, 2, 1, 3, 4, 5, 4, 5, 6, 7, 6 ,7, 8, 8]))
print(solution([23, 56, 11, 67, 120, 560, 812, 960, 560, 777, 888, 960]))
print(solution([11, 73, 156, 789, 345, 156, 789, 345, 678, 555, 678]))
print(solution([1, 3, 1, 5, 7, 2, 3, 1, 5]))