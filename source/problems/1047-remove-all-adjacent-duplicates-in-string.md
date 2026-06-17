# 1047-remove-all-adjacent-duplicates-in-string


Try it on <a href='https://leetcode.com/problems/1047-remove-all-adjacent-duplicates-in-string'>leetcode</a>

## Description
<div class="description">
<div><p>You are given a string <code>s</code> consisting of lowercase English letters. A <strong>duplicate removal</strong> consists of choosing two <strong>adjacent</strong> and <strong>equal</strong> letters and removing them.</p>

<p>We repeatedly make <strong>duplicate removals</strong> on <code>s</code> until we no longer can.</p>

<p>Return <em>the final string after all such duplicate removals have been made</em>. It can be proven that the answer is <strong>unique</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "abbaca"
<strong>Output:</strong> "ca"
<strong>Explanation:</strong> 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "azxxzy"
<strong>Output:</strong> "ay"
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
    def removeDuplicates(self, s: str) -> str:
        res = []
        for c in s:
            if res and res[-1] == c:
                res.pop()
            else:
                res.append(c)
        return "".join(res)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1047. Remove All Adjacent Duplicates In String",
    "text": "You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.\nWe repeatedly make duplicate removals on s until we no longer can.\nReturn the final string after all such duplicate removals have been made. It can be proven that the answer is unique.\n\u00a0\nExample 1:\nInput: s = \"abbaca\"\nOutput: \"ca\"\nExplanation: \nFor example, in \"abbaca\" we could remove \"bb\" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is \"aaca\", of which only \"aa\" is possible, so the final string is \"ca\".\n\nExample 2:\nInput: s = \"azxxzy\"\nOutput: \"ay\"\n\n\u00a0\nConstraints:\n\n1 <= s.length <= 105\ns consists of lowercase English letters.\n\n",
    "url": "https://leetcode.com/problems/1047-remove-all-adjacent-duplicates-in-string",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def removeDuplicates(self, s: str) -> str:\n        res = []\n        for c in s:\n            if res and res[-1] == c:\n                res.pop()\n            else:\n                res.append(c)\n        return \"\".join(res)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1047-remove-all-adjacent-duplicates-in-string/",
      "datePublished": "2024-11-27",
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