# 823-binary-trees-with-factors


Try it on <a href='https://leetcode.com/problems/823-binary-trees-with-factors'>leetcode</a>

## Description
<div class="description">
<div><p>Given an array of unique integers, <code>arr</code>, where each integer <code>arr[i]</code> is strictly greater than <code>1</code>.</p>

<p>We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.</p>

<p>Return <em>the number of binary trees we can make</em>. The answer may be too large so return the answer <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> arr = [2,4]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can make these trees: <code>[2], [4], [4, 2, 2]</code></pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> arr = [2,4,5,10]
<strong>Output:</strong> 7
<strong>Explanation:</strong> We can make these trees: <code>[2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2]</code>.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 1000</code></li>
	<li><code>2 &lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
	<li>All the values of <code>arr</code> are <strong>unique</strong>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution(object):
    def numFactoredBinaryTrees(self, A):
        MOD = 10**9 + 7
        N = len(A)
        A.sort()
        dp = [1] * N
        index = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for j in range(i):
                if x % A[j] == 0:  # A[j] will be left child
                    right = x / A[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= MOD

        return sum(dp) % MOD

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "823. Binary Trees With Factors",
    "text": "Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.\nWe make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.\nReturn the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.\n\u00a0\nExample 1:\nInput: arr = [2,4]\nOutput: 3\nExplanation: We can make these trees: [2], [4], [4, 2, 2]\nExample 2:\nInput: arr = [2,4,5,10]\nOutput: 7\nExplanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].\n\u00a0\nConstraints:\n\n1 <= arr.length <= 1000\n2 <= arr[i] <= 109\nAll the values of arr are unique.\n\n",
    "url": "https://leetcode.com/problems/823-binary-trees-with-factors",
    "answerCount": 1,
    "datePublished": "2022-08-09T21:21:26+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution(object):\n    def numFactoredBinaryTrees(self, A):\n        MOD = 10**9 + 7\n        N = len(A)\n        A.sort()\n        dp = [1] * N\n        index = {x: i for i, x in enumerate(A)}\n        for i, x in enumerate(A):\n            for j in range(i):\n                if x % A[j] == 0:  # A[j] will be left child\n                    right = x / A[j]\n                    if right in index:\n                        dp[i] += dp[j] * dp[index[right]]\n                        dp[i] %= MOD\n\n        return sum(dp) % MOD\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/823-binary-trees-with-factors/",
      "datePublished": "2022-08-09T21:21:26+05:30",
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