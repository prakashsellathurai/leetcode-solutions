# 2279-maximum-bags-with-full-capacity-of-rocks


Try it on <a href='https://leetcode.com/problems/2279-maximum-bags-with-full-capacity-of-rocks'>leetcode</a>

## Description
<div class="description">
<div><p>You have <code>n</code> bags numbered from <code>0</code> to <code>n - 1</code>. You are given two <strong>0-indexed</strong> integer arrays <code>capacity</code> and <code>rocks</code>. The <code>i<sup>th</sup></code> bag can hold a maximum of <code>capacity[i]</code> rocks and currently contains <code>rocks[i]</code> rocks. You are also given an integer <code>additionalRocks</code>, the number of additional rocks you can place in <strong>any</strong> of the bags.</p>

<p>Return<em> the <strong>maximum</strong> number of bags that could have full capacity after placing the additional rocks in some bags.</em></p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong>
Place 1 rock in bag 0 and 1 rock in bag 1.
The number of rocks in each bag are now [2,3,4,4].
Bags 0, 1, and 2 have full capacity.
There are 3 bags at full capacity, so we return 3.
It can be shown that it is not possible to have more than 3 bags at full capacity.
Note that there may be other ways of placing the rocks that result in an answer of 3.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> capacity = [10,2,2], rocks = [2,2,0], additionalRocks = 100
<strong>Output:</strong> 3
<strong>Explanation:</strong>
Place 8 rocks in bag 0 and 2 rocks in bag 2.
The number of rocks in each bag are now [10,2,2].
Bags 0, 1, and 2 have full capacity.
There are 3 bags at full capacity, so we return 3.
It can be shown that it is not possible to have more than 3 bags at full capacity.
Note that we did not use all of the additional rocks.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == capacity.length == rocks.length</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= capacity[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= rocks[i] &lt;= capacity[i]</code></li>
	<li><code>1 &lt;= additionalRocks &lt;= 10<sup>9</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def maximumBags(self, capacity, rocks, x):
        count = sorted(c - r for c,r in zip(capacity, rocks))[::-1]
        cnt = 0
        while count and x and count[-1] <= x:
            x -= count.pop()
            cnt += 1
        return cnt
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "2279. Maximum Bags With Full Capacity of Rocks",
    "text": "You have n bags numbered from 0 to n - 1. You are given two 0-indexed integer arrays capacity and rocks. The ith bag can hold a maximum of capacity[i] rocks and currently contains rocks[i] rocks. You are also given an integer additionalRocks, the number of additional rocks you can place in any of the bags.\nReturn the maximum number of bags that could have full capacity after placing the additional rocks in some bags.\n\u00a0\nExample 1:\nInput: capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2\nOutput: 3\nExplanation:\nPlace 1 rock in bag 0 and 1 rock in bag 1.\nThe number of rocks in each bag are now [2,3,4,4].\nBags 0, 1, and 2 have full capacity.\nThere are 3 bags at full capacity, so we return 3.\nIt can be shown that it is not possible to have more than 3 bags at full capacity.\nNote that there may be other ways of placing the rocks that result in an answer of 3.\n\nExample 2:\nInput: capacity = [10,2,2], rocks = [2,2,0], additionalRocks = 100\nOutput: 3\nExplanation:\nPlace 8 rocks in bag 0 and 2 rocks in bag 2.\nThe number of rocks in each bag are now [10,2,2].\nBags 0, 1, and 2 have full capacity.\nThere are 3 bags at full capacity, so we return 3.\nIt can be shown that it is not possible to have more than 3 bags at full capacity.\nNote that we did not use all of the additional rocks.\n\n\u00a0\nConstraints:\n\nn == capacity.length == rocks.length\n1 <= n <= 5 * 104\n1 <= capacity[i] <= 109\n0 <= rocks[i] <= capacity[i]\n1 <= additionalRocks <= 109\n\n",
    "url": "https://leetcode.com/problems/2279-maximum-bags-with-full-capacity-of-rocks",
    "answerCount": 1,
    "datePublished": "2022-07-04T20:30:27+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def maximumBags(self, capacity, rocks, x):\n        count = sorted(c - r for c,r in zip(capacity, rocks))[::-1]\n        cnt = 0\n        while count and x and count[-1] <= x:\n            x -= count.pop()\n            cnt += 1\n        return cnt",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/2279-maximum-bags-with-full-capacity-of-rocks/",
      "datePublished": "2022-07-04T20:30:27+05:30",
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