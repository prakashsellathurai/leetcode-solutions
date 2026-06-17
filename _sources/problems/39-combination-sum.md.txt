# 39-combination-sum


Try it on <a href='https://leetcode.com/problems/39-combination-sum'>leetcode</a>

## Description
<div class="description">
<div><p>Given an array of <strong>distinct</strong> integers <code>candidates</code> and a target integer <code>target</code>, return <em>a list of all <strong>unique combinations</strong> of </em><code>candidates</code><em> where the chosen numbers sum to </em><code>target</code><em>.</em> You may return the combinations in <strong>any order</strong>.</p>

<p>The <strong>same</strong> number may be chosen from <code>candidates</code> an <strong>unlimited number of times</strong>. Two combinations are unique if the frequency of at least one of the chosen numbers is different.</p>

<p>It is <strong>guaranteed</strong> that the number of unique combinations that sum up to <code>target</code> is less than <code>150</code> combinations for the given input.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> candidates = [2,3,6,7], target = 7
<strong>Output:</strong> [[2,2,3],[7]]
<strong>Explanation:</strong>
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> candidates = [2,3,5], target = 8
<strong>Output:</strong> [[2,2,2,2],[2,3,3],[3,5]]
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> candidates = [2], target = 1
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= candidates.length &lt;= 30</code></li>
	<li><code>1 &lt;= candidates[i] &lt;= 200</code></li>
	<li>All elements of <code>candidates</code> are <strong>distinct</strong>.</li>
	<li><code>1 &lt;= target &lt;= 500</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.candidates = candidates
        self.backtrack([], target, 0)
        return self.res

    def backtrack(self, candidate, target, i):
        if sum(candidate) == target:
            self.res.append(candidate[:])
            return
        if sum(candidate) > target:
            return

        for j in range(i, len(self.candidates)):
            if self.candidates[j] <= target:

                candidate.append(self.candidates[j])
                self.backtrack(candidate, target, j)
                candidate.pop()

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "39. Combination Sum",
    "text": "Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.\nThe same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.\nIt is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.\n\u00a0\nExample 1:\nInput: candidates = [2,3,6,7], target = 7\nOutput: [[2,2,3],[7]]\nExplanation:\n2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.\n7 is a candidate, and 7 = 7.\nThese are the only two combinations.\n\nExample 2:\nInput: candidates = [2,3,5], target = 8\nOutput: [[2,2,2,2],[2,3,3],[3,5]]\n\nExample 3:\nInput: candidates = [2], target = 1\nOutput: []\n\n\u00a0\nConstraints:\n\n1 <= candidates.length <= 30\n1 <= candidates[i] <= 200\nAll elements of candidates are distinct.\n1 <= target <= 500\n\n",
    "url": "https://leetcode.com/problems/39-combination-sum",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:\n        self.res = []\n        self.candidates = candidates\n        self.backtrack([], target, 0)\n        return self.res\n\n    def backtrack(self, candidate, target, i):\n        if sum(candidate) == target:\n            self.res.append(candidate[:])\n            return\n        if sum(candidate) > target:\n            return\n\n        for j in range(i, len(self.candidates)):\n            if self.candidates[j] <= target:\n\n                candidate.append(self.candidates[j])\n                self.backtrack(candidate, target, j)\n                candidate.pop()\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/39-combination-sum/",
      "datePublished": "2022-06-19T23:02:59+05:30",
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