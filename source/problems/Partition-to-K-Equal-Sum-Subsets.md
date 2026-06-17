# partition-to-k-equal-sum-subsets


Try it on <a href='https://leetcode.com/problems/partition-to-k-equal-sum-subsets'>leetcode</a>

## Description
<div class="description">
<div><p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <code>true</code> if it is possible to divide this array into <code>k</code> non-empty subsets whose sums are all equal.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [4,3,2,3,5,2,1], k = 4
<strong>Output:</strong> true
<strong>Explanation:</strong> It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3,4], k = 3
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 16</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li>The frequency of each element is in the range <code>[1, 4]</code>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        nums.sort()
        target, rem = divmod(sum(nums), k)
        if rem or nums[-1] > target:
            return False
        dp = [False] * (1 << len(nums))
        dp[0] = True
        total = [0] * (1 << len(nums))

        for state in range(1 << len(nums)):
            if not dp[state]:
                continue
            for i, num in enumerate(nums):
                future = state | (1 << i)
                if state != future and not dp[future]:
                    if num <= target - (total[state] % target):
                        dp[future] = True
                        total[future] = total[state] + num
                    else:
                        break
        return dp[-1]

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "698. Partition to K Equal Sum Subsets",
    "text": "Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.\n\u00a0\nExample 1:\nInput: nums = [4,3,2,3,5,2,1], k = 4\nOutput: true\nExplanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.\n\nExample 2:\nInput: nums = [1,2,3,4], k = 3\nOutput: false\n\n\u00a0\nConstraints:\n\n1 <= k <= nums.length <= 16\n1 <= nums[i] <= 104\nThe frequency of each element is in the range [1, 4].\n\n",
    "url": "https://leetcode.com/problems/partition-to-k-equal-sum-subsets",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution(object):\n    def canPartitionKSubsets(self, nums, k):\n        nums.sort()\n        target, rem = divmod(sum(nums), k)\n        if rem or nums[-1] > target:\n            return False\n        dp = [False] * (1 << len(nums))\n        dp[0] = True\n        total = [0] * (1 << len(nums))\n\n        for state in range(1 << len(nums)):\n            if not dp[state]:\n                continue\n            for i, num in enumerate(nums):\n                future = state | (1 << i)\n                if state != future and not dp[future]:\n                    if num <= target - (total[state] % target):\n                        dp[future] = True\n                        total[future] = total[state] + num\n                    else:\n                        break\n        return dp[-1]\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/partition-to-k-equal-sum-subsets/",
      "datePublished": "2023-03-25",
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