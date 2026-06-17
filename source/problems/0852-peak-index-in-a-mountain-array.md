# 0852-peak-index-in-a-mountain-array


Try it on <a href='https://leetcode.com/problems/0852-peak-index-in-a-mountain-array'>leetcode</a>

## Description
<div class="description">
<p>You are given an integer <strong>mountain</strong> array <code>arr</code> of length <code>n</code> where the values increase to a <strong>peak element</strong> and then decrease.</p>

<p>Return the index of the peak element.</p>

<p>Your task is to solve it in <code>O(log(n))</code> time complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">arr = [0,1,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">arr = [0,2,1,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">arr = [0,10,5,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>arr</code> is <strong>guaranteed</strong> to be a mountain array.</li>
</ul>

</div>

## Solution(Python)
```Python
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l = 0
        r = n-1

        while l < r:
            m = (l + r) // 2

            if arr[m] > arr[m+1]:
                r = m
            else:
                l = m + 1

        return l
        
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "852. Peak Index in a Mountain Array",
    "text": "You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.\nReturn the index of the peak element.\nYour task is to solve it in O(log(n)) time complexity.\n\u00a0\nExample 1:\n\nInput: arr = [0,1,0]\nOutput: 1\n\nExample 2:\n\nInput: arr = [0,2,1,0]\nOutput: 1\n\nExample 3:\n\nInput: arr = [0,10,5,2]\nOutput: 1\n\n\u00a0\nConstraints:\n\n3 <= arr.length <= 105\n0 <= arr[i] <= 106\narr is guaranteed to be a mountain array.\n\n",
    "url": "https://leetcode.com/problems/0852-peak-index-in-a-mountain-array",
    "answerCount": 1,
    "datePublished": "2024-12-26T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def peakIndexInMountainArray(self, arr: List[int]) -> int:\n        n = len(arr)\n        l = 0\n        r = n-1\n\n        while l < r:\n            m = (l + r) // 2\n\n            if arr[m] > arr[m+1]:\n                r = m\n            else:\n                l = m + 1\n\n        return l\n        ",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/0852-peak-index-in-a-mountain-array/",
      "datePublished": "2024-12-26T00:00:00Z",
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