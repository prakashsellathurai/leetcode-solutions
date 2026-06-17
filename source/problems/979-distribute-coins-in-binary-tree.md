# 979-distribute-coins-in-binary-tree


Try it on <a href='https://leetcode.com/problems/979-distribute-coins-in-binary-tree'>leetcode</a>

## Description
<div class="description">
<div><p>You are given the <code>root</code> of a binary tree with <code>n</code> nodes where each <code>node</code> in the tree has <code>node.val</code> coins. There are <code>n</code> coins in total throughout the whole tree.</p>

<p>In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.</p>

<p>Return <em>the <strong>minimum</strong> number of moves required to make every node have <strong>exactly</strong> one coin</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/01/18/tree1.png" style="width: 250px; height: 236px;">
<pre><strong>Input:</strong> root = [3,0,0]
<strong>Output:</strong> 2
<strong>Explanation: </strong>From the root of the tree, we move one coin to its left child, and one coin to its right child.
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/01/18/tree2.png" style="width: 250px; height: 236px;">
<pre><strong>Input:</strong> root = [0,3,0]
<strong>Output:</strong> 3
<strong>Explanation: </strong>From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is <code>n</code>.</li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>0 &lt;= Node.val &lt;= n</code></li>
	<li>The sum of all <code>Node.val</code> is <code>n</code>.</li>
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
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return 0
            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + L + R - 1

        dfs(root)
        return self.ans

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "979. Distribute Coins in Binary Tree",
    "text": "You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.\nIn one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.\nReturn the minimum number of moves required to make every node have exactly one coin.\n\u00a0\nExample 1:\n\nInput: root = [3,0,0]\nOutput: 2\nExplanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.\n\nExample 2:\n\nInput: root = [0,3,0]\nOutput: 3\nExplanation: From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child.\n\n\u00a0\nConstraints:\n\nThe number of nodes in the tree is n.\n1 <= n <= 100\n0 <= Node.val <= n\nThe sum of all Node.val is n.\n\n",
    "url": "https://leetcode.com/problems/979-distribute-coins-in-binary-tree",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def distributeCoins(self, root: Optional[TreeNode]) -> int:\n        self.ans = 0\n\n        def dfs(node):\n            if not node:\n                return 0\n            L, R = dfs(node.left), dfs(node.right)\n            self.ans += abs(L) + abs(R)\n            return node.val + L + R - 1\n\n        dfs(root)\n        return self.ans\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/979-distribute-coins-in-binary-tree/",
      "datePublished": "2022-06-05",
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