# 초기설정
N, M = map(int, input().split())
tree_length = list(map(int, input().split()))

# 최소 M 미터의 나무를 집에 가져가기 위해 
# 절단기에 설정할 수 있는 높이의 최댓값
# 나무를 최소한으로 가져갈 수 있는 높이 탐색

left = 0 # 절단기 최소 높이: 0미터
# 최고 나무의 높이 이후부터는 가져갈 수 있는 나무의 길이가 같음
right = max(tree_length) 
answer = 0 # 절단기 갈이

def len_tree(mid):
    length = 0 # 자른 나무의 길이
    for tree in tree_length:
        # 절단기보다 같거나 높은 나무만 길이에 추가
        if mid <= tree:
            length += (tree - mid)
    # 최소 길이(M) 이상 자를 수 있는지 확인하기
    return length >= M

while left <= right:
    mid = (left + right) // 2
    
    # True면(최소 길이 이상 자를 수 있으면) 절단기 높이기
    if len_tree(mid):
        answer = mid
        left = mid + 1
        
    # False면(최소 길이 이상 자를 수 없으면) 절단기 낮추기
    else:
        right = mid - 1

print(answer)