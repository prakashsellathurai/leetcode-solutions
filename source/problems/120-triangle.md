# 120-triangle


Try it on <a href='https://leetcode.com/problems/120-triangle'>leetcode</a>

## Description
<div class="description">
<div><p>Given a <code>triangle</code> array, return <em>the minimum path sum from top to bottom</em>.</p>

<p>For each step, you may move to an adjacent number of the row below. More formally, if you are on index <code>i</code> on the current row, you may move to either index <code>i</code> or index <code>i + 1</code> on the next row.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
<strong>Output:</strong> 11
<strong>Explanation:</strong> The triangle looks like:
   <u>2</u>
  <u>3</u> 4
 6 <u>5</u> 7
4 <u>1</u> 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> triangle = [[-10]]
<strong>Output:</strong> -10
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= triangle.length &lt;= 200</code></li>
	<li><code>triangle[0].length == 1</code></li>
	<li><code>triangle[i].length == triangle[i - 1].length + 1</code></li>
	<li><code>-10<sup>4</sup> &lt;= triangle[i][j] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you&nbsp;do this using only <code>O(n)</code> extra space, where <code>n</code> is the total number of rows in the triangle?</div>
</div>

## Solution(Python)
```Python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.bottomupdplessspace(triangle)

    # Time complexity: O(2^n)
    # space Complexity: O(n)
    def bruteforce(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        min_sum = 0

        def dfs(i, j, sum_so_far):
            if i == n:
                return sum_so_far

            return min(
                dfs(i + 1, j, sum_so_far + triangle[i][j]),
                dfs(i + 1, j + 1, sum_so_far + triangle[i][j]),
            )

        return dfs(0, 0, 0)

    # Time complexity: O(n^2)
    # space Complexity: O(n^2)
    def topdowndp(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        @cache
        def dfs(i, j):
            if i == n - 1:
                return triangle[i][j]

            return triangle[i][j] + min(dfs(i + 1, j), dfs(i + 1, j + 1))

        return dfs(0, 0)

    # Time complexity: O(n^2)
    # space Complexity: O(n^2)
    def bottomupdp(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[float("inf")] * (i) for i in range(1, n + 1)]
        dp[n - 1] = triangle[n - 1]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
        return dp[0][0]

    # Time complexity: O(n^2)
    # space Complexity: O(n)
    def bottomupdplessspace(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        if not n:
            return 0

        if n == 1:
            return triangle[0][0]

        dp = [float("inf")] * (n - 1)
        prev_state = triangle[n - 1]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(prev_state[j], prev_state[j + 1])
            prev_state = dp

        return dp[0]

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "120. Triangle",
    "text": "Given a triangle array, return the minimum path sum from top to bottom.\nFor each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.\n\u00a0\nExample 1:\nInput: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]\nOutput: 11\nExplanation: The triangle looks like:\n   2\n  3 4\n 6 5 7\n4 1 8 3\nThe minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).\n\nExample 2:\nInput: triangle = [[-10]]\nOutput: -10\n\n\u00a0\nConstraints:\n\n1 <= triangle.length <= 200\ntriangle[0].length == 1\ntriangle[i].length == triangle[i - 1].length + 1\n-104 <= triangle[i][j] <= 104\n\n\u00a0\nFollow up: Could you\u00a0do this using only O(n) extra space, where n is the total number of rows in the triangle?",
    "url": "https://leetcode.com/problems/120-triangle",
    "answerCount": 1,
    "datePublished": "2022-02-16T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def minimumTotal(self, triangle: List[List[int]]) -> int:\n        return self.bottomupdplessspace(triangle)\n\n    # Time complexity: O(2^n)\n    # space Complexity: O(n)\n    def bruteforce(self, triangle: List[List[int]]) -> int:\n        n = len(triangle)\n\n        min_sum = 0\n\n        def dfs(i, j, sum_so_far):\n            if i == n:\n                return sum_so_far\n\n            return min(\n                dfs(i + 1, j, sum_so_far + triangle[i][j]),\n                dfs(i + 1, j + 1, sum_so_far + triangle[i][j]),\n            )\n\n        return dfs(0, 0, 0)\n\n    # Time complexity: O(n^2)\n    # space Complexity: O(n^2)\n    def topdowndp(self, triangle: List[List[int]]) -> int:\n        n = len(triangle)\n\n        @cache\n        def dfs(i, j):\n            if i == n - 1:\n                return triangle[i][j]\n\n            return triangle[i][j] + min(dfs(i + 1, j), dfs(i + 1, j + 1))\n\n        return dfs(0, 0)\n\n    # Time complexity: O(n^2)\n    # space Complexity: O(n^2)\n    def bottomupdp(self, triangle: List[List[int]]) -> int:\n        n = len(triangle)\n        dp = [[float(\"inf\")] * (i) for i in range(1, n + 1)]\n        dp[n - 1] = triangle[n - 1]\n        for i in range(n - 2, -1, -1):\n            for j in range(i + 1):\n                dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])\n        return dp[0][0]\n\n    # Time complexity: O(n^2)\n    # space Complexity: O(n)\n    def bottomupdplessspace(self, triangle: List[List[int]]) -> int:\n        n = len(triangle)\n\n        if not n:\n            return 0\n\n        if n == 1:\n            return triangle[0][0]\n\n        dp = [float(\"inf\")] * (n - 1)\n        prev_state = triangle[n - 1]\n\n        for i in range(n - 2, -1, -1):\n            for j in range(i + 1):\n                dp[j] = triangle[i][j] + min(prev_state[j], prev_state[j + 1])\n            prev_state = dp\n\n        return dp[0]\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/120-triangle/",
      "datePublished": "2022-02-16T00:00:00Z",
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