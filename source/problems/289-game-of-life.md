# 289-game-of-life


Try it on <a href='https://leetcode.com/problems/289-game-of-life'>leetcode</a>

## Description
<div class="description">
<div><p>According to&nbsp;<a href="https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life" target="_blank">Wikipedia's article</a>: "The <b>Game of Life</b>, also known simply as <b>Life</b>, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."</p>

<p>The board is made up of an <code>m x n</code> grid of cells, where each cell has an initial state: <b>live</b> (represented by a <code>1</code>) or <b>dead</b> (represented by a <code>0</code>). Each cell interacts with its <a href="https://en.wikipedia.org/wiki/Moore_neighborhood" target="_blank">eight neighbors</a> (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):</p>

<ol>
	<li>Any live cell with fewer than two live neighbors dies as if caused by under-population.</li>
	<li>Any live cell with two or three live neighbors lives on to the next generation.</li>
	<li>Any live cell with more than three live neighbors dies, as if by over-population.</li>
	<li>Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.</li>
</ol>

<p><span>The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the <code>m x n</code> grid <code>board</code>, return <em>the next state</em>.</span></p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/26/grid1.jpg" style="width: 562px; height: 322px;">
<pre><strong>Input:</strong> board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
<strong>Output:</strong> [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/26/grid2.jpg" style="width: 402px; height: 162px;">
<pre><strong>Input:</strong> board = [[1,1],[1,0]]
<strong>Output:</strong> [[1,1],[1,1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n == board[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 25</code></li>
	<li><code>board[i][j]</code> is <code>0</code> or <code>1</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<ul>
	<li>Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.</li>
	<li>In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    #     def gameOfLife(self, board: List[List[int]]) -> None:
    #         """
    #         Do not return anything, modify board in-place instead.
    #         """
    #         if board is None or len(board) == 0:
    #             return

    #         m = len(board)
    #         n = len(board[0])

    #         for i in range(m):
    #             for j in range(n):
    #                 lives = self.count_live_neighours(i,j,m,n,board)

    #                 if board[i][j] == 1  and lives >= 2 and lives <= 3:
    #                     board[i][j] = 3
    #                 if  board[i][j] == 0 and lives == 3:
    #                     board[i][j] = 2

    #         for i in range(m):
    #             for j in range(n):
    #                 board[i][j]  >>= 1

    #     def count_live_neighours(self,i,j,m,n,board):
    #         lives = 0

    #         for x in  range(max(i-1,0),min(i+1,m-1)+1):
    #             for y in range(max(j-1,0),min(j+1,n-1)+1):
    #                 lives+=board[x][y]&1
    #         lives -= board[i][j]&1

    #         return lives

    def gameOfLifeInfinite(self, live):
        ctr = collections.Counter(
            (I, J)
            for i, j in live
            for I in range(i - 1, i + 2)
            for J in range(j - 1, j + 2)
            if I != i or J != j
        )
        return {ij for ij in ctr if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}

    def gameOfLife(self, board):
        live = {
            (i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live
        }
        live = self.gameOfLifeInfinite(live)
        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i, j) in live)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "289. Game of Life",
    "text": "According to\u00a0Wikipedia's article: \"The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.\"\nThe board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):\n\nAny live cell with fewer than two live neighbors dies as if caused by under-population.\nAny live cell with two or three live neighbors lives on to the next generation.\nAny live cell with more than three live neighbors dies, as if by over-population.\nAny dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.\n\nThe next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.\n\u00a0\nExample 1:\n\nInput: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]\nOutput: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]\n\nExample 2:\n\nInput: board = [[1,1],[1,0]]\nOutput: [[1,1],[1,1]]\n\n\u00a0\nConstraints:\n\nm == board.length\nn == board[i].length\n1 <= m, n <= 25\nboard[i][j] is 0 or 1.\n\n\u00a0\nFollow up:\n\nCould you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.\nIn this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?\n\n",
    "url": "https://leetcode.com/problems/289-game-of-life",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    #     def gameOfLife(self, board: List[List[int]]) -> None:\n    #         \"\"\"\n    #         Do not return anything, modify board in-place instead.\n    #         \"\"\"\n    #         if board is None or len(board) == 0:\n    #             return\n\n    #         m = len(board)\n    #         n = len(board[0])\n\n    #         for i in range(m):\n    #             for j in range(n):\n    #                 lives = self.count_live_neighours(i,j,m,n,board)\n\n    #                 if board[i][j] == 1  and lives >= 2 and lives <= 3:\n    #                     board[i][j] = 3\n    #                 if  board[i][j] == 0 and lives == 3:\n    #                     board[i][j] = 2\n\n    #         for i in range(m):\n    #             for j in range(n):\n    #                 board[i][j]  >>= 1\n\n    #     def count_live_neighours(self,i,j,m,n,board):\n    #         lives = 0\n\n    #         for x in  range(max(i-1,0),min(i+1,m-1)+1):\n    #             for y in range(max(j-1,0),min(j+1,n-1)+1):\n    #                 lives+=board[x][y]&1\n    #         lives -= board[i][j]&1\n\n    #         return lives\n\n    def gameOfLifeInfinite(self, live):\n        ctr = collections.Counter(\n            (I, J)\n            for i, j in live\n            for I in range(i - 1, i + 2)\n            for J in range(j - 1, j + 2)\n            if I != i or J != j\n        )\n        return {ij for ij in ctr if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}\n\n    def gameOfLife(self, board):\n        live = {\n            (i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live\n        }\n        live = self.gameOfLifeInfinite(live)\n        for i, row in enumerate(board):\n            for j in range(len(row)):\n                row[j] = int((i, j) in live)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/289-game-of-life/",
      "datePublished": "2023-05-21",
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