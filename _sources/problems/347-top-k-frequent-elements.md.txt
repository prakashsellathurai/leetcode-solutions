# 347-top-k-frequent-elements


Try it on <a href='https://leetcode.com/problems/347-top-k-frequent-elements'>leetcode</a>

## Description
<div class="description">
<div><p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the</em> <code>k</code> <em>most frequent elements</em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,1,1,2,2,3], k = 2
<strong>Output:</strong> [1,2]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1], k = 1
<strong>Output:</strong> [1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>k</code> is in the range <code>[1, the number of unique elements in the array]</code>.</li>
	<li>It is <strong>guaranteed</strong> that the answer is <strong>unique</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Your algorithm's time complexity must be better than <code>O(n log n)</code>, where n is the array's size.</p>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.prioirtyQueue(nums, k)

    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
    def naive(self, nums: List[int], k: int) -> List[int]:
        freqmap = Counter(nums)
        freqmap = sorted(freqmap, key=freqmap.get, reverse=True)
        return freqmap[:k]

    # Time Complexity: O(nlogk)
    # Space Complexity: O(n)
    def prioirtyQueue(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        count = Counter(nums)

        return heapq.nlargest(k, count.keys(), key=count.get)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "347. Top K Frequent Elements",
    "text": "Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.\n\u00a0\nExample 1:\nInput: nums = [1,1,1,2,2,3], k = 2\nOutput: [1,2]\nExample 2:\nInput: nums = [1], k = 1\nOutput: [1]\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 105\nk is in the range [1, the number of unique elements in the array].\nIt is guaranteed that the answer is unique.\n\n\u00a0\nFollow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.\n",
    "url": "https://leetcode.com/problems/347-top-k-frequent-elements",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def topKFrequent(self, nums: List[int], k: int) -> List[int]:\n        return self.prioirtyQueue(nums, k)\n\n    # Time Complexity: O(nlogn)\n    # Space Complexity: O(n)\n    def naive(self, nums: List[int], k: int) -> List[int]:\n        freqmap = Counter(nums)\n        freqmap = sorted(freqmap, key=freqmap.get, reverse=True)\n        return freqmap[:k]\n\n    # Time Complexity: O(nlogk)\n    # Space Complexity: O(n)\n    def prioirtyQueue(self, nums: List[int], k: int) -> List[int]:\n        if k == len(nums):\n            return nums\n\n        count = Counter(nums)\n\n        return heapq.nlargest(k, count.keys(), key=count.get)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/347-top-k-frequent-elements/",
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