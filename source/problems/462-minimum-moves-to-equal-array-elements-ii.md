# 462-minimum-moves-to-equal-array-elements-ii


Try it on <a href='https://leetcode.com/problems/462-minimum-moves-to-equal-array-elements-ii'>leetcode</a>

## Description
<div class="description">
<div><p>Given an integer array <code>nums</code> of size <code>n</code>, return <em>the minimum number of moves required to make all array elements equal</em>.</p>

<p>In one move, you can increment or decrement an element of the array by <code>1</code>.</p>

<p>Test cases are designed so that the answer will fit in a <strong>32-bit</strong> integer.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
Only two moves are needed (remember each move increments or decrements one element):
[<u>1</u>,2,3]  =&gt;  [2,2,<u>3</u>]  =&gt;  [2,2,2]
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,10,2,9]
<strong>Output:</strong> 16
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        return self.sorting(nums)

    # Time Complexity: O(nlogn)
    # Space Complexity: O(1)
    def sorting(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        median = nums[n // 2]
        steps = 0
        for num in nums:
            steps += abs(median - num)
        return steps

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "462. Minimum Moves to Equal Array Elements II",
    "text": "Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.\nIn one move, you can increment or decrement an element of the array by 1.\nTest cases are designed so that the answer will fit in a 32-bit integer.\n\u00a0\nExample 1:\nInput: nums = [1,2,3]\nOutput: 2\nExplanation:\nOnly two moves are needed (remember each move increments or decrements one element):\n[1,2,3]  =>  [2,2,3]  =>  [2,2,2]\n\nExample 2:\nInput: nums = [1,10,2,9]\nOutput: 16\n\n\u00a0\nConstraints:\n\nn == nums.length\n1 <= nums.length <= 105\n-109 <= nums[i] <= 109\n\n",
    "url": "https://leetcode.com/problems/462-minimum-moves-to-equal-array-elements-ii",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def minMoves2(self, nums: List[int]) -> int:\n        return self.sorting(nums)\n\n    # Time Complexity: O(nlogn)\n    # Space Complexity: O(1)\n    def sorting(self, nums: List[int]) -> int:\n        nums.sort()\n        n = len(nums)\n        median = nums[n // 2]\n        steps = 0\n        for num in nums:\n            steps += abs(median - num)\n        return steps\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/462-minimum-moves-to-equal-array-elements-ii/",
      "datePublished": "2024-07-12",
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