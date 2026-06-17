# 3229-minimum-operations-to-make-array-equal-to-target


Try it on <a href='https://leetcode.com/problems/3229-minimum-operations-to-make-array-equal-to-target'>leetcode</a>

## Description
<div class="description">
<p>You are given two positive integer arrays <code>nums</code> and <code>target</code>, of the same length.</p>

<p>In a single operation, you can select any subarray of <code>nums</code> and increment each element within that subarray by 1 or decrement each element within that subarray by 1.</p>

<p>Return the <strong>minimum</strong> number of operations required to make <code>nums</code> equal to the array <code>target</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,5,1,2], target = [4,6,2,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>We will perform the following operations to make <code>nums</code> equal to <code>target</code>:<br />
- Increment&nbsp;<code>nums[0..3]</code> by 1, <code>nums = [4,6,2,3]</code>.<br />
- Increment&nbsp;<code>nums[3..3]</code> by 1, <code>nums = [4,6,2,4]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,3,2], target = [2,1,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>We will perform the following operations to make <code>nums</code> equal to <code>target</code>:<br />
- Increment&nbsp;<code>nums[0..0]</code> by 1, <code>nums = [2,3,2]</code>.<br />
- Decrement&nbsp;<code>nums[1..1]</code> by 1, <code>nums = [2,2,2]</code>.<br />
- Decrement&nbsp;<code>nums[1..1]</code> by 1, <code>nums = [2,1,2]</code>.<br />
- Increment&nbsp;<code>nums[2..2]</code> by 1, <code>nums = [2,1,3]</code>.<br />
- Increment&nbsp;<code>nums[2..2]</code> by 1, <code>nums = [2,1,4]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length == target.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i], target[i] &lt;= 10<sup>8</sup></code></li>
</ul>

</div>

## Solution(Python)
```Python
class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
                # length of array
        n = len(nums)

        # calculate difference array 
        # includes +ve and -ve values
        diff = [target[i] - nums[i] for i in range(n)]

        # the initial difference has to fully contribute to operations.
        min_ops = abs(diff[0])

        # loop through rest of the array
        for i in range(1, n):

            # if both differences are positive,
            if diff[i-1] >= 0 and diff[i] >= 0:

                # the subsequent difference will only add operations if it is
                # bigger than the previous difference
                min_ops += max(diff[i] - diff[i - 1], 0)
            
            # if both differences are negative,
            elif diff[i-1] <= 0 and diff[i] <= 0:
                # the subsequent difference will only add operations if it is
                # more negative than the previous difference
                min_ops += max(abs(diff[i]) - abs(diff[i - 1]), 0)
            
            # if both differences are opposite parity,
            else:
                # the difference contributes fully to operations
                min_ops += abs(diff[i])
        
        return min_ops
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "3229. Minimum Operations to Make Array Equal to Target",
    "text": "You are given two positive integer arrays nums and target, of the same length.\nIn a single operation, you can select any subarray of nums and increment each element within that subarray by 1 or decrement each element within that subarray by 1.\nReturn the minimum number of operations required to make nums equal to the array target.\n\u00a0\nExample 1:\n\nInput: nums = [3,5,1,2], target = [4,6,2,4]\nOutput: 2\nExplanation:\nWe will perform the following operations to make nums equal to target:\n- Increment\u00a0nums[0..3] by 1, nums = [4,6,2,3].\n- Increment\u00a0nums[3..3] by 1, nums = [4,6,2,4].\n\nExample 2:\n\nInput: nums = [1,3,2], target = [2,1,4]\nOutput: 5\nExplanation:\nWe will perform the following operations to make nums equal to target:\n- Increment\u00a0nums[0..0] by 1, nums = [2,3,2].\n- Decrement\u00a0nums[1..1] by 1, nums = [2,2,2].\n- Decrement\u00a0nums[1..1] by 1, nums = [2,1,2].\n- Increment\u00a0nums[2..2] by 1, nums = [2,1,3].\n- Increment\u00a0nums[2..2] by 1, nums = [2,1,4].\n\n\u00a0\nConstraints:\n\n1 <= nums.length == target.length <= 105\n1 <= nums[i], target[i] <= 108\n\n",
    "url": "https://leetcode.com/problems/3229-minimum-operations-to-make-array-equal-to-target",
    "answerCount": 1,
    "datePublished": "2025-10-09T23:04:36+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def minimumOperations(self, nums: List[int], target: List[int]) -> int:\n                # length of array\n        n = len(nums)\n\n        # calculate difference array \n        # includes +ve and -ve values\n        diff = [target[i] - nums[i] for i in range(n)]\n\n        # the initial difference has to fully contribute to operations.\n        min_ops = abs(diff[0])\n\n        # loop through rest of the array\n        for i in range(1, n):\n\n            # if both differences are positive,\n            if diff[i-1] >= 0 and diff[i] >= 0:\n\n                # the subsequent difference will only add operations if it is\n                # bigger than the previous difference\n                min_ops += max(diff[i] - diff[i - 1], 0)\n            \n            # if both differences are negative,\n            elif diff[i-1] <= 0 and diff[i] <= 0:\n                # the subsequent difference will only add operations if it is\n                # more negative than the previous difference\n                min_ops += max(abs(diff[i]) - abs(diff[i - 1]), 0)\n            \n            # if both differences are opposite parity,\n            else:\n                # the difference contributes fully to operations\n                min_ops += abs(diff[i])\n        \n        return min_ops",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/3229-minimum-operations-to-make-array-equal-to-target/",
      "datePublished": "2025-10-09T23:04:36+05:30",
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