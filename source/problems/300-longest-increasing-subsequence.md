# 300-longest-increasing-subsequence


Try it on <a href='https://leetcode.com/problems/300-longest-increasing-subsequence'>leetcode</a>

## Description
<div class="description">
<div><p>Given an integer array <code>nums</code>, return the length of the longest strictly increasing subsequence.</p>

<p>A <strong>subsequence</strong> is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, <code>[3,6,2,7]</code> is a subsequence of the array <code>[0,3,1,6,2,2,7]</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [10,9,2,5,3,7,101,18]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [0,1,0,3,2,3]
<strong>Output:</strong> 4
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [7,7,7,7,7,7,7]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2500</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><b>Follow up:</b>&nbsp;Can you come up with an algorithm that runs in&nbsp;<code>O(n log(n))</code> time complexity?</p>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = []
        for num in nums:
            if not LIS or LIS[-1] < num:
                LIS.append(num)
            else:
                pos = bisect_left(LIS,num)
                LIS[pos] = num

        return len(LIS)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "300. Longest Increasing Subsequence",
    "text": "Given an integer array nums, return the length of the longest strictly increasing subsequence.\nA subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].\n\u00a0\nExample 1:\nInput: nums = [10,9,2,5,3,7,101,18]\nOutput: 4\nExplanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.\n\nExample 2:\nInput: nums = [0,1,0,3,2,3]\nOutput: 4\n\nExample 3:\nInput: nums = [7,7,7,7,7,7,7]\nOutput: 1\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 2500\n-104 <= nums[i] <= 104\n\n\u00a0\nFollow up:\u00a0Can you come up with an algorithm that runs in\u00a0O(n log(n)) time complexity?\n",
    "url": "https://leetcode.com/problems/300-longest-increasing-subsequence",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def lengthOfLIS(self, nums: List[int]) -> int:\n        LIS = []\n        for num in nums:\n            if not LIS or LIS[-1] < num:\n                LIS.append(num)\n            else:\n                pos = bisect_left(LIS,num)\n                LIS[pos] = num\n\n        return len(LIS)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/300-longest-increasing-subsequence/",
      "datePublished": "2025-09-25",
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