# 101-symmetric-tree


Try it on <a href='https://leetcode.com/problems/101-symmetric-tree'>leetcode</a>

## Description
<div class="description">
<div><p>Given the <code>root</code> of a binary tree, <em>check whether it is a mirror of itself</em> (i.e., symmetric around its center).</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg" style="width: 354px; height: 291px;">
<pre><strong>Input:</strong> root = [1,2,2,3,4,4,3]
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg" style="width: 308px; height: 258px;">
<pre><strong>Input:</strong> root = [1,2,2,null,3,null,3]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it both recursively and iteratively?</div>
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.iterative(root)

    # Time Complexity: O(n)
    # Space Complexity: O(h)
    def recursive(self, root1, root2=None):
        if root1 is None and root2 is None:
            return True

        if root1 is not None and root2 is not None:
            if root1.val == root2.val:
                return self.recursive(root1.left, root2.right) and self.recursive(
                    root1.right, root2.left
                )

        return False

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def iterative(self, root):
        q = deque([])
        q.append(root)
        q.append(root)

        while q:
            original_node = q.popleft()
            mirrored_node = q.popleft()

            if original_node.val != mirrored_node.val:
                return False

            if original_node.left and mirrored_node.right:
                q.append(original_node.left)
                q.append(mirrored_node.right)
            elif original_node.left or mirrored_node.right:
                return False

            if original_node.right and mirrored_node.left:
                q.append(original_node.right)
                q.append(mirrored_node.left)
            elif original_node.right or mirrored_node.left:
                return False

        return True

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "101. Symmetric Tree",
    "text": "Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).\n\u00a0\nExample 1:\n\nInput: root = [1,2,2,3,4,4,3]\nOutput: true\n\nExample 2:\n\nInput: root = [1,2,2,null,3,null,3]\nOutput: false\n\n\u00a0\nConstraints:\n\nThe number of nodes in the tree is in the range [1, 1000].\n-100 <= Node.val <= 100\n\n\u00a0\nFollow up: Could you solve it both recursively and iteratively?",
    "url": "https://leetcode.com/problems/101-symmetric-tree",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def isSymmetric(self, root: Optional[TreeNode]) -> bool:\n        return self.iterative(root)\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(h)\n    def recursive(self, root1, root2=None):\n        if root1 is None and root2 is None:\n            return True\n\n        if root1 is not None and root2 is not None:\n            if root1.val == root2.val:\n                return self.recursive(root1.left, root2.right) and self.recursive(\n                    root1.right, root2.left\n                )\n\n        return False\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(n)\n    def iterative(self, root):\n        q = deque([])\n        q.append(root)\n        q.append(root)\n\n        while q:\n            original_node = q.popleft()\n            mirrored_node = q.popleft()\n\n            if original_node.val != mirrored_node.val:\n                return False\n\n            if original_node.left and mirrored_node.right:\n                q.append(original_node.left)\n                q.append(mirrored_node.right)\n            elif original_node.left or mirrored_node.right:\n                return False\n\n            if original_node.right and mirrored_node.left:\n                q.append(original_node.right)\n                q.append(mirrored_node.left)\n            elif original_node.right or mirrored_node.left:\n                return False\n\n        return True\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/101-symmetric-tree/",
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