# 905-sort-array-by-parity


Try it on <a href='https://leetcode.com/problems/905-sort-array-by-parity'>leetcode</a>

## Description
<div class="description">
<div><p>Given an integer array <code>nums</code>, move all the even integers at the beginning of the array followed by all the odd integers.</p>

<p>Return <em><strong>any array</strong> that satisfies this condition</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [3,1,2,4]
<strong>Output:</strong> [2,4,3,1]
<strong>Explanation:</strong> The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 5000</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return self.inPlace(nums)

    # Time Complexity: O(NlogN)
    # Space Complexity: O(N)
    def sorting(self, nums):
        nums.sort(key=lambda x: x % 2)
        return nums

    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def twopass(self, nums):
        return [x for x in nums if not x % 2] + [x for x in nums if x % 2]

    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def inPlace(self, nums):
        i, j = 0, len(nums) - 1
        while i < j:
            i_par = nums[i] % 2
            j_par = nums[j] % 2

            if i_par and not j_par:
                nums[i], nums[j] = nums[j], nums[i]

            if not i_par:
                i += 1
            if j_par:
                j -= 1

        return nums

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "905. Sort Array By Parity",
    "text": "Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.\nReturn any array that satisfies this condition.\n\u00a0\nExample 1:\nInput: nums = [3,1,2,4]\nOutput: [2,4,3,1]\nExplanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.\n\nExample 2:\nInput: nums = [0]\nOutput: [0]\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 5000\n0 <= nums[i] <= 5000\n\n",
    "url": "https://leetcode.com/problems/905-sort-array-by-parity",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def sortArrayByParity(self, nums: List[int]) -> List[int]:\n        return self.inPlace(nums)\n\n    # Time Complexity: O(NlogN)\n    # Space Complexity: O(N)\n    def sorting(self, nums):\n        nums.sort(key=lambda x: x % 2)\n        return nums\n\n    # Time Complexity: O(N)\n    # Space Complexity: O(N)\n    def twopass(self, nums):\n        return [x for x in nums if not x % 2] + [x for x in nums if x % 2]\n\n    # Time Complexity: O(N)\n    # Space Complexity: O(1)\n    def inPlace(self, nums):\n        i, j = 0, len(nums) - 1\n        while i < j:\n            i_par = nums[i] % 2\n            j_par = nums[j] % 2\n\n            if i_par and not j_par:\n                nums[i], nums[j] = nums[j], nums[i]\n\n            if not i_par:\n                i += 1\n            if j_par:\n                j -= 1\n\n        return nums\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/905-sort-array-by-parity/",
      "datePublished": "2022-12-22",
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