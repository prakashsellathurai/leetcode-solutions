# 647-palindromic-substrings


Try it on <a href='https://leetcode.com/problems/647-palindromic-substrings'>leetcode</a>

## Description
<div class="description">
<div><p>Given a string <code>s</code>, return <em>the number of <strong>palindromic substrings</strong> in it</em>.</p>

<p>A string is a <strong>palindrome</strong> when it reads the same backward as forward.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters within the string.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "abc"
<strong>Output:</strong> 3
<strong>Explanation:</strong> Three palindromic strings: "a", "b", "c".
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "aaa"
<strong>Output:</strong> 6
<strong>Explanation:</strong> Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def countSubstrings(self, s: str) -> int:
        return self.dptable(s)

    # Time Complexity: O(n^3)
    # Space Complexity: O(1)
    def bruteforce(self, s: str) -> int:
        n = len(s)
        cnt = 0
        for i in range(n):
            for j in range(i, n):
                if self.ispalindrome(s[i: j + 1]):
                    cnt += 1
        return cnt

    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    def topdown(self, s: str) -> int:
        n = len(s)
        cnt = 0
        dp = [[-1 for _ in range(n)] for _ in range(n)]

        def solve(i, j):
            if i >= j:
                return 1

            if dp[i][j] != -1:
                return dp[i][j]

            dp[i][j] = solve(i + 1, j - 1) if s[i] == s[j] else 0
            return dp[i][j]

        for i in range(n):
            for j in range(i, n):
                cnt += solve(i, j)
        return cnt

    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    def dptable(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if i + 1 >= j:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j]:
                    ans += 1
        return ans

    def ispalindrome(self, string):
        s, e = 0, len(string) - 1

        while s <= e:
            if string[s] != string[e]:
                return False
            s += 1
            e -= 1

        return True

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "647. Palindromic Substrings",
    "text": "Given a string s, return the number of palindromic substrings in it.\nA string is a palindrome when it reads the same backward as forward.\nA substring is a contiguous sequence of characters within the string.\n\u00a0\nExample 1:\nInput: s = \"abc\"\nOutput: 3\nExplanation: Three palindromic strings: \"a\", \"b\", \"c\".\n\nExample 2:\nInput: s = \"aaa\"\nOutput: 6\nExplanation: Six palindromic strings: \"a\", \"a\", \"a\", \"aa\", \"aa\", \"aaa\".\n\n\u00a0\nConstraints:\n\n1 <= s.length <= 1000\ns consists of lowercase English letters.\n\n",
    "url": "https://leetcode.com/problems/647-palindromic-substrings",
    "answerCount": 1,
    "datePublished": "2022-09-14T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def countSubstrings(self, s: str) -> int:\n        return self.dptable(s)\n\n    # Time Complexity: O(n^3)\n    # Space Complexity: O(1)\n    def bruteforce(self, s: str) -> int:\n        n = len(s)\n        cnt = 0\n        for i in range(n):\n            for j in range(i, n):\n                if self.ispalindrome(s[i: j + 1]):\n                    cnt += 1\n        return cnt\n\n    # Time Complexity: O(n^2)\n    # Space Complexity: O(n^2)\n    def topdown(self, s: str) -> int:\n        n = len(s)\n        cnt = 0\n        dp = [[-1 for _ in range(n)] for _ in range(n)]\n\n        def solve(i, j):\n            if i >= j:\n                return 1\n\n            if dp[i][j] != -1:\n                return dp[i][j]\n\n            dp[i][j] = solve(i + 1, j - 1) if s[i] == s[j] else 0\n            return dp[i][j]\n\n        for i in range(n):\n            for j in range(i, n):\n                cnt += solve(i, j)\n        return cnt\n\n    # Time Complexity: O(n^2)\n    # Space Complexity: O(n^2)\n    def dptable(self, s: str) -> int:\n        n = len(s)\n        dp = [[False] * n for _ in range(n)]\n\n        ans = 0\n        for i in range(n - 1, -1, -1):\n            for j in range(i, n):\n                if s[i] == s[j]:\n                    if i + 1 >= j:\n                        dp[i][j] = True\n                    else:\n                        dp[i][j] = dp[i + 1][j - 1]\n\n                if dp[i][j]:\n                    ans += 1\n        return ans\n\n    def ispalindrome(self, string):\n        s, e = 0, len(string) - 1\n\n        while s <= e:\n            if string[s] != string[e]:\n                return False\n            s += 1\n            e -= 1\n\n        return True\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/647-palindromic-substrings/",
      "datePublished": "2022-09-14T00:00:00Z",
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