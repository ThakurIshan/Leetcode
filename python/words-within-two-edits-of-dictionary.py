class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for i in queries:
            for j in dictionary:
                x = 0
                for k in range(len(j)):
                    if (i[k] != j[k]):
                        x += 1
                if x < 3:
                    ans.append(i)
                    break
        return ans
