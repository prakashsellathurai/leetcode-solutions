# perfect-squares


Try it on <a href='https://leetcode.com/problems/perfect-squares'>leetcode</a>

## Description
<div class="description">
<div><p>Given an integer <code>n</code>, return <em>the least number of perfect square numbers that sum to</em> <code>n</code>.</p>

<p>A <strong>perfect square</strong> is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, <code>1</code>, <code>4</code>, <code>9</code>, and <code>16</code> are perfect squares while <code>3</code> and <code>11</code> are not.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> n = 12
<strong>Output:</strong> 3
<strong>Explanation:</strong> 12 = 4 + 4 + 4.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> n = 13
<strong>Output:</strong> 2
<strong>Explanation:</strong> 13 = 4 + 9.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def numSquares(self, n: int) -> int:
        squareNumber = [i**2 for i in range(0, int(n ** (1 / 2)) + 1)]

        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for num in squareNumber:
            for amt in range(1, n + 1):
                if amt >= num:
                    dp[amt] = min(dp[amt], dp[amt - num] + 1)

        return dp[-1]

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "279. Perfect Squares",
    "text": "Given an integer n, return the least number of perfect square numbers that sum to n.\nA perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.\n\u00a0\nExample 1:\nInput: n = 12\nOutput: 3\nExplanation: 12 = 4 + 4 + 4.\n\nExample 2:\nInput: n = 13\nOutput: 2\nExplanation: 13 = 4 + 9.\n\n\u00a0\nConstraints:\n\n1 <= n <= 104\n\n",
    "url": "https://leetcode.com/problems/perfect-squares",
    "answerCount": 1,
    "datePublished": "2023-07-13T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def numSquares(self, n: int) -> int:\n        squareNumber = [i**2 for i in range(0, int(n ** (1 / 2)) + 1)]\n\n        dp = [float(\"inf\")] * (n + 1)\n        dp[0] = 0\n        for num in squareNumber:\n            for amt in range(1, n + 1):\n                if amt >= num:\n                    dp[amt] = min(dp[amt], dp[amt - num] + 1)\n\n        return dp[-1]\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/perfect-squares/",
      "datePublished": "2023-07-13T00:00:00Z",
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