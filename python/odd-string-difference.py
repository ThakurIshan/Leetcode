class Solution:
    def oddString(self, words: List[str]) -> str:
        ans = []
        for i, s in enumerate(words):
            if len(set(s)) == 1:
                t = [0 for _ in range(len(s) - 1)]
                ans.append(tuple(t))
                continue
            t = []
            for i in range(1, len(s)):
                t.append((ord(s[i]) - 97) - (ord(s[i - 1]) - 97))
            ans.append(tuple(t))
        r = collections.Counter(ans)
        for k, v in r.items():
            if v == 1:
                return words[ans.index(k)]
