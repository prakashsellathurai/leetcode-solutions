# 1365-how-many-numbers-are-smaller-than-the-current-number


Try it on <a href='https://leetcode.com/problems/1365-how-many-numbers-are-smaller-than-the-current-number'>leetcode</a>

## Description
<div class="description">
<p>Given the array <code>nums</code>, for each <code>nums[i]</code> find out how many numbers in the array are smaller than it. That is, for each <code>nums[i]</code> you have to count the number of valid <code>j&#39;s</code>&nbsp;such that&nbsp;<code>j != i</code> <strong>and</strong> <code>nums[j] &lt; nums[i]</code>.</p>

<p>Return the answer in an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [8,1,2,2,3]
<strong>Output:</strong> [4,0,1,1,3]
<strong>Explanation:</strong> 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [6,5,4,8]
<strong>Output:</strong> [2,1,0,3]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [7,7,7,7]
<strong>Output:</strong> [0,0,0,0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 500</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>

</div>

## Solution(Python)
```Python
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return  self.sorting(nums)
    def sorting(self, nums: List[int]) -> List[int]:
        res  = []
        # sort the array using bucket sort
        bucket = [0] * (max(nums) + 1)
        for num in nums:
            bucket[num] += 1 # [0 1 2 1 0 0 0 0 1]
        for i in range(1, len(bucket)):
            bucket[i] += bucket[i-1] # [0 1 3 4 4 4 4 4 5]
        for num in nums:
            if num == 0:
                res.append(0)
            else:
                res.append(bucket[num-1])
        return res
            
        
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1365. How Many Numbers Are Smaller Than the Current Number",
    "text": "Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's\u00a0such that\u00a0j != i and nums[j] < nums[i].\nReturn the answer in an array.\n\u00a0\nExample 1:\n\nInput: nums = [8,1,2,2,3]\nOutput: [4,0,1,1,3]\nExplanation: \nFor nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). \nFor nums[1]=1 does not exist any smaller number than it.\nFor nums[2]=2 there exist one smaller number than it (1). \nFor nums[3]=2 there exist one smaller number than it (1). \nFor nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).\n\nExample 2:\n\nInput: nums = [6,5,4,8]\nOutput: [2,1,0,3]\n\nExample 3:\n\nInput: nums = [7,7,7,7]\nOutput: [0,0,0,0]\n\n\u00a0\nConstraints:\n\n2 <= nums.length <= 500\n0 <= nums[i] <= 100\n\n",
    "url": "https://leetcode.com/problems/1365-how-many-numbers-are-smaller-than-the-current-number",
    "answerCount": 1,
    "datePublished": "2026-01-06T16:42:57+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:\n        return  self.sorting(nums)\n    def sorting(self, nums: List[int]) -> List[int]:\n        res  = []\n        # sort the array using bucket sort\n        bucket = [0] * (max(nums) + 1)\n        for num in nums:\n            bucket[num] += 1 # [0 1 2 1 0 0 0 0 1]\n        for i in range(1, len(bucket)):\n            bucket[i] += bucket[i-1] # [0 1 3 4 4 4 4 4 5]\n        for num in nums:\n            if num == 0:\n                res.append(0)\n            else:\n                res.append(bucket[num-1])\n        return res\n            \n        ",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1365-how-many-numbers-are-smaller-than-the-current-number/",
      "datePublished": "2026-01-06T16:42:57+05:30",
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