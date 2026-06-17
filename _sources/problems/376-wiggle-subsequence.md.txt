# 376-wiggle-subsequence


Try it on <a href='https://leetcode.com/problems/376-wiggle-subsequence'>leetcode</a>

## Description
<div class="description">
<div><p>A <strong>wiggle sequence</strong> is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.</p>

<ul>
	<li>For example, <code>[1, 7, 4, 9, 2, 5]</code> is a <strong>wiggle sequence</strong> because the differences <code>(6, -3, 5, -7, 3)</code> alternate between positive and negative.</li>
	<li>In contrast, <code>[1, 4, 7, 2, 5]</code> and <code>[1, 7, 4, 5, 5]</code> are not wiggle sequences. The first is not because its first two differences are positive, and the second is not because its last difference is zero.</li>
</ul>

<p>A <strong>subsequence</strong> is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.</p>

<p>Given an integer array <code>nums</code>, return <em>the length of the longest <strong>wiggle subsequence</strong> of </em><code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,7,4,9,2,5]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,17,5,10,13,15,10,5,16,8]
<strong>Output:</strong> 7
<strong>Explanation:</strong> There are several subsequences that achieve this length.
One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3,4,5,6,7,8,9]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you solve this in <code>O(n)</code> time?</p>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        return self.spaceoptimizeddp(nums)

    # Time Complexity: O(n!)
    # Space Complexity: O(n)
    def bruteforce(self, nums: List[int]) -> int:
        def recur(nums, index, isUp):
            maxcnt = 0
            for i in range(index + 1, len(nums)):
                if (isUp and nums[i] > nums[i + 1]) or (
                    not isUp and nums[i] < nums[i + 1]
                ):
                    cnt = 1 + recur(nums, i, not isUp)
                    if cnt > maxcnt:
                        maxcnt = cnt
            return maxcnt

        if len(nums) < 2:
            return len(nums)

        return 1 + max(recur(nums, 0, True), recur(nums, 0, False))

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def dp(self, nums: List[int]) -> int:
        n = len(nums)
        up = [0] * n
        down = [0] * n
        up[0] = 1
        down[0] = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                down[i] = up[i - 1] + 1
                up[i] = up[i - 1]
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]

        return max(up[n - 1], down[n - 1])

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def spaceoptimizeddp(self, nums: List[int]) -> int:
        n = len(nums)
        curUp = 0
        curDown = 0
        prevUp = 1
        prevDown = 1

        if n == 1:
            return 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                curUp = prevDown + 1
                curDown = prevDown
            elif nums[i] < nums[i - 1]:
                curDown = prevUp + 1
                curUp = prevUp
            else:
                curUp = prevUp
                curDown = prevDown

            prevDown = curDown
            prevUp = curUp
        return max(curUp, curDown)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "376. Wiggle Subsequence",
    "text": "A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.\n\nFor example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative.\nIn contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. The first is not because its first two differences are positive, and the second is not because its last difference is zero.\n\nA subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.\nGiven an integer array nums, return the length of the longest wiggle subsequence of nums.\n\u00a0\nExample 1:\nInput: nums = [1,7,4,9,2,5]\nOutput: 6\nExplanation: The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).\n\nExample 2:\nInput: nums = [1,17,5,10,13,15,10,5,16,8]\nOutput: 7\nExplanation: There are several subsequences that achieve this length.\nOne is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).\n\nExample 3:\nInput: nums = [1,2,3,4,5,6,7,8,9]\nOutput: 2\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 1000\n0 <= nums[i] <= 1000\n\n\u00a0\nFollow up: Could you solve this in O(n) time?\n",
    "url": "https://leetcode.com/problems/376-wiggle-subsequence",
    "answerCount": 1,
    "datePublished": "2022-07-03T19:37:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def wiggleMaxLength(self, nums: List[int]) -> int:\n        return self.spaceoptimizeddp(nums)\n\n    # Time Complexity: O(n!)\n    # Space Complexity: O(n)\n    def bruteforce(self, nums: List[int]) -> int:\n        def recur(nums, index, isUp):\n            maxcnt = 0\n            for i in range(index + 1, len(nums)):\n                if (isUp and nums[i] > nums[i + 1]) or (\n                    not isUp and nums[i] < nums[i + 1]\n                ):\n                    cnt = 1 + recur(nums, i, not isUp)\n                    if cnt > maxcnt:\n                        maxcnt = cnt\n            return maxcnt\n\n        if len(nums) < 2:\n            return len(nums)\n\n        return 1 + max(recur(nums, 0, True), recur(nums, 0, False))\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(n)\n    def dp(self, nums: List[int]) -> int:\n        n = len(nums)\n        up = [0] * n\n        down = [0] * n\n        up[0] = 1\n        down[0] = 1\n        for i in range(1, n):\n            if nums[i] > nums[i - 1]:\n                up[i] = down[i - 1] + 1\n                down[i] = down[i - 1]\n            elif nums[i] < nums[i - 1]:\n                down[i] = up[i - 1] + 1\n                up[i] = up[i - 1]\n            else:\n                up[i] = up[i - 1]\n                down[i] = down[i - 1]\n\n        return max(up[n - 1], down[n - 1])\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(1)\n    def spaceoptimizeddp(self, nums: List[int]) -> int:\n        n = len(nums)\n        curUp = 0\n        curDown = 0\n        prevUp = 1\n        prevDown = 1\n\n        if n == 1:\n            return 1\n\n        for i in range(1, n):\n            if nums[i] > nums[i - 1]:\n                curUp = prevDown + 1\n                curDown = prevDown\n            elif nums[i] < nums[i - 1]:\n                curDown = prevUp + 1\n                curUp = prevUp\n            else:\n                curUp = prevUp\n                curDown = prevDown\n\n            prevDown = curDown\n            prevUp = curUp\n        return max(curUp, curDown)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/376-wiggle-subsequence/",
      "datePublished": "2022-07-03T19:37:59+05:30",
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