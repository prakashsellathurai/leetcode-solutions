# 1463-cherry-pickup-ii


Try it on <a href='https://leetcode.com/problems/1463-cherry-pickup-ii'>leetcode</a>

## Description
<div class="description">
<div><p>You are given a <code>rows x cols</code> matrix <code>grid</code> representing a field of cherries where <code>grid[i][j]</code> represents the number of cherries that you can collect from the <code>(i, j)</code> cell.</p>

<p>You have two robots that can collect cherries for you:</p>

<ul>
	<li><strong>Robot #1</strong> is located at the <strong>top-left corner</strong> <code>(0, 0)</code>, and</li>
	<li><strong>Robot #2</strong> is located at the <strong>top-right corner</strong> <code>(0, cols - 1)</code>.</li>
</ul>

<p>Return <em>the maximum number of cherries collection using both robots by following the rules below</em>:</p>

<ul>
	<li>From a cell <code>(i, j)</code>, robots can move to cell <code>(i + 1, j - 1)</code>, <code>(i + 1, j)</code>, or <code>(i + 1, j + 1)</code>.</li>
	<li>When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.</li>
	<li>When both robots stay in the same cell, only one takes the cherries.</li>
	<li>Both robots cannot move outside of the grid at any moment.</li>
	<li>Both robots should reach the bottom row in <code>grid</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/04/29/sample_1_1802.png" style="width: 374px; height: 501px;">
<pre><strong>Input:</strong> grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
<strong>Output:</strong> 24
<strong>Explanation:</strong> Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
Total of cherries: 12 + 12 = 24.
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/04/23/sample_2_1802.png" style="width: 500px; height: 452px;">
<pre><strong>Input:</strong> grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
<strong>Output:</strong> 28
<strong>Explanation:</strong> Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
Total of cherries: 17 + 11 = 28.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>rows == grid.length</code></li>
	<li><code>cols == grid[i].length</code></li>
	<li><code>2 &lt;= rows, cols &lt;= 70</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 100</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
