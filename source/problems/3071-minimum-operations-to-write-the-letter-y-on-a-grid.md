# 3071-minimum-operations-to-write-the-letter-y-on-a-grid


Try it on <a href='https://leetcode.com/problems/3071-minimum-operations-to-write-the-letter-y-on-a-grid'>leetcode</a>

## Description
<div class="description">
<p>You are given a <strong>0-indexed</strong> <code>n x n</code> grid where <code>n</code> is odd, and <code>grid[r][c]</code> is <code>0</code>, <code>1</code>, or <code>2</code>.</p>

<p>We say that a cell belongs to the Letter <strong>Y</strong> if it belongs to one of the following:</p>

<ul>
	<li>The diagonal starting at the top-left cell and ending at the center cell of the grid.</li>
	<li>The diagonal starting at the top-right cell and ending at the center cell of the grid.</li>
	<li>The vertical line starting at the center cell and ending at the bottom border of the grid.</li>
</ul>

<p>The Letter <strong>Y</strong> is written on the grid if and only if:</p>

<ul>
	<li>All values at cells belonging to the Y are equal.</li>
	<li>All values at cells not belonging to the Y are equal.</li>
	<li>The values at cells belonging to the Y are different from the values at cells not belonging to the Y.</li>
</ul>

<p>Return <em>the <strong>minimum</strong> number of operations needed to write the letter Y on the grid given that in one operation you can change the value at any cell to</em> <code>0</code><em>,</em> <code>1</code><em>,</em> <em>or</em> <code>2</code><em>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/22/y2.png" style="width: 461px; height: 121px;" />
<pre>
<strong>Input:</strong> grid = [[1,2,2],[1,1,0],[0,1,0]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can write Y on the grid by applying the changes highlighted in blue in the image above. After the operations, all cells that belong to Y, denoted in bold, have the same value of 1 while those that do not belong to Y are equal to 0.
It can be shown that 3 is the minimum number of operations needed to write Y on the grid.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/22/y3.png" style="width: 701px; height: 201px;" />
<pre>
<strong>Input:</strong> grid = [[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]]
<strong>Output:</strong> 12
<strong>Explanation:</strong> We can write Y on the grid by applying the changes highlighted in blue in the image above. After the operations, all cells that belong to Y, denoted in bold, have the same value of 0 while those that do not belong to Y are equal to 2. 
It can be shown that 12 is the minimum number of operations needed to write Y on the grid.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= n &lt;= 49 </code></li>
	<li><code>n == grid.length == grid[i].length</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 2</code></li>
	<li><code>n</code> is odd.</li>
</ul>

</div>

## Solution(Python)
```Python
class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        y_cells_counter = Counter()
        non_y_cells_counter = Counter()
        for row_idx, row in enumerate(grid):
            for col_idx, cell_value in enumerate(row):

                is_left_diagnol = (row_idx == col_idx) and row_idx <= n//2 
                is_right_diagnol = (row_idx + col_idx == n-1) and row_idx <= n//2 
                is_center_stem = ( col_idx == n//2) and row_idx >= n//2 

                if is_left_diagnol or is_right_diagnol or is_center_stem:
                    y_cells_counter[cell_value] +=1
                else:
                    non_y_cells_counter[cell_value] +=1
        total_cells = n*n

        min_ops = min(
            total_cells -  y_cells_counter[y_color] -  non_y_cells_counter[non_y_color]
            for y_color in range(3)
            for non_y_color in range(3)
            if y_color != non_y_color
        )

        return min_ops
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "3071. Minimum Operations to Write the Letter Y on a Grid",
    "text": "You are given a 0-indexed n x n grid where n is odd, and grid[r][c] is 0, 1, or 2.\nWe say that a cell belongs to the Letter Y if it belongs to one of the following:\n\nThe diagonal starting at the top-left cell and ending at the center cell of the grid.\nThe diagonal starting at the top-right cell and ending at the center cell of the grid.\nThe vertical line starting at the center cell and ending at the bottom border of the grid.\n\nThe Letter Y is written on the grid if and only if:\n\nAll values at cells belonging to the Y are equal.\nAll values at cells not belonging to the Y are equal.\nThe values at cells belonging to the Y are different from the values at cells not belonging to the Y.\n\nReturn the minimum number of operations needed to write the letter Y on the grid given that in one operation you can change the value at any cell to 0, 1, or 2.\n\u00a0\nExample 1:\n\n\nInput: grid = [[1,2,2],[1,1,0],[0,1,0]]\nOutput: 3\nExplanation: We can write Y on the grid by applying the changes highlighted in blue in the image above. After the operations, all cells that belong to Y, denoted in bold, have the same value of 1 while those that do not belong to Y are equal to 0.\nIt can be shown that 3 is the minimum number of operations needed to write Y on the grid.\n\nExample 2:\n\n\nInput: grid = [[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]]\nOutput: 12\nExplanation: We can write Y on the grid by applying the changes highlighted in blue in the image above. After the operations, all cells that belong to Y, denoted in bold, have the same value of 0 while those that do not belong to Y are equal to 2. \nIt can be shown that 12 is the minimum number of operations needed to write Y on the grid.\n\u00a0\nConstraints:\n\n3 <= n <= 49 \nn == grid.length == grid[i].length\n0 <= grid[i][j] <= 2\nn is odd.\n\n",
    "url": "https://leetcode.com/problems/3071-minimum-operations-to-write-the-letter-y-on-a-grid",
    "answerCount": 1,
    "datePublished": "2022-10-21T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:\n        n = len(grid)\n        y_cells_counter = Counter()\n        non_y_cells_counter = Counter()\n        for row_idx, row in enumerate(grid):\n            for col_idx, cell_value in enumerate(row):\n\n                is_left_diagnol = (row_idx == col_idx) and row_idx <= n//2 \n                is_right_diagnol = (row_idx + col_idx == n-1) and row_idx <= n//2 \n                is_center_stem = ( col_idx == n//2) and row_idx >= n//2 \n\n                if is_left_diagnol or is_right_diagnol or is_center_stem:\n                    y_cells_counter[cell_value] +=1\n                else:\n                    non_y_cells_counter[cell_value] +=1\n        total_cells = n*n\n\n        min_ops = min(\n            total_cells -  y_cells_counter[y_color] -  non_y_cells_counter[non_y_color]\n            for y_color in range(3)\n            for non_y_color in range(3)\n            if y_color != non_y_color\n        )\n\n        return min_ops",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/3071-minimum-operations-to-write-the-letter-y-on-a-grid/",
      "datePublished": "2022-10-21T00:00:00Z",
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