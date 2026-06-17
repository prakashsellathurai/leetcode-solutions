# 1475-final-prices-with-a-special-discount-in-a-shop


Try it on <a href='https://leetcode.com/problems/1475-final-prices-with-a-special-discount-in-a-shop'>leetcode</a>

## Description
<div class="description">
<p>You are given an integer array <code>prices</code> where <code>prices[i]</code> is the price of the <code>i<sup>th</sup></code> item in a shop.</p>

<p>There is a special discount for items in the shop. If you buy the <code>i<sup>th</sup></code> item, then you will receive a discount equivalent to <code>prices[j]</code> where <code>j</code> is the minimum index such that <code>j &gt; i</code> and <code>prices[j] &lt;= prices[i]</code>. Otherwise, you will not receive any discount at all.</p>

<p>Return an integer array <code>answer</code> where <code>answer[i]</code> is the final price you will pay for the <code>i<sup>th</sup></code> item of the shop, considering the special discount.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [8,4,6,2,3]
<strong>Output:</strong> [4,2,4,2,3]
<strong>Explanation:</strong> 
For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
For items 3 and 4 you will not receive any discount at all.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [1,2,3,4,5]
<strong>Output:</strong> [1,2,3,4,5]
<strong>Explanation:</strong> In this case, for all items, you will not receive any discount at all.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> prices = [10,1,1,6]
<strong>Output:</strong> [9,0,1,6]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 500</code></li>
	<li><code>1 &lt;= prices[i] &lt;= 1000</code></li>
</ul>

</div>

## Solution(Python)
```Python
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        return self.monotonicstack(prices)

    # Time complexity: O(n^2)
    # spac ecomplexity: O(n)
    def bruteforce(self, prices: List[int]) -> List[int]:
        n = len(prices)
        for i in range(n):
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
                else:
                    continue
        return prices

    # Time complexity: O(n)
    # spac ecomplexity: O(n)
    def monotonicstack(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack = []
        for i in range(n): # 10 1 1 6
            while stack and prices[stack[-1]] >= prices[i]: # 
                prices[stack[-1]] -= prices[i] # 9 0 0 0
                stack.pop()
            stack.append(i) # stack -> 1

        return prices
        
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1475. Final Prices With a Special Discount in a Shop",
    "text": "You are given an integer array prices where prices[i] is the price of the ith item in a shop.\nThere is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.\nReturn an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.\n\u00a0\nExample 1:\n\nInput: prices = [8,4,6,2,3]\nOutput: [4,2,4,2,3]\nExplanation: \nFor item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.\nFor item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.\nFor item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.\nFor items 3 and 4 you will not receive any discount at all.\n\nExample 2:\n\nInput: prices = [1,2,3,4,5]\nOutput: [1,2,3,4,5]\nExplanation: In this case, for all items, you will not receive any discount at all.\n\nExample 3:\n\nInput: prices = [10,1,1,6]\nOutput: [9,0,1,6]\n\n\u00a0\nConstraints:\n\n1 <= prices.length <= 500\n1 <= prices[i] <= 1000\n\n",
    "url": "https://leetcode.com/problems/1475-final-prices-with-a-special-discount-in-a-shop",
    "answerCount": 1,
    "datePublished": "2024-03-18T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def finalPrices(self, prices: List[int]) -> List[int]:\n        return self.monotonicstack(prices)\n\n    # Time complexity: O(n^2)\n    # spac ecomplexity: O(n)\n    def bruteforce(self, prices: List[int]) -> List[int]:\n        n = len(prices)\n        for i in range(n):\n            for j in range(i+1, n):\n                if prices[j] <= prices[i]:\n                    prices[i] -= prices[j]\n                    break\n                else:\n                    continue\n        return prices\n\n    # Time complexity: O(n)\n    # spac ecomplexity: O(n)\n    def monotonicstack(self, prices: List[int]) -> List[int]:\n        n = len(prices)\n        stack = []\n        for i in range(n): # 10 1 1 6\n            while stack and prices[stack[-1]] >= prices[i]: # \n                prices[stack[-1]] -= prices[i] # 9 0 0 0\n                stack.pop()\n            stack.append(i) # stack -> 1\n\n        return prices\n        ",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1475-final-prices-with-a-special-discount-in-a-shop/",
      "datePublished": "2024-03-18T00:00:00Z",
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