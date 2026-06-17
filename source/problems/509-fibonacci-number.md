# 509-fibonacci-number


Try it on <a href='https://leetcode.com/problems/509-fibonacci-number'>leetcode</a>

## Description
<div class="description">
<div><p>The <b>Fibonacci numbers</b>, commonly denoted <code>F(n)</code> form a sequence, called the <b>Fibonacci sequence</b>, such that each number is the sum of the two preceding ones, starting from <code>0</code> and <code>1</code>. That is,</p>

<pre>F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n &gt; 1.
</pre>

<p>Given <code>n</code>, calculate <code>F(n)</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> F(2) = F(1) + F(0) = 1 + 0 = 1.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> F(3) = F(2) + F(1) = 1 + 1 = 2.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> n = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong> F(4) = F(3) + F(2) = 2 + 1 = 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 30</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def fib(self, n: int) -> int:
        return self.Iterativelesspace(n)

    # Time Complexity: O(2^n)
    # Space Complexity: O(n)
    def Recursive(self, n):
        if n <= 1:
            return n
        else:
            return self.Recursive(n - 1) + self.Recursive(n - 2)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def Iterative(self, n):
        if n <= 1:
            return n
        fib = [0] * (n + 1)

        fib[1] = 1

        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]

        return fib[n]

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def Iterativelesspace(self, n):
        if n <= 1:
            return n

        prev2, prev1 = 0, 1

        for i in range(2, n + 1):
            cur = prev2 + prev1
            prev2 = prev1
            prev1 = cur

        return cur

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "509. Fibonacci Number",
    "text": "The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,\nF(0) = 0, F(1) = 1\nF(n) = F(n - 1) + F(n - 2), for n > 1.\n\nGiven n, calculate F(n).\n\u00a0\nExample 1:\nInput: n = 2\nOutput: 1\nExplanation: F(2) = F(1) + F(0) = 1 + 0 = 1.\n\nExample 2:\nInput: n = 3\nOutput: 2\nExplanation: F(3) = F(2) + F(1) = 1 + 1 = 2.\n\nExample 3:\nInput: n = 4\nOutput: 3\nExplanation: F(4) = F(3) + F(2) = 2 + 1 = 3.\n\n\u00a0\nConstraints:\n\n0 <= n <= 30\n\n",
    "url": "https://leetcode.com/problems/509-fibonacci-number",
    "answerCount": 1,
    "datePublished": "2023-04-12T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def fib(self, n: int) -> int:\n        return self.Iterativelesspace(n)\n\n    # Time Complexity: O(2^n)\n    # Space Complexity: O(n)\n    def Recursive(self, n):\n        if n <= 1:\n            return n\n        else:\n            return self.Recursive(n - 1) + self.Recursive(n - 2)\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(n)\n    def Iterative(self, n):\n        if n <= 1:\n            return n\n        fib = [0] * (n + 1)\n\n        fib[1] = 1\n\n        for i in range(2, n + 1):\n            fib[i] = fib[i - 1] + fib[i - 2]\n\n        return fib[n]\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(1)\n    def Iterativelesspace(self, n):\n        if n <= 1:\n            return n\n\n        prev2, prev1 = 0, 1\n\n        for i in range(2, n + 1):\n            cur = prev2 + prev1\n            prev2 = prev1\n            prev1 = cur\n\n        return cur\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/509-fibonacci-number/",
      "datePublished": "2023-04-12T00:00:00Z",
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