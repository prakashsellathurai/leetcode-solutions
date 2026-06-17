# 720-longest-word-in-dictionary


Try it on <a href='https://leetcode.com/problems/720-longest-word-in-dictionary'>leetcode</a>

## Description
<div class="description">
<div><p>Given an array of strings <code>words</code> representing an English Dictionary, return <em>the longest word in</em> <code>words</code> <em>that can be built one character at a time by other words in</em> <code>words</code>.</p>

<p>If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> words = ["w","wo","wor","worl","world"]
<strong>Output:</strong> "world"
<strong>Explanation:</strong> The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> words = ["a","banana","app","appl","ap","apply","apple"]
<strong>Output:</strong> "apple"
<strong>Explanation:</strong> Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 30</code></li>
	<li><code>words[i]</code> consists of lowercase English letters.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def longestWord(self, words: List[str]) -> str:
        return self.bruteforce(words)

    def bruteforce(self, words: List[str]) -> str:
        ans = ""
        wordset = set(words)

        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                if all(word[:k] in wordset for k in range(1, len(word))):
                    ans = word
        return ans

    def trie(self, words: List[str]) -> str:
        pass

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "720. Longest Word in Dictionary",
    "text": "Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.\nIf there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.\n\u00a0\nExample 1:\nInput: words = [\"w\",\"wo\",\"wor\",\"worl\",\"world\"]\nOutput: \"world\"\nExplanation: The word \"world\" can be built one character at a time by \"w\", \"wo\", \"wor\", and \"worl\".\n\nExample 2:\nInput: words = [\"a\",\"banana\",\"app\",\"appl\",\"ap\",\"apply\",\"apple\"]\nOutput: \"apple\"\nExplanation: Both \"apply\" and \"apple\" can be built from other words in the dictionary. However, \"apple\" is lexicographically smaller than \"apply\".\n\n\u00a0\nConstraints:\n\n1 <= words.length <= 1000\n1 <= words[i].length <= 30\nwords[i] consists of lowercase English letters.\n\n",
    "url": "https://leetcode.com/problems/720-longest-word-in-dictionary",
    "answerCount": 1,
    "datePublished": "2024-05-26T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def longestWord(self, words: List[str]) -> str:\n        return self.bruteforce(words)\n\n    def bruteforce(self, words: List[str]) -> str:\n        ans = \"\"\n        wordset = set(words)\n\n        for word in words:\n            if len(word) > len(ans) or len(word) == len(ans) and word < ans:\n                if all(word[:k] in wordset for k in range(1, len(word))):\n                    ans = word\n        return ans\n\n    def trie(self, words: List[str]) -> str:\n        pass\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/720-longest-word-in-dictionary/",
      "datePublished": "2024-05-26T00:00:00Z",
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