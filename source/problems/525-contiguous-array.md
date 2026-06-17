# 525-contiguous-array


Try it on <a href='https://leetcode.com/problems/525-contiguous-array'>leetcode</a>

## Description
<div class="description">
<div><p>Given a binary array <code>nums</code>, return <em>the maximum length of a contiguous subarray with an equal number of </em><code>0</code><em> and </em><code>1</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [0,1,0]
<strong>Output:</strong> 2
<strong>Explanation:</strong> [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        return self.optimized(nums)

    """
    Idea:
    lets take a subarray of index between [i:j] in nums
    
    how do we find the whether it contains equal number of 0 and 1?
    
    we need Hashtable storing the frequency of 0 and 1 if they are same then it's a possible solution we could use a separate counter for 1 and 0
    
    
    Brutforce solution is to generate all possible contiguos subarray and check if it is valid and whether it is maximum or not is so store them in separate variable
    
    Time Complexity: O(n^2)
    Space Complexity: O(1) 
    """

    def bruteforce(self, nums: List[int]) -> int:
        n = len(nums)
        maxLen = 0

        for i in range(n):
            zeroCount = 0
            oneCount = 0
            for j in range(i, n):

                if nums[j]:
                    oneCount += 1
                else:
                    zeroCount += 1

                if oneCount == zeroCount and zeroCount + oneCount > maxLen:
                    maxLen = zeroCount + oneCount
        return maxLen

    """
    Idea:
   while on a single pass what if we store the count in the hasmap with it's respective index
    both count can be combined by having a single variable that increaments on one and decrements on 0
    
    when a count is encountered on Hashmap update the maxlen since the count resets to 0 on subarray with equal number of 1s and 0s 
    
    Time Complexity: O(n)
    Space Complexityt: O(n)
    """

    def optimized(self, nums: List[int]) -> int:
        Hashmap = {0: -1}
        maxLen = 0
        cnt = 0

        for i in range(len(nums)):
            cnt += 1 if nums[i] else -1
            if cnt in Hashmap:
                Len = i - Hashmap[cnt]
                if Len > maxLen:
                    maxLen = Len
            else:
                Hashmap[cnt] = i

        return maxLen

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "525. Contiguous Array",
    "text": "Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.\n\u00a0\nExample 1:\nInput: nums = [0,1]\nOutput: 2\nExplanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.\n\nExample 2:\nInput: nums = [0,1,0]\nOutput: 2\nExplanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 105\nnums[i] is either 0 or 1.\n\n",
    "url": "https://leetcode.com/problems/525-contiguous-array",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def findMaxLength(self, nums: List[int]) -> int:\n        return self.optimized(nums)\n\n    \"\"\"\n    Idea:\n    lets take a subarray of index between [i:j] in nums\n    \n    how do we find the whether it contains equal number of 0 and 1?\n    \n    we need Hashtable storing the frequency of 0 and 1 if they are same then it's a possible solution we could use a separate counter for 1 and 0\n    \n    \n    Brutforce solution is to generate all possible contiguos subarray and check if it is valid and whether it is maximum or not is so store them in separate variable\n    \n    Time Complexity: O(n^2)\n    Space Complexity: O(1) \n    \"\"\"\n\n    def bruteforce(self, nums: List[int]) -> int:\n        n = len(nums)\n        maxLen = 0\n\n        for i in range(n):\n            zeroCount = 0\n            oneCount = 0\n            for j in range(i, n):\n\n                if nums[j]:\n                    oneCount += 1\n                else:\n                    zeroCount += 1\n\n                if oneCount == zeroCount and zeroCount + oneCount > maxLen:\n                    maxLen = zeroCount + oneCount\n        return maxLen\n\n    \"\"\"\n    Idea:\n   while on a single pass what if we store the count in the hasmap with it's respective index\n    both count can be combined by having a single variable that increaments on one and decrements on 0\n    \n    when a count is encountered on Hashmap update the maxlen since the count resets to 0 on subarray with equal number of 1s and 0s \n    \n    Time Complexity: O(n)\n    Space Complexityt: O(n)\n    \"\"\"\n\n    def optimized(self, nums: List[int]) -> int:\n        Hashmap = {0: -1}\n        maxLen = 0\n        cnt = 0\n\n        for i in range(len(nums)):\n            cnt += 1 if nums[i] else -1\n            if cnt in Hashmap:\n                Len = i - Hashmap[cnt]\n                if Len > maxLen:\n                    maxLen = Len\n            else:\n                Hashmap[cnt] = i\n\n        return maxLen\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/525-contiguous-array/",
      "datePublished": "2023-03-27",
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