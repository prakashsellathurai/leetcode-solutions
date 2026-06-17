# 104-maximum-depth-of-binary-tree


Try it on <a href='https://leetcode.com/problems/104-maximum-depth-of-binary-tree'>leetcode</a>

## Description
<div class="description">

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.morrisinorder(root)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def morrisinorder(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 1
        maxdepth = depth
        while root:
            if not root.left:
                maxdepth = max(maxdepth, depth)
                root = root.right
            else:
                pre = root.left
                preDepth = 1

                while pre.right and pre.right is not root:
                    preDepth += 1
                    pre = pre.right

                if pre.right is root:
                    pre.right = None
                    depth -= preDepth + 1
                    maxdepth = max(maxdepth, depth)
                    root = root.right
                else:
                    pre.right = root
                    root = root.left
            depth += 1
        return maxdepth

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "104-maximum-depth-of-binary-tree",
    "text": "",
    "url": "https://leetcode.com/problems/104-maximum-depth-of-binary-tree",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def maxDepth(self, root: Optional[TreeNode]) -> int:\n        return self.morrisinorder(root)\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(n)\n    def dfs(self, root: Optional[TreeNode]) -> int:\n        if not root:\n            return 0\n        left = self.maxDepth(root.left)\n        right = self.maxDepth(root.right)\n        return max(left, right) + 1\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(1)\n    def morrisinorder(self, root: Optional[TreeNode]) -> int:\n        if not root:\n            return 0\n        depth = 1\n        maxdepth = depth\n        while root:\n            if not root.left:\n                maxdepth = max(maxdepth, depth)\n                root = root.right\n            else:\n                pre = root.left\n                preDepth = 1\n\n                while pre.right and pre.right is not root:\n                    preDepth += 1\n                    pre = pre.right\n\n                if pre.right is root:\n                    pre.right = None\n                    depth -= preDepth + 1\n                    maxdepth = max(maxdepth, depth)\n                    root = root.right\n                else:\n                    pre.right = root\n                    root = root.left\n            depth += 1\n        return maxdepth\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/104-maximum-depth-of-binary-tree/",
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