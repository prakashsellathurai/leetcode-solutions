# 240-search-a-2d-matrix-ii


Try it on <a href='https://leetcode.com/problems/240-search-a-2d-matrix-ii'>leetcode</a>

## Description
<div class="description">
<div><p>Write an efficient algorithm that searches for a <code>target</code> value in an <code>m x n</code> integer <code>matrix</code>. The <code>matrix</code> has the following properties:</p>

<ul>
	<li>Integers in each row are sorted in ascending from left to right.</li>
	<li>Integers in each column are sorted in ascending from top to bottom.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/24/searchgrid2.jpg" style="width: 300px; height: 300px;">
<pre><strong>Input:</strong> matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/24/searchgrid.jpg" style="width: 300px; height: 300px;">
<pre><strong>Input:</strong> matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= n, m &lt;= 300</code></li>
	<li><code>-10<sup>9</sup> &lt;= matrix[i][j] &lt;= 10<sup>9</sup></code></li>
	<li>All the integers in each row are <strong>sorted</strong> in ascending order.</li>
	<li>All the integers in each column are <strong>sorted</strong> in ascending order.</li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.linearSearch(matrix, target)

    # Time Complexity: O(MN)
    # Space Complexity: O(1)
    def bruteforce(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True
        return False

    # Time Complexity: O(M+N)
    # Space Complexity: O(1)
    def linearSearch(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1

        while i <= m - 1 and j >= 0:
            curr = matrix[i][j]

            if target == curr:
                return True

            if target > curr:
                i += 1
            else:
                j -= 1

        return False

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "240. Search a 2D Matrix II",
    "text": "Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:\n\nIntegers in each row are sorted in ascending from left to right.\nIntegers in each column are sorted in ascending from top to bottom.\n\n\u00a0\nExample 1:\n\nInput: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5\nOutput: true\n\nExample 2:\n\nInput: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20\nOutput: false\n\n\u00a0\nConstraints:\n\nm == matrix.length\nn == matrix[i].length\n1 <= n, m <= 300\n-109 <= matrix[i][j] <= 109\nAll the integers in each row are sorted in ascending order.\nAll the integers in each column are sorted in ascending order.\n-109 <= target <= 109\n\n",
    "url": "https://leetcode.com/problems/240-search-a-2d-matrix-ii",
    "answerCount": 1,
    "datePublished": "2023-11-06T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:\n        return self.linearSearch(matrix, target)\n\n    # Time Complexity: O(MN)\n    # Space Complexity: O(1)\n    def bruteforce(self, matrix: List[List[int]], target: int) -> bool:\n        m, n = len(matrix), len(matrix[0])\n\n        for i in range(m):\n            for j in range(n):\n                if matrix[i][j] == target:\n                    return True\n        return False\n\n    # Time Complexity: O(M+N)\n    # Space Complexity: O(1)\n    def linearSearch(self, matrix: List[List[int]], target: int) -> bool:\n        m, n = len(matrix), len(matrix[0])\n        i, j = 0, n - 1\n\n        while i <= m - 1 and j >= 0:\n            curr = matrix[i][j]\n\n            if target == curr:\n                return True\n\n            if target > curr:\n                i += 1\n            else:\n                j -= 1\n\n        return False\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/240-search-a-2d-matrix-ii/",
      "datePublished": "2023-11-06T00:00:00Z",
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