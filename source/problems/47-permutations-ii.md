# 47-permutations-ii


Try it on <a href='https://leetcode.com/problems/47-permutations-ii'>leetcode</a>

## Description
<div class="description">
<div><p>Given a collection of numbers, <code>nums</code>,&nbsp;that might contain duplicates, return <em>all possible unique permutations <strong>in any order</strong>.</em></p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,1,2]
<strong>Output:</strong>
[[1,1,2],
 [1,2,1],
 [2,1,1]]
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 8</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(comb, counter):
            if len(comb) == len(nums):
                res.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    backtrack(comb, counter)
                    counter[num] += 1
                    comb.pop()

        backtrack([], Counter(nums))
        return res

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "47. Permutations II",
    "text": "Given a collection of numbers, nums,\u00a0that might contain duplicates, return all possible unique permutations in any order.\n\u00a0\nExample 1:\nInput: nums = [1,1,2]\nOutput:\n[[1,1,2],\n [1,2,1],\n [2,1,1]]\n\nExample 2:\nInput: nums = [1,2,3]\nOutput: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 8\n-10 <= nums[i] <= 10\n\n",
    "url": "https://leetcode.com/problems/47-permutations-ii",
    "answerCount": 1,
    "datePublished": "2022-11-25T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def permuteUnique(self, nums: List[int]) -> List[List[int]]:\n        res = []\n\n        def backtrack(comb, counter):\n            if len(comb) == len(nums):\n                res.append(list(comb))\n                return\n\n            for num in counter:\n                if counter[num] > 0:\n                    comb.append(num)\n                    counter[num] -= 1\n                    backtrack(comb, counter)\n                    counter[num] += 1\n                    comb.pop()\n\n        backtrack([], Counter(nums))\n        return res\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/47-permutations-ii/",
      "datePublished": "2022-11-25T00:00:00Z",
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