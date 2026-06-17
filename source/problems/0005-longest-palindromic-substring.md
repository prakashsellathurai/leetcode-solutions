# 0005-longest-palindromic-substring


Try it on <a href='https://leetcode.com/problems/0005-longest-palindromic-substring'>leetcode</a>

## Description
<div class="description">
<p>Given a string <code>s</code>, return <em>the longest</em> <span data-keyword="palindromic-string"><em>palindromic</em></span> <span data-keyword="substring-nonempty"><em>substring</em></span> in <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;babad&quot;
<strong>Output:</strong> &quot;bab&quot;
<strong>Explanation:</strong> &quot;aba&quot; is also a valid answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cbbd&quot;
<strong>Output:</strong> &quot;bb&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consist of only digits and English letters.</li>
</ul>

</div>

## Solution(Python)
```Python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        left, right = 0, 1

        for end in range(0, n):
            for start in range(end - 1, -1, -1):
                if s[start] == s[end]:
                    if end - start == 1 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        palindrome_len = end - start + 1
                        if right - left < palindrome_len:
                            left = start
                            right = left + palindrome_len
        return s[left: right]
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "5. Longest Palindromic Substring",
    "text": "Given a string s, return the longest palindromic substring in s.\n\u00a0\nExample 1:\n\nInput: s = \"babad\"\nOutput: \"bab\"\nExplanation: \"aba\" is also a valid answer.\n\nExample 2:\n\nInput: s = \"cbbd\"\nOutput: \"bb\"\n\n\u00a0\nConstraints:\n\n1 <= s.length <= 1000\ns consist of only digits and English letters.\n\n",
    "url": "https://leetcode.com/problems/0005-longest-palindromic-substring",
    "answerCount": 1,
    "datePublished": "2025-06-21T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def longestPalindrome(self, s: str) -> str:\n        n = len(s)\n        dp = [[False] * n for _ in range(n)]\n        for i in range(n):\n            dp[i][i] = True\n        left, right = 0, 1\n\n        for end in range(0, n):\n            for start in range(end - 1, -1, -1):\n                if s[start] == s[end]:\n                    if end - start == 1 or dp[start + 1][end - 1]:\n                        dp[start][end] = True\n                        palindrome_len = end - start + 1\n                        if right - left < palindrome_len:\n                            left = start\n                            right = left + palindrome_len\n        return s[left: right]",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/0005-longest-palindromic-substring/",
      "datePublished": "2025-06-21T00:00:00Z",
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