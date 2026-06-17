# 0238-product-of-array-except-self


Try it on <a href='https://leetcode.com/problems/0238-product-of-array-except-self'>leetcode</a>

## Description
<div class="description">
<p>Given an integer array <code>nums</code>, return <em>an array</em> <code>answer</code> <em>such that</em> <code>answer[i]</code> <em>is equal to the product of all the elements of</em> <code>nums</code> <em>except</em> <code>nums[i]</code>.</p>

<p>The product of any prefix or suffix of <code>nums</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time and without using the division operation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [24,12,8,6]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [-1,1,0,-3,3]
<strong>Output:</strong> [0,0,9,0,0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-30 &lt;= nums[i] &lt;= 30</code></li>
	<li>The input is generated such that <code>answer[i]</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong>&nbsp;Can you solve the problem in <code>O(1)</code>&nbsp;extra&nbsp;space complexity? (The output array <strong>does not</strong> count as extra space for space complexity analysis.)</p>

</div>

## Solution(Python)
```Python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.presum_lessspace(nums)
    
    # Time Complexity: O(n^2)
    # Space COmplexity: O(1)
    def bruteforce(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        for i in range(n):
            curEle = 1
            for j in range(i):
                curEle*=nums[j]
            for j in range(i+1, n):
                curEle*=nums[j]
            res[i] = curEle
        return res
    
    # Time Complexity: O(n)
    # Space COmplexity: O(n)
    def presum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        presum = [1] * n
        postsum = [1] * n
        presum[0] = 1
        presum[1] = nums[0] 
        for i in range(2, n):
            presum[i] = presum[i-1] * nums[i-1]
        postsum[n-1] = 1
        postsum[n-2] = nums[n-1]
        for i in range(n-2, -1, -1):
            postsum[i] = postsum[i+1] * nums[i+1]

        res = [1] *n

        for i in range(n):
            res[i] = presum[i] * postsum[i]
        return res

    # Time Complexity: O(n)
    # Space COmplexity: O(1)
    def presum_lessspace(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] *n
        res[0] = 1
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        rightMul= 1
        for i in range(n-1, -1, -1):
            res[i] = res[i] * rightMul
            rightMul*=nums[i]

        return res
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "238. Product of Array Except Self",
    "text": "Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].\nThe product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.\nYou must write an algorithm that runs in\u00a0O(n)\u00a0time and without using the division operation.\n\u00a0\nExample 1:\nInput: nums = [1,2,3,4]\nOutput: [24,12,8,6]\nExample 2:\nInput: nums = [-1,1,0,-3,3]\nOutput: [0,0,9,0,0]\n\n\u00a0\nConstraints:\n\n2 <= nums.length <= 105\n-30 <= nums[i] <= 30\nThe input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.\n\n\u00a0\nFollow up:\u00a0Can you solve the problem in O(1)\u00a0extra\u00a0space complexity? (The output array does not count as extra space for space complexity analysis.)\n",
    "url": "https://leetcode.com/problems/0238-product-of-array-except-self",
    "answerCount": 1,
    "datePublished": "2025-09-05T18:06:22+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def productExceptSelf(self, nums: List[int]) -> List[int]:\n        return self.presum_lessspace(nums)\n    \n    # Time Complexity: O(n^2)\n    # Space COmplexity: O(1)\n    def bruteforce(self, nums: List[int]) -> List[int]:\n        n = len(nums)\n        res = [0] * n\n        for i in range(n):\n            curEle = 1\n            for j in range(i):\n                curEle*=nums[j]\n            for j in range(i+1, n):\n                curEle*=nums[j]\n            res[i] = curEle\n        return res\n    \n    # Time Complexity: O(n)\n    # Space COmplexity: O(n)\n    def presum(self, nums: List[int]) -> List[int]:\n        n = len(nums)\n        presum = [1] * n\n        postsum = [1] * n\n        presum[0] = 1\n        presum[1] = nums[0] \n        for i in range(2, n):\n            presum[i] = presum[i-1] * nums[i-1]\n        postsum[n-1] = 1\n        postsum[n-2] = nums[n-1]\n        for i in range(n-2, -1, -1):\n            postsum[i] = postsum[i+1] * nums[i+1]\n\n        res = [1] *n\n\n        for i in range(n):\n            res[i] = presum[i] * postsum[i]\n        return res\n\n    # Time Complexity: O(n)\n    # Space COmplexity: O(1)\n    def presum_lessspace(self, nums: List[int]) -> List[int]:\n        n = len(nums)\n        res = [0] *n\n        res[0] = 1\n        for i in range(1, n):\n            res[i] = res[i-1] * nums[i-1]\n        rightMul= 1\n        for i in range(n-1, -1, -1):\n            res[i] = res[i] * rightMul\n            rightMul*=nums[i]\n\n        return res",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/0238-product-of-array-except-self/",
      "datePublished": "2025-09-05T18:06:22+05:30",
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