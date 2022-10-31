class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for s in arr:
            if len(set(s)) < len(s):
                continue
            s = set(s)
            for x in dp:
                if s & x:
                    continue
                dp.append(s | x)
        return max(len(x) for x in dp)
