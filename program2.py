def is_match(message, pattern):
    m, n = len(message), len(pattern)
    
    # dp[i][j] will be True if pattern[0:i] matches message[0:j]
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    
    # Empty pattern matches empty message
    dp[0][0] = True
    
    # Fill the dp array for the pattern starting with '*'
    for i in range(1, n + 1):
        if pattern[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]
    
    # Fill the rest of the dp table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pattern[i - 1] == '?' or pattern[i - 1] == message[j - 1]:
                # If it's a '?' or a character matches, take the diagonal value
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[i - 1] == '*':
                # If it's a '*', either take the value above or to the left
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return dp[n][m]

# Test cases
print(is_match("aa", "a"))      # Output: False
print(is_match("aa", "*"))      # Output: True
print(is_match("cb", "?a"))     # Output: False
print(is_match("adceb", "*a*b")) # Output: True
print(is_match("acdcb", "a*c?b")) # Output: False



  
        