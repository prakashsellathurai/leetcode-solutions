# 581-shortest-unsorted-continuous-subarray


Try it on <a href='https://leetcode.com/problems/581-shortest-unsorted-continuous-subarray'>leetcode</a>

## Description
<div class="description">
<div><p>Given an integer array <code>nums</code>, you need to find one <b>continuous subarray</b> that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.</p>

<p>Return <em>the shortest such subarray and output its length</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [2,6,4,8,10,9,15]
<strong>Output:</strong> 5
<strong>Explanation:</strong> You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> 0
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Can you solve it in <code>O(n)</code> time complexity?</div>
</div>

## Solution(Python)
```Python
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        return self.stacklesspace(nums)

    # Time Complexity: O(n^2)
    # Space Comeplxity: O(1)
    def bruteforce(self, nums):
        n = len(nums)
        l = n
        r = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    r = max(r, j)
                    l = min(l, i)
        return 0 if r - l < 0 else r - l + 1

    # Time Complexity: O(nlogn)
    # Space Comeplxity: O(n)
    def sorting(self, nums):
        n = len(nums)
        temp = nums.copy()
        temp.sort()
        l = n
        r = 0
        for i in range(n):
            if temp[i] != nums[i]:
                r = max(r, i)
                l = min(l, i)
        return r - l + 1 if r - l > 0 else 0

    # Time Complexity: O(n)
    # Space Comeplxity: O(n)
    def stack(self, nums):
        stack = []
        n = len(nums)
        l = n
        r = 0
        for i in range(n - 1):
            while stack and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)

        stack.clear()
        for j in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[j]:
                r = max(r, stack.pop())
            stack.append(j)
        return r - l + 1 if r - l > 0 else 0

    # Time Complexity: O(n)
    # Space Comeplxity: O(1)
    def stacklesspace(self, nums):
        n = len(nums)

        max_seen = float("-inf")
        end = 0
        for i in range(n):
            max_seen = max(max_seen, nums[i])
            if nums[i] < max_seen:
                end = i
        min_seen = float("inf")
        start = 0
        for i in reversed(range(n)):
            min_seen = min(min_seen, nums[i])
            if nums[i] > min_seen:
                start = i

        if end > 0:
            return end - start + 1
        else:
            return 0

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "581. Shortest Unsorted Continuous Subarray",
    "text": "Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.\nReturn the shortest such subarray and output its length.\n\u00a0\nExample 1:\nInput: nums = [2,6,4,8,10,9,15]\nOutput: 5\nExplanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.\n\nExample 2:\nInput: nums = [1,2,3,4]\nOutput: 0\n\nExample 3:\nInput: nums = [1]\nOutput: 0\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 104\n-105 <= nums[i] <= 105\n\n\u00a0\nFollow up: Can you solve it in O(n) time complexity?",
    "url": "https://leetcode.com/problems/581-shortest-unsorted-continuous-subarray",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def findUnsortedSubarray(self, nums: List[int]) -> int:\n        return self.stacklesspace(nums)\n\n    # Time Complexity: O(n^2)\n    # Space Comeplxity: O(1)\n    def bruteforce(self, nums):\n        n = len(nums)\n        l = n\n        r = 0\n        for i in range(n):\n            for j in range(i + 1, n):\n                if nums[j] < nums[i]:\n                    r = max(r, j)\n                    l = min(l, i)\n        return 0 if r - l < 0 else r - l + 1\n\n    # Time Complexity: O(nlogn)\n    # Space Comeplxity: O(n)\n    def sorting(self, nums):\n        n = len(nums)\n        temp = nums.copy()\n        temp.sort()\n        l = n\n        r = 0\n        for i in range(n):\n            if temp[i] != nums[i]:\n                r = max(r, i)\n                l = min(l, i)\n        return r - l + 1 if r - l > 0 else 0\n\n    # Time Complexity: O(n)\n    # Space Comeplxity: O(n)\n    def stack(self, nums):\n        stack = []\n        n = len(nums)\n        l = n\n        r = 0\n        for i in range(n - 1):\n            while stack and nums[stack[-1]] > nums[i]:\n                l = min(l, stack.pop())\n            stack.append(i)\n\n        stack.clear()\n        for j in range(n - 1, -1, -1):\n            while stack and nums[stack[-1]] < nums[j]:\n                r = max(r, stack.pop())\n            stack.append(j)\n        return r - l + 1 if r - l > 0 else 0\n\n    # Time Complexity: O(n)\n    # Space Comeplxity: O(1)\n    def stacklesspace(self, nums):\n        n = len(nums)\n\n        max_seen = float(\"-inf\")\n        end = 0\n        for i in range(n):\n            max_seen = max(max_seen, nums[i])\n            if nums[i] < max_seen:\n                end = i\n        min_seen = float(\"inf\")\n        start = 0\n        for i in reversed(range(n)):\n            min_seen = min(min_seen, nums[i])\n            if nums[i] > min_seen:\n                start = i\n\n        if end > 0:\n            return end - start + 1\n        else:\n            return 0\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/581-shortest-unsorted-continuous-subarray/",
      "datePublished": "2023-12-12",
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