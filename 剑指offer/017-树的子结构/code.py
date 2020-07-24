# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def helper(treeA, treeB): #注意三个if的顺序如果颠倒的话会出错
    if not treeB:
        return True
    elif not treeA:
        return False
    elif treeA.val != treeB.val:
        return False
    else:
        return helper(treeA.left, treeB.left) and helper(treeA.right, treeB.right)
class Solution:
#    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
    def HasSubtree(self,pRoot1, pRoot2):
    # write code here
        if not pRoot1 or not pRoot2: return False
    # 2 是不是 1的子树
        res = False
        if pRoot1.val == pRoot2.val:
            res = helper(pRoot1, pRoot2)
        if res: 
            return True
        else:
            return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
        

    

