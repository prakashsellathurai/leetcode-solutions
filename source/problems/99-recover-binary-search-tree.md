# 99-recover-binary-search-tree


Try it on <a href='https://leetcode.com/problems/99-recover-binary-search-tree'>leetcode</a>

## Description
<div class="description">
<div><p>You are given the <code>root</code> of a binary search tree (BST), where the values of <strong>exactly</strong> two nodes of the tree were swapped by mistake. <em>Recover the tree without changing its structure</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/28/recover1.jpg" style="width: 422px; height: 302px;">
<pre><strong>Input:</strong> root = [1,3,null,null,2]
<strong>Output:</strong> [3,1,null,null,2]
<strong>Explanation:</strong> 3 cannot be a left child of 1 because 3 &gt; 1. Swapping 1 and 3 makes the BST valid.
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/28/recover2.jpg" style="width: 581px; height: 302px;">
<pre><strong>Input:</strong> root = [3,1,4,null,null,2]
<strong>Output:</strong> [2,1,4,null,null,3]
<strong>Explanation:</strong> 2 cannot be in the right subtree of 3 because 2 &lt; 3. Swapping 2 and 3 makes the BST valid.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[2, 1000]</code>.</li>
	<li><code>-2<sup>31</sup> &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> A solution using <code>O(n)</code> space is pretty straight-forward. Could you devise a constant <code>O(1)</code> space solution?</div>
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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.better(root)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def naive(self, root):
        def traversal(node):
            return (
                traversal(node.left) + [node.val] + traversal(node.right)
                if node
                else []
            )

        inorder = traversal(root)

        n = len(inorder)

        for i in range(n):
            key = inorder[i]
            j = i - 1
            while j >= 0 and inorder[j] >= key:
                inorder[j + 1] = inorder[j]
                j -= 1
            inorder[j + 1] = key

        def update(node):
            nonlocal i
            if node:
                update(node.left)
                node.val = inorder[i]
                i += 1
                update(node.right)

        i = 0
        update(root)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def better(self, root):
        cur, prev, First, Second = root, TreeNode(-float("inf")), None, None
        i = 0

        while cur:

            if cur.left:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right

                if pre.right is None:
                    pre.right = cur
                    cur = cur.left
                else:
                    if cur.val < prev.val:
                        if First is None:
                            First = prev
                        Second = cur
                    pre.right = None
                    prev = cur
                    cur = cur.right
            else:
                if cur.val < prev.val:
                    if First is None:
                        First = prev
                    Second = cur
                prev = cur
                cur = cur.right
        First.val, Second.val = Second.val, First.val

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "99. Recover Binary Search Tree",
    "text": "You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.\n\u00a0\nExample 1:\n\nInput: root = [1,3,null,null,2]\nOutput: [3,1,null,null,2]\nExplanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.\n\nExample 2:\n\nInput: root = [3,1,4,null,null,2]\nOutput: [2,1,4,null,null,3]\nExplanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.\n\n\u00a0\nConstraints:\n\nThe number of nodes in the tree is in the range [2, 1000].\n-231 <= Node.val <= 231 - 1\n\n\u00a0\nFollow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?",
    "url": "https://leetcode.com/problems/99-recover-binary-search-tree",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def recoverTree(self, root: Optional[TreeNode]) -> None:\n        \"\"\"\n        Do not return anything, modify root in-place instead.\n        \"\"\"\n        self.better(root)\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(n)\n    def naive(self, root):\n        def traversal(node):\n            return (\n                traversal(node.left) + [node.val] + traversal(node.right)\n                if node\n                else []\n            )\n\n        inorder = traversal(root)\n\n        n = len(inorder)\n\n        for i in range(n):\n            key = inorder[i]\n            j = i - 1\n            while j >= 0 and inorder[j] >= key:\n                inorder[j + 1] = inorder[j]\n                j -= 1\n            inorder[j + 1] = key\n\n        def update(node):\n            nonlocal i\n            if node:\n                update(node.left)\n                node.val = inorder[i]\n                i += 1\n                update(node.right)\n\n        i = 0\n        update(root)\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(1)\n    def better(self, root):\n        cur, prev, First, Second = root, TreeNode(-float(\"inf\")), None, None\n        i = 0\n\n        while cur:\n\n            if cur.left:\n                pre = cur.left\n                while pre.right and pre.right != cur:\n                    pre = pre.right\n\n                if pre.right is None:\n                    pre.right = cur\n                    cur = cur.left\n                else:\n                    if cur.val < prev.val:\n                        if First is None:\n                            First = prev\n                        Second = cur\n                    pre.right = None\n                    prev = cur\n                    cur = cur.right\n            else:\n                if cur.val < prev.val:\n                    if First is None:\n                        First = prev\n                    Second = cur\n                prev = cur\n                cur = cur.right\n        First.val, Second.val = Second.val, First.val\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/99-recover-binary-search-tree/",
      "datePublished": "2024-12-12",
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