n, score = int(input()), list(map(int, input().split()))
dp = [0] * n # 공식 느낌..

for i in range(n):
    max_score = score[i]
    min_score = score[i]
    for j in range(i, -1, -1):  # j부터 i까지를 마지막 조로 한다
        max_score = max(max_score, score[j])
        min_score = min(min_score, score[j])
        if j == 0:
            dp[i] = max(dp[i], max_score - min_score)
        else:
            dp[i] = max(dp[i], dp[j - 1] + (max_score - min_score))

print(dp[n - 1])
