"""
 Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

    Given target value is a floating point.
    You are guaranteed to have only one unique value in the BST that is closest to the target.

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildtree(num):
    if num is None:return []
    root = TreeNode(num[0])
    def buildnode(idx):
        if idx >= len(num):
            return None
        nd = TreeNode(num[idx])
        nd.left = buildnode(2*idx+1)
        nd.right = buildnode(2*idx+2)
        return nd
    
    root.left = buildnode(1)
    root.right = buildnode(2)
    return root


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        def helper(root,target,div):
            if root == None:return div
            div = root.val if abs(root.val-target) < abs(div-target) else div
            if root.val == target:return root.val
            elif root.val < target:return helper(root.right,target,div)
            else:return helper(root.left,target,div)
        
        return helper(root,target,float('inf'))
        
        


if __name__ == "__main__":
    cls = Solution()
    target = 1.2
    root = TreeNode(0)
    num = [1,None,2]
    root = buildtree(num)
    print root.val
    print root.left.val,root.right.val
    #print root.left.left.val,root.left.right.val,root.right.left.val,root.right.right.val
    print cls.closestValue(root,target)



"""
This problem I already solved in professor's class, need to record a minimum difference through every node. Becareful, this difference need to be the absolute number, and do remember to return the node number instead of the difference value.
"""

