# 5-longest-palindromic-substring


Try it on <a href='https://leetcode.com/problems/5-longest-palindromic-substring'>leetcode</a>

## Description
<div class="description">
<div><p>Given a string <code>s</code>, return <em>the longest palindromic substring</em> in <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "babad"
<strong>Output:</strong> "bab"
<strong>Explanation:</strong> "aba" is also a valid answer.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "cbbd"
<strong>Output:</strong> "bb"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consist of only digits and English letters.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n < 2:
            return s

        maxlen = 1
        start = 0

        for i in range(n):
            low = i - 1
            high = i + 1
            while high < n and s[high] == s[i]:
                high += 1
            while low >= 0 and s[low] == s[i]:
                low -= 1

            while low >= 0 and high < n and s[low] == s[high]:
                low -= 1
                high += 1

            cur_len = high - low - 1

            if cur_len > maxlen:
                maxlen = cur_len
                start = low + 1

        return s[start: start + maxlen]

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "5. Longest Palindromic Substring",
    "text": "Given a string s, return the longest palindromic substring in s.\n\u00a0\nExample 1:\nInput: s = \"babad\"\nOutput: \"bab\"\nExplanation: \"aba\" is also a valid answer.\n\nExample 2:\nInput: s = \"cbbd\"\nOutput: \"bb\"\n\n\u00a0\nConstraints:\n\n1 <= s.length <= 1000\ns consist of only digits and English letters.\n\n",
    "url": "https://leetcode.com/problems/5-longest-palindromic-substring",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def longestPalindrome(self, s: str) -> str:\n        n = len(s)\n\n        if n < 2:\n            return s\n\n        maxlen = 1\n        start = 0\n\n        for i in range(n):\n            low = i - 1\n            high = i + 1\n            while high < n and s[high] == s[i]:\n                high += 1\n            while low >= 0 and s[low] == s[i]:\n                low -= 1\n\n            while low >= 0 and high < n and s[low] == s[high]:\n                low -= 1\n                high += 1\n\n            cur_len = high - low - 1\n\n            if cur_len > maxlen:\n                maxlen = cur_len\n                start = low + 1\n\n        return s[start: start + maxlen]\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/5-longest-palindromic-substring/",
      "datePublished": "2024-06-22",
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