# 0633-sum-of-square-numbers


Try it on <a href='https://leetcode.com/problems/0633-sum-of-square-numbers'>leetcode</a>

## Description
<div class="description">
<p>Given a non-negative integer <code>c</code>, decide whether there&#39;re two integers <code>a</code> and <code>b</code> such that <code>a<sup>2</sup> + b<sup>2</sup> = c</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> c = 5
<strong>Output:</strong> true
<strong>Explanation:</strong> 1 * 1 + 2 * 2 = 5
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> c = 3
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= c &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

</div>

## Solution(Python)
```Python
class Solution(object):
    def judgeSquareSum(self, c):
        def binary_search(s, e, n):
            if s > e:
                return False
            mid = s + (e - s) // 2
            if mid * mid == n:
                return True
            elif mid * mid > n:
                return binary_search(s, mid - 1, n)
            else:
                return binary_search(mid + 1, e, n)

        for a in range(
            int(c**0.5) + 1
        ):  # equivalent to `for (long a = 0; a * a <= c; a++)` in Java
            b = c - a * a
            if binary_search(0, b, b):
                return True
        return False
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "633. Sum of Square Numbers",
    "text": "Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.\n\u00a0\nExample 1:\n\nInput: c = 5\nOutput: true\nExplanation: 1 * 1 + 2 * 2 = 5\n\nExample 2:\n\nInput: c = 3\nOutput: false\n\n\u00a0\nConstraints:\n\n0 <= c <= 231 - 1\n\n",
    "url": "https://leetcode.com/problems/0633-sum-of-square-numbers",
    "answerCount": 1,
    "datePublished": "2026-03-16T11:00:52+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution(object):\n    def judgeSquareSum(self, c):\n        def binary_search(s, e, n):\n            if s > e:\n                return False\n            mid = s + (e - s) // 2\n            if mid * mid == n:\n                return True\n            elif mid * mid > n:\n                return binary_search(s, mid - 1, n)\n            else:\n                return binary_search(mid + 1, e, n)\n\n        for a in range(\n            int(c**0.5) + 1\n        ):  # equivalent to `for (long a = 0; a * a <= c; a++)` in Java\n            b = c - a * a\n            if binary_search(0, b, b):\n                return True\n        return False",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/0633-sum-of-square-numbers/",
      "datePublished": "2026-03-16T11:00:52+05:30",
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