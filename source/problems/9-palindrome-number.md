# 9-palindrome-number


Try it on <a href='https://leetcode.com/problems/9-palindrome-number'>leetcode</a>

## Description
<div class="description">
<div><p>Given an integer <code>x</code>, return <code>true</code> if <code>x</code> is palindrome integer.</p>

<p>An integer is a <strong>palindrome</strong> when it reads the same backward as forward.</p>

<ul>
	<li>For example, <code>121</code> is a palindrome while <code>123</code> is not.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> x = 121
<strong>Output:</strong> true
<strong>Explanation:</strong> 121 reads as 121 from left to right and from right to left.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> x = -121
<strong>Output:</strong> false
<strong>Explanation:</strong> From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> x = 10
<strong>Output:</strong> false
<strong>Explanation:</strong> Reads 01 from right to left. Therefore it is not a palindrome.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup>&nbsp;&lt;= x &lt;= 2<sup>31</sup>&nbsp;- 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it without converting the integer to a string?</div>
</div>

## Solution(Python)
```Python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (
            x > 0 and x % 10 == 0
        ):  # if x is negative, return False. if x is positive and last digit is 0, that also cannot form a palindrome, return False.
            return False

        result = 0
        while x > result:
            result = result * 10 + x % 10
            x = x // 10

        return True if (x == result or x == result // 10) else False

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "9. Palindrome Number",
    "text": "Given an integer x, return true if x is palindrome integer.\nAn integer is a palindrome when it reads the same backward as forward.\n\nFor example, 121 is a palindrome while 123 is not.\n\n\u00a0\nExample 1:\nInput: x = 121\nOutput: true\nExplanation: 121 reads as 121 from left to right and from right to left.\n\nExample 2:\nInput: x = -121\nOutput: false\nExplanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.\n\nExample 3:\nInput: x = 10\nOutput: false\nExplanation: Reads 01 from right to left. Therefore it is not a palindrome.\n\n\u00a0\nConstraints:\n\n-231\u00a0<= x <= 231\u00a0- 1\n\n\u00a0\nFollow up: Could you solve it without converting the integer to a string?",
    "url": "https://leetcode.com/problems/9-palindrome-number",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def isPalindrome(self, x: int) -> bool:\n        if x < 0 or (\n            x > 0 and x % 10 == 0\n        ):  # if x is negative, return False. if x is positive and last digit is 0, that also cannot form a palindrome, return False.\n            return False\n\n        result = 0\n        while x > result:\n            result = result * 10 + x % 10\n            x = x // 10\n\n        return True if (x == result or x == result // 10) else False\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/9-palindrome-number/",
      "datePublished": "2025-08-15",
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