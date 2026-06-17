# 680-valid-palindrome-ii


Try it on <a href='https://leetcode.com/problems/680-valid-palindrome-ii'>leetcode</a>

## Description
<div class="description">
<div><p>Given a string <code>s</code>, return <code>true</code> <em>if the </em><code>s</code><em> can be palindrome after deleting <strong>at most one</strong> character from it</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "aba"
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "abca"
<strong>Output:</strong> true
<strong>Explanation:</strong> You could delete the character 'c'.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "abc"
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return self.checkPalindrome(s, i + 1, j) or self.checkPalindrome(
                    s, i, j - 1
                )
            i += 1
            j -= 1
        return True

    def checkPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1
        return True

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "680. Valid Palindrome II",
    "text": "Given a string s, return true if the s can be palindrome after deleting at most one character from it.\n\u00a0\nExample 1:\nInput: s = \"aba\"\nOutput: true\n\nExample 2:\nInput: s = \"abca\"\nOutput: true\nExplanation: You could delete the character 'c'.\n\nExample 3:\nInput: s = \"abc\"\nOutput: false\n\n\u00a0\nConstraints:\n\n1 <= s.length <= 105\ns consists of lowercase English letters.\n\n",
    "url": "https://leetcode.com/problems/680-valid-palindrome-ii",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def validPalindrome(self, s: str) -> bool:\n        i = 0\n        j = len(s) - 1\n\n        while i < j:\n            if s[i] != s[j]:\n                return self.checkPalindrome(s, i + 1, j) or self.checkPalindrome(\n                    s, i, j - 1\n                )\n            i += 1\n            j -= 1\n        return True\n\n    def checkPalindrome(self, s, i, j):\n        while i < j:\n            if s[i] != s[j]:\n                return False\n\n            i += 1\n            j -= 1\n        return True\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/680-valid-palindrome-ii/",
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