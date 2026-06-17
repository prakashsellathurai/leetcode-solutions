# 128-longest-consecutive-sequence


Try it on <a href='https://leetcode.com/problems/128-longest-consecutive-sequence'>leetcode</a>

## Description
<div class="description">
<div><p>Given an unsorted array of integers <code>nums</code>, return <em>the length of the longest consecutive elements sequence.</em></p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [100,4,200,1,3,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest consecutive elements sequence is <code>[1, 2, 3, 4]</code>. Therefore its length is 4.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [0,3,7,2,5,8,4,6,0,1]
<strong>Output:</strong> 9
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def longestConsecutive(self, nums):

        longest_streak = 0
        num_set = set(nums)

        for num in nums:
            if num-1 not in num_set:
                current_streak = 1
                cur_num = num
                while cur_num+1 in num_set:
                    cur_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak,current_streak)

        return longest_streak
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "128. Longest Consecutive Sequence",
    "text": "Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.\nYou must write an algorithm that runs in\u00a0O(n)\u00a0time.\n\u00a0\nExample 1:\nInput: nums = [100,4,200,1,3,2]\nOutput: 4\nExplanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.\n\nExample 2:\nInput: nums = [0,3,7,2,5,8,4,6,0,1]\nOutput: 9\n\n\u00a0\nConstraints:\n\n0 <= nums.length <= 105\n-109 <= nums[i] <= 109\n\n",
    "url": "https://leetcode.com/problems/128-longest-consecutive-sequence",
    "answerCount": 1,
    "datePublished": "2022-07-05T20:37:06+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def longestConsecutive(self, nums):\n\n        longest_streak = 0\n        num_set = set(nums)\n\n        for num in nums:\n            if num-1 not in num_set:\n                current_streak = 1\n                cur_num = num\n                while cur_num+1 in num_set:\n                    cur_num += 1\n                    current_streak += 1\n                longest_streak = max(longest_streak,current_streak)\n\n        return longest_streak",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/128-longest-consecutive-sequence/",
      "datePublished": "2022-07-05T20:37:06+05:30",
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