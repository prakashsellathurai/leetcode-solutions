# 1711-count-good-meals


Try it on <a href='https://leetcode.com/problems/1711-count-good-meals'>leetcode</a>

## Description
<div class="description">
<div><p>A <strong>good meal</strong> is a meal that contains <strong>exactly two different food items</strong> with a sum of deliciousness equal to a power of two.</p>

<p>You can pick <strong>any</strong> two different foods to make a good meal.</p>

<p>Given an array of integers <code>deliciousness</code> where <code>deliciousness[i]</code> is the deliciousness of the <code>i<sup>​​​​​​th</sup>​​​​</code>​​​​ item of food, return <em>the number of different <strong>good meals</strong> you can make from this list modulo</em> <code>10<sup>9</sup> + 7</code>.</p>

<p>Note that items with different indices are considered different even if they have the same deliciousness value.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> deliciousness = [1,3,5,7,9]
<strong>Output:</strong> 4
<strong>Explanation: </strong>The good meals are (1,3), (1,7), (3,5) and, (7,9).
Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> deliciousness = [1,1,1,3,3,3,7]
<strong>Output:</strong> 15
<strong>Explanation: </strong>The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= deliciousness.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= deliciousness[i] &lt;= 2<sup>20</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def __init__(self):
        self.mod = (10**9) + 7
        self.targets = [2**i for i in range(22)]

    def countPairs(self, deliciousness: List[int]) -> int:
        return self.hashing(deliciousness)

    # Time Complexity: O(n^2)
    # space Complexity: O(1)
    def bruteforce(self, deliciousness: List[int]) -> int:
        n = len(deliciousness)
        cnt = 0

        for i in range(n):
            for j in range(i + 1, n):
                target = deliciousness[i] + deliciousness[j]
                if self.isPowerOfTwo(target):
                    cnt = cnt % self.mod + 1

        return cnt % self.mod

    def isPowerOfTwo(self, x):
        return x != 0 and not (x & x - 1)

    # Time Complexity: O(n)
    # space Complexity: O(n)
    def hashing(self, deliciousness: List[int]) -> int:
        n = len(deliciousness)
        cnt = 0
        FreqhashTable = defaultdict(int)

        for i in range(n):
            for target in self.targets:
                exp_deliciousness = target - deliciousness[i]
                if exp_deliciousness in FreqhashTable:
                    cnt += FreqhashTable[exp_deliciousness]
            FreqhashTable[deliciousness[i]] += 1

        return cnt % self.mod

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1711. Count Good Meals",
    "text": "A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.\nYou can pick any two different foods to make a good meal.\nGiven an array of integers deliciousness where deliciousness[i] is the deliciousness of the i\u200b\u200b\u200b\u200b\u200b\u200bth\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b item of food, return the number of different good meals you can make from this list modulo 109 + 7.\nNote that items with different indices are considered different even if they have the same deliciousness value.\n\u00a0\nExample 1:\nInput: deliciousness = [1,3,5,7,9]\nOutput: 4\nExplanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).\nTheir respective sums are 4, 8, 8, and 16, all of which are powers of 2.\n\nExample 2:\nInput: deliciousness = [1,1,1,3,3,3,7]\nOutput: 15\nExplanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.\n\u00a0\nConstraints:\n\n1 <= deliciousness.length <= 105\n0 <= deliciousness[i] <= 220\n\n",
    "url": "https://leetcode.com/problems/1711-count-good-meals",
    "answerCount": 1,
    "datePublished": "2026-04-17T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def __init__(self):\n        self.mod = (10**9) + 7\n        self.targets = [2**i for i in range(22)]\n\n    def countPairs(self, deliciousness: List[int]) -> int:\n        return self.hashing(deliciousness)\n\n    # Time Complexity: O(n^2)\n    # space Complexity: O(1)\n    def bruteforce(self, deliciousness: List[int]) -> int:\n        n = len(deliciousness)\n        cnt = 0\n\n        for i in range(n):\n            for j in range(i + 1, n):\n                target = deliciousness[i] + deliciousness[j]\n                if self.isPowerOfTwo(target):\n                    cnt = cnt % self.mod + 1\n\n        return cnt % self.mod\n\n    def isPowerOfTwo(self, x):\n        return x != 0 and not (x & x - 1)\n\n    # Time Complexity: O(n)\n    # space Complexity: O(n)\n    def hashing(self, deliciousness: List[int]) -> int:\n        n = len(deliciousness)\n        cnt = 0\n        FreqhashTable = defaultdict(int)\n\n        for i in range(n):\n            for target in self.targets:\n                exp_deliciousness = target - deliciousness[i]\n                if exp_deliciousness in FreqhashTable:\n                    cnt += FreqhashTable[exp_deliciousness]\n            FreqhashTable[deliciousness[i]] += 1\n\n        return cnt % self.mod\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1711-count-good-meals/",
      "datePublished": "2026-04-17T00:00:00Z",
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