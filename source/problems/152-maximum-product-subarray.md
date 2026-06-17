# 152-maximum-product-subarray


Try it on <a href='https://leetcode.com/problems/152-maximum-product-subarray'>leetcode</a>

## Description
<div class="description">
<div><p>Given an integer array <code>nums</code>, find a contiguous non-empty subarray within the array that has the largest product, and return <em>the product</em>.</p>

<p>The test cases are generated so that the answer will fit in a <strong>32-bit</strong> integer.</p>

<p>A <strong>subarray</strong> is a contiguous subsequence of the array.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [2,3,-2,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> [2,3] has the largest product 6.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [-2,0,-1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The result cannot be 2, because [-2,-1] is not a subarray.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li>The product of any prefix or suffix of <code>nums</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        # max positive product
        # ending at the current position
        max_ending_here = arr[0]
        n = len(arr)

        # min negative product ending
        # at the current position
        min_ending_here = arr[0]

        # Initialize overall max product
        max_so_far = arr[0]

        # /* Traverse through the array.
        # the maximum product subarray ending at an index
        # will be the maximum of the element itself,
        # the product of element and max product ending previously
        # and the min product ending previously. */
        for i in range(1, n):
            temp = max(max(arr[i], arr[i] * max_ending_here), arr[i] * min_ending_here)
            min_ending_here = min(min(arr[i], arr[i] * max_ending_here), arr[i] * min_ending_here)
            max_ending_here = temp
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "152. Maximum Product Subarray",
    "text": "Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.\nThe test cases are generated so that the answer will fit in a 32-bit integer.\nA subarray is a contiguous subsequence of the array.\n\u00a0\nExample 1:\nInput: nums = [2,3,-2,4]\nOutput: 6\nExplanation: [2,3] has the largest product 6.\n\nExample 2:\nInput: nums = [-2,0,-1]\nOutput: 0\nExplanation: The result cannot be 2, because [-2,-1] is not a subarray.\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 2 * 104\n-10 <= nums[i] <= 10\nThe product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.\n\n",
    "url": "https://leetcode.com/problems/152-maximum-product-subarray",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def maxProduct(self, arr: List[int]) -> int:\n        # max positive product\n        # ending at the current position\n        max_ending_here = arr[0]\n        n = len(arr)\n\n        # min negative product ending\n        # at the current position\n        min_ending_here = arr[0]\n\n        # Initialize overall max product\n        max_so_far = arr[0]\n\n        # /* Traverse through the array.\n        # the maximum product subarray ending at an index\n        # will be the maximum of the element itself,\n        # the product of element and max product ending previously\n        # and the min product ending previously. */\n        for i in range(1, n):\n            temp = max(max(arr[i], arr[i] * max_ending_here), arr[i] * min_ending_here)\n            min_ending_here = min(min(arr[i], arr[i] * max_ending_here), arr[i] * min_ending_here)\n            max_ending_here = temp\n            max_so_far = max(max_so_far, max_ending_here)\n\n        return max_so_far",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/152-maximum-product-subarray/",
      "datePublished": "2024-11-19",
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