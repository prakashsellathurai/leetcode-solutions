# 290-word-pattern


Try it on <a href='https://leetcode.com/problems/290-word-pattern'>leetcode</a>

## Description
<div class="description">
<div><p>Given a <code>pattern</code> and a string <code>s</code>, find if <code>s</code>&nbsp;follows the same pattern.</p>

<p>Here <b>follow</b> means a full match, such that there is a bijection between a letter in <code>pattern</code> and a <b>non-empty</b> word in <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> pattern = "abba", s = "dog cat cat dog"
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> pattern = "abba", s = "dog cat cat fish"
<strong>Output:</strong> false
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> pattern = "aaaa", s = "dog cat cat dog"
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= pattern.length &lt;= 300</code></li>
	<li><code>pattern</code> contains only lower-case English letters.</li>
	<li><code>1 &lt;= s.length &lt;= 3000</code></li>
	<li><code>s</code> contains only lowercase English letters and spaces <code>' '</code>.</li>
	<li><code>s</code> <strong>does not contain</strong> any leading or trailing spaces.</li>
	<li>All the words in <code>s</code> are separated by a <strong>single space</strong>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        wordhashmap = {}
        charhashmap = {}
        if len(s) != len(pattern):
            return False
        for ch, word in zip(pattern, s):
            if word not in wordhashmap:
                wordhashmap[word] = ch
            elif wordhashmap[word] != ch:
                return False

            if ch not in charhashmap:
                charhashmap[ch] = word
            elif charhashmap[ch] != word:
                return False
        return True

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "290. Word Pattern",
    "text": "Given a pattern and a string s, find if s\u00a0follows the same pattern.\nHere follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.\n\u00a0\nExample 1:\nInput: pattern = \"abba\", s = \"dog cat cat dog\"\nOutput: true\n\nExample 2:\nInput: pattern = \"abba\", s = \"dog cat cat fish\"\nOutput: false\n\nExample 3:\nInput: pattern = \"aaaa\", s = \"dog cat cat dog\"\nOutput: false\n\n\u00a0\nConstraints:\n\n1 <= pattern.length <= 300\npattern contains only lower-case English letters.\n1 <= s.length <= 3000\ns contains only lowercase English letters and spaces ' '.\ns does not contain any leading or trailing spaces.\nAll the words in s are separated by a single space.\n\n",
    "url": "https://leetcode.com/problems/290-word-pattern",
    "answerCount": 1,
    "datePublished": "2025-07-12T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def wordPattern(self, pattern: str, s: str) -> bool:\n        s = s.split(\" \")\n        wordhashmap = {}\n        charhashmap = {}\n        if len(s) != len(pattern):\n            return False\n        for ch, word in zip(pattern, s):\n            if word not in wordhashmap:\n                wordhashmap[word] = ch\n            elif wordhashmap[word] != ch:\n                return False\n\n            if ch not in charhashmap:\n                charhashmap[ch] = word\n            elif charhashmap[ch] != word:\n                return False\n        return True\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/290-word-pattern/",
      "datePublished": "2025-07-12T00:00:00Z",
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