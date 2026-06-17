# 1695-maximum-erasure-value


Try it on <a href='https://leetcode.com/problems/1695-maximum-erasure-value'>leetcode</a>

## Description
<div class="description">
<div><p>You are given an array of positive integers <code>nums</code> and want to erase a subarray containing&nbsp;<strong>unique elements</strong>. The <strong>score</strong> you get by erasing the subarray is equal to the <strong>sum</strong> of its elements.</p>

<p>Return <em>the <strong>maximum score</strong> you can get by erasing <strong>exactly one</strong> subarray.</em></p>

<p>An array <code>b</code> is called to be a <span class="tex-font-style-it">subarray</span> of <code>a</code> if it forms a contiguous subsequence of <code>a</code>, that is, if it is equal to <code>a[l],a[l+1],...,a[r]</code> for some <code>(l,r)</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [4,2,4,5,6]
<strong>Output:</strong> 17
<strong>Explanation:</strong> The optimal subarray here is [2,4,5,6].
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [5,2,1,2,5,2,1,2,5]
<strong>Output:</strong> 8
<strong>Explanation:</strong> The optimal subarray here is [5,2,1] or [1,2,5].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        return self.optimal(nums)

    # time complexity: O(n^2)
    # Space complexity: O(n)
    def bruteforce(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = 0
        seen = set()
        for i in range(n):
            seen.clear()
            cur_sum = 0

            for j in range(i, n):
                if nums[j] in seen:
                    break
                cur_sum += nums[j]
                seen.add(nums[j])
            max_sum = max(max_sum, cur_sum)
        return max_sum

    # time complexity: O(n)
    # Space complexity: O(n)
    def optimal(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = 0
        cur_sum = 0
        seen = set()
        l = 0
        for num in nums:
            while num in seen:
                seen.remove(nums[l])
                cur_sum -= nums[l]
                l += 1
            cur_sum += num
            seen.add(num)
            max_sum = max(max_sum, cur_sum)
        return max_sum

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1695. Maximum Erasure Value",
    "text": "You are given an array of positive integers nums and want to erase a subarray containing\u00a0unique elements. The score you get by erasing the subarray is equal to the sum of its elements.\nReturn the maximum score you can get by erasing exactly one subarray.\nAn array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).\n\u00a0\nExample 1:\nInput: nums = [4,2,4,5,6]\nOutput: 17\nExplanation: The optimal subarray here is [2,4,5,6].\n\nExample 2:\nInput: nums = [5,2,1,2,5,2,1,2,5]\nOutput: 8\nExplanation: The optimal subarray here is [5,2,1] or [1,2,5].\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 105\n1 <= nums[i] <= 104\n\n",
    "url": "https://leetcode.com/problems/1695-maximum-erasure-value",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def maximumUniqueSubarray(self, nums: List[int]) -> int:\n        return self.optimal(nums)\n\n    # time complexity: O(n^2)\n    # Space complexity: O(n)\n    def bruteforce(self, nums: List[int]) -> int:\n        n = len(nums)\n        max_sum = 0\n        seen = set()\n        for i in range(n):\n            seen.clear()\n            cur_sum = 0\n\n            for j in range(i, n):\n                if nums[j] in seen:\n                    break\n                cur_sum += nums[j]\n                seen.add(nums[j])\n            max_sum = max(max_sum, cur_sum)\n        return max_sum\n\n    # time complexity: O(n)\n    # Space complexity: O(n)\n    def optimal(self, nums: List[int]) -> int:\n        n = len(nums)\n        max_sum = 0\n        cur_sum = 0\n        seen = set()\n        l = 0\n        for num in nums:\n            while num in seen:\n                seen.remove(nums[l])\n                cur_sum -= nums[l]\n                l += 1\n            cur_sum += num\n            seen.add(num)\n            max_sum = max(max_sum, cur_sum)\n        return max_sum\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1695-maximum-erasure-value/",
      "datePublished": "2025-12-22",
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