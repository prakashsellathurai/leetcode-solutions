# 454-4sum-ii


Try it on <a href='https://leetcode.com/problems/454-4sum-ii'>leetcode</a>

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
        return self.optmizedapproach(nums1, nums2, nums3, nums4)

    """
    cntr = 0
    for all possible pairings (atmost n^4 )
        if condition satisfies:
            cntr+=1
    Time Complexity: O(n^4)
    Space Complexity: O(1)
    """

    def bruteforce(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        n = len(nums1)
        cntr = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    for l in range(n):
                        if nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0:
                            cntr += 1

        return cntr

    """
    cntr = 0
    put -num4 frequency in hashmap
    
    for 3 loops with i,j,k
        if num2+num3+num4 in hashmap:
            cntr+=hashmap[num2+num3+num4]
    Time Complexity: O(n^3)
    Space Complexity: O(n)
    """

    def optmizedbruteforce(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        n = len(nums1)
        cntr = 0
        hashmap = {}
        for num1 in nums1:
            if -num1 not in hashmap:
                hashmap[-num1] = 1
            else:
                hashmap[-num1] += 1

        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if nums2[j] + nums3[k] + nums4[l] in hashmap:
                        cntr += hashmap[nums2[j] + nums3[k] + nums4[l]]

        return cntr

    """
    cntr = 0
    put -num1-num2 frequency in hashmap
    
    for 2 loops with k,l
        if num3 + num4 in hashmap:
            cntr+=hashmap[num3 + num4]
            
            
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """

    def optmizedapproach(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        n = len(nums1)
        cntr = 0
        hashmap = {}
        for num1 in nums1:
            for num2 in nums2:
                if -num1 - num2 not in hashmap:
                    hashmap[-num1 - num2] = 1
                else:
                    hashmap[-num1 - num2] += 1

        for k in range(n):
            for l in range(n):
                if nums3[k] + nums4[l] in hashmap:
                    cntr += hashmap[nums3[k] + nums4[l]]

        return cntr

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "454. 4Sum II",
    "text": "Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:\n\n0 <= i, j, k, l < n\nnums1[i] + nums2[j] + nums3[k] + nums4[l] == 0\n\n\u00a0\nExample 1:\nInput: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]\nOutput: 2\nExplanation:\nThe two tuples are:\n1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0\n2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0\n\nExample 2:\nInput: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]\nOutput: 1\n\n\u00a0\nConstraints:\n\nn == nums1.length\nn == nums2.length\nn == nums3.length\nn == nums4.length\n1 <= n <= 200\n-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228\n\n",
    "url": "https://leetcode.com/problems/454-4sum-ii",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def fourSumCount(\n        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]\n    ) -> int:\n        return self.optmizedapproach(nums1, nums2, nums3, nums4)\n\n    \"\"\"\n    cntr = 0\n    for all possible pairings (atmost n^4 )\n        if condition satisfies:\n            cntr+=1\n    Time Complexity: O(n^4)\n    Space Complexity: O(1)\n    \"\"\"\n\n    def bruteforce(\n        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]\n    ) -> int:\n        n = len(nums1)\n        cntr = 0\n        for i in range(n):\n            for j in range(n):\n                for k in range(n):\n                    for l in range(n):\n                        if nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0:\n                            cntr += 1\n\n        return cntr\n\n    \"\"\"\n    cntr = 0\n    put -num4 frequency in hashmap\n    \n    for 3 loops with i,j,k\n        if num2+num3+num4 in hashmap:\n            cntr+=hashmap[num2+num3+num4]\n    Time Complexity: O(n^3)\n    Space Complexity: O(n)\n    \"\"\"\n\n    def optmizedbruteforce(\n        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]\n    ) -> int:\n        n = len(nums1)\n        cntr = 0\n        hashmap = {}\n        for num1 in nums1:\n            if -num1 not in hashmap:\n                hashmap[-num1] = 1\n            else:\n                hashmap[-num1] += 1\n\n        for j in range(n):\n            for k in range(n):\n                for l in range(n):\n                    if nums2[j] + nums3[k] + nums4[l] in hashmap:\n                        cntr += hashmap[nums2[j] + nums3[k] + nums4[l]]\n\n        return cntr\n\n    \"\"\"\n    cntr = 0\n    put -num1-num2 frequency in hashmap\n    \n    for 2 loops with k,l\n        if num3 + num4 in hashmap:\n            cntr+=hashmap[num3 + num4]\n            \n            \n    Time Complexity: O(n^2)\n    Space Complexity: O(n)\n    \"\"\"\n\n    def optmizedapproach(\n        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]\n    ) -> int:\n        n = len(nums1)\n        cntr = 0\n        hashmap = {}\n        for num1 in nums1:\n            for num2 in nums2:\n                if -num1 - num2 not in hashmap:\n                    hashmap[-num1 - num2] = 1\n                else:\n                    hashmap[-num1 - num2] += 1\n\n        for k in range(n):\n            for l in range(n):\n                if nums3[k] + nums4[l] in hashmap:\n                    cntr += hashmap[nums3[k] + nums4[l]]\n\n        return cntr\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/454-4sum-ii/",
      "datePublished": "2026-06-06",
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