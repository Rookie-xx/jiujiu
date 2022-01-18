> ***给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。***

```python
示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
```

```python
import bisect

class Solution:
    def search(self, nums: [int], target: int) -> int:
        return ans if (ans := bisect.bisect_left(nums, target)) < len(nums) and nums[ans] == target else -1
```

[:star:bisect用法](https://www.cnblogs.com/skydesign/archive/2011/09/02/2163592.html)

:moon:[二分法总结](https://leetcode-cn.com/problems/two-sum/solution/suo-you-ti-jie-de-mu-lu-lian-jie-si-wei-ecnoo/)

:m:[二分总结2](https://leetcode-cn.com/leetbook/read/learning-algorithms-with-leetcode/xsz9zc/)