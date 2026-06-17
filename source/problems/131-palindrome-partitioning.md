# 131-palindrome-partitioning


Try it on <a href='https://leetcode.com/problems/131-palindrome-partitioning'>leetcode</a>

## Description
<div class="description">
<div><p>Given a string <code>s</code>, partition <code>s</code> such that every substring of the partition is a <strong>palindrome</strong>. Return all possible palindrome partitioning of <code>s</code>.</p>

<p>A <strong>palindrome</strong> string is a string that reads the same backward as forward.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aab"
<strong>Output:</strong> [["a","a","b"],["aa","b"]]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "a"
<strong>Output:</strong> [["a"]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 16</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    #  Problem Statement: Given a str s return all possible palindromic
    #  partitions
    #
    #   Input: a string
    #   Output: array of all possible palindromics substring partitions
    #
    #   Example:
    #       1.for s="aaab" return [["a","a","b"],["aa","b"]]
    #
    #   Constraints: 1<= s.length <= 16
    #
    #   Solution:
    #       1.Bruteforce : use backtracking choose a potential candidate (i.e
    #       palindromic substring )from the generated substring from given
    #       constraints
    #
    #       Pseudo code:
    #           fn bactrack (candidate,res,start)
    #               if start reaches end of string
    #                   res.push(cur)
    #
    #               for end=start;end<len(s);end++
    #                   if isPalindrome(s,start,end):
    #                       candidate.push_back(s[start:end+1])
    #                       backtrack(candidate,res,end+1)
    #                       candidate.pop()
    #   Time Complexity: O(N.2^N)
    #   (since our constraint is 1<=n<=16 This is acceptable)
    #   SpaceComplexity: O(n)
    def partition(self, s: str) -> List[List[str]]:
        self.res = []

        @cache
        def isPalindrome(low, high):
            while low < high:
                if s[low] != s[high]:
                    return False
                low += 1
                high -= 1
            return True

        def backtrack(start, cur):
            # candidate selection
            if start >= len(s):
                self.res.append(cur[:])
            # Recursive case
            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    cur.append(s[start: end + 1])
                    backtrack(end + 1, cur)
                    cur.pop()

        backtrack(0, [])
        return self.res

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "131. Palindrome Partitioning",
    "text": "Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.\nA palindrome string is a string that reads the same backward as forward.\n\u00a0\nExample 1:\nInput: s = \"aab\"\nOutput: [[\"a\",\"a\",\"b\"],[\"aa\",\"b\"]]\nExample 2:\nInput: s = \"a\"\nOutput: [[\"a\"]]\n\n\u00a0\nConstraints:\n\n1 <= s.length <= 16\ns contains only lowercase English letters.\n\n",
    "url": "https://leetcode.com/problems/131-palindrome-partitioning",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    #  Problem Statement: Given a str s return all possible palindromic\n    #  partitions\n    #\n    #   Input: a string\n    #   Output: array of all possible palindromics substring partitions\n    #\n    #   Example:\n    #       1.for s=\"aaab\" return [[\"a\",\"a\",\"b\"],[\"aa\",\"b\"]]\n    #\n    #   Constraints: 1<= s.length <= 16\n    #\n    #   Solution:\n    #       1.Bruteforce : use backtracking choose a potential candidate (i.e\n    #       palindromic substring )from the generated substring from given\n    #       constraints\n    #\n    #       Pseudo code:\n    #           fn bactrack (candidate,res,start)\n    #               if start reaches end of string\n    #                   res.push(cur)\n    #\n    #               for end=start;end<len(s);end++\n    #                   if isPalindrome(s,start,end):\n    #                       candidate.push_back(s[start:end+1])\n    #                       backtrack(candidate,res,end+1)\n    #                       candidate.pop()\n    #   Time Complexity: O(N.2^N)\n    #   (since our constraint is 1<=n<=16 This is acceptable)\n    #   SpaceComplexity: O(n)\n    def partition(self, s: str) -> List[List[str]]:\n        self.res = []\n\n        @cache\n        def isPalindrome(low, high):\n            while low < high:\n                if s[low] != s[high]:\n                    return False\n                low += 1\n                high -= 1\n            return True\n\n        def backtrack(start, cur):\n            # candidate selection\n            if start >= len(s):\n                self.res.append(cur[:])\n            # Recursive case\n            for end in range(start, len(s)):\n                if isPalindrome(start, end):\n                    cur.append(s[start: end + 1])\n                    backtrack(end + 1, cur)\n                    cur.pop()\n\n        backtrack(0, [])\n        return self.res\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/131-palindrome-partitioning/",
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