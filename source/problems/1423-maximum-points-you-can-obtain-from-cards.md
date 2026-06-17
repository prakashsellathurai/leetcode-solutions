# 1423-maximum-points-you-can-obtain-from-cards


Try it on <a href='https://leetcode.com/problems/1423-maximum-points-you-can-obtain-from-cards'>leetcode</a>

## Description
<div class="description">
<div><p>There are several cards <strong>arranged in a row</strong>, and each card has an associated number of points. The points are given in the integer array <code>cardPoints</code>.</p>

<p>In one step, you can take one card from the beginning or from the end of the row. You have to take exactly <code>k</code> cards.</p>

<p>Your score is the sum of the points of the cards you have taken.</p>

<p>Given the integer array <code>cardPoints</code> and the integer <code>k</code>, return the <em>maximum score</em> you can obtain.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> cardPoints = [1,2,3,4,5,6,1], k = 3
<strong>Output:</strong> 12
<strong>Explanation:</strong> After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> cardPoints = [2,2,2], k = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> Regardless of which two cards you take, your score will always be 4.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> cardPoints = [9,7,7,9,7,7,9], k = 7
<strong>Output:</strong> 55
<strong>Explanation:</strong> You have to take all the cards. Your score is the sum of points of all cards.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= cardPoints.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= cardPoints[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= k &lt;= cardPoints.length</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        max_sum = cur_sum = sum(cardPoints[: n - k])
        total_sum = cur_sum
        for i in range(n - k, n):
            cur_sum += cardPoints[i] - cardPoints[i - (n - k)]
            total_sum += cardPoints[i]
            max_sum = min(max_sum, cur_sum)
        return total_sum - max_sum

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1423. Maximum Points You Can Obtain from Cards",
    "text": "There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.\nIn one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.\nYour score is the sum of the points of the cards you have taken.\nGiven the integer array cardPoints and the integer k, return the maximum score you can obtain.\n\u00a0\nExample 1:\nInput: cardPoints = [1,2,3,4,5,6,1], k = 3\nOutput: 12\nExplanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.\n\nExample 2:\nInput: cardPoints = [2,2,2], k = 2\nOutput: 4\nExplanation: Regardless of which two cards you take, your score will always be 4.\n\nExample 3:\nInput: cardPoints = [9,7,7,9,7,7,9], k = 7\nOutput: 55\nExplanation: You have to take all the cards. Your score is the sum of points of all cards.\n\n\u00a0\nConstraints:\n\n1 <= cardPoints.length <= 105\n1 <= cardPoints[i] <= 104\n1 <= k <= cardPoints.length\n\n",
    "url": "https://leetcode.com/problems/1423-maximum-points-you-can-obtain-from-cards",
    "answerCount": 1,
    "datePublished": "2023-10-09T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def maxScore(self, cardPoints: List[int], k: int) -> int:\n        n = len(cardPoints)\n        max_sum = cur_sum = sum(cardPoints[: n - k])\n        total_sum = cur_sum\n        for i in range(n - k, n):\n            cur_sum += cardPoints[i] - cardPoints[i - (n - k)]\n            total_sum += cardPoints[i]\n            max_sum = min(max_sum, cur_sum)\n        return total_sum - max_sum\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1423-maximum-points-you-can-obtain-from-cards/",
      "datePublished": "2023-10-09T00:00:00Z",
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