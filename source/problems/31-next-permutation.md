# 31-next-permutation


Try it on <a href='https://leetcode.com/problems/31-next-permutation'>leetcode</a>

## Description
<div class="description">
<div><p>A <strong>permutation</strong> of an array of integers is an arrangement of its members into a sequence or linear order.</p>

<ul>
	<li>For example, for <code>arr = [1,2,3]</code>, the following are considered permutations of <code>arr</code>: <code>[1,2,3]</code>, <code>[1,3,2]</code>, <code>[3,1,2]</code>, <code>[2,3,1]</code>.</li>
</ul>

<p>The <strong>next permutation</strong> of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the <strong>next permutation</strong> of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).</p>

<ul>
	<li>For example, the next permutation of <code>arr = [1,2,3]</code> is <code>[1,3,2]</code>.</li>
	<li>Similarly, the next permutation of <code>arr = [2,3,1]</code> is <code>[3,1,2]</code>.</li>
	<li>While the next permutation of <code>arr = [3,2,1]</code> is <code>[1,2,3]</code> because <code>[3,2,1]</code> does not have a lexicographical larger rearrangement.</li>
</ul>

<p>Given an array of integers <code>nums</code>, <em>find the next permutation of</em> <code>nums</code>.</p>

<p>The replacement must be <strong><a href="http://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in place</a></strong> and use only constant extra memory.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [1,3,2]
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [3,2,1]
<strong>Output:</strong> [1,2,3]
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [1,1,5]
<strong>Output:</strong> [1,5,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2

        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1

        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1

            nums[j], nums[i] = nums[i], nums[j]

        s = i + 1
        e = n - 1

        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "31. Next Permutation",
    "text": "A permutation of an array of integers is an arrangement of its members into a sequence or linear order.\n\nFor example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].\n\nThe next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).\n\nFor example, the next permutation of arr = [1,2,3] is [1,3,2].\nSimilarly, the next permutation of arr = [2,3,1] is [3,1,2].\nWhile the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.\n\nGiven an array of integers nums, find the next permutation of nums.\nThe replacement must be in place and use only constant extra memory.\n\u00a0\nExample 1:\nInput: nums = [1,2,3]\nOutput: [1,3,2]\n\nExample 2:\nInput: nums = [3,2,1]\nOutput: [1,2,3]\n\nExample 3:\nInput: nums = [1,1,5]\nOutput: [1,5,1]\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 100\n0 <= nums[i] <= 100\n\n",
    "url": "https://leetcode.com/problems/31-next-permutation",
    "answerCount": 1,
    "datePublished": "2026-04-12T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def nextPermutation(self, nums: List[int]) -> None:\n        \"\"\"\n        Do not return anything, modify nums in-place instead.\n        \"\"\"\n        n = len(nums)\n        i = n - 2\n\n        while i >= 0 and nums[i + 1] <= nums[i]:\n            i -= 1\n\n        if i >= 0:\n            j = n - 1\n            while nums[j] <= nums[i]:\n                j -= 1\n\n            nums[j], nums[i] = nums[i], nums[j]\n\n        s = i + 1\n        e = n - 1\n\n        while s < e:\n            nums[s], nums[e] = nums[e], nums[s]\n            s += 1\n            e -= 1\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/31-next-permutation/",
      "datePublished": "2026-04-12T00:00:00Z",
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