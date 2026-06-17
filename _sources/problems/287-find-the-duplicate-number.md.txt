# 287-find-the-duplicate-number


Try it on <a href='https://leetcode.com/problems/287-find-the-duplicate-number'>leetcode</a>

## Description
<div class="description">
<div><p>Given an array of integers <code>nums</code> containing&nbsp;<code>n + 1</code> integers where each integer is in the range <code>[1, n]</code> inclusive.</p>

<p>There is only <strong>one repeated number</strong> in <code>nums</code>, return <em>this&nbsp;repeated&nbsp;number</em>.</p>

<p>You must solve the problem <strong>without</strong> modifying the array <code>nums</code>&nbsp;and uses only constant extra space.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,3,4,2,2]
<strong>Output:</strong> 2
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [3,1,3,4,2]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>nums.length == n + 1</code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
	<li>All the integers in <code>nums</code> appear only <strong>once</strong> except for <strong>precisely one integer</strong> which appears <strong>two or more</strong> times.</li>
</ul>

<p>&nbsp;</p>
<p><b>Follow up:</b></p>

<ul>
	<li>How can we prove that at least one duplicate number must exist in <code>nums</code>?</li>
	<li>Can you solve the problem in linear runtime complexity?</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        while nums[0] != nums[nums[0]]:
            nums[nums[0]],  nums[0] = nums[0],nums[nums[0]]
        return nums[0]
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "287. Find the Duplicate Number",
    "text": "Given an array of integers nums containing\u00a0n + 1 integers where each integer is in the range [1, n] inclusive.\nThere is only one repeated number in nums, return this\u00a0repeated\u00a0number.\nYou must solve the problem without modifying the array nums\u00a0and uses only constant extra space.\n\u00a0\nExample 1:\nInput: nums = [1,3,4,2,2]\nOutput: 2\n\nExample 2:\nInput: nums = [3,1,3,4,2]\nOutput: 3\n\n\u00a0\nConstraints:\n\n1 <= n <= 105\nnums.length == n + 1\n1 <= nums[i] <= n\nAll the integers in nums appear only once except for precisely one integer which appears two or more times.\n\n\u00a0\nFollow up:\n\nHow can we prove that at least one duplicate number must exist in nums?\nCan you solve the problem in linear runtime complexity?\n\n",
    "url": "https://leetcode.com/problems/287-find-the-duplicate-number",
    "answerCount": 1,
    "datePublished": "2022-07-13T11:04:51+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def findDuplicate(self, nums):\n        # Find the intersection point of the two runners.\n        while nums[0] != nums[nums[0]]:\n            nums[nums[0]],  nums[0] = nums[0],nums[nums[0]]\n        return nums[0]",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/287-find-the-duplicate-number/",
      "datePublished": "2022-07-13T11:04:51+05:30",
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