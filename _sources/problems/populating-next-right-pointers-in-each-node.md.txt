# populating-next-right-pointers-in-each-node


Try it on <a href='https://leetcode.com/problems/populating-next-right-pointers-in-each-node'>leetcode</a>

## Description
<div class="description">
<div><p>You are given a <strong>perfect binary tree</strong> where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:</p>

<pre>struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
</pre>

<p>Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to <code>NULL</code>.</p>

<p>Initially, all next pointers are set to <code>NULL</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/02/14/116_sample.png" style="width: 500px; height: 171px;">
<pre><strong>Input:</strong> root = [1,2,3,4,5,6,7]
<strong>Output:</strong> [1,#,2,3,#,4,5,6,7,#]
<strong>Explanation: </strong>Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 2<sup>12</sup> - 1]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow-up:</strong></p>

<ul>
	<li>You may only use constant extra space.</li>
	<li>The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if root is None:
            return None
        if root.left is not None:
            root.left.next = root.right
        if root.right is not None and root.next is not None:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "116. Populating Next Right Pointers in Each Node",
    "text": "You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:\nstruct Node {\n  int val;\n  Node *left;\n  Node *right;\n  Node *next;\n}\n\nPopulate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.\nInitially, all next pointers are set to NULL.\n\u00a0\nExample 1:\n\nInput: root = [1,2,3,4,5,6,7]\nOutput: [1,#,2,3,#,4,5,6,7,#]\nExplanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.\n\nExample 2:\nInput: root = []\nOutput: []\n\n\u00a0\nConstraints:\n\nThe number of nodes in the tree is in the range [0, 212 - 1].\n-1000 <= Node.val <= 1000\n\n\u00a0\nFollow-up:\n\nYou may only use constant extra space.\nThe recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.\n\n",
    "url": "https://leetcode.com/problems/populating-next-right-pointers-in-each-node",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "\"\"\"\n# Definition for a Node.\nclass Node:\n    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):\n        self.val = val\n        self.left = left\n        self.right = right\n        self.next = next\n\"\"\"\n\n\nclass Solution:\n    def connect(self, root: \"Optional[Node]\") -> \"Optional[Node]\":\n        if root is None:\n            return None\n        if root.left is not None:\n            root.left.next = root.right\n        if root.right is not None and root.next is not None:\n            root.right.next = root.next.left\n        self.connect(root.left)\n        self.connect(root.right)\n        return root\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/populating-next-right-pointers-in-each-node/",
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