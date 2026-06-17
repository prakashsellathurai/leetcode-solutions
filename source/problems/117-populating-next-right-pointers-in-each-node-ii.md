# 117-populating-next-right-pointers-in-each-node-ii


Try it on <a href='https://leetcode.com/problems/117-populating-next-right-pointers-in-each-node-ii'>leetcode</a>

## Description
<div class="description">
<div><p>Given a binary tree</p>

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
<img alt="" src="https://assets.leetcode.com/uploads/2019/02/15/117_sample.png" style="width: 500px; height: 171px;">
<pre><strong>Input:</strong> root = [1,2,3,4,5,null,7]
<strong>Output:</strong> [1,#,2,3,#,4,5,7,#]
<strong>Explanation: </strong>Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 6000]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
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
    def connect(self, root: "Node") -> "Node":
        return self.constantspace(root)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def levelordertraversal(self, root: "Node") -> "Node":
        q = deque([])
        q.append(root)
        while q:
            qsize = len(q)
            for i in range(qsize):
                node = q.popleft()
                if node:
                    if i == qsize - 1:
                        node.next = None
                    else:
                        node.next = q[0]

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        return root

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def constantspace(self, root: "Node") -> "Node":
        node = root
        while node:
            curr = sentinel = Node(-1)
            while node:
                if node.left:
                    curr.next = node.left
                    curr = curr.next
                if node.right:
                    curr.next = node.right
                    curr = curr.next
                node = node.next

            node = sentinel.next
            sentinel.next = None

        return root

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "117. Populating Next Right Pointers in Each Node II",
    "text": "Given a binary tree\nstruct Node {\n  int val;\n  Node *left;\n  Node *right;\n  Node *next;\n}\n\nPopulate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.\nInitially, all next pointers are set to NULL.\n\u00a0\nExample 1:\n\nInput: root = [1,2,3,4,5,null,7]\nOutput: [1,#,2,3,#,4,5,7,#]\nExplanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.\n\nExample 2:\nInput: root = []\nOutput: []\n\n\u00a0\nConstraints:\n\nThe number of nodes in the tree is in the range [0, 6000].\n-100 <= Node.val <= 100\n\n\u00a0\nFollow-up:\n\nYou may only use constant extra space.\nThe recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.\n\n",
    "url": "https://leetcode.com/problems/117-populating-next-right-pointers-in-each-node-ii",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "\"\"\"\n# Definition for a Node.\nclass Node:\n    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):\n        self.val = val\n        self.left = left\n        self.right = right\n        self.next = next\n\"\"\"\n\n\nclass Solution:\n    def connect(self, root: \"Node\") -> \"Node\":\n        return self.constantspace(root)\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(n)\n    def levelordertraversal(self, root: \"Node\") -> \"Node\":\n        q = deque([])\n        q.append(root)\n        while q:\n            qsize = len(q)\n            for i in range(qsize):\n                node = q.popleft()\n                if node:\n                    if i == qsize - 1:\n                        node.next = None\n                    else:\n                        node.next = q[0]\n\n                    if node.left:\n                        q.append(node.left)\n                    if node.right:\n                        q.append(node.right)\n        return root\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(1)\n    def constantspace(self, root: \"Node\") -> \"Node\":\n        node = root\n        while node:\n            curr = sentinel = Node(-1)\n            while node:\n                if node.left:\n                    curr.next = node.left\n                    curr = curr.next\n                if node.right:\n                    curr.next = node.right\n                    curr = curr.next\n                node = node.next\n\n            node = sentinel.next\n            sentinel.next = None\n\n        return root\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/117-populating-next-right-pointers-in-each-node-ii/",
      "datePublished": "2022-06-01",
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