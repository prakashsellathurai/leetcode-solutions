# distinct-subsequences


Try it on <a href='https://leetcode.com/problems/distinct-subsequences'>leetcode</a>

## Description
<div class="description">
<div><p>Given two strings <code>s</code> and <code>t</code>, return <em>the number of distinct subsequences of <code>s</code> which equals <code>t</code></em>.</p>

<p>A string's <strong>subsequence</strong> is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., <code>"ACE"</code> is a subsequence of <code>"ABCDE"</code> while <code>"AEC"</code> is not).</p>

<p>The test cases are generated so that the answer fits on a 32-bit signed integer.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "rabbbit", t = "rabbit"
<strong>Output:</strong> 3
<strong>Explanation:</strong>
As shown below, there are 3 ways you can generate "rabbit" from S.
<code><strong><u>rabb</u></strong>b<strong><u>it</u></strong></code>
<code><strong><u>ra</u></strong>b<strong><u>bbit</u></strong></code>
<code><strong><u>rab</u></strong>b<strong><u>bit</u></strong></code>
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "babgbag", t = "bag"
<strong>Output:</strong> 5
<strong>Explanation:</strong>
As shown below, there are 5 ways you can generate "bag" from S.
<code><strong><u>ba</u></strong>b<u><strong>g</strong></u>bag</code>
<code><strong><u>ba</u></strong>bgba<strong><u>g</u></strong></code>
<code><u><strong>b</strong></u>abgb<strong><u>ag</u></strong></code>
<code>ba<u><strong>b</strong></u>gb<u><strong>ag</strong></u></code>
<code>babg<strong><u>bag</u></strong></code></pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 1000</code></li>
	<li><code>s</code> and <code>t</code> consist of English letters.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    @cache
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) == 0:
            return 1

        elif len(s) == 0:
            return 0

        elif s[-1] == t[-1]:
            return self.numDistinct(s[:-1], t[:-1]) + self.numDistinct(s[:-1], t)

        else:
            return self.numDistinct(s[:-1], t)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "115. Distinct Subsequences",
    "text": "Given two strings s and t, return the number of distinct subsequences of s which equals t.\nA string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., \"ACE\" is a subsequence of \"ABCDE\" while \"AEC\" is not).\nThe test cases are generated so that the answer fits on a 32-bit signed integer.\n\u00a0\nExample 1:\nInput: s = \"rabbbit\", t = \"rabbit\"\nOutput: 3\nExplanation:\nAs shown below, there are 3 ways you can generate \"rabbit\" from S.\nrabbbit\nrabbbit\nrabbbit\n\nExample 2:\nInput: s = \"babgbag\", t = \"bag\"\nOutput: 5\nExplanation:\nAs shown below, there are 5 ways you can generate \"bag\" from S.\nbabgbag\nbabgbag\nbabgbag\nbabgbag\nbabgbag\n\u00a0\nConstraints:\n\n1 <= s.length, t.length <= 1000\ns and t consist of English letters.\n\n",
    "url": "https://leetcode.com/problems/distinct-subsequences",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    @cache\n    def numDistinct(self, s: str, t: str) -> int:\n        if len(t) == 0:\n            return 1\n\n        elif len(s) == 0:\n            return 0\n\n        elif s[-1] == t[-1]:\n            return self.numDistinct(s[:-1], t[:-1]) + self.numDistinct(s[:-1], t)\n\n        else:\n            return self.numDistinct(s[:-1], t)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/distinct-subsequences/",
      "datePublished": "2024-10-15",
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