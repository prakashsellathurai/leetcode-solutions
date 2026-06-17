# 216-combination-sum-iii


Try it on <a href='https://leetcode.com/problems/216-combination-sum-iii'>leetcode</a>

## Description
<div class="description">
<div><p>Find all valid combinations of <code>k</code> numbers that sum up to <code>n</code> such that the following conditions are true:</p>

<ul>
	<li>Only numbers <code>1</code> through <code>9</code> are used.</li>
	<li>Each number is used <strong>at most once</strong>.</li>
</ul>

<p>Return <em>a list of all possible valid combinations</em>. The list must not contain the same combination twice, and the combinations may be returned in any order.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> k = 3, n = 7
<strong>Output:</strong> [[1,2,4]]
<strong>Explanation:</strong>
1 + 2 + 4 = 7
There are no other valid combinations.</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> k = 3, n = 9
<strong>Output:</strong> [[1,2,6],[1,3,5],[2,3,4]]
<strong>Explanation:</strong>
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> k = 4, n = 1
<strong>Output:</strong> []
<strong>Explanation:</strong> There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 &gt; 1, there are no valid combination.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= k &lt;= 9</code></li>
	<li><code>1 &lt;= n &lt;= 60</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return self.backtrack(k, n)

    def backtrack(self, k: int, n: int) -> List[List[int]]:
        res = []

        def recur(candidate, i, sum_so_far):
            if sum_so_far == n and len(candidate) == k:
                res.append(candidate[:])

            for j in range(i, 10):
                if len(candidate) > k:
                    continue

                if sum_so_far + j > n:
                    continue

                candidate.append(j)
                sum_so_far += j
                recur(candidate, j + 1, sum_so_far)
                sum_so_far -= j
                candidate.pop()

        recur([], 1, 0)
        return res

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "216. Combination Sum III",
    "text": "Find all valid combinations of k numbers that sum up to n such that the following conditions are true:\n\nOnly numbers 1 through 9 are used.\nEach number is used at most once.\n\nReturn a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.\n\u00a0\nExample 1:\nInput: k = 3, n = 7\nOutput: [[1,2,4]]\nExplanation:\n1 + 2 + 4 = 7\nThere are no other valid combinations.\nExample 2:\nInput: k = 3, n = 9\nOutput: [[1,2,6],[1,3,5],[2,3,4]]\nExplanation:\n1 + 2 + 6 = 9\n1 + 3 + 5 = 9\n2 + 3 + 4 = 9\nThere are no other valid combinations.\n\nExample 3:\nInput: k = 4, n = 1\nOutput: []\nExplanation: There are no valid combinations.\nUsing 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.\n\n\u00a0\nConstraints:\n\n2 <= k <= 9\n1 <= n <= 60\n\n",
    "url": "https://leetcode.com/problems/216-combination-sum-iii",
    "answerCount": 1,
    "datePublished": "2024-08-07T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def combinationSum3(self, k: int, n: int) -> List[List[int]]:\n        return self.backtrack(k, n)\n\n    def backtrack(self, k: int, n: int) -> List[List[int]]:\n        res = []\n\n        def recur(candidate, i, sum_so_far):\n            if sum_so_far == n and len(candidate) == k:\n                res.append(candidate[:])\n\n            for j in range(i, 10):\n                if len(candidate) > k:\n                    continue\n\n                if sum_so_far + j > n:\n                    continue\n\n                candidate.append(j)\n                sum_so_far += j\n                recur(candidate, j + 1, sum_so_far)\n                sum_so_far -= j\n                candidate.pop()\n\n        recur([], 1, 0)\n        return res\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/216-combination-sum-iii/",
      "datePublished": "2024-08-07T00:00:00Z",
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