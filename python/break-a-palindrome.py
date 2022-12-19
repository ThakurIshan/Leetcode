class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        if 'a' in set(palindrome) and len(set(palindrome)) == 1:
            return palindrome[:-1] + 'b'
        
        for i, s in enumerate(palindrome):
            if s != 'a':
                if i != len(palindrome) // 2:
                    return palindrome[:i] + 'a' + palindrome[i+1:]
                else:
                    return palindrome[:-1] + 'b'
        return ""
