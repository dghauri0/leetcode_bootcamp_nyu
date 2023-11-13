from typing import List

import treenode
from solution import Solution
from treenode import TreeNode

sol = Solution()

if __name__ == '__main__':
    root_0 = [3, 1, 4, None, 2]
    root_0_tn = treenode.insertLevelOrder(root_0, 0, len(root_0))
    k_0 = 1

    root_1 = [5, 3, 6, 2, 4, None, None, 1]
    root_1_tn = treenode.insertLevelOrder(root_1, 0, len(root_1))
    k_1 = 3

    print(sol.kthSmallest(root_0_tn, k_0))
    print(sol.kthSmallest(root_1_tn, k_1))
