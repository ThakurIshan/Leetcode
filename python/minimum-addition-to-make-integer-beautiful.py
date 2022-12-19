class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        if sum([int(x) for x in str(n)]) <= target:
            return 0
        x = 0
        s = 0
        a = str(n)
        for i in range(len(a)):
            s += int(a[i])
            if s >= target:
                break
            x += 1
        ans = int("1" + len(a[x:]) * "0") - int(a[x:])
        return ans
