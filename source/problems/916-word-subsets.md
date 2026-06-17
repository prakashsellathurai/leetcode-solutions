# 916-word-subsets


Try it on <a href='https://leetcode.com/problems/916-word-subsets'>leetcode</a>

## Description
<div class="description">
<div><p>You are given two string arrays <code>words1</code> and <code>words2</code>.</p>

<p>A string <code>b</code> is a <strong>subset</strong> of string <code>a</code> if every letter in <code>b</code> occurs in <code>a</code> including multiplicity.</p>

<ul>
	<li>For example, <code>"wrr"</code> is a subset of <code>"warrior"</code> but is not a subset of <code>"world"</code>.</li>
</ul>

<p>A string <code>a</code> from <code>words1</code> is <strong>universal</strong> if for every string <code>b</code> in <code>words2</code>, <code>b</code> is a subset of <code>a</code>.</p>

<p>Return an array of all the <strong>universal</strong> strings in <code>words1</code>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
<strong>Output:</strong> ["facebook","google","leetcode"]
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
<strong>Output:</strong> ["apple","google","leetcode"]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words1.length, words2.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= words1[i].length, words2[i].length &lt;= 10</code></li>
	<li><code>words1[i]</code> and <code>words2[i]</code> consist only of lowercase English letters.</li>
	<li>All the strings of <code>words1</code> are <strong>unique</strong>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution(object):
    def wordSubsets(self, A, B):
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans

        bmax = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        ans = []
        for a in A:
            if all(x >= y for x, y in zip(count(a), bmax)):
                ans.append(a)
        return ans
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "916. Word Subsets",
    "text": "You are given two string arrays words1 and words2.\nA string b is a subset of string a if every letter in b occurs in a including multiplicity.\n\nFor example, \"wrr\" is a subset of \"warrior\" but is not a subset of \"world\".\n\nA string a from words1 is universal if for every string b in words2, b is a subset of a.\nReturn an array of all the universal strings in words1. You may return the answer in any order.\n\u00a0\nExample 1:\nInput: words1 = [\"amazon\",\"apple\",\"facebook\",\"google\",\"leetcode\"], words2 = [\"e\",\"o\"]\nOutput: [\"facebook\",\"google\",\"leetcode\"]\n\nExample 2:\nInput: words1 = [\"amazon\",\"apple\",\"facebook\",\"google\",\"leetcode\"], words2 = [\"l\",\"e\"]\nOutput: [\"apple\",\"google\",\"leetcode\"]\n\n\u00a0\nConstraints:\n\n1 <= words1.length, words2.length <= 104\n1 <= words1[i].length, words2[i].length <= 10\nwords1[i] and words2[i] consist only of lowercase English letters.\nAll the strings of words1 are unique.\n\n",
    "url": "https://leetcode.com/problems/916-word-subsets",
    "answerCount": 1,
    "datePublished": "2026-05-16T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution(object):\n    def wordSubsets(self, A, B):\n        def count(word):\n            ans = [0] * 26\n            for letter in word:\n                ans[ord(letter) - ord('a')] += 1\n            return ans\n\n        bmax = [0] * 26\n        for b in B:\n            for i, c in enumerate(count(b)):\n                bmax[i] = max(bmax[i], c)\n\n        ans = []\n        for a in A:\n            if all(x >= y for x, y in zip(count(a), bmax)):\n                ans.append(a)\n        return ans",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/916-word-subsets/",
      "datePublished": "2026-05-16T00:00:00Z",
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