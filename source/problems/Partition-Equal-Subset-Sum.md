# Partition-Equal-Subset-Sum


Try it on <a href='https://leetcode.com/problems/partition-equal-subset-sum'>leetcode</a>

## Description
<div class="description">
<div><p>Given a <strong>non-empty</strong> array <code>nums</code> containing <strong>only positive integers</strong>, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,5,11,5]
<strong>Output:</strong> true
<strong>Explanation:</strong> The array can be partitioned as [1, 5, 5] and [11].
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3,5]
<strong>Output:</strong> false
<strong>Explanation:</strong> The array cannot be partitioned into equal sum subsets.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 200</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) & 1:
            return False
        total = sum(nums) // 2
        n = len(nums)
        memo = {}
        def dfs(t, index):
            if t in memo:
                return memo[t]
            if t < 0 :
                return 0
            elif t == 0:
                return 1
            for i in range(index,n):
                if dfs(t-nums[i], i+1):
                    memo[t] = 1
                    return 1
            memo[t] = 0
            return 0
        ans = dfs(total, 0)
        return (ans)
```