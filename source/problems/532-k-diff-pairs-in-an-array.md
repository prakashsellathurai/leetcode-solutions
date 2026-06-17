# 532-k-diff-pairs-in-an-array


Try it on <a href='https://leetcode.com/problems/532-k-diff-pairs-in-an-array'>leetcode</a>

## Description
<div class="description">
<div><p>Given an array of integers <code>nums</code> and an integer <code>k</code>, return <em>the number of <b>unique</b> k-diff pairs in the array</em>.</p>

<p>A <strong>k-diff</strong> pair is an integer pair <code>(nums[i], nums[j])</code>, where the following are true:</p>

<ul>
	<li><code>0 &lt;= i &lt; j &lt; nums.length</code></li>
	<li><code>|nums[i] - nums[j]| == k</code></li>
</ul>

<p><strong>Notice</strong> that <code>|val|</code> denotes the absolute value of <code>val</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [3,1,4,1,5], k = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of <strong>unique</strong> pairs.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3,4,5], k = 1
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [1,3,1,5,4], k = 0
<strong>Output:</strong> 1
<strong>Explanation:</strong> There is one 0-diff pair in the array, (1, 1).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>7</sup> &lt;= nums[i] &lt;= 10<sup>7</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>7</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        return self.HashingSolution(nums, k)

    """
    bruteforce solution is to try all possible n(n-1)/2 pairs from the array of size n
    keep a set with unique difference of value == k
    
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """

    def bruteforceSolution(self, nums: List[int], k: int) -> int:
        seen = set()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) == k:
                    seen.add((nums[i], nums[j]))

        return len(seen)

    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    def bruteforceConstantSpaceSolution(self, nums: List[int], k: int) -> int:
        kdiff = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) == k:
                    kdiff += 1

        return kdiff

    """
    similar to two sum problem if we hash num1  in hashmap and look for num2+k for the second time we could increment the kidff counter
    
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    """

    def HashingSolution(self, nums: List[int], k: int) -> int:
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        kdiff = 0
        if k == 0:
            for key in hashmap:
                if hashmap[key] > 1:
                    kdiff += 1
        else:

            for num in set(nums):
                if num + k in hashmap:
                    kdiff += 1

        return kdiff

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "532. K-diff Pairs in an Array",
    "text": "Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.\nA k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:\n\n0 <= i < j < nums.length\n|nums[i] - nums[j]| == k\n\nNotice that |val| denotes the absolute value of val.\n\u00a0\nExample 1:\nInput: nums = [3,1,4,1,5], k = 2\nOutput: 2\nExplanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).\nAlthough we have two 1s in the input, we should only return the number of unique pairs.\n\nExample 2:\nInput: nums = [1,2,3,4,5], k = 1\nOutput: 4\nExplanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).\n\nExample 3:\nInput: nums = [1,3,1,5,4], k = 0\nOutput: 1\nExplanation: There is one 0-diff pair in the array, (1, 1).\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 104\n-107 <= nums[i] <= 107\n0 <= k <= 107\n\n",
    "url": "https://leetcode.com/problems/532-k-diff-pairs-in-an-array",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def findPairs(self, nums: List[int], k: int) -> int:\n        return self.HashingSolution(nums, k)\n\n    \"\"\"\n    bruteforce solution is to try all possible n(n-1)/2 pairs from the array of size n\n    keep a set with unique difference of value == k\n    \n    \n    Time Complexity: O(n^2)\n    Space Complexity: O(n)\n    \"\"\"\n\n    def bruteforceSolution(self, nums: List[int], k: int) -> int:\n        seen = set()\n        n = len(nums)\n        for i in range(n):\n            for j in range(i + 1, n):\n                if abs(nums[i] - nums[j]) == k:\n                    seen.add((nums[i], nums[j]))\n\n        return len(seen)\n\n    \"\"\"\n    Time Complexity: O(n^2)\n    Space Complexity: O(1)\n    \"\"\"\n\n    def bruteforceConstantSpaceSolution(self, nums: List[int], k: int) -> int:\n        kdiff = 0\n        n = len(nums)\n        for i in range(n):\n            for j in range(i + 1, n):\n                if abs(nums[i] - nums[j]) == k:\n                    kdiff += 1\n\n        return kdiff\n\n    \"\"\"\n    similar to two sum problem if we hash num1  in hashmap and look for num2+k for the second time we could increment the kidff counter\n    \n    \n    Time Complexity: O(n)\n    Space Complexity: O(n)\n    \n    \"\"\"\n\n    def HashingSolution(self, nums: List[int], k: int) -> int:\n        hashmap = {}\n\n        for num in nums:\n            if num not in hashmap:\n                hashmap[num] = 1\n            else:\n                hashmap[num] += 1\n\n        kdiff = 0\n        if k == 0:\n            for key in hashmap:\n                if hashmap[key] > 1:\n                    kdiff += 1\n        else:\n\n            for num in set(nums):\n                if num + k in hashmap:\n                    kdiff += 1\n\n        return kdiff\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/532-k-diff-pairs-in-an-array/",
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