# "1" -> "A"
# "26" -> "Z"
def num_decodings(s: str):
    if not s or s[0] == "0":
        return 0
    
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, len(s) + 1):
        oned = int(s[i-1: i])
        twod = int(s[i-2: i])
        if 1 <= oned <= 9:
            dp[i] += dp[i-1]
        
        if 10 <= twod <= 26:
            dp[i] += dp[i-2]
    
    return dp[len(s)]