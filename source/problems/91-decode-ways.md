# 91-decode-ways


Try it on <a href='https://leetcode.com/problems/91-decode-ways'>leetcode</a>

## Description
<div class="description">
<div><p>A message containing letters from <code>A-Z</code> can be <strong>encoded</strong> into numbers using the following mapping:</p>

<pre>'A' -&gt; "1"
'B' -&gt; "2"
...
'Z' -&gt; "26"
</pre>

<p>To <strong>decode</strong> an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, <code>"11106"</code> can be mapped into:</p>

<ul>
	<li><code>"AAJF"</code> with the grouping <code>(1 1 10 6)</code></li>
	<li><code>"KJF"</code> with the grouping <code>(11 10 6)</code></li>
</ul>

<p>Note that the grouping <code>(1 11 06)</code> is invalid because <code>"06"</code> cannot be mapped into <code>'F'</code> since <code>"6"</code> is different from <code>"06"</code>.</p>

<p>Given a string <code>s</code> containing only digits, return <em>the <strong>number</strong> of ways to <strong>decode</strong> it</em>.</p>

<p>The test cases are generated so that the answer fits in a <strong>32-bit</strong> integer.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "12"
<strong>Output:</strong> 2
<strong>Explanation:</strong> "12" could be decoded as "AB" (1 2) or "L" (12).
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "226"
<strong>Output:</strong> 3
<strong>Explanation:</strong> "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "06"
<strong>Output:</strong> 0
<strong>Explanation:</strong> "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> contains only digits and may contain leading zero(s).</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        @cache
        def dfs(i):
            if i >= n:
                return 1
            
            res = 0
            if 1 <= int(s[i]) <= 9 :
                res += dfs(i+1)
            if 10 <= int(s[i:i+2]) <= 26:
                res += dfs(i+2)
            return res
        
        return dfs(0) if s and s[0] != '0' else 0
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "91. Decode Ways",
    "text": "A message containing letters from A-Z can be encoded into numbers using the following mapping:\n'A' -> \"1\"\n'B' -> \"2\"\n...\n'Z' -> \"26\"\n\nTo decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, \"11106\" can be mapped into:\n\n\"AAJF\" with the grouping (1 1 10 6)\n\"KJF\" with the grouping (11 10 6)\n\nNote that the grouping (1 11 06) is invalid because \"06\" cannot be mapped into 'F' since \"6\" is different from \"06\".\nGiven a string s containing only digits, return the number of ways to decode it.\nThe test cases are generated so that the answer fits in a 32-bit integer.\n\u00a0\nExample 1:\nInput: s = \"12\"\nOutput: 2\nExplanation: \"12\" could be decoded as \"AB\" (1 2) or \"L\" (12).\n\nExample 2:\nInput: s = \"226\"\nOutput: 3\nExplanation: \"226\" could be decoded as \"BZ\" (2 26), \"VF\" (22 6), or \"BBF\" (2 2 6).\n\nExample 3:\nInput: s = \"06\"\nOutput: 0\nExplanation: \"06\" cannot be mapped to \"F\" because of the leading zero (\"6\" is different from \"06\").\n\n\u00a0\nConstraints:\n\n1 <= s.length <= 100\ns contains only digits and may contain leading zero(s).\n\n",
    "url": "https://leetcode.com/problems/91-decode-ways",
    "answerCount": 1,
    "datePublished": "2024-08-22T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def numDecodings(self, s: str) -> int:\n        n = len(s)\n        @cache\n        def dfs(i):\n            if i >= n:\n                return 1\n            \n            res = 0\n            if 1 <= int(s[i]) <= 9 :\n                res += dfs(i+1)\n            if 10 <= int(s[i:i+2]) <= 26:\n                res += dfs(i+2)\n            return res\n        \n        return dfs(0) if s and s[0] != '0' else 0",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/91-decode-ways/",
      "datePublished": "2024-08-22T00:00:00Z",
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