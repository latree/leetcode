
void BST(TreeNode root, int target) {
    if (root.val == target)
        // 找到目标，做点什么
    if (root.val < target) 
        BST(root.right, target);
    if (root.val > target)
        BST(root.left, target);


# 文章金句：
# BST 的一个优化方式是通过在TreeNode 里增加一个var


# 我们通过使用辅助函数，增加函数参数列表，在参数中携带额外信息，将这种约束传递给子树的所有节点，这也是二叉树算法的一个小技巧吧。比如leetcode 98题Validate Binary Search Tree

# 讲了中序遍历对 BST 的重要意义
# 写了 BST 的基本操作

# ****以我的刷题经验，我们要尽可能避免递归函数中调用其他递归函数