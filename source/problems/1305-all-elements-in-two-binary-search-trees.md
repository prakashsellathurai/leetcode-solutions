# 1305-all-elements-in-two-binary-search-trees


Try it on <a href='https://leetcode.com/problems/1305-all-elements-in-two-binary-search-trees'>leetcode</a>

## Description
<div class="description">
<div><p>Given two binary search trees <code>root1</code> and <code>root2</code>, return <em>a list containing all the integers from both trees sorted in <strong>ascending</strong> order</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/12/18/q2-e1.png" style="width: 457px; height: 207px;">
<pre><strong>Input:</strong> root1 = [2,1,4], root2 = [1,0,3]
<strong>Output:</strong> [0,1,1,2,3,4]
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/12/18/q2-e5-.png" style="width: 352px; height: 197px;">
<pre><strong>Input:</strong> root1 = [1,null,8], root2 = [8,1]
<strong>Output:</strong> [1,1,8,8]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in each tree is in the range <code>[0, 5000]</code>.</li>
	<li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
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
    def inorder(self, root, lst):
        if not root:
            return
        self.inorder(root.left, lst)
        lst.append(root.val)
        self.inorder(root.right, lst)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        return self.Linear(root1, root2)

    """
    Time Complexity: O((m+n)*log(m+n))
    Space Complexity: O(max(m,n))
    """

    def bruteforce(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        self.inorder(root1, res)
        self.inorder(root2, res)

        res.sort()
        return res

    """
    Time Complexity: O(m+n)
    Space Complexity: O(m+n)
    """

    def Linear(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        lst1, lst2 = [], []
        self.inorder(root1, lst1)
        self.inorder(root2, lst2)

        res = []
        i, j = 0, 0

        while i < len(lst1) and j < len(lst2):
            if lst1[i] < lst2[j]:
                res.append(lst1[i])
                i += 1
            else:
                res.append(lst2[j])
                j += 1
        while i < len(lst1):
            res.append(lst1[i])
            i += 1
        while j < len(lst2):
            res.append(lst2[j])
            j += 1
        return res

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1305. All Elements in Two Binary Search Trees",
    "text": "Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.\n\u00a0\nExample 1:\n\nInput: root1 = [2,1,4], root2 = [1,0,3]\nOutput: [0,1,1,2,3,4]\n\nExample 2:\n\nInput: root1 = [1,null,8], root2 = [8,1]\nOutput: [1,1,8,8]\n\n\u00a0\nConstraints:\n\nThe number of nodes in each tree is in the range [0, 5000].\n-105 <= Node.val <= 105\n\n",
    "url": "https://leetcode.com/problems/1305-all-elements-in-two-binary-search-trees",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def inorder(self, root, lst):\n        if not root:\n            return\n        self.inorder(root.left, lst)\n        lst.append(root.val)\n        self.inorder(root.right, lst)\n\n    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:\n        return self.Linear(root1, root2)\n\n    \"\"\"\n    Time Complexity: O((m+n)*log(m+n))\n    Space Complexity: O(max(m,n))\n    \"\"\"\n\n    def bruteforce(self, root1: TreeNode, root2: TreeNode) -> List[int]:\n        res = []\n        self.inorder(root1, res)\n        self.inorder(root2, res)\n\n        res.sort()\n        return res\n\n    \"\"\"\n    Time Complexity: O(m+n)\n    Space Complexity: O(m+n)\n    \"\"\"\n\n    def Linear(self, root1: TreeNode, root2: TreeNode) -> List[int]:\n        lst1, lst2 = [], []\n        self.inorder(root1, lst1)\n        self.inorder(root2, lst2)\n\n        res = []\n        i, j = 0, 0\n\n        while i < len(lst1) and j < len(lst2):\n            if lst1[i] < lst2[j]:\n                res.append(lst1[i])\n                i += 1\n            else:\n                res.append(lst2[j])\n                j += 1\n        while i < len(lst1):\n            res.append(lst1[i])\n            i += 1\n        while j < len(lst2):\n            res.append(lst2[j])\n            j += 1\n        return res\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1305-all-elements-in-two-binary-search-trees/",
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