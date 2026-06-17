# 98-validate-binary-search-tree


Try it on <a href='https://leetcode.com/problems/98-validate-binary-search-tree'>leetcode</a>

## Description
<div class="description">
<div><p>Given the <code>root</code> of a binary tree, <em>determine if it is a valid binary search tree (BST)</em>.</p>

<p>A <strong>valid BST</strong> is defined as follows:</p>

<ul>
	<li>The left subtree of a node contains only nodes with keys <strong>less than</strong> the node's key.</li>
	<li>The right subtree of a node contains only nodes with keys <strong>greater than</strong> the node's key.</li>
	<li>Both the left and right subtrees must also be binary search trees.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg" style="width: 302px; height: 182px;">
<pre><strong>Input:</strong> root = [2,1,3]
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg" style="width: 422px; height: 292px;">
<pre><strong>Input:</strong> root = [5,1,4,null,null,3,6]
<strong>Output:</strong> false
<strong>Explanation:</strong> The root node's value is 5 but its right child's value is 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-2<sup>31</sup> &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code></li>
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.naive(root)

    # Time Complexity: O(n)
    # Space Complexity: O(h)
    def naive(self, root: Optional[TreeNode]) -> bool:
        def inorder(node):
            if node:
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)

        res = []
        inorder(root)
        if len(res) == 2:
            return res[0] < res[1]
        for i in range(1, len(res) - 1):
            if not (res[i - 1] < res[i] < res[i + 1]):
                return False
        return True

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "98. Validate Binary Search Tree",
    "text": "Given the root of a binary tree, determine if it is a valid binary search tree (BST).\nA valid BST is defined as follows:\n\nThe left subtree of a node contains only nodes with keys less than the node's key.\nThe right subtree of a node contains only nodes with keys greater than the node's key.\nBoth the left and right subtrees must also be binary search trees.\n\n\u00a0\nExample 1:\n\nInput: root = [2,1,3]\nOutput: true\n\nExample 2:\n\nInput: root = [5,1,4,null,null,3,6]\nOutput: false\nExplanation: The root node's value is 5 but its right child's value is 4.\n\n\u00a0\nConstraints:\n\nThe number of nodes in the tree is in the range [1, 104].\n-231 <= Node.val <= 231 - 1\n\n",
    "url": "https://leetcode.com/problems/98-validate-binary-search-tree",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def isValidBST(self, root: Optional[TreeNode]) -> bool:\n        return self.naive(root)\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(h)\n    def naive(self, root: Optional[TreeNode]) -> bool:\n        def inorder(node):\n            if node:\n                inorder(node.left)\n                res.append(node.val)\n                inorder(node.right)\n\n        res = []\n        inorder(root)\n        if len(res) == 2:\n            return res[0] < res[1]\n        for i in range(1, len(res) - 1):\n            if not (res[i - 1] < res[i] < res[i + 1]):\n                return False\n        return True\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/98-validate-binary-search-tree/",
      "datePublished": "2025-08-23",
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