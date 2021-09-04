from typing_extensions import Unpack
from Data_Structure.tree_node import TreeNode

# 二叉树遍历框架
def traverse(root: TreeNode):
    # 前序遍历
    traverse(root.left)
    # 中序遍历
    traverse(root.right)
    # 后序遍历

# 心得：
# ***这是二叉树的最基本框架。我一直没有理解的问题就是最简单的记住了前，中，后的遍历方式，
# 但是从来没有把这三个遍历的方式正确的运用到每一道tree的题或者recursion的题的解题当中

# ***之前总是以最开始考虑recursion的想法想到最基本的case是什么，去想最基本的case其实很容易让人去往implementation的细节方向去想。这种思维方式是不对的
# *****最开始的出发点就从进入recursion的第一层开始想，而不是从recursion的最深层开始想。
# *****一定要假设recursion的left，right 已经帮你做好了深层的运算。假设left tree 和right tree的操作已经做好了。那么在当前节点（层）你应该做什么操作

# ***比如quick sort：就从第一层开始，给你一个nums:List[int]， 假设你的左子树和右子树都是sort好了，那么在当前层/节点（也就是第一层）你需要做什么操作？
# 需要的操作就是在当前节点/层找到 找到一个pivot（idx）， 然后把大于pivot switch到右边，把小于等于pivot的放左边。然后进行下一层的操作。

# *****那么怎么决定是前中后序遍历呢？应该看你需要不需要用左子树和右子树的结果来进行当前层的操作。如果你需要，那么就是后序，如果不需要就是前序。前序就top down，后序是bottom up


# 文章金句
# 快速排序就是个二叉树的前序遍历，归并排序就是个二叉树的后序遍历
# ***写递归算法的关键是要明确函数的「定义」是什么，然后相信这个定义，利用这个定义推导最终结果，绝不要跳入递归的细节。
# ***写树相关的算法，简单说就是，先搞清楚当前 root 节点「该做什么」以及「什么时候做」，然后根据函数定义递归调用子节点，递归调用会让孩子节点做相同的事情。