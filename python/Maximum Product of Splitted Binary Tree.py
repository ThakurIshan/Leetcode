class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        modulo = (10**9 + 7)
        def dfs(root, totalSum):
            if root == None: return 0
            currSum = dfs(root.left, totalSum) + dfs(root.right, totalSum) + root.val
            self.ans = max(self.ans, currSum * (totalSum - currSum))
            return currSum
        self.ans, self.totalSum = 0, 0
        self.totalSum = dfs(root, self.totalSum)
        dfs(root, self.totalSum)

        return self.ans % modulo


        