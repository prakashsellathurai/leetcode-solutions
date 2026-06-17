# 46-permutations


Try it on <a href='https://leetcode.com/problems/46-permutations'>leetcode</a>

## Description
<div class="description">
<div><p>Given an array <code>nums</code> of distinct integers, return <em>all the possible permutations</em>. You can return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> [[0,1],[1,0]]
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> [[1]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 6</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li>All the integers of <code>nums</code> are <strong>unique</strong>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    #     def permute(self, nums: List[int]) -> List[List[int]]:
    #         res = []

    #         def backtrack(nums,k):
    #             if k == len(nums):
    #                 res.append(nums[:])
    #                 return

    #             for i in range(k,len(nums)):
    #                 nums[i],nums[k] = nums[k],nums[i]
    #                 backtrack(nums,k+1)
    #                 nums[k],nums[i] = nums[i],nums[k]

    #         backtrack(nums,0)

    #         return res
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        times = 1
        for i in range(1, n + 1):
            times *= i

        for i in range(1, times + 1):
            nums = self.nextperm(nums)
            res.append(nums[:])
        return res

    def nextperm(self, nums: List[int]) -> List[int]:
        n = len(nums)

        i = n - 2

        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1

        if i >= 0:
            j = n - 1

            while j >= 0 and nums[i] >= nums[j]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        # reverse from i+1

        s = i + 1
        e = n - 1

        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1

        return nums

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "46. Permutations",
    "text": "Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.\n\u00a0\nExample 1:\nInput: nums = [1,2,3]\nOutput: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]\nExample 2:\nInput: nums = [0,1]\nOutput: [[0,1],[1,0]]\nExample 3:\nInput: nums = [1]\nOutput: [[1]]\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 6\n-10 <= nums[i] <= 10\nAll the integers of nums are unique.\n\n",
    "url": "https://leetcode.com/problems/46-permutations",
    "answerCount": 1,
    "datePublished": "2023-01-11T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    #     def permute(self, nums: List[int]) -> List[List[int]]:\n    #         res = []\n\n    #         def backtrack(nums,k):\n    #             if k == len(nums):\n    #                 res.append(nums[:])\n    #                 return\n\n    #             for i in range(k,len(nums)):\n    #                 nums[i],nums[k] = nums[k],nums[i]\n    #                 backtrack(nums,k+1)\n    #                 nums[k],nums[i] = nums[i],nums[k]\n\n    #         backtrack(nums,0)\n\n    #         return res\n    def permute(self, nums: List[int]) -> List[List[int]]:\n        res = []\n        n = len(nums)\n\n        times = 1\n        for i in range(1, n + 1):\n            times *= i\n\n        for i in range(1, times + 1):\n            nums = self.nextperm(nums)\n            res.append(nums[:])\n        return res\n\n    def nextperm(self, nums: List[int]) -> List[int]:\n        n = len(nums)\n\n        i = n - 2\n\n        while i >= 0 and nums[i + 1] <= nums[i]:\n            i -= 1\n\n        if i >= 0:\n            j = n - 1\n\n            while j >= 0 and nums[i] >= nums[j]:\n                j -= 1\n\n            nums[i], nums[j] = nums[j], nums[i]\n\n        # reverse from i+1\n\n        s = i + 1\n        e = n - 1\n\n        while s < e:\n            nums[s], nums[e] = nums[e], nums[s]\n            s += 1\n            e -= 1\n\n        return nums\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/46-permutations/",
      "datePublished": "2023-01-11T00:00:00Z",
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