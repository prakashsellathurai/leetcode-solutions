# squares-of-a-sorted-array


Try it on <a href='https://leetcode.com/problems/squares-of-a-sorted-array'>leetcode</a>

## Description
<div class="description">
<div><p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing</strong> order, return <em>an array of <strong>the squares of each number</strong> sorted in non-decreasing order</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [-4,-1,0,3,10]
<strong>Output:</strong> [0,1,9,16,100]
<strong>Explanation:</strong> After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [-7,-3,2,3,11]
<strong>Output:</strong> [4,9,9,49,121]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code><span>1 &lt;= nums.length &lt;= </span>10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Squaring each element and sorting the new array is very trivial, could you find an <code>O(n)</code> solution using a different approach?</div>
</div>

## Solution(Python)
```Python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n =len(nums)
        left = 0
        right = n-1
        square = 0
        result = [0] * n
        for i in range(n-1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result
    
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": " \u00a0Squares of a Sorted Array",
    "text": "Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.\n\u00a0\nExample 1:\nInput: nums = [-4,-1,0,3,10]\nOutput: [0,1,9,16,100]\nExplanation: After squaring, the array becomes [16,1,0,9,100].\nAfter sorting, it becomes [0,1,9,16,100].\n\nExample 2:\nInput: nums = [-7,-3,2,3,11]\nOutput: [4,9,9,49,121]\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 104\n-104 <= nums[i] <= 104\nnums is sorted in non-decreasing order.\n\n\u00a0\nFollow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?",
    "url": "https://leetcode.com/problems/squares-of-a-sorted-array",
    "answerCount": 1,
    "datePublished": "2025-02-10T20:50:51+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def sortedSquares(self, nums: List[int]) -> List[int]:\n        n =len(nums)\n        left = 0\n        right = n-1\n        square = 0\n        result = [0] * n\n        for i in range(n-1, -1, -1):\n            if abs(nums[left]) < abs(nums[right]):\n                square = nums[right]\n                right -= 1\n            else:\n                square = nums[left]\n                left += 1\n            result[i] = square * square\n        return result\n    ",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/squares-of-a-sorted-array/",
      "datePublished": "2025-02-10T20:50:51+05:30",
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