# 897-increasing-order-search-tree


Try it on <a href='https://leetcode.com/problems/897-increasing-order-search-tree'>leetcode</a>

## Description
<div class="description">
<div><p>Given the <code>root</code> of a binary search tree, rearrange the tree in <strong>in-order</strong> so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/17/ex1.jpg" style="width: 600px; height: 350px;">
<pre><strong>Input:</strong> root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
<strong>Output:</strong> [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/17/ex2.jpg" style="width: 300px; height: 114px;">
<pre><strong>Input:</strong> root = [5,1,7]
<strong>Output:</strong> [1,null,5,null,7]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the given tree will be in the range <code>[1, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 1000</code></li>
</ul></div>
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
    def increasingBST(self, root: TreeNode) -> TreeNode:
        return self.morrisTraversal(root)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def recursiveInorderTraversal(self, root):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = cur = TreeNode(None)

        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right

    # Time Complexity: O(n)
    # Space Complexity: O(H)
    def relink(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def morrisTraversal(self, root):
        dummy = TreeNode(0)
        node = dummy
        curr = root
        while curr:
            if not curr.left:
                node.right = TreeNode(curr.val)
                # print(curr.val)
                node = node.right
                curr = curr.right
            else:
                pre = curr.left
                while pre and pre.right and pre.right != curr:
                    pre = pre.right
                if not pre.right:
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right = None
                    node.right = TreeNode(curr.val)
                    # print(curr.val)
                    node = node.right
                    curr = curr.right
        return dummy.right

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "897. Increasing Order Search Tree",
    "text": "Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.\n\u00a0\nExample 1:\n\nInput: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]\nOutput: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]\n\nExample 2:\n\nInput: root = [5,1,7]\nOutput: [1,null,5,null,7]\n\n\u00a0\nConstraints:\n\nThe number of nodes in the given tree will be in the range [1, 100].\n0 <= Node.val <= 1000\n",
    "url": "https://leetcode.com/problems/897-increasing-order-search-tree",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def increasingBST(self, root: TreeNode) -> TreeNode:\n        return self.morrisTraversal(root)\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(n)\n    def recursiveInorderTraversal(self, root):\n        def inorder(node):\n            if node:\n                yield from inorder(node.left)\n                yield node.val\n                yield from inorder(node.right)\n\n        ans = cur = TreeNode(None)\n\n        for v in inorder(root):\n            cur.right = TreeNode(v)\n            cur = cur.right\n        return ans.right\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(H)\n    def relink(self, root):\n        def inorder(node):\n            if node:\n                inorder(node.left)\n                node.left = None\n                self.cur.right = node\n                self.cur = node\n                inorder(node.right)\n\n        ans = self.cur = TreeNode(None)\n        inorder(root)\n        return ans.right\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(1)\n    def morrisTraversal(self, root):\n        dummy = TreeNode(0)\n        node = dummy\n        curr = root\n        while curr:\n            if not curr.left:\n                node.right = TreeNode(curr.val)\n                # print(curr.val)\n                node = node.right\n                curr = curr.right\n            else:\n                pre = curr.left\n                while pre and pre.right and pre.right != curr:\n                    pre = pre.right\n                if not pre.right:\n                    pre.right = curr\n                    curr = curr.left\n                else:\n                    pre.right = None\n                    node.right = TreeNode(curr.val)\n                    # print(curr.val)\n                    node = node.right\n                    curr = curr.right\n        return dummy.right\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/897-increasing-order-search-tree/",
      "datePublished": "2023-02-06",
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