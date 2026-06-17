# 543-diameter-of-binary-tree


Try it on <a href='https://leetcode.com/problems/543-diameter-of-binary-tree'>leetcode</a>

## Description
<div class="description">
<div><p>Given the <code>root</code> of a binary tree, return <em>the length of the <strong>diameter</strong> of the tree</em>.</p>

<p>The <strong>diameter</strong> of a binary tree is the <strong>length</strong> of the longest path between any two nodes in a tree. This path may or may not pass through the <code>root</code>.</p>

<p>The <strong>length</strong> of a path between two nodes is represented by the number of edges between them.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg" style="width: 292px; height: 302px;">
<pre><strong>Input:</strong> root = [1,2,3,4,5]
<strong>Output:</strong> 3
<strong>Explanation:</strong> 3 is the length of the path [4,2,1,3] or [5,2,1,3].
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> root = [1,2]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.optimize(root)

    # Time Complexity: O(n^2)
    # Space Complexity: O(H)
    def bruteforce(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        lheight = self.height(node.left)
        rheight = self.height(node.right)

        ldiameter = self.bruteforce(node.left)
        rdiameter = self.bruteforce(node.right)

        return max(lheight + rheight, max(ldiameter, rdiameter))

    # Time Complexity: O(n)
    # Space Complexity: O(H)
    def optimize(self, node: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            if node is None:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            cur_width = left_height + right_height

            if cur_width > ans:
                ans = cur_width

            return 1 + max(left_height, right_height)

        dfs(node)
        return ans

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "543. Diameter of Binary Tree",
    "text": "Given the root of a binary tree, return the length of the diameter of the tree.\nThe diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.\nThe length of a path between two nodes is represented by the number of edges between them.\n\u00a0\nExample 1:\n\nInput: root = [1,2,3,4,5]\nOutput: 3\nExplanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].\n\nExample 2:\nInput: root = [1,2]\nOutput: 1\n\n\u00a0\nConstraints:\n\nThe number of nodes in the tree is in the range [1, 104].\n-100 <= Node.val <= 100\n\n",
    "url": "https://leetcode.com/problems/543-diameter-of-binary-tree",
    "answerCount": 1,
    "datePublished": "2023-06-23T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:\n        return self.optimize(root)\n\n    # Time Complexity: O(n^2)\n    # Space Complexity: O(H)\n    def bruteforce(self, node: Optional[TreeNode]) -> int:\n        if node is None:\n            return 0\n\n        lheight = self.height(node.left)\n        rheight = self.height(node.right)\n\n        ldiameter = self.bruteforce(node.left)\n        rdiameter = self.bruteforce(node.right)\n\n        return max(lheight + rheight, max(ldiameter, rdiameter))\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(H)\n    def optimize(self, node: Optional[TreeNode]) -> int:\n        ans = 0\n\n        def dfs(node):\n            nonlocal ans\n            if node is None:\n                return 0\n\n            left_height = dfs(node.left)\n            right_height = dfs(node.right)\n\n            cur_width = left_height + right_height\n\n            if cur_width > ans:\n                ans = cur_width\n\n            return 1 + max(left_height, right_height)\n\n        dfs(node)\n        return ans\n\n    def height(self, node):\n        if node is None:\n            return 0\n        return 1 + max(self.height(node.left), self.height(node.right))\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/543-diameter-of-binary-tree/",
      "datePublished": "2023-06-23T00:00:00Z",
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