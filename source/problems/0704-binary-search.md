# 0704-binary-search


Try it on <a href='https://leetcode.com/problems/0704-binary-search'>leetcode</a>

## Description
<div class="description">
<p>Given an array of integers <code>nums</code> which is sorted in ascending order, and an integer <code>target</code>, write a function to search <code>target</code> in <code>nums</code>. If <code>target</code> exists, then return its index. Otherwise, return <code>-1</code>.</p>

<p>You must write an algorithm with <code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,0,3,5,9,12], target = 9
<strong>Output:</strong> 4
<strong>Explanation:</strong> 9 exists in nums and its index is 4
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,0,3,5,9,12], target = 2
<strong>Output:</strong> -1
<strong>Explanation:</strong> 2 does not exist in nums so return -1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt; nums[i], target &lt; 10<sup>4</sup></code></li>
	<li>All the integers in <code>nums</code> are <strong>unique</strong>.</li>
	<li><code>nums</code> is sorted in ascending order.</li>
</ul>

</div>

## Solution(Python)
```Python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # arr[0] < arr[i] < arr[n-1]
        #   mid < target  l = mid + 1
        #   mid >= target r = mid
        #  -1 0 3 5 9 12
        #     5 < 9 l = 3 r =6
        l = 0
        r = len(nums) - 1
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        return -1   
        
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "704. Binary Search",
    "text": "Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.\nYou must write an algorithm with O(log n) runtime complexity.\n\u00a0\nExample 1:\n\nInput: nums = [-1,0,3,5,9,12], target = 9\nOutput: 4\nExplanation: 9 exists in nums and its index is 4\n\nExample 2:\n\nInput: nums = [-1,0,3,5,9,12], target = 2\nOutput: -1\nExplanation: 2 does not exist in nums so return -1\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 104\n-104 < nums[i], target < 104\nAll the integers in nums are unique.\nnums is sorted in ascending order.\n\n",
    "url": "https://leetcode.com/problems/0704-binary-search",
    "answerCount": 1,
    "datePublished": "2026-03-07T21:39:18+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def search(self, nums: List[int], target: int) -> int:\n        # arr[0] < arr[i] < arr[n-1]\n        #   mid < target  l = mid + 1\n        #   mid >= target r = mid\n        #  -1 0 3 5 9 12\n        #     5 < 9 l = 3 r =6\n        l = 0\n        r = len(nums) - 1\n        if nums[l] == target:\n            return l\n        if nums[r] == target:\n            return r\n        while l < r:\n            mid = (l + r) // 2\n            if nums[mid] == target:\n                return mid\n            elif nums[mid] < target:\n                l = mid + 1\n            else:\n                r = mid\n\n        return -1   \n        ",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/0704-binary-search/",
      "datePublished": "2026-03-07T21:39:18+05:30",
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