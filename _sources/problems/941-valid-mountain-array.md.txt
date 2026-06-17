# 941-valid-mountain-array


Try it on <a href='https://leetcode.com/problems/941-valid-mountain-array'>leetcode</a>

## Description
<div class="description">
<div><p>Given an array of integers <code>arr</code>, return <em><code>true</code> if and only if it is a valid mountain array</em>.</p>

<p>Recall that arr is a mountain array if and only if:</p>

<ul>
	<li><code>arr.length &gt;= 3</code></li>
	<li>There exists some <code>i</code> with <code>0 &lt; i &lt; arr.length - 1</code> such that:
	<ul>
		<li><code>arr[0] &lt; arr[1] &lt; ... &lt; arr[i - 1] &lt; arr[i] </code></li>
		<li><code>arr[i] &gt; arr[i + 1] &gt; ... &gt; arr[arr.length - 1]</code></li>
	</ul>
	</li>
</ul>
<img src="https://assets.leetcode.com/uploads/2019/10/20/hint_valid_mountain_array.png" width="500">
<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> arr = [2,1]
<strong>Output:</strong> false
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> arr = [3,5,5]
<strong>Output:</strong> false
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> arr = [0,3,2,1]
<strong>Output:</strong> true
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>4</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        i = 0

        while i < n - 1 and arr[i] < arr[i + 1]:
            i += 1

        if i == 0 or i == n - 1:
            return False

        while i < n - 1 and arr[i] > arr[i + 1]:
            i += 1
        return i == n - 1

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "941. Valid Mountain Array",
    "text": "Given an array of integers arr, return true if and only if it is a valid mountain array.\nRecall that arr is a mountain array if and only if:\n\narr.length >= 3\nThere exists some i with 0 < i < arr.length - 1 such that:\n\t\narr[0] < arr[1] < ... < arr[i - 1] < arr[i] \narr[i] > arr[i + 1] > ... > arr[arr.length - 1]\n\n\n\n\n\u00a0\nExample 1:\nInput: arr = [2,1]\nOutput: false\nExample 2:\nInput: arr = [3,5,5]\nOutput: false\nExample 3:\nInput: arr = [0,3,2,1]\nOutput: true\n\n\u00a0\nConstraints:\n\n1 <= arr.length <= 104\n0 <= arr[i] <= 104\n\n",
    "url": "https://leetcode.com/problems/941-valid-mountain-array",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def validMountainArray(self, arr: List[int]) -> bool:\n        n = len(arr)\n        if n < 3:\n            return False\n        i = 0\n\n        while i < n - 1 and arr[i] < arr[i + 1]:\n            i += 1\n\n        if i == 0 or i == n - 1:\n            return False\n\n        while i < n - 1 and arr[i] > arr[i + 1]:\n            i += 1\n        return i == n - 1\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/941-valid-mountain-array/",
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