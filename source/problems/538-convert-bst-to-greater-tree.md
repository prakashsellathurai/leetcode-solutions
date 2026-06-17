# 538-convert-bst-to-greater-tree


Try it on <a href='https://leetcode.com/problems/538-convert-bst-to-greater-tree'>leetcode</a>

## Description
<div class="description">
<div><p>Given the <code>root</code> of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.</p>

<p>As a reminder, a <em>binary search tree</em> is a tree that satisfies these constraints:</p>

<ul>
	<li>The left subtree of a node contains only nodes with keys <strong>less than</strong> the node's key.</li>
	<li>The right subtree of a node contains only nodes with keys <strong>greater than</strong> the node's key.</li>
	<li>Both the left and right subtrees must also be binary search trees.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/05/02/tree.png" style="width: 500px; height: 341px;">
<pre><strong>Input:</strong> root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
<strong>Output:</strong> [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> root = [0,null,1]
<strong>Output:</strong> [1,null,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li>All the values in the tree are <strong>unique</strong>.</li>
	<li><code>root</code> is guaranteed to be a valid binary search tree.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as 1038: <a href="https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/" target="_blank">https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/</a></p>
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
    def __init__(self):
        self.total = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.reverseInorderMorris(root)

    def recursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is not None:
            self.recursive(root.right)
            self.total += root.val
            root.val = self.total
            self.recursive(root.left)
        return root

    def reverseInorderMorris(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def get_succ(node):
            succ = node.right
            while succ.left is not None and succ.left is not node:
                succ = succ.left
            return succ

        total = 0
        node = root
        while node is not None:
            if node.right is None:
                total += node.val
                node.val = total
                node = node.left
            else:
                succ = get_succ(node)
                if succ.left is None:
                    succ.left = node
                    node = node.right
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left
        return root

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "538. Convert BST to Greater Tree",
    "text": "Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.\nAs a reminder, a binary search tree is a tree that satisfies these constraints:\n\nThe left subtree of a node contains only nodes with keys less than the node's key.\nThe right subtree of a node contains only nodes with keys greater than the node's key.\nBoth the left and right subtrees must also be binary search trees.\n\n\u00a0\nExample 1:\n\nInput: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]\nOutput: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]\n\nExample 2:\nInput: root = [0,null,1]\nOutput: [1,null,1]\n\n\u00a0\nConstraints:\n\nThe number of nodes in the tree is in the range [0, 104].\n-104 <= Node.val <= 104\nAll the values in the tree are unique.\nroot is guaranteed to be a valid binary search tree.\n\n\u00a0\nNote: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/\n",
    "url": "https://leetcode.com/problems/538-convert-bst-to-greater-tree",
    "answerCount": 1,
    "datePublished": "2022-04-23T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def __init__(self):\n        self.total = 0\n\n    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:\n        return self.reverseInorderMorris(root)\n\n    def recursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:\n        if root is not None:\n            self.recursive(root.right)\n            self.total += root.val\n            root.val = self.total\n            self.recursive(root.left)\n        return root\n\n    def reverseInorderMorris(self, root: Optional[TreeNode]) -> Optional[TreeNode]:\n        def get_succ(node):\n            succ = node.right\n            while succ.left is not None and succ.left is not node:\n                succ = succ.left\n            return succ\n\n        total = 0\n        node = root\n        while node is not None:\n            if node.right is None:\n                total += node.val\n                node.val = total\n                node = node.left\n            else:\n                succ = get_succ(node)\n                if succ.left is None:\n                    succ.left = node\n                    node = node.right\n                else:\n                    succ.left = None\n                    total += node.val\n                    node.val = total\n                    node = node.left\n        return root\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/538-convert-bst-to-greater-tree/",
      "datePublished": "2022-04-23T00:00:00Z",
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