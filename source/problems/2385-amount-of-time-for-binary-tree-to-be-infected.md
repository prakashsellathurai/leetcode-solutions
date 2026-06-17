# 2385-amount-of-time-for-binary-tree-to-be-infected


Try it on <a href='https://leetcode.com/problems/2385-amount-of-time-for-binary-tree-to-be-infected'>leetcode</a>

## Description
<div class="description">
<p>You are given the <code>root</code> of a binary tree with <strong>unique</strong> values, and an integer <code>start</code>. At minute <code>0</code>, an <strong>infection</strong> starts from the node with value <code>start</code>.</p>

<p>Each minute, a node becomes infected if:</p>

<ul>
	<li>The node is currently uninfected.</li>
	<li>The node is adjacent to an infected node.</li>
</ul>

<p>Return <em>the number of minutes needed for the entire tree to be infected.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/06/25/image-20220625231744-1.png" style="width: 400px; height: 306px;" />
<pre>
<strong>Input:</strong> root = [1,5,3,null,4,10,6,9,2], start = 3
<strong>Output:</strong> 4
<strong>Explanation:</strong> The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/06/25/image-20220625231812-2.png" style="width: 75px; height: 66px;" />
<pre>
<strong>Input:</strong> root = [1], start = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> At minute 0, the only node in the tree is infected so we return 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>5</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li>Each node has a <strong>unique</strong> value.</li>
	<li>A node with a value of <code>start</code> exists in the tree.</li>
</ul>

</div>

## Solution(Python)
```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        return self.onepass(root, start)

    # TIme complexity: O(n)
    # Space complexiy: O(n)
    def twopass(self, root: Optional[TreeNode], start: int) -> int:
        # 1 build the graph from tree make connectionfrom node -> parents
        graph = defaultdict(list)
        def buidlGraph(cur, parent):
            if cur is not None and parent is not None:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            if cur.left is not None:
                buidlGraph(cur.left, cur)
            if cur.right is not None:
                buidlGraph(cur.right, cur)
        buidlGraph(root, None)
        # 2 run dfs from the start node and track the maximum length by a max _length variable
        max_len = 0
        queue = deque([(start, 0)])
        visited = set([start])

        while len(queue) > 0:
            node, distance = queue.popleft()
            if distance > max_len:
                max_len = distance
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, distance+1))
        return max_len

    # TIme complexity: O(n)
    # Space complexiy: O(n)
    def onepass(self, root: Optional[TreeNode], start: int) -> int:
        max_distance = 0
        def traverse(root, start):
            nonlocal  max_distance
            depth = 0
            if root is None:
                return depth
            
            left_depth = traverse(root.left, start)
            right_depth = traverse(root.right, start)

            if root.val == start:
                max_distance = max(left_depth, right_depth)
                depth =  -1
            elif left_depth >= 0 and right_depth >= 0:
                depth = max(left_depth, right_depth) + 1
            else:
                distance = abs(left_depth) + abs(right_depth)
                max_distance = max(max_distance, distance)
                depth = min(left_depth, right_depth) - 1
            return depth
        traverse(root,start)
        return max_distance
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "2385. Amount of Time for Binary Tree to Be Infected",
    "text": "You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.\nEach minute, a node becomes infected if:\n\nThe node is currently uninfected.\nThe node is adjacent to an infected node.\n\nReturn the number of minutes needed for the entire tree to be infected.\n\u00a0\nExample 1:\n\n\nInput: root = [1,5,3,null,4,10,6,9,2], start = 3\nOutput: 4\nExplanation: The following nodes are infected during:\n- Minute 0: Node 3\n- Minute 1: Nodes 1, 10 and 6\n- Minute 2: Node 5\n- Minute 3: Node 4\n- Minute 4: Nodes 9 and 2\nIt takes 4 minutes for the whole tree to be infected so we return 4.\n\nExample 2:\n\n\nInput: root = [1], start = 1\nOutput: 0\nExplanation: At minute 0, the only node in the tree is infected so we return 0.\n\n\u00a0\nConstraints:\n\nThe number of nodes in the tree is in the range [1, 105].\n1 <= Node.val <= 105\nEach node has a unique value.\nA node with a value of start exists in the tree.\n\n",
    "url": "https://leetcode.com/problems/2385-amount-of-time-for-binary-tree-to-be-infected",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nfrom collections import defaultdict, deque\nclass Solution:\n    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:\n        return self.onepass(root, start)\n\n    # TIme complexity: O(n)\n    # Space complexiy: O(n)\n    def twopass(self, root: Optional[TreeNode], start: int) -> int:\n        # 1 build the graph from tree make connectionfrom node -> parents\n        graph = defaultdict(list)\n        def buidlGraph(cur, parent):\n            if cur is not None and parent is not None:\n                graph[cur.val].append(parent.val)\n                graph[parent.val].append(cur.val)\n            if cur.left is not None:\n                buidlGraph(cur.left, cur)\n            if cur.right is not None:\n                buidlGraph(cur.right, cur)\n        buidlGraph(root, None)\n        # 2 run dfs from the start node and track the maximum length by a max _length variable\n        max_len = 0\n        queue = deque([(start, 0)])\n        visited = set([start])\n\n        while len(queue) > 0:\n            node, distance = queue.popleft()\n            if distance > max_len:\n                max_len = distance\n            for neighbour in graph[node]:\n                if neighbour not in visited:\n                    visited.add(neighbour)\n                    queue.append((neighbour, distance+1))\n        return max_len\n\n    # TIme complexity: O(n)\n    # Space complexiy: O(n)\n    def onepass(self, root: Optional[TreeNode], start: int) -> int:\n        max_distance = 0\n        def traverse(root, start):\n            nonlocal  max_distance\n            depth = 0\n            if root is None:\n                return depth\n            \n            left_depth = traverse(root.left, start)\n            right_depth = traverse(root.right, start)\n\n            if root.val == start:\n                max_distance = max(left_depth, right_depth)\n                depth =  -1\n            elif left_depth >= 0 and right_depth >= 0:\n                depth = max(left_depth, right_depth) + 1\n            else:\n                distance = abs(left_depth) + abs(right_depth)\n                max_distance = max(max_distance, distance)\n                depth = min(left_depth, right_depth) - 1\n            return depth\n        traverse(root,start)\n        return max_distance",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/2385-amount-of-time-for-binary-tree-to-be-infected/",
      "datePublished": "2023-01-19",
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