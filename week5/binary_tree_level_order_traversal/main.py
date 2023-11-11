from typing import List
from solution import Solution
from treenode import TreeNode

sol = Solution()

if __name__ == '__main__':
    root_0 = [3,9,20,None,None,15,7]
    root_0_tn = TreeNode(root_0[0], None, None)
    for i in range(1, len(root_0), 2):
        curr_node = root_0_tn
        curr_node.left = root_0[i]
        curr_node.right = root_0[i + 1]

    root_1 = [1]
    root_2 = []
    print(sol.levelOrder(root_0))
    print(sol.levelOrder(root_1))
    print(sol.levelOrder(root_2))

def populateTree(self, input: List[int]):
    