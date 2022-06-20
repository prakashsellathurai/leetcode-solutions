# Maximal-Square


Try it on <a href='https://leetcode.com/problems/maximal-square'>leetcode</a>

## Description
<div class="description">
<div><p>Given an <code>m x n</code> binary <code>matrix</code> filled with <code>0</code>'s and <code>1</code>'s, <em>find the largest square containing only</em> <code>1</code>'s <em>and return its area</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/max1grid.jpg" style="width: 400px; height: 319px;">
<pre><strong>Input:</strong> matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
<strong>Output:</strong> 4
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/max2grid.jpg" style="width: 165px; height: 165px;">
<pre><strong>Input:</strong> matrix = [["0","1"],["1","0"]]
<strong>Output:</strong> 1
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> matrix = [["0"]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 300</code></li>
	<li><code>matrix[i][j]</code> is <code>'0'</code> or <code>'1'</code>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def maximalSquare(self, A):
        maxSol = 0
        for i in range(len(A)):
            for j in range(len(A[i])):
                A[i][j] = int(A[i][j])
                if A[i][j] and i and j:
                    A[i][j] = min(A[i-1][j], A[i-1][j-1], A[i][j-1]) + 1
                if maxSol < A[i][j]:
                    maxSol = A[i][j]
        return  maxSol *maxSol
```