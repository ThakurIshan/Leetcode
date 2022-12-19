# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        curr = root
        s = []
        h = []
        while True:
            if curr:
                s.append(curr)
                curr = curr.left
            elif s:
                curr = s.pop()
                t = k - curr.val
                if t in h:
                    return True
                else:
                    h.append(curr.val)
                curr = curr.right
            else:
                break
        return False
