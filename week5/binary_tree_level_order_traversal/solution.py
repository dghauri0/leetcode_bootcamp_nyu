# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from typing import Optional, List
from treenode import TreeNode

# High-level idea: BFS makes sense here as it is doing a level-order
# search by default.
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Initialize output
        output = []

        # Initialize queue for BFS and add root
        queue = collections.deque()
        queue.append(root)

        # BFS algorithm. At each level end driven by for loop,
        # append to output list. Any null nodes or levels are disregarded.
        while queue:
            curr_level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    curr_level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if curr_level:
                output.append(curr_level)

        return output
