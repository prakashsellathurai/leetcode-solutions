# power-of-two


Try it on <a href='https://leetcode.com/problems/power-of-two'>leetcode</a>

## Description
<div class="description">
<div><p>Given an integer <code>n</code>, return <em><code>true</code> if it is a power of two. Otherwise, return <code>false</code></em>.</p>

<p>An integer <code>n</code> is a power of two, if there exists an integer <code>x</code> such that <code>n == 2<sup>x</sup></code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> true
<strong>Explanation: </strong>2<sup>0</sup> = 1
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> n = 16
<strong>Output:</strong> true
<strong>Explanation: </strong>2<sup>4</sup> = 16
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it without loops/recursion?</div>
</div>

## Solution(Python)
```Python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & n - 1)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "231. Power of Two",
    "text": "Given an integer n, return true if it is a power of two. Otherwise, return false.\nAn integer n is a power of two, if there exists an integer x such that n == 2x.\n\u00a0\nExample 1:\nInput: n = 1\nOutput: true\nExplanation: 20 = 1\n\nExample 2:\nInput: n = 16\nOutput: true\nExplanation: 24 = 16\n\nExample 3:\nInput: n = 3\nOutput: false\n\n\u00a0\nConstraints:\n\n-231 <= n <= 231 - 1\n\n\u00a0\nFollow up: Could you solve it without loops/recursion?",
    "url": "https://leetcode.com/problems/power-of-two",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def isPowerOfTwo(self, n: int) -> bool:\n        return n > 0 and not (n & n - 1)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/power-of-two/",
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