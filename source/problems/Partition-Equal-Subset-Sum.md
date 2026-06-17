# partition-equal-subset-sum


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
            if t < 0:
                return 0
            elif t == 0:
                return 1
            for i in range(index, n):
                if dfs(t - nums[i], i + 1):
                    memo[t] = 1
                    return 1
            memo[t] = 0
            return 0

        ans = dfs(total, 0)
        return ans

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "416. Partition Equal Subset Sum",
    "text": "Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.\n\u00a0\nExample 1:\nInput: nums = [1,5,11,5]\nOutput: true\nExplanation: The array can be partitioned as [1, 5, 5] and [11].\n\nExample 2:\nInput: nums = [1,2,3,5]\nOutput: false\nExplanation: The array cannot be partitioned into equal sum subsets.\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 200\n1 <= nums[i] <= 100\n\n",
    "url": "https://leetcode.com/problems/partition-equal-subset-sum",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def canPartition(self, nums: List[int]) -> bool:\n        if sum(nums) & 1:\n            return False\n        total = sum(nums) // 2\n        n = len(nums)\n        memo = {}\n\n        def dfs(t, index):\n            if t in memo:\n                return memo[t]\n            if t < 0:\n                return 0\n            elif t == 0:\n                return 1\n            for i in range(index, n):\n                if dfs(t - nums[i], i + 1):\n                    memo[t] = 1\n                    return 1\n            memo[t] = 0\n            return 0\n\n        ans = dfs(total, 0)\n        return ans\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/partition-equal-subset-sum/",
      "datePublished": "2022-06-19T23:02:59+05:30",
      "upvoteCount": 0,
      "author": {
        "@type": "Person",
        "name": "Prakash Sellathurai",
        "url": "https://github.com/prakashsellathurai"
      }
    }
  }
}
</script>