# 867-transpose-matrix


Try it on <a href='https://leetcode.com/problems/867-transpose-matrix'>leetcode</a>

## Description
<div class="description">
<div><p>Given a 2D integer array <code>matrix</code>, return <em>the <strong>transpose</strong> of</em> <code>matrix</code>.</p>

<p>The <strong>transpose</strong> of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/02/10/hint_transpose.png" style="width: 600px; height: 197px;"></p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> matrix = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [[1,4,7],[2,5,8],[3,6,9]]
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> matrix = [[1,2,3],[4,5,6]]
<strong>Output:</strong> [[1,4],[2,5],[3,6]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 1000</code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= matrix[i][j] &lt;= 10<sup>9</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return self.zipit(matrix)

    def naive(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        res = [[0 for i in range(m)] for i in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][i] = matrix[i][j]
        return res

    def oneline(self, matrix: List[List[int]]) -> List[List[int]]:
        return [
            [matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))
        ]

    def zipit(self, matrix: List[List[int]]) -> List[List[int]]:
        return zip(*matrix)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "867. Transpose Matrix",
    "text": "Given a 2D integer array matrix, return the transpose of matrix.\nThe transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.\n\n\u00a0\nExample 1:\nInput: matrix = [[1,2,3],[4,5,6],[7,8,9]]\nOutput: [[1,4,7],[2,5,8],[3,6,9]]\n\nExample 2:\nInput: matrix = [[1,2,3],[4,5,6]]\nOutput: [[1,4],[2,5],[3,6]]\n\n\u00a0\nConstraints:\n\nm == matrix.length\nn == matrix[i].length\n1 <= m, n <= 1000\n1 <= m * n <= 105\n-109 <= matrix[i][j] <= 109\n\n",
    "url": "https://leetcode.com/problems/867-transpose-matrix",
    "answerCount": 1,
    "datePublished": "2025-08-02T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:\n        return self.zipit(matrix)\n\n    def naive(self, matrix: List[List[int]]) -> List[List[int]]:\n        m, n = len(matrix), len(matrix[0])\n        res = [[0 for i in range(m)] for i in range(n)]\n        for i in range(m):\n            for j in range(n):\n                res[j][i] = matrix[i][j]\n        return res\n\n    def oneline(self, matrix: List[List[int]]) -> List[List[int]]:\n        return [\n            [matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))\n        ]\n\n    def zipit(self, matrix: List[List[int]]) -> List[List[int]]:\n        return zip(*matrix)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/867-transpose-matrix/",
      "datePublished": "2025-08-02T00:00:00Z",
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