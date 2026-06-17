# 1379-find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree


Try it on <a href='https://leetcode.com/problems/1379-find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree'>leetcode</a>

## Description
<div class="description">
<div><p>Given two binary trees <code>original</code> and <code>cloned</code> and given a reference to a node <code>target</code> in the original tree.</p>

<p>The <code>cloned</code> tree is a <strong>copy of</strong> the <code>original</code> tree.</p>

<p>Return <em>a reference to the same node</em> in the <code>cloned</code> tree.</p>

<p><strong>Note</strong> that you are <strong>not allowed</strong> to change any of the two trees or the <code>target</code> node and the answer <strong>must be</strong> a reference to a node in the <code>cloned</code> tree.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/21/e1.png" style="width: 544px; height: 426px;">
<pre><strong>Input:</strong> tree = [7,4,3,null,null,6,19], target = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/21/e2.png" style="width: 221px; height: 159px;">
<pre><strong>Input:</strong> tree = [7], target =  7
<strong>Output:</strong> 7
</pre>

<p><strong>Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/21/e3.png" style="width: 459px; height: 486px;">
<pre><strong>Input:</strong> tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the <code>tree</code> is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li>The values of the nodes of the <code>tree</code> are unique.</li>
	<li><code>target</code> node is a node from the <code>original</code> tree and is not <code>null</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you solve the problem if repeated values on the tree are allowed?</p>
</div>
</div>

## Solution(Python)
```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        def inorder(o: TreeNode, c: TreeNode):
            if o:
                inorder(o.left, c.left)
                if o is target:
                    self.ans = c
                inorder(o.right, c.right)

        inorder(original, cloned)
        return self.ans

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree",
    "text": "Given two binary trees original and cloned and given a reference to a node target in the original tree.\nThe cloned tree is a copy of the original tree.\nReturn a reference to the same node in the cloned tree.\nNote that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.\n\u00a0\nExample 1:\n\nInput: tree = [7,4,3,null,null,6,19], target = 3\nOutput: 3\nExplanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.\n\nExample 2:\n\nInput: tree = [7], target =  7\nOutput: 7\n\nExample 3:\n\nInput: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4\nOutput: 4\n\n\u00a0\nConstraints:\n\nThe number of nodes in the tree is in the range [1, 104].\nThe values of the nodes of the tree are unique.\ntarget node is a node from the original tree and is not null.\n\n\u00a0\nFollow up: Could you solve the problem if repeated values on the tree are allowed?\n",
    "url": "https://leetcode.com/problems/1379-find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, x):\n#         self.val = x\n#         self.left = None\n#         self.right = None\n\n\nclass Solution:\n    def getTargetCopy(\n        self, original: TreeNode, cloned: TreeNode, target: TreeNode\n    ) -> TreeNode:\n        def inorder(o: TreeNode, c: TreeNode):\n            if o:\n                inorder(o.left, c.left)\n                if o is target:\n                    self.ans = c\n                inorder(o.right, c.right)\n\n        inorder(original, cloned)\n        return self.ans\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1379-find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/",
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