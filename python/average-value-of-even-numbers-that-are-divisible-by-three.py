class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s = 0
        n = 0
        for i in nums:
            if i % 6 == 0:
                s += i
                n += 1
        return s // n if n else 0
