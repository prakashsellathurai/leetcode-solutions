# 191-number-of-1-bits


Try it on <a href='https://leetcode.com/problems/191-number-of-1-bits'>leetcode</a>

## Description
<div class="description">
<div><p>Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the <a href="http://en.wikipedia.org/wiki/Hamming_weight" target="_blank">Hamming weight</a>).</p>

<p><strong>Note:</strong></p>

<ul>
	<li>Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.</li>
	<li>In Java, the compiler represents the signed integers using <a href="https://en.wikipedia.org/wiki/Two%27s_complement" target="_blank">2's complement notation</a>. Therefore, in <strong>Example 3</strong>, the input represents the signed integer. <code>-3</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> n = 00000000000000000000000000001011
<strong>Output:</strong> 3
<strong>Explanation:</strong> The input binary string <strong>00000000000000000000000000001011</strong> has a total of three '1' bits.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> n = 00000000000000000000000010000000
<strong>Output:</strong> 1
<strong>Explanation:</strong> The input binary string <strong>00000000000000000000000010000000</strong> has a total of one '1' bit.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> n = 11111111111111111111111111111101
<strong>Output:</strong> 31
<strong>Explanation:</strong> The input binary string <strong>11111111111111111111111111111101</strong> has a total of thirty one '1' bits.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The input must be a <strong>binary string</strong> of length <code>32</code>.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> If this function is called many times, how would you optimize it?</div>
</div>

## Solution(Python)
```Python
class Solution:
    def hammingWeight(self, n: int) -> int:
        return self.bitmanipulation(n)

    # Time Complexity: O(2^logn)
    # Space Complexity: O(logn)
    def bruteforce(self, n):
        n = bin(n)

        def recur(n):
            if not n:
                return 0
            return recur(n[1:]) + 1 if n[0] == "1" else recur(n[1:])

        return recur(n)

    # Time Complexity: O(log(n))
    # Space Complexity: O(logn)
    def naive(self, n):
        return bin(n).count("1")

    # Time Complexity: O(log(n))
    # Space Complexity: O(1)
    def bitmanipulation(self, n):
        cnt = 0
        while n:
            n &= n - 1
            cnt += 1
        return cnt

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "191. Number of 1 Bits",
    "text": "Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).\nNote:\n\nNote that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.\nIn Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.\n\n\u00a0\nExample 1:\nInput: n = 00000000000000000000000000001011\nOutput: 3\nExplanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.\n\nExample 2:\nInput: n = 00000000000000000000000010000000\nOutput: 1\nExplanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.\n\nExample 3:\nInput: n = 11111111111111111111111111111101\nOutput: 31\nExplanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.\n\n\u00a0\nConstraints:\n\nThe input must be a binary string of length 32.\n\n\u00a0\nFollow up: If this function is called many times, how would you optimize it?",
    "url": "https://leetcode.com/problems/191-number-of-1-bits",
    "answerCount": 1,
    "datePublished": "2024-07-13T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def hammingWeight(self, n: int) -> int:\n        return self.bitmanipulation(n)\n\n    # Time Complexity: O(2^logn)\n    # Space Complexity: O(logn)\n    def bruteforce(self, n):\n        n = bin(n)\n\n        def recur(n):\n            if not n:\n                return 0\n            return recur(n[1:]) + 1 if n[0] == \"1\" else recur(n[1:])\n\n        return recur(n)\n\n    # Time Complexity: O(log(n))\n    # Space Complexity: O(logn)\n    def naive(self, n):\n        return bin(n).count(\"1\")\n\n    # Time Complexity: O(log(n))\n    # Space Complexity: O(1)\n    def bitmanipulation(self, n):\n        cnt = 0\n        while n:\n            n &= n - 1\n            cnt += 1\n        return cnt\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/191-number-of-1-bits/",
      "datePublished": "2024-07-13T00:00:00Z",
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