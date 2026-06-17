# 669-trim-a-binary-search-tree


Try it on <a href='https://leetcode.com/problems/669-trim-a-binary-search-tree'>leetcode</a>

## Description
<div class="description">
<div><p>Given the <code>root</code> of a binary search tree and the lowest and highest boundaries as <code>low</code> and <code>high</code>, trim the tree so that all its elements lies in <code>[low, high]</code>. Trimming the tree should <strong>not</strong> change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a <strong>unique answer</strong>.</p>

<p>Return <em>the root of the trimmed binary search tree</em>. Note that the root may change depending on the given bounds.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/trim1.jpg" style="width: 450px; height: 126px;">
<pre><strong>Input:</strong> root = [1,0,2], low = 1, high = 2
<strong>Output:</strong> [1,null,2]
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/trim2.jpg" style="width: 450px; height: 277px;">
<pre><strong>Input:</strong> root = [3,0,4,null,2,null,null,1], low = 1, high = 3
<strong>Output:</strong> [3,2,null,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li>The value of each node in the tree is <strong>unique</strong>.</li>
	<li><code>root</code> is guaranteed to be a valid binary search tree.</li>
	<li><code>0 &lt;= low &lt;= high &lt;= 10<sup>4</sup></code></li>
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
    def trimBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        return self.recursive(root, low, high)

    def recursive(
        self, node: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        if not node:
            return None
        elif node.val > high:
            return self.recursive(node.left, low, high)
        elif node.val < low:
            return self.recursive(node.right, low, high)
        else:
            node.left = self.recursive(node.left, low, high)
            node.right = self.recursive(node.right, low, high)
            return node

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "669. Trim a Binary Search Tree",
    "text": "Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.\nReturn the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.\n\u00a0\nExample 1:\n\nInput: root = [1,0,2], low = 1, high = 2\nOutput: [1,null,2]\n\nExample 2:\n\nInput: root = [3,0,4,null,2,null,null,1], low = 1, high = 3\nOutput: [3,2,null,1]\n\n\u00a0\nConstraints:\n\nThe number of nodes in the tree in the range [1, 104].\n0 <= Node.val <= 104\nThe value of each node in the tree is unique.\nroot is guaranteed to be a valid binary search tree.\n0 <= low <= high <= 104\n\n",
    "url": "https://leetcode.com/problems/669-trim-a-binary-search-tree",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def trimBST(\n        self, root: Optional[TreeNode], low: int, high: int\n    ) -> Optional[TreeNode]:\n        return self.recursive(root, low, high)\n\n    def recursive(\n        self, node: Optional[TreeNode], low: int, high: int\n    ) -> Optional[TreeNode]:\n        if not node:\n            return None\n        elif node.val > high:\n            return self.recursive(node.left, low, high)\n        elif node.val < low:\n            return self.recursive(node.right, low, high)\n        else:\n            node.left = self.recursive(node.left, low, high)\n            node.right = self.recursive(node.right, low, high)\n            return node\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/669-trim-a-binary-search-tree/",
      "datePublished": "2025-01-30",
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