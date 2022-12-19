class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = [''] * numRows
        step, i = (numRows == 1) - 1, 0
        for c in s:
            ans[i] += c
            if i == 0 or i == numRows - 1:
                step = -step
            i += step
        return ''.join(ans)
