# 1480-running-sum-of-1d-array


Try it on <a href='https://leetcode.com/problems/1480-running-sum-of-1d-array'>leetcode</a>

## Description
<div class="description">
<div><p>Given an array <code>nums</code>. We define a running sum of an array as&nbsp;<code>runningSum[i] = sum(nums[0]…nums[i])</code>.</p>

<p>Return the running sum of <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [1,3,6,10]
<strong>Explanation:</strong> Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,1,1,1,1]
<strong>Output:</strong> [1,2,3,4,5]
<strong>Explanation:</strong> Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [3,1,2,10,1]
<strong>Output:</strong> [3,4,6,16,17]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-10^6&nbsp;&lt;= nums[i] &lt;=&nbsp;10^6</code></li>
</ul></div>
</div>

## Solution(Python)
```Python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return self.inline(nums)

    # Time Complexity: O(n^2)
    def naive(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        for i in range(n):
            res[i] = sum(nums[j] for j in range(i + 1))
        return res

    # Time Complexity: O(n)
    def better(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        for i in range(n):
            if i == 0:
                res[i] = nums[i]
            else:
                res[i] = res[i - 1] + nums[i]
        return res

    # Time Complexity: O(n)
    def builtinfunc(self, nums: List[int]) -> List[int]:
        return accumulate(nums)

    # Time Complexity: O(n)
    def inline(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        return nums

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1480. Running Sum of 1d Array",
    "text": "Given an array nums. We define a running sum of an array as\u00a0runningSum[i] = sum(nums[0]\u2026nums[i]).\nReturn the running sum of nums.\n\u00a0\nExample 1:\nInput: nums = [1,2,3,4]\nOutput: [1,3,6,10]\nExplanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].\nExample 2:\nInput: nums = [1,1,1,1,1]\nOutput: [1,2,3,4,5]\nExplanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].\nExample 3:\nInput: nums = [3,1,2,10,1]\nOutput: [3,4,6,16,17]\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 1000\n-10^6\u00a0<= nums[i] <=\u00a010^6\n",
    "url": "https://leetcode.com/problems/1480-running-sum-of-1d-array",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def runningSum(self, nums: List[int]) -> List[int]:\n        return self.inline(nums)\n\n    # Time Complexity: O(n^2)\n    def naive(self, nums: List[int]) -> List[int]:\n        n = len(nums)\n        res = [0] * n\n        for i in range(n):\n            res[i] = sum(nums[j] for j in range(i + 1))\n        return res\n\n    # Time Complexity: O(n)\n    def better(self, nums: List[int]) -> List[int]:\n        n = len(nums)\n        res = [0] * n\n        for i in range(n):\n            if i == 0:\n                res[i] = nums[i]\n            else:\n                res[i] = res[i - 1] + nums[i]\n        return res\n\n    # Time Complexity: O(n)\n    def builtinfunc(self, nums: List[int]) -> List[int]:\n        return accumulate(nums)\n\n    # Time Complexity: O(n)\n    def inline(self, nums: List[int]) -> List[int]:\n        n = len(nums)\n        for i in range(1, n):\n            nums[i] += nums[i - 1]\n        return nums\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1480-running-sum-of-1d-array/",
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