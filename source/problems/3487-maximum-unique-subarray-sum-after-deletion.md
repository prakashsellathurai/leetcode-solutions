# 3487-maximum-unique-subarray-sum-after-deletion


Try it on <a href='https://leetcode.com/problems/3487-maximum-unique-subarray-sum-after-deletion'>leetcode</a>

## Description
<div class="description">
<p>You are given an integer array <code>nums</code>.</p>

<p>You are allowed to delete any number of elements from <code>nums</code> without making it <strong>empty</strong>. After performing the deletions, select a <span data-keyword="subarray-nonempty">subarray</span> of <code>nums</code> such that:</p>

<ol>
	<li>All elements in the subarray are <strong>unique</strong>.</li>
	<li>The sum of the elements in the subarray is <strong>maximized</strong>.</li>
</ol>

<p>Return the <strong>maximum sum</strong> of such a subarray.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">15</span></p>

<p><strong>Explanation:</strong></p>

<p>Select the entire array without deleting any element to obtain the maximum sum.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,0,1,1]</span></p>

<p><strong>Output:</strong> 1</p>

<p><strong>Explanation:</strong></p>

<p>Delete the element <code>nums[0] == 1</code>, <code>nums[1] == 1</code>, <code>nums[2] == 0</code>, and <code>nums[3] == 1</code>. Select the entire array <code>[1]</code> to obtain the maximum sum.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,-1,-2,1,0,-1]</span></p>

<p><strong>Output:</strong> 3</p>

<p><strong>Explanation:</strong></p>

<p>Delete the elements <code>nums[2] == -1</code> and <code>nums[3] == -2</code>, and select the subarray <code>[2, 1]</code> from <code>[1, 2, 1, 0, -1]</code> to obtain the maximum sum.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
</ul>

</div>

## Solution(Python)
```Python
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def maxSum(self, nums: List[int]) -> int:
        positiveSet = set([num for num in nums if num > 0])
        return max(nums) if len(positiveSet) == 0 else sum(positiveSet)
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "3487. Maximum Unique Subarray Sum After Deletion",
    "text": "You are given an integer array nums.\nYou are allowed to delete any number of elements from nums without making it empty. After performing the deletions, select a subarray of nums such that:\n\nAll elements in the subarray are unique.\nThe sum of the elements in the subarray is maximized.\n\nReturn the maximum sum of such a subarray.\n\u00a0\nExample 1:\n\nInput: nums = [1,2,3,4,5]\nOutput: 15\nExplanation:\nSelect the entire array without deleting any element to obtain the maximum sum.\n\nExample 2:\n\nInput: nums = [1,1,0,1,1]\nOutput: 1\nExplanation:\nDelete the element nums[0] == 1, nums[1] == 1, nums[2] == 0, and nums[3] == 1. Select the entire array [1] to obtain the maximum sum.\n\nExample 3:\n\nInput: nums = [1,2,-1,-2,1,0,-1]\nOutput: 3\nExplanation:\nDelete the elements nums[2] == -1 and nums[3] == -2, and select the subarray [2, 1] from [1, 2, 1, 0, -1] to obtain the maximum sum.\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 100\n-100 <= nums[i] <= 100\n\n",
    "url": "https://leetcode.com/problems/3487-maximum-unique-subarray-sum-after-deletion",
    "answerCount": 1,
    "datePublished": "2023-09-07T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    # Time Complexity: O(n)\n    # Space Complexity: O(n)\n    def maxSum(self, nums: List[int]) -> int:\n        positiveSet = set([num for num in nums if num > 0])\n        return max(nums) if len(positiveSet) == 0 else sum(positiveSet)",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/3487-maximum-unique-subarray-sum-after-deletion/",
      "datePublished": "2023-09-07T00:00:00Z",
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