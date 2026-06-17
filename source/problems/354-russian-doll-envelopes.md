# 354-russian-doll-envelopes


Try it on <a href='https://leetcode.com/problems/354-russian-doll-envelopes'>leetcode</a>

## Description
<div class="description">
<div><p>You are given a 2D array of integers <code>envelopes</code> where <code>envelopes[i] = [w<sub>i</sub>, h<sub>i</sub>]</code> represents the width and the height of an envelope.</p>

<p>One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.</p>

<p>Return <em>the maximum number of envelopes you can Russian doll (i.e., put one inside the other)</em>.</p>

<p><strong>Note:</strong> You cannot rotate an envelope.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> envelopes = [[5,4],[6,4],[6,7],[2,3]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The maximum number of envelopes you can Russian doll is <code>3</code> ([2,3] =&gt; [5,4] =&gt; [6,7]).
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> envelopes = [[1,1],[1,1],[1,1]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= envelopes.length &lt;= 10<sup>5</sup></code></li>
	<li><code>envelopes[i].length == 2</code></li>
	<li><code>1 &lt;= w<sub>i</sub>, h<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        return self.binarysearch(envelopes)

    # Time Complexity: O(2^n)
    # Space Complexity: O(n)
    def bruteforce(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        n = len(envelopes)

        def dfs(i):
            res = 1
            for j in range(i):
                if (
                    envelopes[i][0] > envelopes[j][0]
                    and envelopes[i][1] > envelopes[j][1]
                ):
                    res = max(res, 1 + dfs(j))
            return res

        maxlen = 0
        for i in range(n):
            maxlen = max(maxlen, dfs(i))
        return maxlen

    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    # H[j] = i<j{max(H(i))}+1
    def dynamicprogramming(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()

        n = len(envelopes)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if (
                    envelopes[i][0] > envelopes[j][0]
                    and envelopes[i][1] > envelopes[j][1]
                ):
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def sortingwithmemoize(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        n = len(envelopes)
        dp = [-1] * n

        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            res = 1
            for j in range(i):
                if (
                    envelopes[i][0] > envelopes[j][0]
                    and envelopes[i][1] > envelopes[j][1]
                ):
                    res = max(res, 1 + dfs(j))
            dp[i] = res
            return dp[i]

        maxlen = 0
        for i in range(n):
            maxlen = max(maxlen, dfs(i))
        return maxlen

    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
    def binarysearch(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for envelope in envelopes:
            pos = bisect.bisect_left(dp, envelope[1])
            if pos == len(dp):
                dp.append(envelope[1])
            else:
                dp[pos] = envelope[1]

        return len(dp)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "354. Russian Doll Envelopes",
    "text": "You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.\nOne envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.\nReturn the maximum number of envelopes you can Russian doll (i.e., put one inside the other).\nNote: You cannot rotate an envelope.\n\u00a0\nExample 1:\nInput: envelopes = [[5,4],[6,4],[6,7],[2,3]]\nOutput: 3\nExplanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).\n\nExample 2:\nInput: envelopes = [[1,1],[1,1],[1,1]]\nOutput: 1\n\n\u00a0\nConstraints:\n\n1 <= envelopes.length <= 105\nenvelopes[i].length == 2\n1 <= wi, hi <= 105\n\n",
    "url": "https://leetcode.com/problems/354-russian-doll-envelopes",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:\n        return self.binarysearch(envelopes)\n\n    # Time Complexity: O(2^n)\n    # Space Complexity: O(n)\n    def bruteforce(self, envelopes: List[List[int]]) -> int:\n        envelopes.sort()\n        n = len(envelopes)\n\n        def dfs(i):\n            res = 1\n            for j in range(i):\n                if (\n                    envelopes[i][0] > envelopes[j][0]\n                    and envelopes[i][1] > envelopes[j][1]\n                ):\n                    res = max(res, 1 + dfs(j))\n            return res\n\n        maxlen = 0\n        for i in range(n):\n            maxlen = max(maxlen, dfs(i))\n        return maxlen\n\n    # Time Complexity: O(n^2)\n    # Space Complexity: O(n)\n    # H[j] = i<j{max(H(i))}+1\n    def dynamicprogramming(self, envelopes: List[List[int]]) -> int:\n        envelopes.sort()\n\n        n = len(envelopes)\n        dp = [1] * n\n        for i in range(n):\n            for j in range(i):\n                if (\n                    envelopes[i][0] > envelopes[j][0]\n                    and envelopes[i][1] > envelopes[j][1]\n                ):\n                    dp[i] = max(dp[i], dp[j] + 1)\n\n        return max(dp)\n\n    # Time Complexity: O(n^2)\n    # Space Complexity: O(n)\n    def sortingwithmemoize(self, envelopes: List[List[int]]) -> int:\n        envelopes.sort()\n        n = len(envelopes)\n        dp = [-1] * n\n\n        def dfs(i):\n            if dp[i] != -1:\n                return dp[i]\n            res = 1\n            for j in range(i):\n                if (\n                    envelopes[i][0] > envelopes[j][0]\n                    and envelopes[i][1] > envelopes[j][1]\n                ):\n                    res = max(res, 1 + dfs(j))\n            dp[i] = res\n            return dp[i]\n\n        maxlen = 0\n        for i in range(n):\n            maxlen = max(maxlen, dfs(i))\n        return maxlen\n\n    # Time Complexity: O(nlogn)\n    # Space Complexity: O(n)\n    def binarysearch(self, envelopes: List[List[int]]) -> int:\n        envelopes.sort(key=lambda x: (x[0], -x[1]))\n        dp = []\n        for envelope in envelopes:\n            pos = bisect.bisect_left(dp, envelope[1])\n            if pos == len(dp):\n                dp.append(envelope[1])\n            else:\n                dp[pos] = envelope[1]\n\n        return len(dp)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/354-russian-doll-envelopes/",
      "datePublished": "2022-09-10",
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