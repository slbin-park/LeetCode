# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxDepth = -1
    value = -1
    dic = {}
    dicNode = {}
    arr = []
    answer = 0

    def dfs(self,node,index,before):
        self.dic[node.val] = before
        self.dicNode[node.val] = node
        if index >= self.maxDepth:
            if index > self.maxDepth:
                self.arr = []
            self.maxDepth = index
            self.arr.append(node.val)
        if node.left != None:
            self.dfs(node.left, index + 1, node.val)
        if node.right != None:
            self.dfs(node.right, index + 1, node.val)

    def getParent(self):
        while True:
            tmp = set()
            tmpArr = []
            for i in range(len(self.arr)):
                tmp.add(self.dic[self.arr[i]])
                tmpArr.append(self.dic[self.arr[i]])
            if len(tmp) == 1:
                self.answer = list(tmp)[0]
                if list(tmp)[0] == -1:
                    self.answer = self.arr[0]
                break
            self.arr = tmpArr

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        print(root)
        self.dfs(root, 0, -1)
        # print(self.arr)
        # print(self.dic)
        # print("=====")
        if len(self.arr) == 1:
            return self.dicNode[self.arr[0]]
        self.getParent()

        # print(self.answer)
        return self.dicNode[self.answer]

        