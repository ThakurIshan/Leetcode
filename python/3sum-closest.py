class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                n = nums[i] + nums[j] + nums[k]
                if n == target:
                    return n
                if abs(target - n) < (target - res):
                    res = n
                if n < target:
                    j += 1
                elif n > target:
                    k -= 1
                else:
                    return res
        return res
