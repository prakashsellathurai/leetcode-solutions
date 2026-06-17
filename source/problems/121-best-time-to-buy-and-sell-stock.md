# 121-best-time-to-buy-and-sell-stock


Try it on <a href='https://leetcode.com/problems/121-best-time-to-buy-and-sell-stock'>leetcode</a>

## Description
<div class="description">
<div><p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>You want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.</p>

<p>Return <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> prices = [7,1,5,3,6,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transactions are done and the max profit = 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10<sup>4</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.optimized(prices)

    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    def bruteforce(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0
        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] - prices[i] > maxProfit:
                    maxProfit = prices[j] - prices[i]

        return maxProfit

    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def optimized(self, prices: List[int]) -> int:
        buyPrice = float("inf")
        profit = 0

        for sellprice in prices:
            if sellprice < buyPrice:
                buyPrice = sellprice
            elif sellprice - buyPrice > profit:
                profit = sellprice - buyPrice
        return profit

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "121. Best Time to Buy and Sell Stock",
    "text": "You are given an array prices where prices[i] is the price of a given stock on the ith day.\nYou want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.\nReturn the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.\n\u00a0\nExample 1:\nInput: prices = [7,1,5,3,6,4]\nOutput: 5\nExplanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.\nNote that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.\n\nExample 2:\nInput: prices = [7,6,4,3,1]\nOutput: 0\nExplanation: In this case, no transactions are done and the max profit = 0.\n\n\u00a0\nConstraints:\n\n1 <= prices.length <= 105\n0 <= prices[i] <= 104\n\n",
    "url": "https://leetcode.com/problems/121-best-time-to-buy-and-sell-stock",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def maxProfit(self, prices: List[int]) -> int:\n        return self.optimized(prices)\n\n    \"\"\"\n    Time Complexity: O(n^2)\n    Space Complexity: O(1)\n    \"\"\"\n\n    def bruteforce(self, prices: List[int]) -> int:\n        n = len(prices)\n        maxProfit = 0\n        for i in range(n):\n            for j in range(i + 1, n):\n                if prices[j] - prices[i] > maxProfit:\n                    maxProfit = prices[j] - prices[i]\n\n        return maxProfit\n\n    \"\"\"\n    Time Complexity: O(n)\n    Space Complexity: O(1)\n    \"\"\"\n\n    def optimized(self, prices: List[int]) -> int:\n        buyPrice = float(\"inf\")\n        profit = 0\n\n        for sellprice in prices:\n            if sellprice < buyPrice:\n                buyPrice = sellprice\n            elif sellprice - buyPrice > profit:\n                profit = sellprice - buyPrice\n        return profit\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/121-best-time-to-buy-and-sell-stock/",
      "datePublished": "2025-09-04",
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