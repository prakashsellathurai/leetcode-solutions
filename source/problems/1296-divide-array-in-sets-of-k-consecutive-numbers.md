# 1296-divide-array-in-sets-of-k-consecutive-numbers


Try it on <a href='https://leetcode.com/problems/1296-divide-array-in-sets-of-k-consecutive-numbers'>leetcode</a>

## Description
<div class="description">
<p>Given an array of integers <code>nums</code> and a positive integer <code>k</code>, check whether it is possible to divide this array into sets of <code>k</code> consecutive numbers.</p>

<p>Return <code>true</code> <em>if it is possible</em>.<strong> </strong>Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,3,4,4,5,6], k = 4
<strong>Output:</strong> true
<strong>Explanation:</strong> Array can be divided into [1,2,3,4] and [3,4,5,6].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
<strong>Output:</strong> true
<strong>Explanation:</strong> Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4], k = 3
<strong>Output:</strong> false
<strong>Explanation:</strong> Each array should be divided in subarrays of size 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<strong>Note:</strong> This question is the same as&nbsp;846:&nbsp;<a href="https://leetcode.com/problems/hand-of-straights/" target="_blank">https://leetcode.com/problems/hand-of-straights/</a>
</div>

## Solution(Python)
```Python
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False
        counts = Counter(nums)
        for num in sorted(nums):
            if counts[num] > 0:
                for consecutive_num in range(num, num + k):
                    if counts[consecutive_num] == 0:
                        return False
                    counts[consecutive_num] -= 1
        return True
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1296. Divide Array in Sets of K Consecutive Numbers",
    "text": "Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.\nReturn true if it is possible. Otherwise, return false.\n\u00a0\nExample 1:\n\nInput: nums = [1,2,3,3,4,4,5,6], k = 4\nOutput: true\nExplanation: Array can be divided into [1,2,3,4] and [3,4,5,6].\n\nExample 2:\n\nInput: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3\nOutput: true\nExplanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].\n\nExample 3:\n\nInput: nums = [1,2,3,4], k = 3\nOutput: false\nExplanation: Each array should be divided in subarrays of size 3.\n\n\u00a0\nConstraints:\n\n1 <= k <= nums.length <= 105\n1 <= nums[i] <= 109\n\n\u00a0\nNote: This question is the same as\u00a0846:\u00a0https://leetcode.com/problems/hand-of-straights/",
    "url": "https://leetcode.com/problems/1296-divide-array-in-sets-of-k-consecutive-numbers",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def isPossibleDivide(self, nums: List[int], k: int) -> bool:\n        n = len(nums)\n        if n % k != 0:\n            return False\n        counts = Counter(nums)\n        for num in sorted(nums):\n            if counts[num] > 0:\n                for consecutive_num in range(num, num + k):\n                    if counts[consecutive_num] == 0:\n                        return False\n                    counts[consecutive_num] -= 1\n        return True",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1296-divide-array-in-sets-of-k-consecutive-numbers/",
      "datePublished": "2024-11-11",
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