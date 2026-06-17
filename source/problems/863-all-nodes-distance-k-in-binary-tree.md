# 863-all-nodes-distance-k-in-binary-tree


Try it on <a href='https://leetcode.com/problems/863-all-nodes-distance-k-in-binary-tree'>leetcode</a>

## Description
<div class="description">
<div><p>Given the <code>root</code> of a binary tree, the value of a target node <code>target</code>, and an integer <code>k</code>, return <em>an array of the values of all nodes that have a distance </em><code>k</code><em> from the target node.</em></p>

<p>You can return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png" style="width: 500px; height: 429px;">
<pre><strong>Input:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
<strong>Output:</strong> [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> root = [1], target = 1, k = 3
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 500]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 500</code></li>
	<li>All the values <code>Node.val</code> are <strong>unique</strong>.</li>
	<li><code>target</code> is the value of one of the nodes in the tree.</li>
	<li><code>0 &lt;= k &lt;= 1000</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution(object):
    def distanceK(self, root, target, K):
        def dfs(node, par=None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        queue = collections.deque([(target, 0)])
        seen = {target}
        while queue:
            if queue[0][1] == K:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d + 1))

        return []

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "863. All Nodes Distance K in Binary Tree",
    "text": "Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.\nYou can return the answer in any order.\n\u00a0\nExample 1:\n\nInput: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2\nOutput: [7,4,1]\nExplanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.\n\nExample 2:\nInput: root = [1], target = 1, k = 3\nOutput: []\n\n\u00a0\nConstraints:\n\nThe number of nodes in the tree is in the range [1, 500].\n0 <= Node.val <= 500\nAll the values Node.val are unique.\ntarget is the value of one of the nodes in the tree.\n0 <= k <= 1000\n\n",
    "url": "https://leetcode.com/problems/863-all-nodes-distance-k-in-binary-tree",
    "answerCount": 1,
    "datePublished": "2024-11-30T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution(object):\n    def distanceK(self, root, target, K):\n        def dfs(node, par=None):\n            if node:\n                node.par = par\n                dfs(node.left, node)\n                dfs(node.right, node)\n\n        dfs(root)\n\n        queue = collections.deque([(target, 0)])\n        seen = {target}\n        while queue:\n            if queue[0][1] == K:\n                return [node.val for node, d in queue]\n            node, d = queue.popleft()\n            for nei in (node.left, node.right, node.par):\n                if nei and nei not in seen:\n                    seen.add(nei)\n                    queue.append((nei, d + 1))\n\n        return []\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/863-all-nodes-distance-k-in-binary-tree/",
      "datePublished": "2024-11-30T00:00:00Z",
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