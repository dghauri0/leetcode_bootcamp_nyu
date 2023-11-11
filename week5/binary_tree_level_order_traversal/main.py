from typing import List

import treenode
from solution import Solution
from treenode import TreeNode

sol = Solution()

if __name__ == '__main__':
    root_0 = [3,9,20,None,None,15,7]
    root_0_tn = treenode.insertLevelOrder(root_0, 0, len(root_0))

    root_1 = [1]
    root_1_tn = treenode.insertLevelOrder(root_1, 0, len(root_1))

    root_2 = []
    root_2_tn = treenode.insertLevelOrder(root_2, 0, len(root_2))
    print(sol.levelOrder(root_0_tn))
    print(sol.levelOrder(root_1))
    print(sol.levelOrder(root_2))

