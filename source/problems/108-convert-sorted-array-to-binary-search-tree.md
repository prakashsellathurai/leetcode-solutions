# 108-convert-sorted-array-to-binary-search-tree


Try it on <a href='https://leetcode.com/problems/108-convert-sorted-array-to-binary-search-tree'>leetcode</a>

## Description
<div class="description">
<div><p>Given an integer array <code>nums</code> where the elements are sorted in <strong>ascending order</strong>, convert <em>it to a <strong>height-balanced</strong> binary search tree</em>.</p>

<p>A <strong>height-balanced</strong> binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg" style="width: 302px; height: 222px;">
<pre><strong>Input:</strong> nums = [-10,-3,0,5,9]
<strong>Output:</strong> [0,-3,9,-10,null,5]
<strong>Explanation:</strong> [0,-10,5,null,-3,null,9] is also accepted:
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg" style="width: 302px; height: 222px;">
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree.jpg" style="width: 342px; height: 142px;">
<pre><strong>Input:</strong> nums = [1,3]
<strong>Output:</strong> [3,1]
<strong>Explanation:</strong> [1,null,3] and [3,1] are both height-balanced BSTs.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> is sorted in a <strong>strictly increasing</strong> order.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        n = len(nums)
        mid = n // 2
        val = nums[mid]
        left = self.sortedArrayToBST(nums[:mid])
        right = self.sortedArrayToBST(nums[mid+1:])
        return TreeNode(val, left, right)
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "108. Convert Sorted Array to Binary Search Tree",
    "text": "Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.\nA height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.\n\u00a0\nExample 1:\n\nInput: nums = [-10,-3,0,5,9]\nOutput: [0,-3,9,-10,null,5]\nExplanation: [0,-10,5,null,-3,null,9] is also accepted:\n\n\nExample 2:\n\nInput: nums = [1,3]\nOutput: [3,1]\nExplanation: [1,null,3] and [3,1] are both height-balanced BSTs.\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 104\n-104 <= nums[i] <= 104\nnums is sorted in a strictly increasing order.\n\n",
    "url": "https://leetcode.com/problems/108-convert-sorted-array-to-binary-search-tree",
    "answerCount": 1,
    "datePublished": "2026-05-18T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:\n        if not nums:\n            return None\n        n = len(nums)\n        mid = n // 2\n        val = nums[mid]\n        left = self.sortedArrayToBST(nums[:mid])\n        right = self.sortedArrayToBST(nums[mid+1:])\n        return TreeNode(val, left, right)",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/108-convert-sorted-array-to-binary-search-tree/",
      "datePublished": "2026-05-18T00:00:00Z",
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