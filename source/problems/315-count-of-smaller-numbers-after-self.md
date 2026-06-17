# 315-count-of-smaller-numbers-after-self


Try it on <a href='https://leetcode.com/problems/315-count-of-smaller-numbers-after-self'>leetcode</a>

## Description
<div class="description">
<div><p>You are given an integer array <code>nums</code> and you have to return a new <code>counts</code> array. The <code>counts</code> array has the property where <code>counts[i]</code> is the number of smaller elements to the right of <code>nums[i]</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [5,2,6,1]
<strong>Output:</strong> [2,1,1,0]
<strong>Explanation:</strong>
To the right of 5 there are <b>2</b> smaller elements (2 and 1).
To the right of 2 there is only <b>1</b> smaller element (1).
To the right of 6 there is <b>1</b> smaller element (1).
To the right of 1 there is <b>0</b> smaller element.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [-1]
<strong>Output:</strong> [0]
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [-1,-1]
<strong>Output:</strong> [0,0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class SelfBST:
    def __init__(self, arr, n):
        self.n = n
        self.cntArray = [0] * n

    def cntArr(self):
        return self.cntArray


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        return self.selfBalanceBst(nums)

    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def naive(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    res[i] += 1
        return res

    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
    def selfBalanceBst(self, nums: List[int]) -> List[int]:
        rank, N, res = {val: i + 1 for i,
                        val in enumerate(sorted(nums))}, len(nums), []
        BITree = [0] * (N + 1)

        def update(i):
            while i <= N:
                BITree[i] += 1
                i += i & -i

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= i & -i
            return s

        for x in reversed(nums):
            res += (getSum(rank[x] - 1),)
            update(rank[x])
        return res[::-1]

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "315. Count of Smaller Numbers After Self",
    "text": "You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].\n\u00a0\nExample 1:\nInput: nums = [5,2,6,1]\nOutput: [2,1,1,0]\nExplanation:\nTo the right of 5 there are 2 smaller elements (2 and 1).\nTo the right of 2 there is only 1 smaller element (1).\nTo the right of 6 there is 1 smaller element (1).\nTo the right of 1 there is 0 smaller element.\n\nExample 2:\nInput: nums = [-1]\nOutput: [0]\n\nExample 3:\nInput: nums = [-1,-1]\nOutput: [0,0]\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 105\n-104 <= nums[i] <= 104\n\n",
    "url": "https://leetcode.com/problems/315-count-of-smaller-numbers-after-self",
    "answerCount": 1,
    "datePublished": "2024-03-06T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class SelfBST:\n    def __init__(self, arr, n):\n        self.n = n\n        self.cntArray = [0] * n\n\n    def cntArr(self):\n        return self.cntArray\n\n\nclass Solution:\n    def countSmaller(self, nums: List[int]) -> List[int]:\n        return self.selfBalanceBst(nums)\n\n    # Time Complexity: O(n^2)\n    # Space Complexity: O(n)\n    def naive(self, nums: List[int]) -> List[int]:\n        n = len(nums)\n        res = [0] * n\n        for i in range(n):\n            for j in range(i + 1, n):\n                if nums[j] < nums[i]:\n                    res[i] += 1\n        return res\n\n    # Time Complexity: O(nlogn)\n    # Space Complexity: O(n)\n    def selfBalanceBst(self, nums: List[int]) -> List[int]:\n        rank, N, res = {val: i + 1 for i,\n                        val in enumerate(sorted(nums))}, len(nums), []\n        BITree = [0] * (N + 1)\n\n        def update(i):\n            while i <= N:\n                BITree[i] += 1\n                i += i & -i\n\n        def getSum(i):\n            s = 0\n            while i:\n                s += BITree[i]\n                i -= i & -i\n            return s\n\n        for x in reversed(nums):\n            res += (getSum(rank[x] - 1),)\n            update(rank[x])\n        return res[::-1]\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/315-count-of-smaller-numbers-after-self/",
      "datePublished": "2024-03-06T00:00:00Z",
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