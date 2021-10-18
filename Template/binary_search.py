
# As for the question "When can we use binary search?", my answer is that, If we can discover some kind of monotonicity, for example, if condition(k) is True then condition(k + 1) is True, then we can consider binary search.
# 1. 这里为什么用binary search？因为一旦判断了mid 和mid+1的大小我们就能缩小一半的搜索区域，即使array不是一个sorted array。
#         这也是从侧面印证了，并不是不是sorted array就不能使用binary search。主要还是在看能不能找到一个条件后就可以缩小左半部或者右半部的搜索区域。如果符合就是可以用binary search


# [Python] Powerful Ultimate Binary Search Template. Solved many problems
# https://leetcode.com/discuss/study-guide/786126/python-powerful-ultimate-binary-search-template-solved-many-problems

# labuladong 的算法小抄 > 第一章、手把手刷数据结构 > 手把手刷数组题目 > 我写了首诗，让你闭着眼睛也能写对二分搜索
# https://labuladong.gitee.io/algo/2/19/52/
# 这篇文章详细的讲述的二叉树的每次定义搜索区间的概念。

# 1. 使用 right = len(nums) 和 while left < right。就是定义一个开区间[left, right)， 这个搜索区间是不含对right的搜索的。
# 1. 使用 right = len(nums)- 1 和 while left <= right。就是定义一个闭区间[left, right]，这个是包含right 搜索的。


# ****** 重中之重 ********
# 而是在于到底要给 mid 加一还是减一，while 里到底用 <= 还是 <。

# binary search 框架
int binarySearch(int[] nums, int target) {
    int left = 0, right = ...;

    while(...) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            ...
        } else if (nums[mid] < target) {
            left = ...
        } else if (nums[mid] > target) {
            right = ...
        }
    }
    return ...;
}
# 分析二分查找的一个技巧是：不要出现 else，而是把所有情况用 else if 写清楚，这样可以清楚地展现所有细节。


int binary_search(int[] nums, int target) {
    int left = 0, right = nums.length - 1; 
    while(left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid - 1; 
        } else if(nums[mid] == target) {
            // 直接返回
            return mid;
        }
    }
    // 直接返回
    return -1;
}

# 找左侧边界template
int left_bound(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid - 1;
        } else if (nums[mid] == target) {
            // 别返回，锁定左侧边界
            right = mid - 1;
        }
    }
    // 最后要检查 left 越界的情况
    if (left >= nums.length || nums[left] != target)
        return -1;
    return left;
}
# 因为left = mid + 1
# 寻找左侧边界的时候可能， 如果target 大于数组的所有数，就会导致left 从数组的右侧out of index的情况。 
# 比如
# target = 6
# 1  2  2  4
#          r l
# 所以最后要有一个check left out of idx
# nums[left] != target的check 是用来检查如果target 小于数组所有数，那么left就会等于0，那么就要看看这个最左边的值是不是等于target。从而决定return的值


# 找右侧边界template
int right_bound(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid - 1;
        } else if (nums[mid] == target) {
            // 别返回，锁定右侧边界
            left = mid + 1;
        }
    }
    // 最后要检查 right 越界的情况
    if (right < 0 || nums[right] != target)
        return -1;
    return right;
}
# 因为right = mid - 1
# 寻找右侧边界的时候可能， 如果target 小于数组的所有数，就会导致right 从数组的左侧out of index的情况。 
# 比如
# target = 0
#   1  2  2  4
# r l
# 所以最后要有一个check right out of idx 
# nums[right] != target的check是用来检查如果target 大于数组的所有的数，那么right就会等于len(nums) - 1 从来没变过。那么就要看这个最右边的值是不是等于target。从而决定return的值
