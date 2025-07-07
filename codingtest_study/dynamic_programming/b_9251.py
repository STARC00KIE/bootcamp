A = input().strip()
B = input().strip()
a, b = len(A), len(B)

dp = [] # a+1 * b+1 크기의 2차원 배열
for i in range(a + 1):
    row = []
    for j in range(b + 1):
        row.append(0)
    dp.append(row)

# 두 문자열의 문자를 하나씩 비교하며 최장 공통 부분 수열 찾기
for i in range(1, a + 1):
    for j in range(1, b + 1): 
        if A[i - 1] == B[j - 1]: # 같으면
            dp[i][j] = dp[i - 1][j - 1] + 1
        else: # 다르면
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) 

print(dp[a][b])