# 69-sqrtx


Try it on <a href='https://leetcode.com/problems/69-sqrtx'>leetcode</a>

## Description
<div class="description">
<div><p>Given a non-negative integer <code>x</code>,&nbsp;compute and return <em>the square root of</em> <code>x</code>.</p>

<p>Since the return type&nbsp;is an integer, the decimal digits are <strong>truncated</strong>, and only <strong>the integer part</strong> of the result&nbsp;is returned.</p>

<p><strong>Note:&nbsp;</strong>You are not allowed to use any built-in exponent function or operator, such as <code>pow(x, 0.5)</code> or&nbsp;<code>x ** 0.5</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> x = 4
<strong>Output:</strong> 2
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> x = 8
<strong>Output:</strong> 2
<strong>Explanation:</strong> The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        lo = 1
        hi = x
        while lo < hi:
            mi = (lo + hi) >> 1

            if mi * mi == x:
                return mi

            if mi * mi > x:
                hi = mi
            else:
                lo = mi + 1
        return lo - 1

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "69. Sqrt(x)",
    "text": "Given a non-negative integer x,\u00a0compute and return the square root of x.\nSince the return type\u00a0is an integer, the decimal digits are truncated, and only the integer part of the result\u00a0is returned.\nNote:\u00a0You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or\u00a0x ** 0.5.\n\u00a0\nExample 1:\nInput: x = 4\nOutput: 2\n\nExample 2:\nInput: x = 8\nOutput: 2\nExplanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.\n\u00a0\nConstraints:\n\n0 <= x <= 231 - 1\n\n",
    "url": "https://leetcode.com/problems/69-sqrtx",
    "answerCount": 1,
    "datePublished": "2022-07-05T19:32:36+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def mySqrt(self, x: int) -> int:\n        if x == 0 or x == 1:\n            return x\n        lo = 1\n        hi = x\n        while lo < hi:\n            mi = (lo + hi) >> 1\n\n            if mi * mi == x:\n                return mi\n\n            if mi * mi > x:\n                hi = mi\n            else:\n                lo = mi + 1\n        return lo - 1\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/69-sqrtx/",
      "datePublished": "2022-07-05T19:32:36+05:30",
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