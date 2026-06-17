# 520-detect-capital


Try it on <a href='https://leetcode.com/problems/520-detect-capital'>leetcode</a>

## Description
<div class="description">
<div><p>We define the usage of capitals in a word to be right when one of the following cases holds:</p>

<ul>
	<li>All letters in this word are capitals, like <code>"USA"</code>.</li>
	<li>All letters in this word are not capitals, like <code>"leetcode"</code>.</li>
	<li>Only the first letter in this word is capital, like <code>"Google"</code>.</li>
</ul>

<p>Given a string <code>word</code>, return <code>true</code> if the usage of capitals in it is right.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> word = "USA"
<strong>Output:</strong> true
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> word = "FlaG"
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 100</code></li>
	<li><code>word</code> consists of lowercase and uppercase English letters.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "520. Detect Capital",
    "text": "We define the usage of capitals in a word to be right when one of the following cases holds:\n\nAll letters in this word are capitals, like \"USA\".\nAll letters in this word are not capitals, like \"leetcode\".\nOnly the first letter in this word is capital, like \"Google\".\n\nGiven a string word, return true if the usage of capitals in it is right.\n\u00a0\nExample 1:\nInput: word = \"USA\"\nOutput: true\nExample 2:\nInput: word = \"FlaG\"\nOutput: false\n\n\u00a0\nConstraints:\n\n1 <= word.length <= 100\nword consists of lowercase and uppercase English letters.\n\n",
    "url": "https://leetcode.com/problems/520-detect-capital",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def detectCapitalUse(self, word: str) -> bool:\n        return word.isupper() or word.islower() or word.istitle()\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/520-detect-capital/",
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