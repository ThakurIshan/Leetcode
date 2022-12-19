class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        @cache
        def solve(i, d):
            if d == 1:
                return max(jobDifficulty[i:])
            ans, maxd = inf, 0
            for j in range(i, n - d + 1):
                maxd = max(maxd, jobDifficulty[j])
                ans = min(ans, maxd + solve(j + 1, d - 1))
            return ans
        return solve(0, d)
