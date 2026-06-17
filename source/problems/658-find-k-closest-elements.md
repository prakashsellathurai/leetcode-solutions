# 658-find-k-closest-elements


Try it on <a href='https://leetcode.com/problems/658-find-k-closest-elements'>leetcode</a>

## Description
<div class="description">
<div><p>Given a <strong>sorted</strong> integer array <code>arr</code>, two integers <code>k</code> and <code>x</code>, return the <code>k</code> closest integers to <code>x</code> in the array. The result should also be sorted in ascending order.</p>

<p>An integer <code>a</code> is closer to <code>x</code> than an integer <code>b</code> if:</p>

<ul>
	<li><code>|a - x| &lt; |b - x|</code>, or</li>
	<li><code>|a - x| == |b - x|</code> and <code>a &lt; b</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> arr = [1,2,3,4,5], k = 4, x = 3
<strong>Output:</strong> [1,2,3,4]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> arr = [1,2,3,4,5], k = 4, x = -1
<strong>Output:</strong> [1,2,3,4]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= arr.length</code></li>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code></li>
	<li><code>arr</code> is sorted in <strong>ascending</strong> order.</li>
	<li><code>-10<sup>4</sup> &lt;= arr[i], x &lt;= 10<sup>4</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "658. Find K Closest Elements",
    "text": "Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.\nAn integer a is closer to x than an integer b if:\n\n|a - x| < |b - x|, or\n|a - x| == |b - x| and a < b\n\n\u00a0\nExample 1:\nInput: arr = [1,2,3,4,5], k = 4, x = 3\nOutput: [1,2,3,4]\nExample 2:\nInput: arr = [1,2,3,4,5], k = 4, x = -1\nOutput: [1,2,3,4]\n\n\u00a0\nConstraints:\n\n1 <= k <= arr.length\n1 <= arr.length <= 104\narr is sorted in ascending order.\n-104 <= arr[i], x <= 104\n\n",
    "url": "https://leetcode.com/problems/658-find-k-closest-elements",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:\n        left, right = 0, len(arr) - k\n        while left < right:\n            mid = (left + right) // 2\n            if x - arr[mid] > arr[mid + k] - x:\n                left = mid + 1\n            else:\n                right = mid\n        return arr[left:left + k]",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/658-find-k-closest-elements/",
      "datePublished": "2024-04-20",
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