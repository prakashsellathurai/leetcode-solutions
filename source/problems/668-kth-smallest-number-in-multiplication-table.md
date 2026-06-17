# 668-kth-smallest-number-in-multiplication-table


Try it on <a href='https://leetcode.com/problems/668-kth-smallest-number-in-multiplication-table'>leetcode</a>

## Description
<div class="description">
<div><p>Nearly everyone has used the <a href="https://en.wikipedia.org/wiki/Multiplication_table" target="_blank">Multiplication Table</a>. The multiplication table of size <code>m x n</code> is an integer matrix <code>mat</code> where <code>mat[i][j] == i * j</code> (<strong>1-indexed</strong>).</p>

<p>Given three integers <code>m</code>, <code>n</code>, and <code>k</code>, return <em>the </em><code>k<sup>th</sup></code><em> smallest element in the </em><code>m x n</code><em> multiplication table</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/02/multtable1-grid.jpg" style="width: 500px; height: 254px;">
<pre><strong>Input:</strong> m = 3, n = 3, k = 5
<strong>Output:</strong> 3
<strong>Explanation:</strong> The 5<sup>th</sup> smallest number is 3.
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/02/multtable2-grid.jpg" style="width: 493px; height: 293px;">
<pre><strong>Input:</strong> m = 2, n = 3, k = 6
<strong>Output:</strong> 6
<strong>Explanation:</strong> The 6<sup>th</sup> smallest number is 6.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= k &lt;= m * n</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution(object):
    def findKthNumber(self, m, n, k):
        def enough(x):
            count = 0
            for i in range(1, m+1):
                count += min(x // i, n)
            return count >= k

        lo, hi = 1, m * n
        while lo < hi:
            mi = (lo + hi) // 2
            if not enough(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "668. Kth Smallest Number in Multiplication Table",
    "text": "Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).\nGiven three integers m, n, and k, return the kth smallest element in the m x n multiplication table.\n\u00a0\nExample 1:\n\nInput: m = 3, n = 3, k = 5\nOutput: 3\nExplanation: The 5th smallest number is 3.\n\nExample 2:\n\nInput: m = 2, n = 3, k = 6\nOutput: 6\nExplanation: The 6th smallest number is 6.\n\n\u00a0\nConstraints:\n\n1 <= m, n <= 3 * 104\n1 <= k <= m * n\n\n",
    "url": "https://leetcode.com/problems/668-kth-smallest-number-in-multiplication-table",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution(object):\n    def findKthNumber(self, m, n, k):\n        def enough(x):\n            count = 0\n            for i in range(1, m+1):\n                count += min(x // i, n)\n            return count >= k\n\n        lo, hi = 1, m * n\n        while lo < hi:\n            mi = (lo + hi) // 2\n            if not enough(mi):\n                lo = mi + 1\n            else:\n                hi = mi\n        return lo",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/668-kth-smallest-number-in-multiplication-table/",
      "datePublished": "2025-05-17",
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