# 4sum-ii


Try it on <a href='https://leetcode.com/problems/4sum-ii'>leetcode</a>

## Description
<div class="description">
<div><p>Given four integer arrays <code>nums1</code>, <code>nums2</code>, <code>nums3</code>, and <code>nums4</code> all of length <code>n</code>, return the number of tuples <code>(i, j, k, l)</code> such that:</p>

<ul>
	<li><code>0 &lt;= i, j, k, l &lt; n</code></li>
	<li><code>nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
The two tuples are:
1. (0, 0, 0, 1) -&gt; nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -&gt; nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums1.length</code></li>
	<li><code>n == nums2.length</code></li>
	<li><code>n == nums3.length</code></li>
	<li><code>n == nums4.length</code></li>
	<li><code>1 &lt;= n &lt;= 200</code></li>
	<li><code>-2<sup>28</sup> &lt;= nums1[i], nums2[i], nums3[i], nums4[i] &lt;= 2<sup>28</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        count = 0
        hashmap = defaultdict(lambda: 0)

        for i, num1 in enumerate(nums1):
            for j, num2 in enumerate(nums2):
                hashmap[-num1 - num2] += 1

        for k, num3 in enumerate(nums3):
            for l, num4 in enumerate(nums4):
                count += hashmap[num3 + num4]
        return count

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "454. 4Sum II",
    "text": "Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:\n\n0 <= i, j, k, l < n\nnums1[i] + nums2[j] + nums3[k] + nums4[l] == 0\n\n\u00a0\nExample 1:\nInput: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]\nOutput: 2\nExplanation:\nThe two tuples are:\n1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0\n2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0\n\nExample 2:\nInput: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]\nOutput: 1\n\n\u00a0\nConstraints:\n\nn == nums1.length\nn == nums2.length\nn == nums3.length\nn == nums4.length\n1 <= n <= 200\n-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228\n\n",
    "url": "https://leetcode.com/problems/4sum-ii",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def fourSumCount(\n        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]\n    ) -> int:\n        count = 0\n        hashmap = defaultdict(lambda: 0)\n\n        for i, num1 in enumerate(nums1):\n            for j, num2 in enumerate(nums2):\n                hashmap[-num1 - num2] += 1\n\n        for k, num3 in enumerate(nums3):\n            for l, num4 in enumerate(nums4):\n                count += hashmap[num3 + num4]\n        return count\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/4sum-ii/",
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