# 118-pascals-triangle


Try it on <a href='https://leetcode.com/problems/118-pascals-triangle'>leetcode</a>

## Description
<div class="description">
<div><p>Given an integer <code>numRows</code>, return the first numRows of <strong>Pascal's triangle</strong>.</p>

<p>In <strong>Pascal's triangle</strong>, each number is the sum of the two numbers directly above it as shown:</p>
<img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" style="height:240px; width:260px">
<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> numRows = 5
<strong>Output:</strong> [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> numRows = 1
<strong>Output:</strong> [[1]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= numRows &lt;= 30</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1 for j in range(i + 1)] for i in range(numRows)]

        for i in range(2, numRows):
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        return dp

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "118. Pascal's Triangle",
    "text": "Given an integer numRows, return the first numRows of Pascal's triangle.\nIn Pascal's triangle, each number is the sum of the two numbers directly above it as shown:\n\n\u00a0\nExample 1:\nInput: numRows = 5\nOutput: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]\nExample 2:\nInput: numRows = 1\nOutput: [[1]]\n\n\u00a0\nConstraints:\n\n1 <= numRows <= 30\n\n",
    "url": "https://leetcode.com/problems/118-pascals-triangle",
    "answerCount": 1,
    "datePublished": "2022-07-19T19:41:13+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def generate(self, numRows: int) -> List[List[int]]:\n        dp = [[1 for j in range(i + 1)] for i in range(numRows)]\n\n        for i in range(2, numRows):\n            for j in range(1, i):\n                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]\n        return dp\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/118-pascals-triangle/",
      "datePublished": "2022-07-19T19:41:13+05:30",
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