# @Problem
#   Given matrix of values and the two robots (0,0) and (0,col-j)
#   Return max number of cherries with condition
#       *from i,j ,valid moves (i+1,j-1),(i+1,j)and(i+1,j+1)
#       *when robot sweeps ,matrix[i][j] = 0
#       *when two robots in the cells only one cantake it
#       *No outside movements
#       *Both Robots should reach bottom row
#
# @Input: 2d Matrix
# @output: maximum number of cherries value
#
# @Simple Example:
#   1. grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
#       Robot 1:  3+2+5+2 = 12
#       Robot 2:  1+5+5+1 = 12
#                 Total   = 24
#
#   2. grid =[[1,0,0,0,0,0,1],
#             [2,0,0,0,0,3,0]
#             [2,0,9,0,0,0,0],
#             [0,3,0,5,4,0,0],
#             [1,0,2,3,0,0,6]]
#       Robot1: 1+0+9+5+2 = 17
#       Robot2: 1+3+0+4+3 = 11
#                 Total   = 28
#
# @constraints:
#   rows == grid.length
#   cols == grid[i].length
#   2 <= rows, cols <= 70
#   0 <= grid[i][j] <= 100
#
#
# @Solution:
#   1.Recursive with DP cache:
#       we can construct recursive solution by considering the  state
#    with  robots on the same row.If we use different rows then
#    solution may not be optmial.since choice of path 1 influences
#    the path 2 which give rises to number of recursive calls
#    in cosmic levels. we will keep it simple with moving the robots
#   simultaneously by making optimal choices from previous moves
#
#   So Dp state will be at (row,Robot1,Robot2) denoting maximum cherries
#   if robots at (row,Robot1) and  (row,Robot2)
#   Base case when Robots reaches the bottom
#   at index (row,Robot1,Robot2) each robot can choose three positions
#   then two robots can make 3*3 possible moves simultaneuously
#   2.Bottom Up Dp:
#      state: p[row][R1][R2]
#      Base case: row = row-1 iterarte from bottom
#      Recursive case:
#           dp[row][R1][R2] += cur_val + max(dp(row+1 for all nine possible values))
#
#
#      Soluiton state: dp[0][0][rows]
#
# Time Complexity: O(mn^2)
# Space Complexity: O(mn^2)


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dp = [[[0] * cols for _ in range(cols)] for _ in range(rows)]

        # since dp state depends on dp+1 work on way up
        for row in reversed(range(rows)):
            for R1 in range(cols):
                for R2 in range(cols):
                    res = grid[row][R1]
                    res += grid[row][R2] if R1 != R2 else 0

                    if row != rows - 1:
                        res += max(
                            dp[row + 1][newR1][newR2]
                            for newR1 in [R1, R1 + 1, R1 - 1]
                            for newR2 in [R2, R2 + 1, R2 - 1]
                            if 0 <= newR1 < cols and 0 <= newR2 < cols
                        )
                    dp[row][R1][R2] = res
        return dp[0][0][cols - 1]

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1463. Cherry Pickup II",
    "text": "You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.\nYou have two robots that can collect cherries for you:\n\nRobot #1 is located at the top-left corner (0, 0), and\nRobot #2 is located at the top-right corner (0, cols - 1).\n\nReturn the maximum number of cherries collection using both robots by following the rules below:\n\nFrom a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).\nWhen any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.\nWhen both robots stay in the same cell, only one takes the cherries.\nBoth robots cannot move outside of the grid at any moment.\nBoth robots should reach the bottom row in grid.\n\n\u00a0\nExample 1:\n\nInput: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]\nOutput: 24\nExplanation: Path of robot #1 and #2 are described in color green and blue respectively.\nCherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.\nCherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.\nTotal of cherries: 12 + 12 = 24.\n\nExample 2:\n\nInput: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]\nOutput: 28\nExplanation: Path of robot #1 and #2 are described in color green and blue respectively.\nCherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.\nCherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.\nTotal of cherries: 17 + 11 = 28.\n\n\u00a0\nConstraints:\n\nrows == grid.length\ncols == grid[i].length\n2 <= rows, cols <= 70\n0 <= grid[i][j] <= 100\n\n",
    "url": "https://leetcode.com/problems/1463-cherry-pickup-ii",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# @Problem\n#   Given matrix of values and the two robots (0,0) and (0,col-j)\n#   Return max number of cherries with condition\n#       *from i,j ,valid moves (i+1,j-1),(i+1,j)and(i+1,j+1)\n#       *when robot sweeps ,matrix[i][j] = 0\n#       *when two robots in the cells only one cantake it\n#       *No outside movements\n#       *Both Robots should reach bottom row\n#\n# @Input: 2d Matrix\n# @output: maximum number of cherries value\n#\n# @Simple Example:\n#   1. grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]\n#       Robot 1:  3+2+5+2 = 12\n#       Robot 2:  1+5+5+1 = 12\n#                 Total   = 24\n#\n#   2. grid =[[1,0,0,0,0,0,1],\n#             [2,0,0,0,0,3,0]\n#             [2,0,9,0,0,0,0],\n#             [0,3,0,5,4,0,0],\n#             [1,0,2,3,0,0,6]]\n#       Robot1: 1+0+9+5+2 = 17\n#       Robot2: 1+3+0+4+3 = 11\n#                 Total   = 28\n#\n# @constraints:\n#   rows == grid.length\n#   cols == grid[i].length\n#   2 <= rows, cols <= 70\n#   0 <= grid[i][j] <= 100\n#\n#\n# @Solution:\n#   1.Recursive with DP cache:\n#       we can construct recursive solution by considering the  state\n#    with  robots on the same row.If we use different rows then\n#    solution may not be optmial.since choice of path 1 influences\n#    the path 2 which give rises to number of recursive calls\n#    in cosmic levels. we will keep it simple with moving the robots\n#   simultaneously by making optimal choices from previous moves\n#\n#   So Dp state will be at (row,Robot1,Robot2) denoting maximum cherries\n#   if robots at (row,Robot1) and  (row,Robot2)\n#   Base case when Robots reaches the bottom\n#   at index (row,Robot1,Robot2) each robot can choose three positions\n#   then two robots can make 3*3 possible moves simultaneuously\n#   2.Bottom Up Dp:\n#      state: p[row][R1][R2]\n#      Base case: row = row-1 iterarte from bottom\n#      Recursive case:\n#           dp[row][R1][R2] += cur_val + max(dp(row+1 for all nine possible values))\n#\n#\n#      Soluiton state: dp[0][0][rows]\n#\n# Time Complexity: O(mn^2)\n# Space Complexity: O(mn^2)\n\n\nclass Solution:\n    def cherryPickup(self, grid: List[List[int]]) -> int:\n        rows = len(grid)\n        cols = len(grid[0])\n\n        dp = [[[0] * cols for _ in range(cols)] for _ in range(rows)]\n\n        # since dp state depends on dp+1 work on way up\n        for row in reversed(range(rows)):\n            for R1 in range(cols):\n                for R2 in range(cols):\n                    res = grid[row][R1]\n                    res += grid[row][R2] if R1 != R2 else 0\n\n                    if row != rows - 1:\n                        res += max(\n                            dp[row + 1][newR1][newR2]\n                            for newR1 in [R1, R1 + 1, R1 - 1]\n                            for newR2 in [R2, R2 + 1, R2 - 1]\n                            if 0 <= newR1 < cols and 0 <= newR2 < cols\n                        )\n                    dp[row][R1][R2] = res\n        return dp[0][0][cols - 1]\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1463-cherry-pickup-ii/",
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