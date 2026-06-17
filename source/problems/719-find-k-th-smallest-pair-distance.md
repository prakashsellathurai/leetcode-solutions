# 719-find-k-th-smallest-pair-distance


Try it on <a href='https://leetcode.com/problems/719-find-k-th-smallest-pair-distance'>leetcode</a>

## Description
<div class="description">
<div><p>The <strong>distance of a pair</strong> of integers <code>a</code> and <code>b</code> is defined as the absolute difference between <code>a</code> and <code>b</code>.</p>

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the</em> <code>k<sup>th</sup></code> <em>smallest <strong>distance among all the pairs</strong></em> <code>nums[i]</code> <em>and</em> <code>nums[j]</code> <em>where</em> <code>0 &lt;= i &lt; j &lt; nums.length</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,3,1], k = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> Here are all the pairs:
(1,3) -&gt; 2
(1,1) -&gt; 0
(3,1) -&gt; 2
Then the 1<sup>st</sup> smallest distance pair is (1,1), and its distance is 0.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,1,1], k = 2
<strong>Output:</strong> 0
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [1,6,1], k = 3
<strong>Output:</strong> 5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= k &lt;= n * (n - 1) / 2</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def enough(distance) -> bool:  # two pointers
            count, i, j = 0, 0, 0
            while i < n or j < n:
                while j < n and nums[j] - nums[i] <= distance:
                    j += 1
                count += j - i - 1
                i += 1
            return count >= k

        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if not enough(mid):
                left = mid + 1
            else:
                right = mid
        return left
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "719. Find K-th Smallest Pair Distance",
    "text": "The distance of a pair of integers a and b is defined as the absolute difference between a and b.\nGiven an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.\n\u00a0\nExample 1:\nInput: nums = [1,3,1], k = 1\nOutput: 0\nExplanation: Here are all the pairs:\n(1,3) -> 2\n(1,1) -> 0\n(3,1) -> 2\nThen the 1st smallest distance pair is (1,1), and its distance is 0.\n\nExample 2:\nInput: nums = [1,1,1], k = 2\nOutput: 0\n\nExample 3:\nInput: nums = [1,6,1], k = 3\nOutput: 5\n\n\u00a0\nConstraints:\n\nn == nums.length\n2 <= n <= 104\n0 <= nums[i] <= 106\n1 <= k <= n * (n - 1) / 2\n\n",
    "url": "https://leetcode.com/problems/719-find-k-th-smallest-pair-distance",
    "answerCount": 1,
    "datePublished": "2022-07-04T18:57:39+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def smallestDistancePair(self, nums: List[int], k: int) -> int:\n        def enough(distance) -> bool:  # two pointers\n            count, i, j = 0, 0, 0\n            while i < n or j < n:\n                while j < n and nums[j] - nums[i] <= distance:\n                    j += 1\n                count += j - i - 1\n                i += 1\n            return count >= k\n\n        nums.sort()\n        n = len(nums)\n        left, right = 0, nums[-1] - nums[0]\n        while left < right:\n            mid = left + (right - left) // 2\n            if not enough(mid):\n                left = mid + 1\n            else:\n                right = mid\n        return left",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/719-find-k-th-smallest-pair-distance/",
      "datePublished": "2022-07-04T18:57:39+05:30",
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