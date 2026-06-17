# 297-serialize-and-deserialize-binary-tree


Try it on <a href='https://leetcode.com/problems/297-serialize-and-deserialize-binary-tree'>leetcode</a>

## Description
<div class="description">
<div><p>Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.</p>

<p>Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.</p>

<p><strong>Clarification:</strong> The input/output format is the same as <a href="/faq/#binary-tree" target="_blank">how LeetCode serializes a binary tree</a>. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg" style="width: 442px; height: 324px;">
<pre><strong>Input:</strong> root = [1,2,3,null,null,4,5]
<strong>Output:</strong> [1,2,3,null,null,4,5]
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def __init__(self):
        self.i = 0

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "#"
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + "," + left + "," + right

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def recur():
            val = next(vals)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = recur()
            node.right = recur()
            return node

        vals = iter(data.split(","))
        return recur()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "297. Serialize and Deserialize Binary Tree",
    "text": "Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.\nDesign an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.\nClarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.\n\u00a0\nExample 1:\n\nInput: root = [1,2,3,null,null,4,5]\nOutput: [1,2,3,null,null,4,5]\n\nExample 2:\nInput: root = []\nOutput: []\n\n\u00a0\nConstraints:\n\nThe number of nodes in the tree is in the range [0, 104].\n-1000 <= Node.val <= 1000\n\n",
    "url": "https://leetcode.com/problems/297-serialize-and-deserialize-binary-tree",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for a binary tree node.\n# class TreeNode(object):\n#     def __init__(self, x):\n#         self.val = x\n#         self.left = None\n#         self.right = None\n\n\nclass Codec:\n    def __init__(self):\n        self.i = 0\n\n    def serialize(self, root):\n        \"\"\"Encodes a tree to a single string.\n\n        :type root: TreeNode\n        :rtype: str\n        \"\"\"\n        if root is None:\n            return \"#\"\n        left = self.serialize(root.left)\n        right = self.serialize(root.right)\n        return str(root.val) + \",\" + left + \",\" + right\n\n    def deserialize(self, data):\n        \"\"\"Decodes your encoded data to tree.\n\n        :type data: str\n        :rtype: TreeNode\n        \"\"\"\n\n        def recur():\n            val = next(vals)\n            if val == \"#\":\n                return None\n            node = TreeNode(int(val))\n            node.left = recur()\n            node.right = recur()\n            return node\n\n        vals = iter(data.split(\",\"))\n        return recur()\n\n\n# Your Codec object will be instantiated and called as such:\n# ser = Codec()\n# deser = Codec()\n# ans = deser.deserialize(ser.serialize(root))\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/297-serialize-and-deserialize-binary-tree/",
      "datePublished": "2022-05-23",
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