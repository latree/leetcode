def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    # could be [0, n], [1, n], [0, n + 1] etc. Depends on problem
    left, right = min(search_space), max(search_space)

    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    # could be left or (left - 1) etc. Depends on problem
    return left

# 1. Setup the left right doundary to include all potential searching elements
# 2. Decide return left or return left - 1. After exiting the loop, left is the minimal k satisfying the the `condition`
# 3. Design the condition function. This is the most difficult and most beautiful part. Needs lots of practice.

# As for the question "When can we use binary search?", my answer is that, If we can discover some kind of monotonicity, for example, if condition(k) is True then condition(k + 1) is True, then we can consider binary search.

# [Python] Powerful Ultimate Binary Search Template. Solved many problems
# https://leetcode.com/discuss/study-guide/786126/python-powerful-ultimate-binary-search-template-solved-many-problems