# 746-min-cost-climbing-stairs


Try it on <a href='https://leetcode.com/problems/746-min-cost-climbing-stairs'>leetcode</a>

## Description
<div class="description">

</div>

## Solution(Python)
```Python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.optimal(cost)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def topdown(self, cost: List[int]) -> int:
        n = len(cost)

        @cache
        def dfs(i):
            if i >= n:
                return 0
            if i == -1:
                return min(dfs(i + 1), dfs(i + 2))
            return cost[i] + min(dfs(i + 1), dfs(i + 2))

        return dfs(-1)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def bottomup(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n)
        dp[n - 1] = cost[n - 1]
        dp[n - 2] = min(cost[n - 2] + dp[n - 1], cost[n - 2])
        for i in range(n - 3, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        return min(dp[0], dp[1])

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def optimal(self, cost: List[int]) -> int:
        n = len(cost)
        prev2 = cost[n - 1]
        prev1 = min(cost[n - 2] + prev2, cost[n - 2])
        for i in range(n - 3, -1, -1):
            cur = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = cur
        return min(prev1, prev2)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "746-min-cost-climbing-stairs",
    "text": "",
    "url": "https://leetcode.com/problems/746-min-cost-climbing-stairs",
    "answerCount": 1,
    "datePublished": "2022-07-10T12:35:00+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def minCostClimbingStairs(self, cost: List[int]) -> int:\n        return self.optimal(cost)\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(n)\n    def topdown(self, cost: List[int]) -> int:\n        n = len(cost)\n\n        @cache\n        def dfs(i):\n            if i >= n:\n                return 0\n            if i == -1:\n                return min(dfs(i + 1), dfs(i + 2))\n            return cost[i] + min(dfs(i + 1), dfs(i + 2))\n\n        return dfs(-1)\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(n)\n    def bottomup(self, cost: List[int]) -> int:\n        n = len(cost)\n        dp = [0] * (n)\n        dp[n - 1] = cost[n - 1]\n        dp[n - 2] = min(cost[n - 2] + dp[n - 1], cost[n - 2])\n        for i in range(n - 3, -1, -1):\n            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])\n        return min(dp[0], dp[1])\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(1)\n    def optimal(self, cost: List[int]) -> int:\n        n = len(cost)\n        prev2 = cost[n - 1]\n        prev1 = min(cost[n - 2] + prev2, cost[n - 2])\n        for i in range(n - 3, -1, -1):\n            cur = cost[i] + min(prev1, prev2)\n            prev2 = prev1\n            prev1 = cur\n        return min(prev1, prev2)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/746-min-cost-climbing-stairs/",
      "datePublished": "2022-07-10T12:35:00+05:30",
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