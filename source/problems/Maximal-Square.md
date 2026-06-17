# maximal-square


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
                    A[i][j] = min(A[i - 1][j], A[i - 1]
                                  [j - 1], A[i][j - 1]) + 1
                if maxSol < A[i][j]:
                    maxSol = A[i][j]
        return maxSol * maxSol

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "221. Maximal Square",
    "text": "Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.\n\u00a0\nExample 1:\n\nInput: matrix = [[\"1\",\"0\",\"1\",\"0\",\"0\"],[\"1\",\"0\",\"1\",\"1\",\"1\"],[\"1\",\"1\",\"1\",\"1\",\"1\"],[\"1\",\"0\",\"0\",\"1\",\"0\"]]\nOutput: 4\n\nExample 2:\n\nInput: matrix = [[\"0\",\"1\"],[\"1\",\"0\"]]\nOutput: 1\n\nExample 3:\nInput: matrix = [[\"0\"]]\nOutput: 0\n\n\u00a0\nConstraints:\n\nm == matrix.length\nn == matrix[i].length\n1 <= m, n <= 300\nmatrix[i][j] is '0' or '1'.\n\n",
    "url": "https://leetcode.com/problems/maximal-square",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def maximalSquare(self, A):\n        maxSol = 0\n        for i in range(len(A)):\n            for j in range(len(A[i])):\n                A[i][j] = int(A[i][j])\n                if A[i][j] and i and j:\n                    A[i][j] = min(A[i - 1][j], A[i - 1]\n                                  [j - 1], A[i][j - 1]) + 1\n                if maxSol < A[i][j]:\n                    maxSol = A[i][j]\n        return maxSol * maxSol\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/maximal-square/",
      "datePublished": "2024-01-28",
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