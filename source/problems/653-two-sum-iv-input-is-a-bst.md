# 653-two-sum-iv-input-is-a-bst


Try it on <a href='https://leetcode.com/problems/653-two-sum-iv-input-is-a-bst'>leetcode</a>

## Description
<div class="description">
<div><p>Given the <code>root</code> of a Binary Search Tree and a target number <code>k</code>, return <em><code>true</code> if there exist two elements in the BST such that their sum is equal to the given target</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/21/sum_tree_1.jpg" style="width: 400px; height: 229px;">
<pre><strong>Input:</strong> root = [5,3,6,2,4,null,7], k = 9
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/21/sum_tree_2.jpg" style="width: 400px; height: 229px;">
<pre><strong>Input:</strong> root = [5,3,6,2,4,null,7], k = 28
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>4</sup>&nbsp;&lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li><code>root</code> is guaranteed to be a <strong>valid</strong> binary search tree.</li>
	<li><code>-10<sup>5</sup>&nbsp;&lt;= k &lt;= 10<sup>5</sup></code></li>
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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def pushLeft(st, root):
            while root:
                st.append(root)
                root = root.left

        def pushRight(st, root):
            while root:
                st.append(root)
                root = root.right

        def nextLeft(st):
            node = st.pop()
            pushLeft(st, node.right)
            return node.val

        def nextRight(st):
            node = st.pop()
            pushRight(st, node.left)
            return node.val

        stLeft, stRight = [], []
        pushLeft(stLeft, root)
        pushRight(stRight, root)

        left, right = nextLeft(stLeft), nextRight(stRight)
        while left < right:
            if left + right == k: return True
            if left + right < k:
                left = nextLeft(stLeft)
            else:
                right = nextRight(stRight)
        return False
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "653. Two Sum IV - Input is a BST",
    "text": "Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.\n\u00a0\nExample 1:\n\nInput: root = [5,3,6,2,4,null,7], k = 9\nOutput: true\n\nExample 2:\n\nInput: root = [5,3,6,2,4,null,7], k = 28\nOutput: false\n\n\u00a0\nConstraints:\n\nThe number of nodes in the tree is in the range [1, 104].\n-104\u00a0<= Node.val <= 104\nroot is guaranteed to be a valid binary search tree.\n-105\u00a0<= k <= 105\n\n",
    "url": "https://leetcode.com/problems/653-two-sum-iv-input-is-a-bst",
    "answerCount": 1,
    "datePublished": "2026-03-05T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:\n        def pushLeft(st, root):\n            while root:\n                st.append(root)\n                root = root.left\n\n        def pushRight(st, root):\n            while root:\n                st.append(root)\n                root = root.right\n\n        def nextLeft(st):\n            node = st.pop()\n            pushLeft(st, node.right)\n            return node.val\n\n        def nextRight(st):\n            node = st.pop()\n            pushRight(st, node.left)\n            return node.val\n\n        stLeft, stRight = [], []\n        pushLeft(stLeft, root)\n        pushRight(stRight, root)\n\n        left, right = nextLeft(stLeft), nextRight(stRight)\n        while left < right:\n            if left + right == k: return True\n            if left + right < k:\n                left = nextLeft(stLeft)\n            else:\n                right = nextRight(stRight)\n        return False",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/653-two-sum-iv-input-is-a-bst/",
      "datePublished": "2026-03-05T00:00:00Z",
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