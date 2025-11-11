
hodnoty = [60, 100, 120]  
vahy = [10, 20, 30]  
kapacita = 50  
n = len(hodnoty)


dp = [[0 for w in range(kapacita + 1)] for i in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, kapacita + 1):
        if vahy[i-1] <= w:
            
            dp[i][w] = max(hodnoty[i-1] + dp[i-1][w-vahy[i-1]], dp[i-1][w])
        else:
            dp[i][w] = dp[i-1][w]

print("Maximální hodnota, kterou můžeme získat:", dp[n][kapacita])
