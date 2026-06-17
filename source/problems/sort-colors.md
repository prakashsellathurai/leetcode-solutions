# sort-colors


Try it on <a href='https://leetcode.com/problems/sort-colors'>leetcode</a>

## Description
<div class="description">
<div><p>Given an array <code>nums</code> with <code>n</code> objects colored red, white, or blue, sort them <strong><a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a> </strong>so that objects of the same color are adjacent, with the colors in the order red, white, and blue.</p>

<p>We will use the integers <code>0</code>, <code>1</code>, and <code>2</code> to represent the color red, white, and blue, respectively.</p>

<p>You must solve this problem without using the library's sort function.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [2,0,2,1,1,0]
<strong>Output:</strong> [0,0,1,1,2,2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [2,0,1]
<strong>Output:</strong> [0,1,2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 300</code></li>
	<li><code>nums[i]</code> is either <code>0</code>, <code>1</code>, or <code>2</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong>&nbsp;Could you come up with a one-pass algorithm using only&nbsp;constant extra space?</p>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.threePointers(nums)
        
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def countingSort(self, nums: List[int]) -> None:
        count = [0] * 3
        
        for num  in nums:
            count[num] += 1
        
        starting_index = 0

        for c, freq in enumerate(count):
            count[c] = starting_index
            starting_index += freq
        sortedList = [0]*len(nums)
        for num in nums:
            sortedList[count[num]] = num
            count[num] += 1
        for i in range(len(nums)):
            nums[i] = sortedList[i]
            
    # Time Complexity: O(n)
    # Space Complexity: O(1)         
    def threePointers(self, nums: List[int]) -> None:
        n = len(nums)
        p1 = 0
        p2 = n-1
        cur = 0
        
        while cur <= p2:
            num = nums[cur]
            if num == 0:
                nums[cur], nums[p1] = nums[p1], nums[cur]
                cur +=1
                p1+=1
            elif num == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2-=1
            else:
                cur += 1
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": " \u00a0Sort Colors",
    "text": "Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.\nWe will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.\nYou must solve this problem without using the library's sort function.\n\u00a0\nExample 1:\nInput: nums = [2,0,2,1,1,0]\nOutput: [0,0,1,1,2,2]\n\nExample 2:\nInput: nums = [2,0,1]\nOutput: [0,1,2]\n\n\u00a0\nConstraints:\n\nn == nums.length\n1 <= n <= 300\nnums[i] is either 0, 1, or 2.\n\n\u00a0\nFollow up:\u00a0Could you come up with a one-pass algorithm using only\u00a0constant extra space?\n",
    "url": "https://leetcode.com/problems/sort-colors",
    "answerCount": 1,
    "datePublished": "2026-03-06T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def sortColors(self, nums: List[int]) -> None:\n        \"\"\"\n        Do not return anything, modify nums in-place instead.\n        \"\"\"\n        self.threePointers(nums)\n        \n    # Time Complexity: O(n)\n    # Space Complexity: O(1)\n    def countingSort(self, nums: List[int]) -> None:\n        count = [0] * 3\n        \n        for num  in nums:\n            count[num] += 1\n        \n        starting_index = 0\n\n        for c, freq in enumerate(count):\n            count[c] = starting_index\n            starting_index += freq\n        sortedList = [0]*len(nums)\n        for num in nums:\n            sortedList[count[num]] = num\n            count[num] += 1\n        for i in range(len(nums)):\n            nums[i] = sortedList[i]\n            \n    # Time Complexity: O(n)\n    # Space Complexity: O(1)         \n    def threePointers(self, nums: List[int]) -> None:\n        n = len(nums)\n        p1 = 0\n        p2 = n-1\n        cur = 0\n        \n        while cur <= p2:\n            num = nums[cur]\n            if num == 0:\n                nums[cur], nums[p1] = nums[p1], nums[cur]\n                cur +=1\n                p1+=1\n            elif num == 2:\n                nums[cur], nums[p2] = nums[p2], nums[cur]\n                p2-=1\n            else:\n                cur += 1",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/sort-colors/",
      "datePublished": "2026-03-06T00:00:00Z",
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