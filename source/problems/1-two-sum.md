# 1-two-sum


Try it on <a href='https://leetcode.com/problems/1-two-sum'>leetcode</a>

## Description
<div class="description">
<div><p>Given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Output:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than&nbsp;<code>O(n<sup>2</sup>)&nbsp;</code>time complexity?</div>
</div>

## Solution(Python)
```Python
class Solution:
    # Input: nums array
    # Output: return the index of two numbers in a Tuple
    #
    # Assumption: only one solution exists
    # Constraints:
    #   1.-10^9 <= nums[i],target <= 10^9
    #   2.2<=nums.length<= 10^4
    #
    #
    # BruteForce: Do exactly what was given in the problems
    #  run two loops to find the numbers that sums to target and
    #   return their target
    #
    # Time Complexity:O(n^2)
    # Space Complexity:O(1)
    #
    # Optimised Approach: we can skip the inside second loop
    # via caching it in the memory i.e a Hashmap
    #
    # since our condition is num1 + num2 = target
    # which implies
    #  num2 = target - num1
    # so if we cache num1 in the hashmap
    # and then later if we found target - num1
    # then num1 and num2 are our required answer
    #
    # Time Complexity:O(n)
    # on average Time Compleixty is 2n so at worst caseit's O(n)
    #
    # Space Complexity:O(n)
    #   extra space for hashmap of size n here we trade extra space for speed
    #
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # Hashmap to store num
        n = len(nums)

        for i in range(n):
            num1 = nums[i]
            num2 = target - num1

            if num2 in hashmap:  # if num2 in found we got the match
                return [i, hashmap[num2]]
            hashmap[num1] = i

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1. Two Sum",
    "text": "Given an array of integers nums\u00a0and an integer target, return indices of the two numbers such that they add up to target.\nYou may assume that each input would have exactly one solution, and you may not use the same element twice.\nYou can return the answer in any order.\n\u00a0\nExample 1:\nInput: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nOutput: Because nums[0] + nums[1] == 9, we return [0, 1].\n\nExample 2:\nInput: nums = [3,2,4], target = 6\nOutput: [1,2]\n\nExample 3:\nInput: nums = [3,3], target = 6\nOutput: [0,1]\n\n\u00a0\nConstraints:\n\n2 <= nums.length <= 104\n-109 <= nums[i] <= 109\n-109 <= target <= 109\nOnly one valid answer exists.\n\n\u00a0\nFollow-up:\u00a0Can you come up with an algorithm that is less than\u00a0O(n2)\u00a0time complexity?",
    "url": "https://leetcode.com/problems/1-two-sum",
    "answerCount": 1,
    "datePublished": "2025-01-30T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    # Input: nums array\n    # Output: return the index of two numbers in a Tuple\n    #\n    # Assumption: only one solution exists\n    # Constraints:\n    #   1.-10^9 <= nums[i],target <= 10^9\n    #   2.2<=nums.length<= 10^4\n    #\n    #\n    # BruteForce: Do exactly what was given in the problems\n    #  run two loops to find the numbers that sums to target and\n    #   return their target\n    #\n    # Time Complexity:O(n^2)\n    # Space Complexity:O(1)\n    #\n    # Optimised Approach: we can skip the inside second loop\n    # via caching it in the memory i.e a Hashmap\n    #\n    # since our condition is num1 + num2 = target\n    # which implies\n    #  num2 = target - num1\n    # so if we cache num1 in the hashmap\n    # and then later if we found target - num1\n    # then num1 and num2 are our required answer\n    #\n    # Time Complexity:O(n)\n    # on average Time Compleixty is 2n so at worst caseit's O(n)\n    #\n    # Space Complexity:O(n)\n    #   extra space for hashmap of size n here we trade extra space for speed\n    #\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        hashmap = {}  # Hashmap to store num\n        n = len(nums)\n\n        for i in range(n):\n            num1 = nums[i]\n            num2 = target - num1\n\n            if num2 in hashmap:  # if num2 in found we got the match\n                return [i, hashmap[num2]]\n            hashmap[num1] = i\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1-two-sum/",
      "datePublished": "2025-01-30T00:00:00Z",
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