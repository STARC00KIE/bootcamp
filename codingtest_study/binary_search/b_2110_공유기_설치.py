# 공유기 사이의 최솟값과 최댓값을 정해 놓고 중간부터 시작하고 그거리 이상인 공유기의 개수 카운트하기

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)] # 집 개수만큼 리스트에 값 입력

# 이진 탐색 준비
houses = sorted(houses)

# 초기 설정
left = 1 # 거리 최솟값
right = houses[N] - houses[0] # 공유기 사이 거리 최댓값
answer = 0  # 정답

# 공유기를 최소 거리 mid 이상으로 설치할 수 있는지 판단하는 함수
def install_count(d): # 공유기 카운트
    cnt = 1 # 첫 번째 집에는 포함시키기
    last = houses[0] # 가장 마지막으로 공유기를 설치한 집의 좌표
    
    # 두 번째 집에서부터 공유기 설치할 수 있는지 확인하기
    # 설치할 수 있으면 개수 카운트하기
    for i in range(1, N):
        if (houses[i] - last) >= d: # d: mid
            cnt += 1    # 개수 카운트
            last = houses[i] #가장 마지막으로 공유기를 설치한 집의 좌표 업데이트
        
    if cnt >= C: # 공유기 개수 만족하면 True 리턴
        return True
    else:
        return False

while left <= right: # 기본 이분 탐색 시작
    mid = (left + right) // 2 # 현재 시도할 값
    
    # mid 거리로 공유기 설치하면 => 거리 늘릴 수 있음
    if install_count(mid):
        answer = mid
        left = mid+1
    # mid 거리로 공유기 설치 못하면 => 거리 줄여야댐
    else:
        right = mid-1

# mid 범위는 left<= mid <= right임
# 조건에 맞게 늘이고 줄이면서 문제 하결
print(answer)