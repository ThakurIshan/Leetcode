class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = collections.defaultdict(list)
        for i, n in enumerate(nums):
            if n not in h:
                h[n].append(i)
                continue
            for x in h[n]:
                if abs(x - i) <= k:
                    return True
            else:
                h[n].append(i)
        return False
