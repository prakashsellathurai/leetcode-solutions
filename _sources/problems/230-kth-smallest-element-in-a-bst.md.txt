# 230-kth-smallest-element-in-a-bst


Try it on <a href='https://leetcode.com/problems/230-kth-smallest-element-in-a-bst'>leetcode</a>

## Description
<div class="description">
<div><p>Given the <code>root</code> of a binary search tree, and an integer <code>k</code>, return <em>the</em> <code>k<sup>th</sup></code> <em>smallest value (<strong>1-indexed</strong>) of all the values of the nodes in the tree</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg" style="width: 212px; height: 301px;">
<pre><strong>Input:</strong> root = [3,1,4,null,2], k = 1
<strong>Output:</strong> 1
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg" style="width: 382px; height: 302px;">
<pre><strong>Input:</strong> root = [5,3,6,2,4,null,null,1], k = 3
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is <code>n</code>.</li>
	<li><code>1 &lt;= k &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?</p>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        cur = root

        while cur:
            if cur.left is None:
                k -= 1
                if k == 0:
                    return cur.val
                cur = cur.right
            else:
                pre = cur.left

                while pre.right and pre.right is not cur:
                    pre = pre.right

                if pre.right is None:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    k -= 1
                    if k == 0:
                        return cur.val
                    cur = cur.right

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "230. Kth Smallest Element in a BST",
    "text": "Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.\n\u00a0\nExample 1:\n\nInput: root = [3,1,4,null,2], k = 1\nOutput: 1\n\nExample 2:\n\nInput: root = [5,3,6,2,4,null,null,1], k = 3\nOutput: 3\n\n\u00a0\nConstraints:\n\nThe number of nodes in the tree is n.\n1 <= k <= n <= 104\n0 <= Node.val <= 104\n\n\u00a0\nFollow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?\n",
    "url": "https://leetcode.com/problems/230-kth-smallest-element-in-a-bst",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def kthSmallest(self, root, k):\n        \"\"\"\n        :type root: TreeNode\n        :type k: int\n        :rtype: int\n        \"\"\"\n\n        cur = root\n\n        while cur:\n            if cur.left is None:\n                k -= 1\n                if k == 0:\n                    return cur.val\n                cur = cur.right\n            else:\n                pre = cur.left\n\n                while pre.right and pre.right is not cur:\n                    pre = pre.right\n\n                if pre.right is None:\n                    pre.right = cur\n                    cur = cur.left\n                else:\n                    pre.right = None\n                    k -= 1\n                    if k == 0:\n                        return cur.val\n                    cur = cur.right\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/230-kth-smallest-element-in-a-bst/",
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