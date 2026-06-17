# 695-max-area-of-island


Try it on <a href='https://leetcode.com/problems/695-max-area-of-island'>leetcode</a>

## Description
<div class="description">
<div><p>You are given an <code>m x n</code> binary matrix <code>grid</code>. An island is a group of <code>1</code>'s (representing land) connected <strong>4-directionally</strong> (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.</p>

<p>The <strong>area</strong> of an island is the number of cells with a value <code>1</code> in the island.</p>

<p>Return <em>the maximum <strong>area</strong> of an island in </em><code>grid</code>. If there is no island, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg" style="width: 500px; height: 310px;">
<pre><strong>Input:</strong> grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The answer is not 11, because the island must be connected 4-directionally.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> grid = [[0,0,0,0,0,0,0,0]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        return self.dfs(grid)
        
    # Time Compleixty: O(m*n)
    # Space complexity: O(m*n)
    def dfs(self, grid: List[List[int]]) -> int:
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))
    
    # Time Compleixty: O(n^2)
    # Space complexity: O(n^2)
    def betterbruteforce(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])if grid[0] else 0 
        if not n or not m:
            return 0
        max_area = 0
        dirs = [(1,0), (-1,0), (0,-1), (0,1)]
        
        def dfs(x,y, visited):
            res = 1
            
            for dx, dy in dirs:
                x1,y1 = x+dx, y+dy
                if 0 <= x1 <= m-1 and 0 <= y1 <= n-1 and (x1,y1) not in visited and grid[i][j]:
                    visited.add((x1,y1))
                    res += dfs(x1,y1, visited)
                else:
                    continue
            return res
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i,j) not in visited:
                    visited.add((i,j))
                    max_area = max(max_area, dfs(i,j, visited))

        return max_area
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "695. Max Area of Island",
    "text": "You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.\nThe area of an island is the number of cells with a value 1 in the island.\nReturn the maximum area of an island in grid. If there is no island, return 0.\n\u00a0\nExample 1:\n\nInput: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]\nOutput: 6\nExplanation: The answer is not 11, because the island must be connected 4-directionally.\n\nExample 2:\nInput: grid = [[0,0,0,0,0,0,0,0]]\nOutput: 0\n\n\u00a0\nConstraints:\n\nm == grid.length\nn == grid[i].length\n1 <= m, n <= 50\ngrid[i][j] is either 0 or 1.\n\n",
    "url": "https://leetcode.com/problems/695-max-area-of-island",
    "answerCount": 1,
    "datePublished": "2023-08-20T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:\n        return self.dfs(grid)\n        \n    # Time Compleixty: O(m*n)\n    # Space complexity: O(m*n)\n    def dfs(self, grid: List[List[int]]) -> int:\n        seen = set()\n        def area(r, c):\n            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])\n                    and (r, c) not in seen and grid[r][c]):\n                return 0\n            seen.add((r, c))\n            return (1 + area(r+1, c) + area(r-1, c) +\n                    area(r, c-1) + area(r, c+1))\n\n        return max(area(r, c)\n                   for r in range(len(grid))\n                   for c in range(len(grid[0])))\n    \n    # Time Compleixty: O(n^2)\n    # Space complexity: O(n^2)\n    def betterbruteforce(self, grid: List[List[int]]) -> int:\n        m,n = len(grid), len(grid[0])if grid[0] else 0 \n        if not n or not m:\n            return 0\n        max_area = 0\n        dirs = [(1,0), (-1,0), (0,-1), (0,1)]\n        \n        def dfs(x,y, visited):\n            res = 1\n            \n            for dx, dy in dirs:\n                x1,y1 = x+dx, y+dy\n                if 0 <= x1 <= m-1 and 0 <= y1 <= n-1 and (x1,y1) not in visited and grid[i][j]:\n                    visited.add((x1,y1))\n                    res += dfs(x1,y1, visited)\n                else:\n                    continue\n            return res\n        visited = set()\n        for i in range(m):\n            for j in range(n):\n                if grid[i][j] and (i,j) not in visited:\n                    visited.add((i,j))\n                    max_area = max(max_area, dfs(i,j, visited))\n\n        return max_area",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/695-max-area-of-island/",
      "datePublished": "2023-08-20T00:00:00Z",
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