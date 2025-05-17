# 이진 탐색
# K < N
# 입력값
K, N = map(int, input().split())
LAN_lst = [int(input()) for _ in range(K)]

# 초기 설정
left = 1 # 최소 1cm 자를수 있음
right = sum(LAN_lst) // N # 가능한 최대 길이 => 제일 긴 값 => max
answer = 0

def LAN_cnt(dist): # dist == mid, 현재 탐색 중인 랜선 길이
    cnt = 0 # 랜선 하나마다 자를수 있는 랜선 개수 카운트
    for LAN in LAN_lst:
        cnt += LAN // dist # 최대로 자를 수 있는 랜선 총 개수 더해주기
    # 자를 수 있는 랜선 개수(cnt)가 N(잘라야 하는 랜선개수 목표)보다 같거나 클 경우 True 리턴
    return cnt >= N

# 이진탐색 알고리즘
while left <= right:
    mid = (left + right) // 2
    
    if LAN_cnt(mid): # 자를수 있을 때
        # left 증가시켜서 더 긴 길이(mid)로 자를 수 있는지 확인하기
        left = mid + 1
        # mid 값 업데이트
        answer = mid
    else: # 자를 수 있는 개수가 부족할 때
        # right 감소시켜서 더 짧은 길이(mid)로 자를 수 있는지 확인하기
        right = mid - 1 

print(answer)