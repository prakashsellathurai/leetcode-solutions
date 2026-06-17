# 29-divide-two-integers


Try it on <a href='https://leetcode.com/problems/29-divide-two-integers'>leetcode</a>

## Description
<div class="description">
<div><p>Given two integers <code>dividend</code> and <code>divisor</code>, divide two integers <strong>without</strong> using multiplication, division, and mod operator.</p>

<p>The integer division should truncate toward zero, which means losing its fractional part. For example, <code>8.345</code> would be truncated to <code>8</code>, and <code>-2.7335</code> would be truncated to <code>-2</code>.</p>

<p>Return <em>the <strong>quotient</strong> after dividing </em><code>dividend</code><em> by </em><code>divisor</code>.</p>

<p><strong>Note: </strong>Assume we are dealing with an environment that could only store integers within the <strong>32-bit</strong> signed integer range: <code>[−2<sup>31</sup>, 2<sup>31</sup> − 1]</code>. For this problem, if the quotient is <strong>strictly greater than</strong> <code>2<sup>31</sup> - 1</code>, then return <code>2<sup>31</sup> - 1</code>, and if the quotient is <strong>strictly less than</strong> <code>-2<sup>31</sup></code>, then return <code>-2<sup>31</sup></code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> dividend = 10, divisor = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> 10/3 = 3.33333.. which is truncated to 3.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> dividend = 7, divisor = -3
<strong>Output:</strong> -2
<strong>Explanation:</strong> 7/-3 = -2.33333.. which is truncated to -2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= dividend, divisor &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>divisor != 0</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return self.bitmanipulation(dividend, divisor)

    # Time Complexity: O(N/M)
    def naive(self, dividend: int, divisor: int) -> int:
        quo = 0

        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        dividend, divisor = abs(dividend), abs(divisor)

        while dividend >= divisor:
            dividend -= divisor
            quo += 1

        if quo < -(2**31):
            return -(2**31)
        if quo > (2**31) - 1:
            return (2**31) - 1
        return sign * quo

    # Time Complexity: O(log(N))
    def bitmanipulation(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        temp = 0

        for i in range(31, -1, -1):
            if dividend >= temp + (divisor << i):
                temp += divisor << i
                quotient |= 1 << i
        if sign == -1:
            quotient = sign * quotient
        return min(max(quotient, -(2**31)), 2**31 - 1)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "29. Divide Two Integers",
    "text": "Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.\nThe integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.\nReturn the quotient after dividing dividend by divisor.\nNote: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [\u2212231, 231 \u2212 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.\n\u00a0\nExample 1:\nInput: dividend = 10, divisor = 3\nOutput: 3\nExplanation: 10/3 = 3.33333.. which is truncated to 3.\n\nExample 2:\nInput: dividend = 7, divisor = -3\nOutput: -2\nExplanation: 7/-3 = -2.33333.. which is truncated to -2.\n\n\u00a0\nConstraints:\n\n-231 <= dividend, divisor <= 231 - 1\ndivisor != 0\n\n",
    "url": "https://leetcode.com/problems/29-divide-two-integers",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def divide(self, dividend: int, divisor: int) -> int:\n        return self.bitmanipulation(dividend, divisor)\n\n    # Time Complexity: O(N/M)\n    def naive(self, dividend: int, divisor: int) -> int:\n        quo = 0\n\n        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1\n\n        dividend, divisor = abs(dividend), abs(divisor)\n\n        while dividend >= divisor:\n            dividend -= divisor\n            quo += 1\n\n        if quo < -(2**31):\n            return -(2**31)\n        if quo > (2**31) - 1:\n            return (2**31) - 1\n        return sign * quo\n\n    # Time Complexity: O(log(N))\n    def bitmanipulation(self, dividend: int, divisor: int) -> int:\n        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1\n        dividend, divisor = abs(dividend), abs(divisor)\n\n        quotient = 0\n        temp = 0\n\n        for i in range(31, -1, -1):\n            if dividend >= temp + (divisor << i):\n                temp += divisor << i\n                quotient |= 1 << i\n        if sign == -1:\n            quotient = sign * quotient\n        return min(max(quotient, -(2**31)), 2**31 - 1)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/29-divide-two-integers/",
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