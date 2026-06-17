# 456-132-pattern


Try it on <a href='https://leetcode.com/problems/456-132-pattern'>leetcode</a>

## Description
<div class="description">
<div><p>Given an array&nbsp;of <code>n</code> integers <code>nums</code>, a <strong>132 pattern</strong> is a subsequence of three integers <code>nums[i]</code>, <code>nums[j]</code> and <code>nums[k]</code> such that <code>i &lt; j &lt; k</code> and <code>nums[i] &lt; nums[k] &lt; nums[j]</code>.</p>

<p>Return <em><code>true</code> if there is a <strong>132 pattern</strong> in <code>nums</code>, otherwise, return <code>false</code>.</em></p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no 132 pattern in the sequence.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [3,1,4,2]
<strong>Output:</strong> true
<strong>Explanation:</strong> There is a 132 pattern in the sequence: [1, 4, 2].
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [-1,3,2,0]
<strong>Output:</strong> true
<strong>Explanation:</strong> There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        return self.arrayasstack(nums)

    # Time Compleity :O(n^3)
    # space Complexity: O(1)
    def bruteforce(self, nums):
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] < nums[k] < nums[j]:
                        return True

        return False

    # Time Compleity :O(n^2)
    # space Complexity: O(1)
    def betterbruteforce(self, nums):
        n = len(nums)
        min_i = inf

        for j in range(n):
            if nums[j] < min_i:
                min_i = nums[j]
            for k in range(j + 1, n):
                if min_i < nums[k] < nums[j]:
                    return True
        return False

    # Time Compleity :O(n^2)
    # space Complexity: O(n)
    def interval(self, nums):
        n = len(nums)
        intervals = []
        min_point_after_last_peak_index = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                if min_point_after_last_peak_index < i - 1:
                    intervals.append(
                        nums[min_point_after_last_peak_index], nums[i - 1])
            min_point_after_last_peak_index = i
            for i_num, j_num in intervals:
                if i_num < nums[i] < j_num:
                    return True
        return False

    # Time Compleity :O(n)
    # space Complexity: O(n)
    def stack(self, nums):
        n = len(nums)

        if n < 3:
            return False

        stack = []
        min_array = [-1] * n

        min_array[0] = nums[0]

        for i in range(1, n):
            min_array[i] = min(min_array[i - 1], nums[i])

        for j in range(n - 1, -1, -1):
            if nums[j] <= min_array[j]:
                continue
            while stack and stack[-1] <= min_array[j]:
                stack.pop()

            if stack and min_array[j] < stack[-1] < nums[j]:
                return True
            stack.append(nums[j])

        return False

    # Time Compleity :O(nlogn)
    # space Complexity: O(n)
    def binarysearch(self, nums):
        n = len(nums)

        if n < 3:
            return False

        min_array = [-1] * n
        min_array[0] = nums[0]
        min_array[0] = nums[0]

        for i in range(1, n):
            min_array[i] = min(min_array[i - 1], nums[i])

        k = n

        for j in range(n - 1, -1, -1):
            if nums[j] <= min_array[j]:
                continue
            k = bisect_left(nums, min_array[j] + 1, k, n)
            if k < n and min_array[j] < nums[k] < nums[j]:
                return True

            k -= 1
            nums[k] = nums[j]
        return False

    # Time Compleity :O(n)
    # space Complexity: O(n)
    def arrayasstack(self, nums):
        if len(nums) < 3:
            return False
        min_array = [-1] * len(nums)
        min_array[0] = nums[0]
        for i in range(1, len(nums)):
            min_array[i] = min(min_array[i - 1], nums[i])

        k = len(nums)
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] <= min_array[j]:
                continue
            while k < len(nums) and nums[k] <= min_array[j]:
                k += 1
            if k < len(nums) and nums[k] < nums[j]:
                return True
            k -= 1
            nums[k] = nums[j]
        return False

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "456. 132 Pattern",
    "text": "Given an array\u00a0of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].\nReturn true if there is a 132 pattern in nums, otherwise, return false.\n\u00a0\nExample 1:\nInput: nums = [1,2,3,4]\nOutput: false\nExplanation: There is no 132 pattern in the sequence.\n\nExample 2:\nInput: nums = [3,1,4,2]\nOutput: true\nExplanation: There is a 132 pattern in the sequence: [1, 4, 2].\n\nExample 3:\nInput: nums = [-1,3,2,0]\nOutput: true\nExplanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].\n\n\u00a0\nConstraints:\n\nn == nums.length\n1 <= n <= 2 * 105\n-109 <= nums[i] <= 109\n\n",
    "url": "https://leetcode.com/problems/456-132-pattern",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def find132pattern(self, nums: List[int]) -> bool:\n        return self.arrayasstack(nums)\n\n    # Time Compleity :O(n^3)\n    # space Complexity: O(1)\n    def bruteforce(self, nums):\n        n = len(nums)\n\n        for i in range(n):\n            for j in range(i + 1, n):\n                for k in range(j + 1, n):\n                    if nums[i] < nums[k] < nums[j]:\n                        return True\n\n        return False\n\n    # Time Compleity :O(n^2)\n    # space Complexity: O(1)\n    def betterbruteforce(self, nums):\n        n = len(nums)\n        min_i = inf\n\n        for j in range(n):\n            if nums[j] < min_i:\n                min_i = nums[j]\n            for k in range(j + 1, n):\n                if min_i < nums[k] < nums[j]:\n                    return True\n        return False\n\n    # Time Compleity :O(n^2)\n    # space Complexity: O(n)\n    def interval(self, nums):\n        n = len(nums)\n        intervals = []\n        min_point_after_last_peak_index = 0\n        for i in range(1, n):\n            if nums[i] < nums[i - 1]:\n                if min_point_after_last_peak_index < i - 1:\n                    intervals.append(\n                        nums[min_point_after_last_peak_index], nums[i - 1])\n            min_point_after_last_peak_index = i\n            for i_num, j_num in intervals:\n                if i_num < nums[i] < j_num:\n                    return True\n        return False\n\n    # Time Compleity :O(n)\n    # space Complexity: O(n)\n    def stack(self, nums):\n        n = len(nums)\n\n        if n < 3:\n            return False\n\n        stack = []\n        min_array = [-1] * n\n\n        min_array[0] = nums[0]\n\n        for i in range(1, n):\n            min_array[i] = min(min_array[i - 1], nums[i])\n\n        for j in range(n - 1, -1, -1):\n            if nums[j] <= min_array[j]:\n                continue\n            while stack and stack[-1] <= min_array[j]:\n                stack.pop()\n\n            if stack and min_array[j] < stack[-1] < nums[j]:\n                return True\n            stack.append(nums[j])\n\n        return False\n\n    # Time Compleity :O(nlogn)\n    # space Complexity: O(n)\n    def binarysearch(self, nums):\n        n = len(nums)\n\n        if n < 3:\n            return False\n\n        min_array = [-1] * n\n        min_array[0] = nums[0]\n        min_array[0] = nums[0]\n\n        for i in range(1, n):\n            min_array[i] = min(min_array[i - 1], nums[i])\n\n        k = n\n\n        for j in range(n - 1, -1, -1):\n            if nums[j] <= min_array[j]:\n                continue\n            k = bisect_left(nums, min_array[j] + 1, k, n)\n            if k < n and min_array[j] < nums[k] < nums[j]:\n                return True\n\n            k -= 1\n            nums[k] = nums[j]\n        return False\n\n    # Time Compleity :O(n)\n    # space Complexity: O(n)\n    def arrayasstack(self, nums):\n        if len(nums) < 3:\n            return False\n        min_array = [-1] * len(nums)\n        min_array[0] = nums[0]\n        for i in range(1, len(nums)):\n            min_array[i] = min(min_array[i - 1], nums[i])\n\n        k = len(nums)\n        for j in range(len(nums) - 1, -1, -1):\n            if nums[j] <= min_array[j]:\n                continue\n            while k < len(nums) and nums[k] <= min_array[j]:\n                k += 1\n            if k < len(nums) and nums[k] < nums[j]:\n                return True\n            k -= 1\n            nums[k] = nums[j]\n        return False\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/456-132-pattern/",
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