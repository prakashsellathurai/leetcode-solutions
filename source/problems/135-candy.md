# 135-candy


Try it on <a href='https://leetcode.com/problems/135-candy'>leetcode</a>

## Description
<div class="description">
<div><p>There are <code>n</code> children standing in a line. Each child is assigned a rating value given in the integer array <code>ratings</code>.</p>

<p>You are giving candies to these children subjected to the following requirements:</p>

<ul>
	<li>Each child must have at least one candy.</li>
	<li>Children with a higher rating get more candies than their neighbors.</li>
</ul>

<p>Return <em>the minimum number of candies you need to have to distribute the candies to the children</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> ratings = [1,0,2]
<strong>Output:</strong> 5
<strong>Explanation:</strong> You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> ratings = [1,2,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == ratings.length</code></li>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= ratings[i] &lt;= 2 * 10<sup>4</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        return self.SinglePassConstantSpace(ratings)

    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def bruteforce(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        hasChanged = True

        while hasChanged:
            hasChanged = False

            for i in range(n):
                if (
                    i != n - 1
                    and ratings[i] > ratings[i + 1]
                    and candies[i] <= candies[i + 1]
                ):
                    candies[i] = candies[i + 1] + 1
                    hasChanged = True
                if (
                    i >= 0
                    and ratings[i] > ratings[i - 1]
                    and candies[i] <= candies[i - 1]
                ):
                    candies[i] = candies[i - 1] + 1
                    hashChanged = True
        return sum(candies)

    # Time Complexity:O(n)
    # Space Complexity: O(n)
    def presum(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i + 1] + 1, candies[i])

        return sum(candies)

    # Time Complexity:O(n)
    # Space Complexity: O(1)
    def SinglePassConstantSpace(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n <= 1:
            return n

        def summateN(n):
            return (n * (n + 1)) // 2

        candies = 0
        up = 0
        down = 0
        oldSlope = 0

        for i in range(1, n):
            newSlope = (
                1
                if ratings[i] > ratings[i - 1]
                else -1
                if ratings[i] < ratings[i - 1]
                else 0
            )

            if oldSlope > 0 and newSlope == 0 or (oldSlope < 0 and newSlope >= 0):
                candies += summateN(up) + summateN(down) + max(up, down)
                up = 0
                down = 0

            if newSlope > 0:
                up += 1
            elif newSlope < 0:
                down += 1
            else:
                candies += 1
            oldSlope = newSlope

        candies += summateN(up) + summateN(down) + max(up, down) + 1
        return candies

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "135. Candy",
    "text": "There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.\nYou are giving candies to these children subjected to the following requirements:\n\nEach child must have at least one candy.\nChildren with a higher rating get more candies than their neighbors.\n\nReturn the minimum number of candies you need to have to distribute the candies to the children.\n\u00a0\nExample 1:\nInput: ratings = [1,0,2]\nOutput: 5\nExplanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.\n\nExample 2:\nInput: ratings = [1,2,2]\nOutput: 4\nExplanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.\nThe third child gets 1 candy because it satisfies the above two conditions.\n\n\u00a0\nConstraints:\n\nn == ratings.length\n1 <= n <= 2 * 104\n0 <= ratings[i] <= 2 * 104\n\n",
    "url": "https://leetcode.com/problems/135-candy",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def candy(self, ratings: List[int]) -> int:\n        return self.SinglePassConstantSpace(ratings)\n\n    # Time Complexity: O(n^2)\n    # Space Complexity: O(n)\n    def bruteforce(self, ratings: List[int]) -> int:\n        n = len(ratings)\n        candies = [1] * n\n        hasChanged = True\n\n        while hasChanged:\n            hasChanged = False\n\n            for i in range(n):\n                if (\n                    i != n - 1\n                    and ratings[i] > ratings[i + 1]\n                    and candies[i] <= candies[i + 1]\n                ):\n                    candies[i] = candies[i + 1] + 1\n                    hasChanged = True\n                if (\n                    i >= 0\n                    and ratings[i] > ratings[i - 1]\n                    and candies[i] <= candies[i - 1]\n                ):\n                    candies[i] = candies[i - 1] + 1\n                    hashChanged = True\n        return sum(candies)\n\n    # Time Complexity:O(n)\n    # Space Complexity: O(n)\n    def presum(self, ratings: List[int]) -> int:\n        n = len(ratings)\n        candies = [1] * n\n\n        for i in range(1, n):\n            if ratings[i] > ratings[i - 1]:\n                candies[i] = candies[i - 1] + 1\n\n        for i in range(n - 2, -1, -1):\n            if ratings[i] > ratings[i + 1]:\n                candies[i] = max(candies[i + 1] + 1, candies[i])\n\n        return sum(candies)\n\n    # Time Complexity:O(n)\n    # Space Complexity: O(1)\n    def SinglePassConstantSpace(self, ratings: List[int]) -> int:\n        n = len(ratings)\n        if n <= 1:\n            return n\n\n        def summateN(n):\n            return (n * (n + 1)) // 2\n\n        candies = 0\n        up = 0\n        down = 0\n        oldSlope = 0\n\n        for i in range(1, n):\n            newSlope = (\n                1\n                if ratings[i] > ratings[i - 1]\n                else -1\n                if ratings[i] < ratings[i - 1]\n                else 0\n            )\n\n            if oldSlope > 0 and newSlope == 0 or (oldSlope < 0 and newSlope >= 0):\n                candies += summateN(up) + summateN(down) + max(up, down)\n                up = 0\n                down = 0\n\n            if newSlope > 0:\n                up += 1\n            elif newSlope < 0:\n                down += 1\n            else:\n                candies += 1\n            oldSlope = newSlope\n\n        candies += summateN(up) + summateN(down) + max(up, down) + 1\n        return candies\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/135-candy/",
      "datePublished": "2025-11-06",
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