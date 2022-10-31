class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        h = set()
        ans = [0] * 2
        for n in nums:
            if n in h:
                ans[0] = n
                continue
            h.add(n)
        for i in range(1, len(nums) + 1):
            if i not in h:
                ans[1] = i
                break
        return ans
