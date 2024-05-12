def matrix_chain_multiplication(dims):
    n = len(dims) - 1  
    dp = [[0] * n for _ in range(n)]
    #print(dp)
    
    for i in range(n):
        dp[i][i] = 0
        #print("dp1= ",dp)

    
    for l in range(2, n + 1):
        print("l = ",l)
        for i in range(n - l + 1):
            print("i=",i)
            j = i + l - 1
            dp[i][j] = float('inf')
            print("j= ",j)
            print("dp2=",dp)  # Initialize to infinity
            for k in range(i, j):
                print("k=",k)
                #print("dims=",dims)
                print("dp[i][k] + dp[k + 1][j] = ",dp[i][k] + dp[k + 1][j])
                print("dims[i] * dims[k + 1] * dims[j + 1]= ",dims[i] * dims[k + 1] * dims[j + 1])
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                print("cost=",cost)
                dp[i][j] = min(dp[i][j], cost)
                #print(dp[i][j],cost)

    return dp[0][n - 1]




# Example usage:
matrix_dimensions = [5,2,4,3,6]
result = matrix_chain_multiplication(matrix_dimensions)
print("Minimum number of multiplications:", result)
