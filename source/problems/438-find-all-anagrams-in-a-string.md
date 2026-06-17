# 438-find-all-anagrams-in-a-string


Try it on <a href='https://leetcode.com/problems/438-find-all-anagrams-in-a-string'>leetcode</a>

## Description
<div class="description">
<div><p>Given two strings <code>s</code> and <code>p</code>, return <em>an array of all the start indices of </em><code>p</code><em>'s anagrams in </em><code>s</code>. You may return the answer in <strong>any order</strong>.</p>

<p>An <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "cbaebabacd", p = "abc"
<strong>Output:</strong> [0,6]
<strong>Explanation:</strong>
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "abab", p = "ab"
<strong>Output:</strong> [0,1,2]
<strong>Explanation:</strong>
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, p.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>p</code> consist of lowercase English letters.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def __init__(self):
        self.a = ord("a")

    def findAnagrams(self, s: str, p: str) -> List[int]:
        return self.windowsliding(s, p)

    """
    create Counter Dict of p
    for all substrings in s:
        check if it's anagram if s 
             
            
    Time Complexty: O(n^2)
    Space Complexity: O(1)
    
    """

    def bruteforce(self, s, p):

        n = len(s)
        cnts = Counter(p)
        res = []
        for i in range(n):
            for j in range(i, n):
                sub_s = s[i: j + 1]
                if Counter(sub_s) == cnts:
                    res.append(i)

        return res

    """
    create Frequency counter table  of p (atmost 26 letters)
    
    create Frequency counter table for current window of size m on s
    
    slide over the s:
        if two frequency table matches:
            add start index to the solution
        increment end of the slider 
        decrement the start of the slider
    
    finally check for substring at the end of the s
            
    Time Complexty: O(n)
    Space Complexity: O(1)          
    """

    def windowsliding(self, s, p):
        n = len(s)
        m = len(p)

        if m > n:
            return []
        res = []

        countP = [0] * 26
        countCW = [0] * 26

        for i in range(m):
            countP[ord(p[i]) - self.a] += 1
            countCW[ord(s[i]) - self.a] += 1

        for i in range(m, n):
            if countP == countCW:
                res.append(i - m)

            countCW[ord(s[i]) - self.a] += 1
            countCW[ord(s[i - m]) - self.a] -= 1

        if countP == countCW:
            res.append(n - m)
        return res

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "438. Find All Anagrams in a String",
    "text": "Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.\nAn Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.\n\u00a0\nExample 1:\nInput: s = \"cbaebabacd\", p = \"abc\"\nOutput: [0,6]\nExplanation:\nThe substring with start index = 0 is \"cba\", which is an anagram of \"abc\".\nThe substring with start index = 6 is \"bac\", which is an anagram of \"abc\".\n\nExample 2:\nInput: s = \"abab\", p = \"ab\"\nOutput: [0,1,2]\nExplanation:\nThe substring with start index = 0 is \"ab\", which is an anagram of \"ab\".\nThe substring with start index = 1 is \"ba\", which is an anagram of \"ab\".\nThe substring with start index = 2 is \"ab\", which is an anagram of \"ab\".\n\n\u00a0\nConstraints:\n\n1 <= s.length, p.length <= 3 * 104\ns and p consist of lowercase English letters.\n\n",
    "url": "https://leetcode.com/problems/438-find-all-anagrams-in-a-string",
    "answerCount": 1,
    "datePublished": "2026-01-05T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def __init__(self):\n        self.a = ord(\"a\")\n\n    def findAnagrams(self, s: str, p: str) -> List[int]:\n        return self.windowsliding(s, p)\n\n    \"\"\"\n    create Counter Dict of p\n    for all substrings in s:\n        check if it's anagram if s \n             \n            \n    Time Complexty: O(n^2)\n    Space Complexity: O(1)\n    \n    \"\"\"\n\n    def bruteforce(self, s, p):\n\n        n = len(s)\n        cnts = Counter(p)\n        res = []\n        for i in range(n):\n            for j in range(i, n):\n                sub_s = s[i: j + 1]\n                if Counter(sub_s) == cnts:\n                    res.append(i)\n\n        return res\n\n    \"\"\"\n    create Frequency counter table  of p (atmost 26 letters)\n    \n    create Frequency counter table for current window of size m on s\n    \n    slide over the s:\n        if two frequency table matches:\n            add start index to the solution\n        increment end of the slider \n        decrement the start of the slider\n    \n    finally check for substring at the end of the s\n            \n    Time Complexty: O(n)\n    Space Complexity: O(1)          \n    \"\"\"\n\n    def windowsliding(self, s, p):\n        n = len(s)\n        m = len(p)\n\n        if m > n:\n            return []\n        res = []\n\n        countP = [0] * 26\n        countCW = [0] * 26\n\n        for i in range(m):\n            countP[ord(p[i]) - self.a] += 1\n            countCW[ord(s[i]) - self.a] += 1\n\n        for i in range(m, n):\n            if countP == countCW:\n                res.append(i - m)\n\n            countCW[ord(s[i]) - self.a] += 1\n            countCW[ord(s[i - m]) - self.a] -= 1\n\n        if countP == countCW:\n            res.append(n - m)\n        return res\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/438-find-all-anagrams-in-a-string/",
      "datePublished": "2026-01-05T00:00:00Z",
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