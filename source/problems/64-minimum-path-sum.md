# 64-minimum-path-sum


Try it on <a href='https://leetcode.com/problems/64-minimum-path-sum'>leetcode</a>

## Description
<div class="description">
<div><p>Given a <code>m x n</code> <code>grid</code> filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.</p>

<p><strong>Note:</strong> You can only move either down or right at any point in time.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg" style="width: 242px; height: 242px;">
<pre><strong>Input:</strong> grid = [[1,3,1],[1,5,1],[4,2,1]]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> grid = [[1,2,3],[4,5,6]]
<strong>Output:</strong> 12
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 100</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
                    
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i][j-1],dp[i-1][j] ) + grid[i][j]
                    
        return dp[-1][-1]
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "64. Minimum Path Sum",
    "text": "Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.\nNote: You can only move either down or right at any point in time.\n\u00a0\nExample 1:\n\nInput: grid = [[1,3,1],[1,5,1],[4,2,1]]\nOutput: 7\nExplanation: Because the path 1 \u2192 3 \u2192 1 \u2192 1 \u2192 1 minimizes the sum.\n\nExample 2:\nInput: grid = [[1,2,3],[4,5,6]]\nOutput: 12\n\n\u00a0\nConstraints:\n\nm == grid.length\nn == grid[i].length\n1 <= m, n <= 200\n0 <= grid[i][j] <= 100\n\n",
    "url": "https://leetcode.com/problems/64-minimum-path-sum",
    "answerCount": 1,
    "datePublished": "2023-06-30T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def minPathSum(self, grid: List[List[int]]) -> int:\n        m = len(grid)\n        n = len(grid[0])\n        dp = [[0 for _ in range(n)] for _ in range(m)]\n        dp[0][0] = grid[0][0]\n        \n        for j in range(1,n):\n            dp[0][j] = dp[0][j-1] + grid[0][j]\n                    \n        for i in range(1,m):\n            dp[i][0] = dp[i-1][0] + grid[i][0]\n\n        for i in range(1,m):\n            for j in range(1,n):\n                dp[i][j] = min(dp[i][j-1],dp[i-1][j] ) + grid[i][j]\n                    \n        return dp[-1][-1]",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/64-minimum-path-sum/",
      "datePublished": "2023-06-30T00:00:00Z",
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