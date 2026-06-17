# path-sum


Try it on <a href='https://leetcode.com/problems/path-sum'>leetcode</a>

## Description
<div class="description">
<div><p>Given the <code>root</code> of a binary tree and an integer <code>targetSum</code>, return <code>true</code> if the tree has a <strong>root-to-leaf</strong> path such that adding up all the values along the path equals <code>targetSum</code>.</p>

<p>A <strong>leaf</strong> is a node with no children.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg" style="width: 500px; height: 356px;">
<pre><strong>Input:</strong> root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
<strong>Output:</strong> true
<strong>Explanation:</strong> The root-to-leaf path with the target sum is shown.
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg">
<pre><strong>Input:</strong> root = [1,2,3], targetSum = 5
<strong>Output:</strong> false
<strong>Explanation:</strong> There two root-to-leaf paths in the tree:
(1 --&gt; 2): The sum is 3.
(1 --&gt; 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> root = [], targetSum = 0
<strong>Output:</strong> false
<strong>Explanation:</strong> Since the tree is empty, there are no root-to-leaf paths.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 5000]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
	<li><code>-1000 &lt;= targetSum &lt;= 1000</code></li>
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans = 0
        subSum = targetSum - (root.val if root is not None else 0)

        # If we reach a leaf node and sum becomes 0, then
        # return True
        if root and subSum == 0 and root.left == None and root.right == None:
            return True

        # Otherwise check both subtrees
        if root and root.left is not None:
            ans = ans or self.hasPathSum(root.left, subSum)
        if root and root.right is not None:
            ans = ans or self.hasPathSum(root.right, subSum)

        return ans

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "112. Path Sum",
    "text": "Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.\nA leaf is a node with no children.\n\u00a0\nExample 1:\n\nInput: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22\nOutput: true\nExplanation: The root-to-leaf path with the target sum is shown.\n\nExample 2:\n\nInput: root = [1,2,3], targetSum = 5\nOutput: false\nExplanation: There two root-to-leaf paths in the tree:\n(1 --> 2): The sum is 3.\n(1 --> 3): The sum is 4.\nThere is no root-to-leaf path with sum = 5.\n\nExample 3:\nInput: root = [], targetSum = 0\nOutput: false\nExplanation: Since the tree is empty, there are no root-to-leaf paths.\n\n\u00a0\nConstraints:\n\nThe number of nodes in the tree is in the range [0, 5000].\n-1000 <= Node.val <= 1000\n-1000 <= targetSum <= 1000\n\n",
    "url": "https://leetcode.com/problems/path-sum",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:\n        ans = 0\n        subSum = targetSum - (root.val if root is not None else 0)\n\n        # If we reach a leaf node and sum becomes 0, then\n        # return True\n        if root and subSum == 0 and root.left == None and root.right == None:\n            return True\n\n        # Otherwise check both subtrees\n        if root and root.left is not None:\n            ans = ans or self.hasPathSum(root.left, subSum)\n        if root and root.right is not None:\n            ans = ans or self.hasPathSum(root.right, subSum)\n\n        return ans\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/path-sum/",
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