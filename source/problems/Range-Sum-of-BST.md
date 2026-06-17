# range-sum-of-bst


Try it on <a href='https://leetcode.com/problems/range-sum-of-bst'>leetcode</a>

## Description
<div class="description">
<div><p>Given the <code>root</code> node of a binary search tree and two integers <code>low</code> and <code>high</code>, return <em>the sum of values of all nodes with a value in the <strong>inclusive</strong> range </em><code>[low, high]</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/bst1.jpg" style="width: 400px; height: 222px;">
<pre><strong>Input:</strong> root = [10,5,15,3,7,null,18], low = 7, high = 15
<strong>Output:</strong> 32
<strong>Explanation:</strong> Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/bst2.jpg" style="width: 400px; height: 335px;">
<pre><strong>Input:</strong> root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
<strong>Output:</strong> 23
<strong>Explanation:</strong> Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 2 * 10<sup>4</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= low &lt;= high &lt;= 10<sup>5</sup></code></li>
	<li>All <code>Node.val</code> are <strong>unique</strong>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution(object):
    def rangeSumBST(self, root, L, R):
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "938. Range Sum of BST",
    "text": "Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].\n\u00a0\nExample 1:\n\nInput: root = [10,5,15,3,7,null,18], low = 7, high = 15\nOutput: 32\nExplanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.\n\nExample 2:\n\nInput: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10\nOutput: 23\nExplanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.\n\n\u00a0\nConstraints:\n\nThe number of nodes in the tree is in the range [1, 2 * 104].\n1 <= Node.val <= 105\n1 <= low <= high <= 105\nAll Node.val are unique.\n\n",
    "url": "https://leetcode.com/problems/range-sum-of-bst",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution(object):\n    def rangeSumBST(self, root, L, R):\n        def dfs(node):\n            if node:\n                if L <= node.val <= R:\n                    self.ans += node.val\n                if L < node.val:\n                    dfs(node.left)\n                if node.val < R:\n                    dfs(node.right)\n\n        self.ans = 0\n        dfs(root)\n        return self.ans\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/range-sum-of-bst/",
      "datePublished": "2025-04-30",
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