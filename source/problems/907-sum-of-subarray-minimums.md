# 907-sum-of-subarray-minimums


Try it on <a href='https://leetcode.com/problems/907-sum-of-subarray-minimums'>leetcode</a>

## Description
<div class="description">
<div><p>Given an array of integers arr, find the sum of <code>min(b)</code>, where <code>b</code> ranges over every (contiguous) subarray of <code>arr</code>. Since the answer may be large, return the answer <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> arr = [3,1,2,4]
<strong>Output:</strong> 17
<strong>Explanation:</strong> 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> arr = [11,81,94,43,3]
<strong>Output:</strong> 444
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 3 * 10<sup>4</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def __init__(self):
        self.mod = (10**9) + 7

    def sumSubarrayMins(self, arr: List[int]) -> int:
        return self.dp(arr)

    # Time Complexity: O(n^3)
    # Space Complexity: O(1)
    def bruteforce(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0

        for end in range(n):
            for start in range(n):
                min_ = float("-inf")
                for i in range(start, end + 1):
                    min_ = min(min_, arr[i])
                res += min_ & self.mod

        return res

    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def betterbruteforce(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0

        for start in range(n):
            min_ = arr[start]
            for i in range(start, n):
                min_ = min(min_, arr[i])
                res += min_ % self.mod

        return res

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def monotonicstack(self, arr: List[int]) -> int:
        n = len(arr)
        s1 = []
        s2 = []
        left = [None] * n
        right = [None] * n

        for i in range(n):
            cnt = 1

            while len(s1) > 0 and s1[-1][0] > arr[i]:
                cnt += s1[-1][1]
                s1.pop()
            s1.append([arr[i], cnt])
            left[i] = cnt

        for i in range(n - 1, -1, -1):
            cnt = 1

            while len(s2) > 0 and s2[-1][0] >= arr[i]:
                cnt += s2[-1][1]
                s2.pop()
            s2.append([arr[i], cnt])
            right[i] = cnt

        res = 0
        for i in range(n):
            res += (left[i] * right[i] * arr[i]) % self.mod
        return res % self.mod

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def dp(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [0] * n

        st = []

        ans = 0

        for i in range(n - 1, -1, -1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()

            if st:
                dp[i] = dp[st[-1]] + arr[i] * (st[-1] - i)

            else:
                dp[i] = arr[i] * (n - i)

            st.append(i)
            ans += dp[i] % self.mod
        return ans % self.mod

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "907. Sum of Subarray Minimums",
    "text": "Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.\n\u00a0\nExample 1:\nInput: arr = [3,1,2,4]\nOutput: 17\nExplanation: \nSubarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. \nMinimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.\nSum is 17.\n\nExample 2:\nInput: arr = [11,81,94,43,3]\nOutput: 444\n\n\u00a0\nConstraints:\n\n1 <= arr.length <= 3 * 104\n1 <= arr[i] <= 3 * 104\n\n",
    "url": "https://leetcode.com/problems/907-sum-of-subarray-minimums",
    "answerCount": 1,
    "datePublished": "2023-07-07T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def __init__(self):\n        self.mod = (10**9) + 7\n\n    def sumSubarrayMins(self, arr: List[int]) -> int:\n        return self.dp(arr)\n\n    # Time Complexity: O(n^3)\n    # Space Complexity: O(1)\n    def bruteforce(self, arr: List[int]) -> int:\n        n = len(arr)\n        res = 0\n\n        for end in range(n):\n            for start in range(n):\n                min_ = float(\"-inf\")\n                for i in range(start, end + 1):\n                    min_ = min(min_, arr[i])\n                res += min_ & self.mod\n\n        return res\n\n    # Time Complexity: O(n^2)\n    # Space Complexity: O(1)\n    def betterbruteforce(self, arr: List[int]) -> int:\n        n = len(arr)\n        res = 0\n\n        for start in range(n):\n            min_ = arr[start]\n            for i in range(start, n):\n                min_ = min(min_, arr[i])\n                res += min_ % self.mod\n\n        return res\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(n)\n    def monotonicstack(self, arr: List[int]) -> int:\n        n = len(arr)\n        s1 = []\n        s2 = []\n        left = [None] * n\n        right = [None] * n\n\n        for i in range(n):\n            cnt = 1\n\n            while len(s1) > 0 and s1[-1][0] > arr[i]:\n                cnt += s1[-1][1]\n                s1.pop()\n            s1.append([arr[i], cnt])\n            left[i] = cnt\n\n        for i in range(n - 1, -1, -1):\n            cnt = 1\n\n            while len(s2) > 0 and s2[-1][0] >= arr[i]:\n                cnt += s2[-1][1]\n                s2.pop()\n            s2.append([arr[i], cnt])\n            right[i] = cnt\n\n        res = 0\n        for i in range(n):\n            res += (left[i] * right[i] * arr[i]) % self.mod\n        return res % self.mod\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(n)\n    def dp(self, arr: List[int]) -> int:\n        n = len(arr)\n        dp = [0] * n\n\n        st = []\n\n        ans = 0\n\n        for i in range(n - 1, -1, -1):\n            while st and arr[st[-1]] >= arr[i]:\n                st.pop()\n\n            if st:\n                dp[i] = dp[st[-1]] + arr[i] * (st[-1] - i)\n\n            else:\n                dp[i] = arr[i] * (n - i)\n\n            st.append(i)\n            ans += dp[i] % self.mod\n        return ans % self.mod\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/907-sum-of-subarray-minimums/",
      "datePublished": "2023-07-07T00:00:00Z",
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