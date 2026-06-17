# 1647-minimum-deletions-to-make-character-frequencies-unique


Try it on <a href='https://leetcode.com/problems/1647-minimum-deletions-to-make-character-frequencies-unique'>leetcode</a>

## Description
<div class="description">
<div><p>A string <code>s</code> is called <strong>good</strong> if there are no two different characters in <code>s</code> that have the same <strong>frequency</strong>.</p>

<p>Given a string <code>s</code>, return<em> the <strong>minimum</strong> number of characters you need to delete to make </em><code>s</code><em> <strong>good</strong>.</em></p>

<p>The <strong>frequency</strong> of a character in a string is the number of times it appears in the string. For example, in the string <code>"aab"</code>, the <strong>frequency</strong> of <code>'a'</code> is <code>2</code>, while the <strong>frequency</strong> of <code>'b'</code> is <code>1</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "aab"
<strong>Output:</strong> 0
<strong>Explanation:</strong> <code>s</code> is already good.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "aaabbbcc"
<strong>Output:</strong> 2
<strong>Explanation:</strong> You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "ceabaacb"
<strong>Output:</strong> 2
<strong>Explanation:</strong> You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code>&nbsp;contains only lowercase English letters.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def minDeletions(self, s: str) -> int:
        return self.sorting(s)

    # Time Complexity: O(n+K^2)
    # Space Complexity: O(K)
    def naive(self, s: str) -> int:
        frequency = [0] * 26
        for c in s:
            frequency[ord(c) - ord("a")] += 1

        delete = 0
        seenFrequencies = set()
        for i in range(26):
            while frequency[i] and frequency[i] in seenFrequencies:
                frequency[i] -= 1
                delete += 1
            seenFrequencies.add(frequency[i])
        return delete

    # Time Complexity: O(n+K^2logK)
    # Space Complexity: O(K)
    def maxheap(self, s: str) -> int:

        frequency = [0] * 26
        for c in s:
            frequency[ord(c) - ord("a")] += 1

        pq = [-freq for freq in frequency if freq != 0]
        delete = 0
        heapq.heapify(pq)
        while len(pq) > 1:
            top = -heapq.heappop(pq)

            if top == -pq[0]:
                if top - 1 > 0:
                    top -= 1
                    heapq.heappush(pq, -top)
                delete += 1

        return delete

    # Time Complexity: O(n)
    # space complexity: O(K)
    def sorting(self, s: str) -> int:
        frequency = [0] * 26
        for c in s:
            frequency[ord(c) - ord("a")] += 1

        frequency.sort(reverse=True)
        max_freq_allowed = len(s)
        delete_count = 0
        for freq in frequency:
            if freq > max_freq_allowed:
                delete_count += freq - max_freq_allowed
                freq = max_freq_allowed
            max_freq_allowed = max(0, freq - 1)
        return delete_count

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1647. Minimum Deletions to Make Character Frequencies Unique",
    "text": "A string s is called good if there are no two different characters in s that have the same frequency.\nGiven a string s, return the minimum number of characters you need to delete to make s good.\nThe frequency of a character in a string is the number of times it appears in the string. For example, in the string \"aab\", the frequency of 'a' is 2, while the frequency of 'b' is 1.\n\u00a0\nExample 1:\nInput: s = \"aab\"\nOutput: 0\nExplanation: s is already good.\n\nExample 2:\nInput: s = \"aaabbbcc\"\nOutput: 2\nExplanation: You can delete two 'b's resulting in the good string \"aaabcc\".\nAnother way it to delete one 'b' and one 'c' resulting in the good string \"aaabbc\".\nExample 3:\nInput: s = \"ceabaacb\"\nOutput: 2\nExplanation: You can delete both 'c's resulting in the good string \"eabaab\".\nNote that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).\n\n\u00a0\nConstraints:\n\n1 <= s.length <= 105\ns\u00a0contains only lowercase English letters.\n\n",
    "url": "https://leetcode.com/problems/1647-minimum-deletions-to-make-character-frequencies-unique",
    "answerCount": 1,
    "datePublished": "2022-06-28T22:00:47+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def minDeletions(self, s: str) -> int:\n        return self.sorting(s)\n\n    # Time Complexity: O(n+K^2)\n    # Space Complexity: O(K)\n    def naive(self, s: str) -> int:\n        frequency = [0] * 26\n        for c in s:\n            frequency[ord(c) - ord(\"a\")] += 1\n\n        delete = 0\n        seenFrequencies = set()\n        for i in range(26):\n            while frequency[i] and frequency[i] in seenFrequencies:\n                frequency[i] -= 1\n                delete += 1\n            seenFrequencies.add(frequency[i])\n        return delete\n\n    # Time Complexity: O(n+K^2logK)\n    # Space Complexity: O(K)\n    def maxheap(self, s: str) -> int:\n\n        frequency = [0] * 26\n        for c in s:\n            frequency[ord(c) - ord(\"a\")] += 1\n\n        pq = [-freq for freq in frequency if freq != 0]\n        delete = 0\n        heapq.heapify(pq)\n        while len(pq) > 1:\n            top = -heapq.heappop(pq)\n\n            if top == -pq[0]:\n                if top - 1 > 0:\n                    top -= 1\n                    heapq.heappush(pq, -top)\n                delete += 1\n\n        return delete\n\n    # Time Complexity: O(n)\n    # space complexity: O(K)\n    def sorting(self, s: str) -> int:\n        frequency = [0] * 26\n        for c in s:\n            frequency[ord(c) - ord(\"a\")] += 1\n\n        frequency.sort(reverse=True)\n        max_freq_allowed = len(s)\n        delete_count = 0\n        for freq in frequency:\n            if freq > max_freq_allowed:\n                delete_count += freq - max_freq_allowed\n                freq = max_freq_allowed\n            max_freq_allowed = max(0, freq - 1)\n        return delete_count\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1647-minimum-deletions-to-make-character-frequencies-unique/",
      "datePublished": "2022-06-28T22:00:47+05:30",
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