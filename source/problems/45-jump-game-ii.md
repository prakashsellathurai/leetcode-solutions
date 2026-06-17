# 45-jump-game-ii


Try it on <a href='https://leetcode.com/problems/45-jump-game-ii'>leetcode</a>

## Description
<div class="description">
<div><p>Given an array of non-negative integers <code>nums</code>, you are initially positioned at the first index of the array.</p>

<p>Each element in the array represents your maximum jump length at that position.</p>

<p>Your goal is to reach the last index in the minimum number of jumps.</p>

<p>You can assume that you can always reach the last index.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [2,3,1,1,4]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [2,3,0,1,4]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        cur_End = 0
        maxReach = 0
        for i in range(len(nums)):
            if i > cur_End:
                steps += 1
                cur_End = maxReach

            maxReach = max(maxReach, i + nums[i])

        return steps

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "45. Jump Game II",
    "text": "Given an array of non-negative integers nums, you are initially positioned at the first index of the array.\nEach element in the array represents your maximum jump length at that position.\nYour goal is to reach the last index in the minimum number of jumps.\nYou can assume that you can always reach the last index.\n\u00a0\nExample 1:\nInput: nums = [2,3,1,1,4]\nOutput: 2\nExplanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.\n\nExample 2:\nInput: nums = [2,3,0,1,4]\nOutput: 2\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 104\n0 <= nums[i] <= 1000\n\n",
    "url": "https://leetcode.com/problems/45-jump-game-ii",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def jump(self, nums: List[int]) -> int:\n        steps = 0\n        cur_End = 0\n        maxReach = 0\n        for i in range(len(nums)):\n            if i > cur_End:\n                steps += 1\n                cur_End = maxReach\n\n            maxReach = max(maxReach, i + nums[i])\n\n        return steps\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/45-jump-game-ii/",
      "datePublished": "2024-11-28",
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