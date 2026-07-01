class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0


        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1

        for i in range(1,n+1):
            if s[i-1]!='0':
                dp[i] +=dp[i-1]

            if i>1 and '10'<=s[i-2:i] <= '26':
                dp[i]+=dp[i-2]
        return dp[n]

        # # test-case: s = "1013"
        # dp[0] = 1 (empty string)
        # i=1 , s[0]='1': dp[1]=dp[0]=1