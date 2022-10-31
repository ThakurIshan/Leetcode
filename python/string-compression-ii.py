class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        mem = {}
        
        def dp(start, k):
            if (start, k) in mem:
                return mem[(start, k)]
            
            if start == n or n - start <= k:
                return 0
            
            ans = inf
            count = defaultdict(int)
            max_freq = 0
            for i in range(start, n):
                c = s[i]
                count[c] += 1
                max_freq = max(max_freq, count[c])
                
                cl = 1 + (len(str(max_freq)) if max_freq > 1 else 0)
                
                if k >= i - start + 1 - max_freq:
                    ans = min(ans, cl + dp(i + 1, k - (i - start + 1 - max_freq)))
            mem[(start, k)] = ans
            return ans
        return dp(0, k)
