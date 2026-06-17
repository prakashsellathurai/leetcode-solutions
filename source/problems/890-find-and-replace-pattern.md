# 890-find-and-replace-pattern


Try it on <a href='https://leetcode.com/problems/890-find-and-replace-pattern'>leetcode</a>

## Description
<div class="description">
<div><p>Given a list of strings <code>words</code> and a string <code>pattern</code>, return <em>a list of</em> <code>words[i]</code> <em>that match</em> <code>pattern</code>. You may return the answer in <strong>any order</strong>.</p>

<p>A word matches the pattern if there exists a permutation of letters <code>p</code> so that after replacing every letter <code>x</code> in the pattern with <code>p(x)</code>, we get the desired word.</p>

<p>Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
<strong>Output:</strong> ["mee","aqq"]
<strong>Explanation:</strong> "mee" matches the pattern because there is a permutation {a -&gt; m, b -&gt; e, ...}. 
"ccc" does not match the pattern because {a -&gt; c, b -&gt; c, ...} is not a permutation, since a and b map to the same letter.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> words = ["a","b","c"], pattern = "a"
<strong>Output:</strong> ["a","b","c"]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= pattern.length &lt;= 20</code></li>
	<li><code>1 &lt;= words.length &lt;= 50</code></li>
	<li><code>words[i].length == pattern.length</code></li>
	<li><code>pattern</code> and <code>words[i]</code> are lowercase English letters.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def is_pattern(s, t):
            s_map = {}
            t_map = {}
            
            n= len(s)
            if n != len(t):
                return False
            
            for i in range(n):
                if s[i] not in s_map:
                    s_map[s[i]] = t[i]
                elif s_map[s[i]] != t[i]:
                        return False
                    
                if t[i] not in t_map:
                    t_map[t[i]] = s[i]
                elif t_map[t[i]] != s[i]:
                    return False
            return True
        
        res = []
        for word in words:
            if is_pattern(word, pattern):
                res.append(word)
        return res
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "890. Find and Replace Pattern",
    "text": "Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.\nA word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.\nRecall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.\n\u00a0\nExample 1:\nInput: words = [\"abc\",\"deq\",\"mee\",\"aqq\",\"dkd\",\"ccc\"], pattern = \"abb\"\nOutput: [\"mee\",\"aqq\"]\nExplanation: \"mee\" matches the pattern because there is a permutation {a -> m, b -> e, ...}. \n\"ccc\" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.\n\nExample 2:\nInput: words = [\"a\",\"b\",\"c\"], pattern = \"a\"\nOutput: [\"a\",\"b\",\"c\"]\n\n\u00a0\nConstraints:\n\n1 <= pattern.length <= 20\n1 <= words.length <= 50\nwords[i].length == pattern.length\npattern and words[i] are lowercase English letters.\n\n",
    "url": "https://leetcode.com/problems/890-find-and-replace-pattern",
    "answerCount": 1,
    "datePublished": "2022-06-26T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:\n        \n        def is_pattern(s, t):\n            s_map = {}\n            t_map = {}\n            \n            n= len(s)\n            if n != len(t):\n                return False\n            \n            for i in range(n):\n                if s[i] not in s_map:\n                    s_map[s[i]] = t[i]\n                elif s_map[s[i]] != t[i]:\n                        return False\n                    \n                if t[i] not in t_map:\n                    t_map[t[i]] = s[i]\n                elif t_map[t[i]] != s[i]:\n                    return False\n            return True\n        \n        res = []\n        for word in words:\n            if is_pattern(word, pattern):\n                res.append(word)\n        return res",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/890-find-and-replace-pattern/",
      "datePublished": "2022-06-26T00:00:00Z",
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