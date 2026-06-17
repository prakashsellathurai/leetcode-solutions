# 179-largest-number


Try it on <a href='https://leetcode.com/problems/179-largest-number'>leetcode</a>

## Description
<div class="description">
<div><p>Given a list of non-negative integers <code>nums</code>, arrange them such that they form the largest number and return it.</p>

<p>Since the result may be very large, so you need to return a string instead of an integer.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [10,2]
<strong>Output:</strong> "210"
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [3,30,34,5,9]
<strong>Output:</strong> "9534330"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        largest_num = "".join(sorted(map(str, nums), key=LargerNumKey))
        return "0" if largest_num[0] == "0" else largest_num

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "179. Largest Number",
    "text": "Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.\nSince the result may be very large, so you need to return a string instead of an integer.\n\u00a0\nExample 1:\nInput: nums = [10,2]\nOutput: \"210\"\n\nExample 2:\nInput: nums = [3,30,34,5,9]\nOutput: \"9534330\"\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 100\n0 <= nums[i] <= 109\n\n",
    "url": "https://leetcode.com/problems/179-largest-number",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class LargerNumKey(str):\n    def __lt__(x, y):\n        return x + y > y + x\n\n\nclass Solution:\n    def largestNumber(self, nums):\n        largest_num = \"\".join(sorted(map(str, nums), key=LargerNumKey))\n        return \"0\" if largest_num[0] == \"0\" else largest_num\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/179-largest-number/",
      "datePublished": "2025-04-23",
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