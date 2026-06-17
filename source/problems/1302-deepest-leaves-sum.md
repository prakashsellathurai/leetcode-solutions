# 1302-deepest-leaves-sum


Try it on <a href='https://leetcode.com/problems/1302-deepest-leaves-sum'>leetcode</a>

## Description
<div class="description">
<div>Given the <code>root</code> of a binary tree, return <em>the sum of values of its deepest leaves</em>.
<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/07/31/1483_ex1.png" style="width: 273px; height: 265px;">
<pre><strong>Input:</strong> root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
<strong>Output:</strong> 15
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
<strong>Output:</strong> 19
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 100</code></li>
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
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        return self.morristraversal(root)

    # Time Complexity: O(n)
    # Space Complexity: O(h)
    def dfs(self, root: Optional[TreeNode]) -> int:
        def lendfs(node):
            if node:
                left = lendfs(node.left)
                right = lendfs(node.right)
                return max(left, right) + 1
            return 0

        length = lendfs(root)
        maxsum = 0

        def calcSum(node, depth):
            nonlocal maxsum
            if not node:
                return
            if depth == 1 and not node.left and not node.right:
                maxsum += node.val

            calcSum(node.left, depth - 1)
            calcSum(node.right, depth - 1)

        calcSum(root, length)
        return maxsum

    # Time Complexity: O(n)
    # Space Complexity: O(h)
    def bfs(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        cursum = 0

        while q:
            cursum = 0
            qsize = len(q)
            for i in range(qsize):
                p = q.popleft()
                cursum += p.val
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
        return cursum

    # Time Complexity: O(n)
    # Space Complexity: O(h)
    def singledfs(self, root: Optional[TreeNode]) -> int:
        maxsum = 0
        maxlevel = 0

        def dfs(node, level):
            nonlocal maxsum, maxlevel
            if not node:
                return

            if level > maxlevel:
                maxsum = node.val
                maxlevel = level
            elif level == maxlevel:
                maxsum += node.val

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return maxsum

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def morristraversal(self, root: Optional[TreeNode]) -> int:
        def morris(node):
            depth = 0
            while node:
                if not node.left:
                    yield node.val, depth
                    node = node.right
                    depth += 1
                else:
                    prev = node.left
                    down = 1
                    while prev.right not in (None, node):
                        prev = prev.right
                        down += 1
                    if prev.right:
                        prev.right = None
                        depth -= down + 1
                        yield node.val, depth
                        node = node.right
                        depth += 1
                    else:
                        prev.right = node
                        node = node.left
                        depth += 1

        maxDepth = max(depth for _, depth in morris(root))
        return sum(val for val, depth in morris(root) if depth == maxDepth)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1302. Deepest Leaves Sum",
    "text": "Given the root of a binary tree, return the sum of values of its deepest leaves.\n\u00a0\nExample 1:\n\nInput: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]\nOutput: 15\n\nExample 2:\nInput: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]\nOutput: 19\n\n\u00a0\nConstraints:\n\nThe number of nodes in the tree is in the range [1, 104].\n1 <= Node.val <= 100\n\n",
    "url": "https://leetcode.com/problems/1302-deepest-leaves-sum",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:\n        return self.morristraversal(root)\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(h)\n    def dfs(self, root: Optional[TreeNode]) -> int:\n        def lendfs(node):\n            if node:\n                left = lendfs(node.left)\n                right = lendfs(node.right)\n                return max(left, right) + 1\n            return 0\n\n        length = lendfs(root)\n        maxsum = 0\n\n        def calcSum(node, depth):\n            nonlocal maxsum\n            if not node:\n                return\n            if depth == 1 and not node.left and not node.right:\n                maxsum += node.val\n\n            calcSum(node.left, depth - 1)\n            calcSum(node.right, depth - 1)\n\n        calcSum(root, length)\n        return maxsum\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(h)\n    def bfs(self, root: Optional[TreeNode]) -> int:\n        q = deque([root])\n        cursum = 0\n\n        while q:\n            cursum = 0\n            qsize = len(q)\n            for i in range(qsize):\n                p = q.popleft()\n                cursum += p.val\n                if p.left:\n                    q.append(p.left)\n                if p.right:\n                    q.append(p.right)\n        return cursum\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(h)\n    def singledfs(self, root: Optional[TreeNode]) -> int:\n        maxsum = 0\n        maxlevel = 0\n\n        def dfs(node, level):\n            nonlocal maxsum, maxlevel\n            if not node:\n                return\n\n            if level > maxlevel:\n                maxsum = node.val\n                maxlevel = level\n            elif level == maxlevel:\n                maxsum += node.val\n\n            dfs(node.left, level + 1)\n            dfs(node.right, level + 1)\n\n        dfs(root, 0)\n        return maxsum\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(1)\n    def morristraversal(self, root: Optional[TreeNode]) -> int:\n        def morris(node):\n            depth = 0\n            while node:\n                if not node.left:\n                    yield node.val, depth\n                    node = node.right\n                    depth += 1\n                else:\n                    prev = node.left\n                    down = 1\n                    while prev.right not in (None, node):\n                        prev = prev.right\n                        down += 1\n                    if prev.right:\n                        prev.right = None\n                        depth -= down + 1\n                        yield node.val, depth\n                        node = node.right\n                        depth += 1\n                    else:\n                        prev.right = node\n                        node = node.left\n                        depth += 1\n\n        maxDepth = max(depth for _, depth in morris(root))\n        return sum(val for val, depth in morris(root) if depth == maxDepth)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1302-deepest-leaves-sum/",
      "datePublished": "2024-02-09",
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