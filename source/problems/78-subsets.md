# 78-subsets


Try it on <a href='https://leetcode.com/problems/78-subsets'>leetcode</a>

## Description
<div class="description">
<div><p>Given an integer array <code>nums</code> of <strong>unique</strong> elements, return <em>all possible subsets (the power set)</em>.</p>

<p>The solution set <strong>must not</strong> contain duplicate subsets. Return the solution in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> [[],[0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li>All the numbers of&nbsp;<code>nums</code> are <strong>unique</strong>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]

        for num in nums:
            output += [curr + [num] for curr in output]

        return output

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "78. Subsets",
    "text": "Given an integer array nums of unique elements, return all possible subsets (the power set).\nThe solution set must not contain duplicate subsets. Return the solution in any order.\n\u00a0\nExample 1:\nInput: nums = [1,2,3]\nOutput: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]\n\nExample 2:\nInput: nums = [0]\nOutput: [[],[0]]\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 10\n-10 <= nums[i] <= 10\nAll the numbers of\u00a0nums are unique.\n\n",
    "url": "https://leetcode.com/problems/78-subsets",
    "answerCount": 1,
    "datePublished": "2022-07-03T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def subsets(self, nums: List[int]) -> List[List[int]]:\n        n = len(nums)\n        output = [[]]\n\n        for num in nums:\n            output += [curr + [num] for curr in output]\n\n        return output\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/78-subsets/",
      "datePublished": "2022-07-03T00:00:00Z",
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