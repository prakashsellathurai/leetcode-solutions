# 3662-filter-characters-by-frequency


Try it on <a href='https://leetcode.com/problems/3662-filter-characters-by-frequency'>leetcode</a>

## Description
<div class="description">
<p>You are given a string <code>s</code> consisting of lowercase English letters and an integer <code>k</code>.</p>

<p>Your task is to construct a new string that contains only those characters from <code>s</code> which appear <strong>fewer</strong> than <code>k</code> times in the entire string. The order of characters in the new string must be the <strong>same</strong> as their <strong>order</strong> in <code>s</code>.</p>

<p>Return the resulting string. If no characters qualify, return an empty string.</p>

<p>Note: <strong>Every occurrence</strong> of a character that occurs fewer than <code>k</code> times is kept.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;aadbbcccca&quot;, k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;dbb&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>Character frequencies in <code>s</code>:</p>

<ul>
	<li><code>&#39;a&#39;</code> appears 3 times</li>
	<li><code>&#39;d&#39;</code> appears 1 time</li>
	<li><code>&#39;b&#39;</code> appears 2 times</li>
	<li><code>&#39;c&#39;</code> appears 4 times</li>
</ul>

<p>Only <code>&#39;d&#39;</code> and <code>&#39;b&#39;</code> appear fewer than 3 times. Preserving their order, the result is <code>&quot;dbb&quot;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;xyz&quot;, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;xyz&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>All characters (<code>&#39;x&#39;</code>, <code>&#39;y&#39;</code>, <code>&#39;z&#39;</code>) appear exactly once, which is fewer than 2. Thus the whole string is returned.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
	<li><code>1 &lt;= k &lt;= s.length</code></li>
</ul>

</div>

## Solution(Python)
```Python
class Solution:
    def filterCharacters(self, s: str, k: int) -> str:
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1
            
        res = ''
        for c in s:
            if freq[c] < k:
                res += c
        return res
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "3662. Filter Characters by Frequency",
    "text": "You are given a string s consisting of lowercase English letters and an integer k.\nYour task is to construct a new string that contains only those characters from s which appear fewer than k times in the entire string. The order of characters in the new string must be the same as their order in s.\nReturn the resulting string. If no characters qualify, return an empty string.\nNote: Every occurrence of a character that occurs fewer than k times is kept.\n\u00a0\nExample 1:\n\nInput: s = \"aadbbcccca\", k = 3\nOutput: \"dbb\"\nExplanation:\nCharacter frequencies in s:\n\n'a' appears 3 times\n'd' appears 1 time\n'b' appears 2 times\n'c' appears 4 times\n\nOnly 'd' and 'b' appear fewer than 3 times. Preserving their order, the result is \"dbb\".\n\nExample 2:\n\nInput: s = \"xyz\", k = 2\nOutput: \"xyz\"\nExplanation:\nAll characters ('x', 'y', 'z') appear exactly once, which is fewer than 2. Thus the whole string is returned.\n\n\u00a0\nConstraints:\n\n1 <= s.length <= 100\ns consists of lowercase English letters.\n1 <= k <= s.length\n\n",
    "url": "https://leetcode.com/problems/3662-filter-characters-by-frequency",
    "answerCount": 1,
    "datePublished": "2025-09-03T16:34:47+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def filterCharacters(self, s: str, k: int) -> str:\n        freq = {}\n        for c in s:\n            if c not in freq:\n                freq[c] = 1\n            else:\n                freq[c] += 1\n            \n        res = ''\n        for c in s:\n            if freq[c] < k:\n                res += c\n        return res",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/3662-filter-characters-by-frequency/",
      "datePublished": "2025-09-03T16:34:47+05:30",
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