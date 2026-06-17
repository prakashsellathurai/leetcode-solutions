# maximum-difference-between-node-and-ancestor


Try it on <a href='https://leetcode.com/problems/maximum-difference-between-node-and-ancestor'>leetcode</a>

## Description
<div class="description">
<div><p>Given the <code>root</code> of a binary tree, find the maximum value <code>v</code> for which there exist <strong>different</strong> nodes <code>a</code> and <code>b</code> where <code>v = |a.val - b.val|</code> and <code>a</code> is an ancestor of <code>b</code>.</p>

<p>A node <code>a</code> is an ancestor of <code>b</code> if either: any child of <code>a</code> is equal to <code>b</code>&nbsp;or any child of <code>a</code> is an ancestor of <code>b</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/09/tmp-tree.jpg" style="width: 400px; height: 390px;">
<pre><strong>Input:</strong> root = [8,3,10,1,6,null,14,null,null,4,7,13]
<strong>Output:</strong> 7
<strong>Explanation: </strong>We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/09/tmp-tree-1.jpg" style="width: 250px; height: 349px;">
<pre><strong>Input:</strong> root = [1,null,2,null,0,3]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[2, 5000]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def maxAncestorDiff(self, root, curMin=inf, curMax=-inf):
        if not root:
            return curMax - curMin

        if root.val < curMin:
            curMin = root.val

        if root.val > curMax:
            curMax = root.val

        left = self.maxAncestorDiff(root.left, curMin, curMax)
        right = self.maxAncestorDiff(root.right, curMin, curMax)

        if left > right:
            return left
        else:
            return right

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1026. Maximum Difference Between Node and Ancestor",
    "text": "Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.\nA node a is an ancestor of b if either: any child of a is equal to b\u00a0or any child of a is an ancestor of b.\n\u00a0\nExample 1:\n\nInput: root = [8,3,10,1,6,null,14,null,null,4,7,13]\nOutput: 7\nExplanation: We have various ancestor-node differences, some of which are given below :\n|8 - 3| = 5\n|3 - 7| = 4\n|8 - 1| = 7\n|10 - 13| = 3\nAmong all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.\nExample 2:\n\nInput: root = [1,null,2,null,0,3]\nOutput: 3\n\n\u00a0\nConstraints:\n\nThe number of nodes in the tree is in the range [2, 5000].\n0 <= Node.val <= 105\n\n",
    "url": "https://leetcode.com/problems/maximum-difference-between-node-and-ancestor",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def maxAncestorDiff(self, root, curMin=inf, curMax=-inf):\n        if not root:\n            return curMax - curMin\n\n        if root.val < curMin:\n            curMin = root.val\n\n        if root.val > curMax:\n            curMax = root.val\n\n        left = self.maxAncestorDiff(root.left, curMin, curMax)\n        right = self.maxAncestorDiff(root.right, curMin, curMax)\n\n        if left > right:\n            return left\n        else:\n            return right\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/maximum-difference-between-node-and-ancestor/",
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