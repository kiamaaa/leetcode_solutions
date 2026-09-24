# 35. Search Insert Position

**Difficulty:** Easy
**Topics:** Array, Binary Search
**Link:** https://leetcode.com/problems/search-insert-position/

## Problem

> Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

## Solution

```python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
```

**Approach:** Check if target exists in the array; if not, insert it and re-sort to find its correct position.

**Complexity:** Time O(n log n) due to sort · Space O(1)

> **Note:** Since the array is already sorted, this can be optimized to O(log n) using binary search (`bisect.insort` or a manual binary search) instead of `.sort()`.