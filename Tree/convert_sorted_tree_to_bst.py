from typing import List
from Data_Structure.tree_node import TreeNode

class sortedArrayToBST:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # solutin 1: always left middle as a root
        # 这个相当于每次都要先找到这个list里面的中间值当做root，以及分辨出root.left 和 root.right range。 
        def helper(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            
            # solutin 1: always left middle as a root
            mid = (left + right) // 2

            # solutin 2: always right middle as a root
            # mid = (left + right) // 2
            # if (left + right) % 2:
            #     mid += 1
            
            # solutin 3: random choose left or right middle as a root
            # mid = (left + right) // 2
            # if (left + right) % 2:
            #     p += randint(0, 1)

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            # 这里必须return root 才能连接到上一层。试想return了本层的TreeNode，到上一层就是别人的root.left
            # 或者root.right。这样在上面的root.left = helper(left, mid - 1) 才能得到node和node之间的衔接
            return root
        return helper(0, len(nums) - 1)


    def call_function(self) -> None:

        print(self.sortedArrayToBST([-10,-3,0,5,9]))