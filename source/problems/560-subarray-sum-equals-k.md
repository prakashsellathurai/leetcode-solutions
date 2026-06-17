# 560-subarray-sum-equals-k


Try it on <a href='https://leetcode.com/problems/560-subarray-sum-equals-k'>leetcode</a>

## Description
<div class="description">
<div>
  

</div>

## Solution(Python)
```Python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        return self.hashingCumulativeSumFrequecny(nums, k)

    """
    Time Complexity: O(n^3)
    Space Complexity: O(1)
    """

    def bruteforce(self, nums: List[int], k: int) -> int:
        cnt = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i: j + 1]) == k:
                    cnt += 1

        return cnt

    """
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """

    def CumulativeSum(self, nums: List[int], k: int) -> int:
        cnt = 0
        n = len(nums)
        CumSum = [0] * (n + 1)
        CumSum[0] = 0
        for i in range(1, n + 1):
            CumSum[i] = CumSum[i - 1] + nums[i - 1]

        for i in range(n):
            for j in range(i + 1, len(nums) + 1):
                if CumSum[j] - CumSum[i] == k:
                    cnt += 1
        return cnt

    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    def ConsecutiveSumOnthefly(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = 0

        for i in range(n):
            curSum = 0
            for j in range(i, n):
                curSum += nums[j]
                if curSum == k:
                    cnt += 1

        return cnt

    """
    Time Complexity: O(n)
    Space Complexity: O(n) 
    """

    def hashingCumulativeSumFrequecny(self, nums: List[int], k: int) -> int:
        n = len(nums)

        CumSum = 0
        CumSumFreq = defaultdict(lambda: 0)
        CumSumFreq[0] = 1  # by default sum with 0 is always going to  be there
        cnt = 0

        for i in range(n):
            CumSum += nums[i]
            if CumSum - k in CumSumFreq:
                cnt += CumSumFreq[CumSum - k]
            CumSumFreq[CumSum] += 1

        return cnt

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "560. Subarray Sum Equals K",
    "text": "\n",
    "url": "https://leetcode.com/problems/560-subarray-sum-equals-k",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def subarraySum(self, nums: List[int], k: int) -> int:\n        return self.hashingCumulativeSumFrequecny(nums, k)\n\n    \"\"\"\n    Time Complexity: O(n^3)\n    Space Complexity: O(1)\n    \"\"\"\n\n    def bruteforce(self, nums: List[int], k: int) -> int:\n        cnt = 0\n\n        for i in range(len(nums)):\n            for j in range(i, len(nums)):\n                if sum(nums[i: j + 1]) == k:\n                    cnt += 1\n\n        return cnt\n\n    \"\"\"\n    Time Complexity: O(n^2)\n    Space Complexity: O(n)\n    \"\"\"\n\n    def CumulativeSum(self, nums: List[int], k: int) -> int:\n        cnt = 0\n        n = len(nums)\n        CumSum = [0] * (n + 1)\n        CumSum[0] = 0\n        for i in range(1, n + 1):\n            CumSum[i] = CumSum[i - 1] + nums[i - 1]\n\n        for i in range(n):\n            for j in range(i + 1, len(nums) + 1):\n                if CumSum[j] - CumSum[i] == k:\n                    cnt += 1\n        return cnt\n\n    \"\"\"\n    Time Complexity: O(n^2)\n    Space Complexity: O(1)\n    \"\"\"\n\n    def ConsecutiveSumOnthefly(self, nums: List[int], k: int) -> int:\n        n = len(nums)\n        cnt = 0\n\n        for i in range(n):\n            curSum = 0\n            for j in range(i, n):\n                curSum += nums[j]\n                if curSum == k:\n                    cnt += 1\n\n        return cnt\n\n    \"\"\"\n    Time Complexity: O(n)\n    Space Complexity: O(n) \n    \"\"\"\n\n    def hashingCumulativeSumFrequecny(self, nums: List[int], k: int) -> int:\n        n = len(nums)\n\n        CumSum = 0\n        CumSumFreq = defaultdict(lambda: 0)\n        CumSumFreq[0] = 1  # by default sum with 0 is always going to  be there\n        cnt = 0\n\n        for i in range(n):\n            CumSum += nums[i]\n            if CumSum - k in CumSumFreq:\n                cnt += CumSumFreq[CumSum - k]\n            CumSumFreq[CumSum] += 1\n\n        return cnt\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/560-subarray-sum-equals-k/",
      "datePublished": "2025-08-23",
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