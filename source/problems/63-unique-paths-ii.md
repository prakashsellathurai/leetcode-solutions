# 63-unique-paths-ii


Try it on <a href='https://leetcode.com/problems/63-unique-paths-ii'>leetcode</a>

## Description
<div class="description">
<div><p>You are given an <code>m x n</code> integer array <code>grid</code>. There is a robot initially located at the <b>top-left corner</b> (i.e., <code>grid[0][0]</code>). The robot tries to move to the <strong>bottom-right corner</strong> (i.e., <code>grid[m-1][n-1]</code>). The robot can only move either down or right at any point in time.</p>

<p>An obstacle and space are marked as <code>1</code> or <code>0</code> respectively in <code>grid</code>. A path that the robot takes cannot include <strong>any</strong> square that is an obstacle.</p>

<p>Return <em>the number of possible unique paths that the robot can take to reach the bottom-right corner</em>.</p>

<p>The testcases are generated so that the answer will be less than or equal to <code>2 * 10<sup>9</sup></code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg" style="width: 242px; height: 242px;">
<pre><strong>Input:</strong> obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -&gt; Right -&gt; Down -&gt; Down
2. Down -&gt; Down -&gt; Right -&gt; Right
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/robot2.jpg" style="width: 162px; height: 162px;">
<pre><strong>Input:</strong> obstacleGrid = [[0,1],[0,0]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == obstacleGrid.length</code></li>
	<li><code>n == obstacleGrid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>obstacleGrid[i][j]</code> is <code>0</code> or <code>1</code>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        self.obstacleGrid = obstacleGrid
        return self.topdown(0, 0)

    def inplacedp(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If the starting cell has an obstacle, then simply return as there would be
        # no paths to the destination.
        if obstacleGrid[0][0] == 1:
            return 0

        # Number of ways of reaching the starting cell = 1.
        obstacleGrid[0][0] = 1

        # Filling the values for the first column
        for i in range(1, m):
            obstacleGrid[i][0] = int(
                obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1
            )

        # Filling the values for the first row
        for j in range(1, n):
            obstacleGrid[0][j] = int(
                obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1
            )

        # Starting from cell(1,1) fill up the values
        # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
        # i.e. From above and left.
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + \
                        obstacleGrid[i][j - 1]
                else:
                    obstacleGrid[i][j] = 0

        # Return value stored in rightmost bottommost cell. That is the destination.
        return obstacleGrid[m - 1][n - 1]

    def dfs(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        def recur(i, j):

            if i == m - 1 and j == n - 1:
                return 1

            if i >= m or j >= n or obstacleGrid[i][j]:
                return 0

            return recur(i + 1, j) + recur(i, j + 1)

        return recur(0, 0)

    @cache
    def topdown(self, i, j):

        m, n = len(self.obstacleGrid), len(self.obstacleGrid[0])

        if i == m - 1 and j == n - 1 and not self.obstacleGrid[i][j]:
            return 1

        if i >= m or j >= n or self.obstacleGrid[i][j]:
            return 0
        return self.topdown(i + 1, j) + self.topdown(i, j + 1)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "63. Unique Paths II",
    "text": "You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.\nAn obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.\nReturn the number of possible unique paths that the robot can take to reach the bottom-right corner.\nThe testcases are generated so that the answer will be less than or equal to 2 * 109.\n\u00a0\nExample 1:\n\nInput: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]\nOutput: 2\nExplanation: There is one obstacle in the middle of the 3x3 grid above.\nThere are two ways to reach the bottom-right corner:\n1. Right -> Right -> Down -> Down\n2. Down -> Down -> Right -> Right\n\nExample 2:\n\nInput: obstacleGrid = [[0,1],[0,0]]\nOutput: 1\n\n\u00a0\nConstraints:\n\nm == obstacleGrid.length\nn == obstacleGrid[i].length\n1 <= m, n <= 100\nobstacleGrid[i][j] is 0 or 1.\n\n",
    "url": "https://leetcode.com/problems/63-unique-paths-ii",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution(object):\n    def uniquePathsWithObstacles(self, obstacleGrid):\n        \"\"\"\n        :type obstacleGrid: List[List[int]]\n        :rtype: int\n        \"\"\"\n        self.obstacleGrid = obstacleGrid\n        return self.topdown(0, 0)\n\n    def inplacedp(self, obstacleGrid):\n        m = len(obstacleGrid)\n        n = len(obstacleGrid[0])\n\n        # If the starting cell has an obstacle, then simply return as there would be\n        # no paths to the destination.\n        if obstacleGrid[0][0] == 1:\n            return 0\n\n        # Number of ways of reaching the starting cell = 1.\n        obstacleGrid[0][0] = 1\n\n        # Filling the values for the first column\n        for i in range(1, m):\n            obstacleGrid[i][0] = int(\n                obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1\n            )\n\n        # Filling the values for the first row\n        for j in range(1, n):\n            obstacleGrid[0][j] = int(\n                obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1\n            )\n\n        # Starting from cell(1,1) fill up the values\n        # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]\n        # i.e. From above and left.\n        for i in range(1, m):\n            for j in range(1, n):\n                if obstacleGrid[i][j] == 0:\n                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + \\\n                        obstacleGrid[i][j - 1]\n                else:\n                    obstacleGrid[i][j] = 0\n\n        # Return value stored in rightmost bottommost cell. That is the destination.\n        return obstacleGrid[m - 1][n - 1]\n\n    def dfs(self, obstacleGrid):\n        m, n = len(obstacleGrid), len(obstacleGrid[0])\n\n        def recur(i, j):\n\n            if i == m - 1 and j == n - 1:\n                return 1\n\n            if i >= m or j >= n or obstacleGrid[i][j]:\n                return 0\n\n            return recur(i + 1, j) + recur(i, j + 1)\n\n        return recur(0, 0)\n\n    @cache\n    def topdown(self, i, j):\n\n        m, n = len(self.obstacleGrid), len(self.obstacleGrid[0])\n\n        if i == m - 1 and j == n - 1 and not self.obstacleGrid[i][j]:\n            return 1\n\n        if i >= m or j >= n or self.obstacleGrid[i][j]:\n            return 0\n        return self.topdown(i + 1, j) + self.topdown(i, j + 1)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/63-unique-paths-ii/",
      "datePublished": "2022-04-02",
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