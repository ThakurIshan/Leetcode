class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        h = collections.defaultdict(int)
        for i in words:
            h[i] += 1
        res = list(h.items())
        res.sort(key=lambda x: (-x[1], x[0]))
        res = [x[0] for x in res]
        return res[:k]
