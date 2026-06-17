# 463-island-perimeter


Try it on <a href='https://leetcode.com/problems/463-island-perimeter'>leetcode</a>

## Description
<div class="description">
<div><p>You are given <code>row x col</code> <code>grid</code> representing a map where <code>grid[i][j] = 1</code> represents&nbsp;land and <code>grid[i][j] = 0</code> represents water.</p>

<p>Grid cells are connected <strong>horizontally/vertically</strong> (not diagonally). The <code>grid</code> is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).</p>

<p>The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2018/10/12/island.png" style="width: 221px; height: 213px;">
<pre><strong>Input:</strong> grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
<strong>Output:</strong> 16
<strong>Explanation:</strong> The perimeter is the 16 yellow stripes in the image above.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> grid = [[1]]
<strong>Output:</strong> 4
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> grid = [[1,0]]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>row == grid.length</code></li>
	<li><code>col == grid[i].length</code></li>
	<li><code>1 &lt;= row, col &lt;= 100</code></li>
	<li><code>grid[i][j]</code> is <code>0</code> or <code>1</code>.</li>
	<li>There is exactly one island in <code>grid</code>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n, Perimeter = len(grid), len(grid[0]), 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    Perimeter += 4
                    if i > 0 and grid[i - 1][j]:
                        Perimeter -= 2

                    if j > 0 and grid[i][j - 1]:
                        Perimeter -= 2

        return Perimeter

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "463. Island Perimeter",
    "text": "You are given row x col grid representing a map where grid[i][j] = 1 represents\u00a0land and grid[i][j] = 0 represents water.\nGrid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).\nThe island doesn't have \"lakes\", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.\n\u00a0\nExample 1:\n\nInput: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]\nOutput: 16\nExplanation: The perimeter is the 16 yellow stripes in the image above.\n\nExample 2:\nInput: grid = [[1]]\nOutput: 4\n\nExample 3:\nInput: grid = [[1,0]]\nOutput: 4\n\n\u00a0\nConstraints:\n\nrow == grid.length\ncol == grid[i].length\n1 <= row, col <= 100\ngrid[i][j] is 0 or 1.\nThere is exactly one island in grid.\n\n",
    "url": "https://leetcode.com/problems/463-island-perimeter",
    "answerCount": 1,
    "datePublished": "2022-07-18T17:45:55+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def islandPerimeter(self, grid: List[List[int]]) -> int:\n        m, n, Perimeter = len(grid), len(grid[0]), 0\n\n        for i in range(m):\n            for j in range(n):\n                if grid[i][j]:\n                    Perimeter += 4\n                    if i > 0 and grid[i - 1][j]:\n                        Perimeter -= 2\n\n                    if j > 0 and grid[i][j - 1]:\n                        Perimeter -= 2\n\n        return Perimeter\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/463-island-perimeter/",
      "datePublished": "2022-07-18T17:45:55+05:30",
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