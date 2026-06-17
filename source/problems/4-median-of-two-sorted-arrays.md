# 4-median-of-two-sorted-arrays


Try it on <a href='https://leetcode.com/problems/4-median-of-two-sorted-arrays'>leetcode</a>

## Description
<div class="description">
<div><p>Given two sorted arrays <code>nums1</code> and <code>nums2</code> of size <code>m</code> and <code>n</code> respectively, return <strong>the median</strong> of the two sorted arrays.</p>

<p>The overall run time complexity should be <code>O(log (m+n))</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums1 = [1,3], nums2 = [2]
<strong>Output:</strong> 2.00000
<strong>Explanation:</strong> merged array = [1,2,3] and median is 2.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums1 = [1,2], nums2 = [3,4]
<strong>Output:</strong> 2.50000
<strong>Explanation:</strong> merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>nums1.length == m</code></li>
	<li><code>nums2.length == n</code></li>
	<li><code>0 &lt;= m &lt;= 1000</code></li>
	<li><code>0 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= m + n &lt;= 2000</code></li>
	<li><code>-10<sup>6</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup>6</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.OptmialbinarySeach(nums1, nums2)

    # Time Complexity: O(m+n)
    # Space Complexity: O(m+n)
    def bruteforce(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        nums1 = nums1[:] + [0] * m

        i = n - 1
        j = m - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1

            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        l = m + n
        mid = l // 2
        print(nums1)
        if l % 2 == 0:
            return (nums1[mid] + nums1[mid - 1]) / 2
        else:
            return nums1[mid]

    # Time Complexity: O(log(m+n))
    def binarySeach(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.0

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2, len(b) // 2
        ma, mb = a[ia], b[ib]

        # when k is bigger than the sum of a and b's median indices
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)

    # Time Complexity: O(min(log(m),log(n))))
    def OptmialbinarySeach(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.0

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2, len(b) // 2
        ma, mb = a[ia], b[ib]

        # when k is bigger than the sum of a and b's median indices
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "4. Median of Two Sorted Arrays",
    "text": "Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.\nThe overall run time complexity should be O(log (m+n)).\n\u00a0\nExample 1:\nInput: nums1 = [1,3], nums2 = [2]\nOutput: 2.00000\nExplanation: merged array = [1,2,3] and median is 2.\n\nExample 2:\nInput: nums1 = [1,2], nums2 = [3,4]\nOutput: 2.50000\nExplanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.\n\n\u00a0\nConstraints:\n\nnums1.length == m\nnums2.length == n\n0 <= m <= 1000\n0 <= n <= 1000\n1 <= m + n <= 2000\n-106 <= nums1[i], nums2[i] <= 106\n\n",
    "url": "https://leetcode.com/problems/4-median-of-two-sorted-arrays",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:\n        return self.OptmialbinarySeach(nums1, nums2)\n\n    # Time Complexity: O(m+n)\n    # Space Complexity: O(m+n)\n    def bruteforce(self, nums1: List[int], nums2: List[int]) -> float:\n        n = len(nums1)\n        m = len(nums2)\n\n        nums1 = nums1[:] + [0] * m\n\n        i = n - 1\n        j = m - 1\n        k = m + n - 1\n\n        while i >= 0 and j >= 0:\n            if nums1[i] > nums2[j]:\n                nums1[k] = nums1[i]\n                i -= 1\n                k -= 1\n\n            else:\n                nums1[k] = nums2[j]\n                j -= 1\n                k -= 1\n        while j >= 0:\n            nums1[k] = nums2[j]\n            j -= 1\n            k -= 1\n\n        l = m + n\n        mid = l // 2\n        print(nums1)\n        if l % 2 == 0:\n            return (nums1[mid] + nums1[mid - 1]) / 2\n        else:\n            return nums1[mid]\n\n    # Time Complexity: O(log(m+n))\n    def binarySeach(self, A, B):\n        l = len(A) + len(B)\n        if l % 2 == 1:\n            return self.kth(A, B, l // 2)\n        else:\n            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.0\n\n    def kth(self, a, b, k):\n        if not a:\n            return b[k]\n        if not b:\n            return a[k]\n        ia, ib = len(a) // 2, len(b) // 2\n        ma, mb = a[ia], b[ib]\n\n        # when k is bigger than the sum of a and b's median indices\n        if ia + ib < k:\n            # if a's median is bigger than b's, b's first half doesn't include k\n            if ma > mb:\n                return self.kth(a, b[ib + 1:], k - ib - 1)\n            else:\n                return self.kth(a[ia + 1:], b, k - ia - 1)\n        # when k is smaller than the sum of a and b's indices\n        else:\n            # if a's median is bigger than b's, a's second half doesn't include k\n            if ma > mb:\n                return self.kth(a[:ia], b, k)\n            else:\n                return self.kth(a, b[:ib], k)\n\n    # Time Complexity: O(min(log(m),log(n))))\n    def OptmialbinarySeach(self, A, B):\n        l = len(A) + len(B)\n        if l % 2 == 1:\n            return self.kth(A, B, l // 2)\n        else:\n            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.0\n\n    def kth(self, a, b, k):\n        if not a:\n            return b[k]\n        if not b:\n            return a[k]\n        ia, ib = len(a) // 2, len(b) // 2\n        ma, mb = a[ia], b[ib]\n\n        # when k is bigger than the sum of a and b's median indices\n        if ia + ib < k:\n            # if a's median is bigger than b's, b's first half doesn't include k\n            if ma > mb:\n                return self.kth(a, b[ib + 1:], k - ib - 1)\n            else:\n                return self.kth(a[ia + 1:], b, k - ia - 1)\n        # when k is smaller than the sum of a and b's indices\n        else:\n            # if a's median is bigger than b's, a's second half doesn't include k\n            if ma > mb:\n                return self.kth(a[:ia], b, k)\n            else:\n                return self.kth(a, b[:ib], k)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/4-median-of-two-sorted-arrays/",
      "datePublished": "2024-01-19",
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