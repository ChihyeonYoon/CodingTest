# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.visited = {}

    def dfs(self, root, depth):

            cur_node = root
            cur_depth = depth

            if cur_depth not in self.visited:
                self.visited[cur_depth] = cur_node.val
            else:
                self.visited[cur_depth] += cur_node.val

            if cur_node.left != None:
                self.dfs(cur_node.left, cur_depth+1)
            if cur_node.right != None:
                self.dfs(cur_node.right, cur_depth+1)

    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.dfs(root, 0)

        print(self.visited)

        max_depth = max(self.visited.keys())
        return self.visited[max_depth]