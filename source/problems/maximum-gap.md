# maximum-gap


Try it on <a href='https://leetcode.com/problems/maximum-gap'>leetcode</a>

## Description
<div class="description">
<div><p>Given an integer array <code>nums</code>, return <em>the maximum difference between two successive elements in its sorted form</em>. If the array contains less than two elements, return <code>0</code>.</p>

<p>You must write an algorithm that runs in linear time and uses linear extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [3,6,9,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [10]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The array contains less than 2 elements, therefore return 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        return self.bucketSort(nums)
    #Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def naiveApproach(self, nums: List[int]) -> int:
        max_diff = 0
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            max_diff = max(max_diff, nums[i]-nums[i-1])
        return max_diff
     
    #Time Complexity: O(n+K)
    # Space Complexity: O(K)
    def countingSortApproach(self, nums: List[int]) -> int:
        min_val, max_val = min(nums), max(nums)
        count = [0] * (max_val - min_val + 1)
        
        for num in nums:
            count[num-min_val]+=1
        result = []
        for i, c in enumerate(count):
            result.extend([i + min_val] * c)
        max_diff = 0
        n = len(nums)
        for i in range(1, n):
            max_diff = max(max_diff, result[i]-result[i-1])
        return max_diff
    
    def radixSort(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        maxVal = max(nums)
        exp = 1
        radix = 10
        aux = [0] * len(nums)

        while maxVal // exp > 0:
            count = [0] * radix
            for num in nums:
                count[(num // exp) % 10] += 1
            for i in range(1, radix):
                count[i] += count[i - 1]
            i = len(nums) - 1
            while i >= 0:
                aux[count[(nums[i] // exp) % 10] - 1] = nums[i]
                count[(nums[i] // exp) % 10] -= 1
                i -= 1
            for i in range(len(nums)):
                nums[i] = aux[i]
            exp *= 10

        maxGap = 0
        for i in range(len(nums) - 1):
            maxGap = max(nums[i + 1] - nums[i], maxGap)
        return maxGap
    
     #Time Complexity: O(n)
    # Space Complexity: O(n)   
    def bucketSort(self, nums):
        if len(nums) < 2:
            return 0

        mini, maxi = min(nums), max(nums)

        bucketSize = max(1, (maxi - mini) // (len(nums) - 1))
        bucketNum = (maxi - mini) // bucketSize + 1
        buckets = [Bucket() for _ in range(bucketNum)]

        for num in nums:
            idx = (num - mini) // bucketSize
            buckets[idx].used = True
            buckets[idx].minval = min(num, buckets[idx].minval)
            buckets[idx].maxval = max(num, buckets[idx].maxval)

        prevBucketMax = mini
        maxGap = 0
        for bucket in buckets:
            if not bucket.used:
                continue

            maxGap = max(maxGap, bucket.minval - prevBucketMax)
            prevBucketMax = bucket.maxval

        return maxGap
    
class Bucket:
    def __init__(self):
        self.used = False
        self.minval = float("inf")
        self.maxval = float("-inf")
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": " \u00a0Maximum Gap",
    "text": "Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.\nYou must write an algorithm that runs in linear time and uses linear extra space.\n\u00a0\nExample 1:\nInput: nums = [3,6,9,1]\nOutput: 3\nExplanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.\n\nExample 2:\nInput: nums = [10]\nOutput: 0\nExplanation: The array contains less than 2 elements, therefore return 0.\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 105\n0 <= nums[i] <= 109\n\n",
    "url": "https://leetcode.com/problems/maximum-gap",
    "answerCount": 1,
    "datePublished": "2024-06-23T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def maximumGap(self, nums: List[int]) -> int:\n        return self.bucketSort(nums)\n    #Time Complexity: O(n^2)\n    # Space Complexity: O(1)\n    def naiveApproach(self, nums: List[int]) -> int:\n        max_diff = 0\n        nums.sort()\n        n = len(nums)\n        for i in range(1, n):\n            max_diff = max(max_diff, nums[i]-nums[i-1])\n        return max_diff\n     \n    #Time Complexity: O(n+K)\n    # Space Complexity: O(K)\n    def countingSortApproach(self, nums: List[int]) -> int:\n        min_val, max_val = min(nums), max(nums)\n        count = [0] * (max_val - min_val + 1)\n        \n        for num in nums:\n            count[num-min_val]+=1\n        result = []\n        for i, c in enumerate(count):\n            result.extend([i + min_val] * c)\n        max_diff = 0\n        n = len(nums)\n        for i in range(1, n):\n            max_diff = max(max_diff, result[i]-result[i-1])\n        return max_diff\n    \n    def radixSort(self, nums: List[int]) -> int:\n        if len(nums) < 2:\n            return 0\n\n        maxVal = max(nums)\n        exp = 1\n        radix = 10\n        aux = [0] * len(nums)\n\n        while maxVal // exp > 0:\n            count = [0] * radix\n            for num in nums:\n                count[(num // exp) % 10] += 1\n            for i in range(1, radix):\n                count[i] += count[i - 1]\n            i = len(nums) - 1\n            while i >= 0:\n                aux[count[(nums[i] // exp) % 10] - 1] = nums[i]\n                count[(nums[i] // exp) % 10] -= 1\n                i -= 1\n            for i in range(len(nums)):\n                nums[i] = aux[i]\n            exp *= 10\n\n        maxGap = 0\n        for i in range(len(nums) - 1):\n            maxGap = max(nums[i + 1] - nums[i], maxGap)\n        return maxGap\n    \n     #Time Complexity: O(n)\n    # Space Complexity: O(n)   \n    def bucketSort(self, nums):\n        if len(nums) < 2:\n            return 0\n\n        mini, maxi = min(nums), max(nums)\n\n        bucketSize = max(1, (maxi - mini) // (len(nums) - 1))\n        bucketNum = (maxi - mini) // bucketSize + 1\n        buckets = [Bucket() for _ in range(bucketNum)]\n\n        for num in nums:\n            idx = (num - mini) // bucketSize\n            buckets[idx].used = True\n            buckets[idx].minval = min(num, buckets[idx].minval)\n            buckets[idx].maxval = max(num, buckets[idx].maxval)\n\n        prevBucketMax = mini\n        maxGap = 0\n        for bucket in buckets:\n            if not bucket.used:\n                continue\n\n            maxGap = max(maxGap, bucket.minval - prevBucketMax)\n            prevBucketMax = bucket.maxval\n\n        return maxGap\n    \nclass Bucket:\n    def __init__(self):\n        self.used = False\n        self.minval = float(\"inf\")\n        self.maxval = float(\"-inf\")",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/maximum-gap/",
      "datePublished": "2024-06-23T00:00:00Z",
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