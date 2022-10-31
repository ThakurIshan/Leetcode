class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        while n > 1:
            i = 0
            ns = ''
            while i < len(s):
                c = 1
                while i < len(s) - 1 and s[i] == s[i + 1]:
                    i += 1
                    c += 1
                ns += str(c) + s[i]
                i += 1
            s = ns
            n -= 1
        return s
