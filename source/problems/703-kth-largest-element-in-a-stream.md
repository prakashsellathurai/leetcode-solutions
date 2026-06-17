# 703-kth-largest-element-in-a-stream


Try it on <a href='https://leetcode.com/problems/703-kth-largest-element-in-a-stream'>leetcode</a>

## Description
<div class="description">
<div><p>Design a class to find the <code>k<sup>th</sup></code> largest element in a stream. Note that it is the <code>k<sup>th</sup></code> largest element in the sorted order, not the <code>k<sup>th</sup></code> distinct element.</p>

<p>Implement <code>KthLargest</code> class:</p>

<ul>
	<li><code>KthLargest(int k, int[] nums)</code> Initializes the object with the integer <code>k</code> and the stream of integers <code>nums</code>.</li>
	<li><code>int add(int val)</code> Appends the integer <code>val</code> to the stream and returns the element representing the <code>k<sup>th</sup></code> largest element in the stream.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input</strong>
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
<strong>Output</strong>
[null, 4, 5, 5, 8, 8]

<strong>Explanation</strong>
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= val &lt;= 10<sup>4</sup></code></li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>add</code>.</li>
	<li>It is guaranteed that there will be at least <code>k</code> elements in the array when you search for the <code>k<sup>th</sup></code> element.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.pq = nums[:k].copy()
        self.k = k

        n = len(nums)
        heapq.heapify(self.pq)
        for i in range(k, n):
            heapq.heappushpop(self.pq, nums[i])

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)
        if len(self.pq) > self.k:
            heapq.heappop(self.pq)
        return self.pq[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "703. Kth Largest Element in a Stream",
    "text": "Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.\nImplement KthLargest class:\n\nKthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.\nint add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.\n\n\u00a0\nExample 1:\nInput\n[\"KthLargest\", \"add\", \"add\", \"add\", \"add\", \"add\"]\n[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]\nOutput\n[null, 4, 5, 5, 8, 8]\n\nExplanation\nKthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);\nkthLargest.add(3);   // return 4\nkthLargest.add(5);   // return 5\nkthLargest.add(10);  // return 5\nkthLargest.add(9);   // return 8\nkthLargest.add(4);   // return 8\n\n\u00a0\nConstraints:\n\n1 <= k <= 104\n0 <= nums.length <= 104\n-104 <= nums[i] <= 104\n-104 <= val <= 104\nAt most 104 calls will be made to add.\nIt is guaranteed that there will be at least k elements in the array when you search for the kth element.\n\n",
    "url": "https://leetcode.com/problems/703-kth-largest-element-in-a-stream",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "import heapq\n\n\nclass KthLargest:\n    def __init__(self, k: int, nums: List[int]):\n        self.pq = nums[:k].copy()\n        self.k = k\n\n        n = len(nums)\n        heapq.heapify(self.pq)\n        for i in range(k, n):\n            heapq.heappushpop(self.pq, nums[i])\n\n    def add(self, val: int) -> int:\n        heapq.heappush(self.pq, val)\n        if len(self.pq) > self.k:\n            heapq.heappop(self.pq)\n        return self.pq[0]\n\n\n# Your KthLargest object will be instantiated and called as such:\n# obj = KthLargest(k, nums)\n# param_1 = obj.add(val)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/703-kth-largest-element-in-a-stream/",
      "datePublished": "2023-10-04",
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