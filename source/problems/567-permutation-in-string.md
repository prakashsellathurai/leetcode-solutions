# 567-permutation-in-string


Try it on <a href='https://leetcode.com/problems/567-permutation-in-string'>leetcode</a>

## Description
<div class="description">
<div><p>Given two strings <code>s1</code> and <code>s2</code>, return <code>true</code><em> if </em><code>s2</code><em> contains a permutation of </em><code>s1</code><em>, or </em><code>false</code><em> otherwise</em>.</p>

<p>In other words, return <code>true</code> if one of <code>s1</code>'s permutations is the substring of <code>s2</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s1 = "ab", s2 = "eidbaooo"
<strong>Output:</strong> true
<strong>Explanation:</strong> s2 contains one permutation of s1 ("ba").
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s1 = "ab", s2 = "eidboaoo"
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s1</code> and <code>s2</code> consist of lowercase English letters.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return self.slidingWindow(s1, s2)

    """
    Time Complexity: O(n!)
    Space Complexity: O(n^2)
    """

    def bruteforce(self, s1: str, s2: str) -> bool:
        self.res = False

        def permute(s1, s2, l):
            if l == len(s1):
                if "".join(s1) in "".join(s2):
                    self.res = True
            else:
                for i in range(l, len(s1)):
                    s1[l], s1[i] = s1[i], s1[l]
                    permute(s1, s2, l + 1)
                    s1[l], s1[i] = s1[i], s1[l]

        permute(list(s1), list(s2), 0)
        return self.res

    """
    we can use either hashmap or an array of size 26 to store the frequency of array
    Time Complexity: O(m*(n-m))
    Space Complexity: O(1)
    """

    def extraDataStructure(self, s1: str, s2: str) -> bool:
        s1Freq = [0] * 26

        for ch in s1:
            s1Freq[ord(ch) - ord("a")] += 1

        n = len(s2)
        m = len(s1)

        for i in range(n - m + 1):
            s2Freq = [0] * 26
            for j in range(m):
                ch = s2[i + j]
                s2Freq[ord(ch) - ord("a")] += 1
            if s1Freq == s2Freq:
                return True
        return False

    """
    Time Complexity: O(m+(n-m))
    Space Complexity: O(1)
    """

    def slidingWindow(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Freq = [0] * 26
        s2Freq = [0] * 26

        for i in range(len(s1)):
            s1Freq[ord(s1[i]) - ord("a")] += 1
            s2Freq[ord(s2[i]) - ord("a")] += 1

        count = 0

        for i in range(26):
            if s1Freq[i] == s2Freq[i]:
                count += 1

        for i in range(len(s2) - len(s1)):
            r = ord(s2[i + len(s1)]) - ord("a")
            l = ord(s2[i]) - ord("a")
            if count == 26:
                return True
            s2Freq[r] += 1
            if s2Freq[r] == s1Freq[r]:
                count += 1
            elif s2Freq[r] == s1Freq[r] + 1:
                count -= 1
            s2Freq[l] -= 1
            if s2Freq[l] == s1Freq[l]:
                count += 1
            elif s2Freq[l] == s1Freq[l] - 1:
                count -= 1

        return count == 26

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "567. Permutation in String",
    "text": "Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.\nIn other words, return true if one of s1's permutations is the substring of s2.\n\u00a0\nExample 1:\nInput: s1 = \"ab\", s2 = \"eidbaooo\"\nOutput: true\nExplanation: s2 contains one permutation of s1 (\"ba\").\n\nExample 2:\nInput: s1 = \"ab\", s2 = \"eidboaoo\"\nOutput: false\n\n\u00a0\nConstraints:\n\n1 <= s1.length, s2.length <= 104\ns1 and s2 consist of lowercase English letters.\n\n",
    "url": "https://leetcode.com/problems/567-permutation-in-string",
    "answerCount": 1,
    "datePublished": "2023-11-16T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def checkInclusion(self, s1: str, s2: str) -> bool:\n        return self.slidingWindow(s1, s2)\n\n    \"\"\"\n    Time Complexity: O(n!)\n    Space Complexity: O(n^2)\n    \"\"\"\n\n    def bruteforce(self, s1: str, s2: str) -> bool:\n        self.res = False\n\n        def permute(s1, s2, l):\n            if l == len(s1):\n                if \"\".join(s1) in \"\".join(s2):\n                    self.res = True\n            else:\n                for i in range(l, len(s1)):\n                    s1[l], s1[i] = s1[i], s1[l]\n                    permute(s1, s2, l + 1)\n                    s1[l], s1[i] = s1[i], s1[l]\n\n        permute(list(s1), list(s2), 0)\n        return self.res\n\n    \"\"\"\n    we can use either hashmap or an array of size 26 to store the frequency of array\n    Time Complexity: O(m*(n-m))\n    Space Complexity: O(1)\n    \"\"\"\n\n    def extraDataStructure(self, s1: str, s2: str) -> bool:\n        s1Freq = [0] * 26\n\n        for ch in s1:\n            s1Freq[ord(ch) - ord(\"a\")] += 1\n\n        n = len(s2)\n        m = len(s1)\n\n        for i in range(n - m + 1):\n            s2Freq = [0] * 26\n            for j in range(m):\n                ch = s2[i + j]\n                s2Freq[ord(ch) - ord(\"a\")] += 1\n            if s1Freq == s2Freq:\n                return True\n        return False\n\n    \"\"\"\n    Time Complexity: O(m+(n-m))\n    Space Complexity: O(1)\n    \"\"\"\n\n    def slidingWindow(self, s1: str, s2: str) -> bool:\n        if len(s1) > len(s2):\n            return False\n\n        s1Freq = [0] * 26\n        s2Freq = [0] * 26\n\n        for i in range(len(s1)):\n            s1Freq[ord(s1[i]) - ord(\"a\")] += 1\n            s2Freq[ord(s2[i]) - ord(\"a\")] += 1\n\n        count = 0\n\n        for i in range(26):\n            if s1Freq[i] == s2Freq[i]:\n                count += 1\n\n        for i in range(len(s2) - len(s1)):\n            r = ord(s2[i + len(s1)]) - ord(\"a\")\n            l = ord(s2[i]) - ord(\"a\")\n            if count == 26:\n                return True\n            s2Freq[r] += 1\n            if s2Freq[r] == s1Freq[r]:\n                count += 1\n            elif s2Freq[r] == s1Freq[r] + 1:\n                count -= 1\n            s2Freq[l] -= 1\n            if s2Freq[l] == s1Freq[l]:\n                count += 1\n            elif s2Freq[l] == s1Freq[l] - 1:\n                count -= 1\n\n        return count == 26\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/567-permutation-in-string/",
      "datePublished": "2023-11-16T00:00:00Z",
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