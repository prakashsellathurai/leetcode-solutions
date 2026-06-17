# 0459-repeated-substring-pattern


Try it on <a href='https://leetcode.com/problems/0459-repeated-substring-pattern'>leetcode</a>

## Description
<div class="description">
<p>Given a string <code>s</code>, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abab&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> It is the substring &quot;ab&quot; twice.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aba&quot;
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcabcabcabc&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> It is the substring &quot;abc&quot; four times or the substring &quot;abcabc&quot; twice.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>

</div>

## Solution(Python)
```Python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def computelps(s):
            n = len(s)
            lps = [0] *n
            i = 1
            len_ = 0
            while i<n:
                if s[i] == s[len_]:
                    len_+=1
                    lps[i] = len_
                    i+=1
                else:
                    if len_ != 0:
                        len_ = lps[len_ - 1]
                    else:
                        lps[i] = 0
                        i+=1
            return lps
        lps = computelps(s)
        n = len(s)
        len_ = lps[n-1]
        if len_>0 and n % (n-len_) == 0 :
            return True
        else:
            return False
        
        
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "459. Repeated Substring Pattern",
    "text": "Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.\n\u00a0\nExample 1:\n\nInput: s = \"abab\"\nOutput: true\nExplanation: It is the substring \"ab\" twice.\n\nExample 2:\n\nInput: s = \"aba\"\nOutput: false\n\nExample 3:\n\nInput: s = \"abcabcabcabc\"\nOutput: true\nExplanation: It is the substring \"abc\" four times or the substring \"abcabc\" twice.\n\n\u00a0\nConstraints:\n\n1 <= s.length <= 104\ns consists of lowercase English letters.\n\n",
    "url": "https://leetcode.com/problems/0459-repeated-substring-pattern",
    "answerCount": 1,
    "datePublished": "2026-01-26T22:52:11+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def repeatedSubstringPattern(self, s: str) -> bool:\n        def computelps(s):\n            n = len(s)\n            lps = [0] *n\n            i = 1\n            len_ = 0\n            while i<n:\n                if s[i] == s[len_]:\n                    len_+=1\n                    lps[i] = len_\n                    i+=1\n                else:\n                    if len_ != 0:\n                        len_ = lps[len_ - 1]\n                    else:\n                        lps[i] = 0\n                        i+=1\n            return lps\n        lps = computelps(s)\n        n = len(s)\n        len_ = lps[n-1]\n        if len_>0 and n % (n-len_) == 0 :\n            return True\n        else:\n            return False\n        \n        ",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/0459-repeated-substring-pattern/",
      "datePublished": "2026-01-26T22:52:11+05:30",
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