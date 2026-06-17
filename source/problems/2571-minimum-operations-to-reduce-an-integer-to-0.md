# 2571-minimum-operations-to-reduce-an-integer-to-0


Try it on <a href='https://leetcode.com/problems/2571-minimum-operations-to-reduce-an-integer-to-0'>leetcode</a>

## Description
<div class="description">
<p>You are given a positive integer <code>n</code>, you can do the following operation <strong>any</strong> number of times:</p>

<ul>
	<li>Add or subtract a <strong>power</strong> of <code>2</code> from <code>n</code>.</li>
</ul>

<p>Return <em>the <strong>minimum</strong> number of operations to make </em><code>n</code><em> equal to </em><code>0</code>.</p>

<p>A number <code>x</code> is power of <code>2</code> if <code>x == 2<sup>i</sup></code>&nbsp;where <code>i &gt;= 0</code><em>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 39
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can do the following operations:
- Add 2<sup>0</sup> = 1 to n, so now n = 40.
- Subtract 2<sup>3</sup> = 8 from n, so now n = 32.
- Subtract 2<sup>5</sup> = 32 from n, so now n = 0.
It can be shown that 3 is the minimum number of operations we need to make n equal to 0.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 54
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can do the following operations:
- Add 2<sup>1</sup> = 2 to n, so now n = 56.
- Add 2<sup>3</sup> = 8 to n, so now n = 64.
- Subtract 2<sup>6</sup> = 64 from n, so now n = 0.
So the minimum number of operations is 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>

</div>

## Solution(Python)
```Python
class Solution:
    def minOperations(self, n: int) -> int:
        return self.minOptimnalOperations(n)
    def minOptimnalOperations(self, n: int) -> int:
        # Initialize result counter and consecutive 1-bits counter
        operations = 0
        consecutive_ones = 0
      
        # Process each bit of n from right to left
        while n > 0:
            # Check if the current least significant bit is 1
            if n & 1:
                # Increment counter for consecutive 1-bits
                consecutive_ones += 1
            elif consecutive_ones > 0:
                # We hit a 0 after seeing 1s, process the group of 1s
                operations += 1
                # Reset counter: if we had exactly one 1, start fresh
                # Otherwise, carry over 1 (for cases like 11 -> 100)
                consecutive_ones = 0 if consecutive_ones == 1 else 1
          
            # Right shift to check the next bit
            n >>= 1
      
        # Handle any remaining consecutive 1-bits after the loop
        if consecutive_ones == 1:
            # Single 1-bit requires one operation
            operations += 1
        elif consecutive_ones > 1:
            # Multiple consecutive 1-bits require two operations
            operations += 2
      
        return operations

    def mindpOperations(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def dp(x):
            if x == 0:
                return 0
            if x == 1:
                return 1
            if x % 2 == 0:
                return dp(x // 2)
            else:
                return 1 + min(dp(x // 2), dp((x + 1) // 2))
        
        return dp(n)


```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "2571. Minimum Operations to Reduce an Integer to 0",
    "text": "You are given a positive integer n, you can do the following operation any number of times:\n\nAdd or subtract a power of 2 from n.\n\nReturn the minimum number of operations to make n equal to 0.\nA number x is power of 2 if x == 2i\u00a0where i >= 0.\n\u00a0\nExample 1:\n\nInput: n = 39\nOutput: 3\nExplanation: We can do the following operations:\n- Add 20 = 1 to n, so now n = 40.\n- Subtract 23 = 8 from n, so now n = 32.\n- Subtract 25 = 32 from n, so now n = 0.\nIt can be shown that 3 is the minimum number of operations we need to make n equal to 0.\n\nExample 2:\n\nInput: n = 54\nOutput: 3\nExplanation: We can do the following operations:\n- Add 21 = 2 to n, so now n = 56.\n- Add 23 = 8 to n, so now n = 64.\n- Subtract 26 = 64 from n, so now n = 0.\nSo the minimum number of operations is 3.\n\n\u00a0\nConstraints:\n\n1 <= n <= 105\n\n",
    "url": "https://leetcode.com/problems/2571-minimum-operations-to-reduce-an-integer-to-0",
    "answerCount": 1,
    "datePublished": "2026-05-25T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def minOperations(self, n: int) -> int:\n        return self.minOptimnalOperations(n)\n    def minOptimnalOperations(self, n: int) -> int:\n        # Initialize result counter and consecutive 1-bits counter\n        operations = 0\n        consecutive_ones = 0\n      \n        # Process each bit of n from right to left\n        while n > 0:\n            # Check if the current least significant bit is 1\n            if n & 1:\n                # Increment counter for consecutive 1-bits\n                consecutive_ones += 1\n            elif consecutive_ones > 0:\n                # We hit a 0 after seeing 1s, process the group of 1s\n                operations += 1\n                # Reset counter: if we had exactly one 1, start fresh\n                # Otherwise, carry over 1 (for cases like 11 -> 100)\n                consecutive_ones = 0 if consecutive_ones == 1 else 1\n          \n            # Right shift to check the next bit\n            n >>= 1\n      \n        # Handle any remaining consecutive 1-bits after the loop\n        if consecutive_ones == 1:\n            # Single 1-bit requires one operation\n            operations += 1\n        elif consecutive_ones > 1:\n            # Multiple consecutive 1-bits require two operations\n            operations += 2\n      \n        return operations\n\n    def mindpOperations(self, n: int) -> int:\n        @lru_cache(maxsize=None)\n        def dp(x):\n            if x == 0:\n                return 0\n            if x == 1:\n                return 1\n            if x % 2 == 0:\n                return dp(x // 2)\n            else:\n                return 1 + min(dp(x // 2), dp((x + 1) // 2))\n        \n        return dp(n)\n\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/2571-minimum-operations-to-reduce-an-integer-to-0/",
      "datePublished": "2026-05-25T00:00:00Z",
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