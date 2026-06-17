# 102-binary-tree-level-order-traversal


Try it on <a href='https://leetcode.com/problems/102-binary-tree-level-order-traversal'>leetcode</a>

## Description
<div class="description">
<div><p>Given the <code>root</code> of a binary tree, return <em>the level order traversal of its nodes' values</em>. (i.e., from left to right, level by level).</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" style="width: 277px; height: 302px;">
<pre><strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> [[3],[9,20],[15,7]]
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> root = [1]
<strong>Output:</strong> [[1]]
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 2000]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            cur_level = []
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node:
                    cur_level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            res.append(cur_level)
        return res
                
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "102. Binary Tree Level Order Traversal",
    "text": "Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).\n\u00a0\nExample 1:\n\nInput: root = [3,9,20,null,null,15,7]\nOutput: [[3],[9,20],[15,7]]\n\nExample 2:\nInput: root = [1]\nOutput: [[1]]\n\nExample 3:\nInput: root = []\nOutput: []\n\n\u00a0\nConstraints:\n\nThe number of nodes in the tree is in the range [0, 2000].\n-1000 <= Node.val <= 1000\n\n",
    "url": "https://leetcode.com/problems/102-binary-tree-level-order-traversal",
    "answerCount": 1,
    "datePublished": "2022-07-13T10:50:18+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:\n        if not root:\n            return []\n        q = deque([root])\n        res = []\n        while q:\n            cur_level = []\n            n = len(q)\n            for _ in range(n):\n                node = q.popleft()\n                if node:\n                    cur_level.append(node.val)\n                    if node.left:\n                        q.append(node.left)\n                    if node.right:\n                        q.append(node.right)\n            res.append(cur_level)\n        return res\n                ",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/102-binary-tree-level-order-traversal/",
      "datePublished": "2022-07-13T10:50:18+05:30",
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