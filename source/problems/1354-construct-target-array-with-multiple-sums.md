# 1354-construct-target-array-with-multiple-sums


Try it on <a href='https://leetcode.com/problems/1354-construct-target-array-with-multiple-sums'>leetcode</a>

## Description
<div class="description">
<p>You are given an array <code>target</code> of n integers. From a starting array <code>arr</code> consisting of <code>n</code> 1&#39;s, you may perform the following procedure :</p>

<ul>
	<li>let <code>x</code> be the sum of all elements currently in your array.</li>
	<li>choose index <code>i</code>, such that <code>0 &lt;= i &lt; n</code> and set the value of <code>arr</code> at index <code>i</code> to <code>x</code>.</li>
	<li>You may repeat this procedure as many times as needed.</li>
</ul>

<p>Return <code>true</code> <em>if it is possible to construct the</em> <code>target</code> <em>array from</em> <code>arr</code><em>, otherwise, return</em> <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> target = [9,3,5]
<strong>Output:</strong> true
<strong>Explanation:</strong> Start with arr = [1, 1, 1] 
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> target = [1,1,1,2]
<strong>Output:</strong> false
<strong>Explanation:</strong> Impossible to create target array from [1,1,1,1].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> target = [8,5]
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == target.length</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= target[i] &lt;= 10<sup>9</sup></code></li>
</ul>

</div>

## Solution(Python)
```Python
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1

        total_sum = sum(target)
        # Use a min-heap by pushing negative values to simulate a max-heap
        max_heap = [-num for num in target]
        heapq.heapify(max_heap)

        while -max_heap[0] > 1:
            max_val = -heapq.heappop(max_heap)
            rest_sum = total_sum - max_val

            # Edge cases and impossibility checks
            if rest_sum == 1:
                return True
            if rest_sum == 0 or max_val <= rest_sum:
                return False

            # Calculate the previous value using modulo
            prev_val = max_val% rest_sum
            
            # If prev_val is 0, it indicates an impossible state
            if prev_val == 0:
                return False

            total_sum = rest_sum + prev_val
            heapq.heappush(max_heap, -prev_val)

        return True
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1354. Construct Target Array With Multiple Sums",
    "text": "You are given an array target of n integers. From a starting array arr consisting of n 1's, you may perform the following procedure :\n\nlet x be the sum of all elements currently in your array.\nchoose index i, such that 0 <= i < n and set the value of arr at index i to x.\nYou may repeat this procedure as many times as needed.\n\nReturn true if it is possible to construct the target array from arr, otherwise, return false.\n\u00a0\nExample 1:\n\nInput: target = [9,3,5]\nOutput: true\nExplanation: Start with arr = [1, 1, 1] \n[1, 1, 1], sum = 3 choose index 1\n[1, 3, 1], sum = 5 choose index 2\n[1, 3, 5], sum = 9 choose index 0\n[9, 3, 5] Done\n\nExample 2:\n\nInput: target = [1,1,1,2]\nOutput: false\nExplanation: Impossible to create target array from [1,1,1,1].\n\nExample 3:\n\nInput: target = [8,5]\nOutput: true\n\n\u00a0\nConstraints:\n\nn == target.length\n1 <= n <= 5 * 104\n1 <= target[i] <= 109\n\n",
    "url": "https://leetcode.com/problems/1354-construct-target-array-with-multiple-sums",
    "answerCount": 1,
    "datePublished": "2022-01-05T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def isPossible(self, target: List[int]) -> bool:\n        if len(target) == 1:\n            return target[0] == 1\n\n        total_sum = sum(target)\n        # Use a min-heap by pushing negative values to simulate a max-heap\n        max_heap = [-num for num in target]\n        heapq.heapify(max_heap)\n\n        while -max_heap[0] > 1:\n            max_val = -heapq.heappop(max_heap)\n            rest_sum = total_sum - max_val\n\n            # Edge cases and impossibility checks\n            if rest_sum == 1:\n                return True\n            if rest_sum == 0 or max_val <= rest_sum:\n                return False\n\n            # Calculate the previous value using modulo\n            prev_val = max_val% rest_sum\n            \n            # If prev_val is 0, it indicates an impossible state\n            if prev_val == 0:\n                return False\n\n            total_sum = rest_sum + prev_val\n            heapq.heappush(max_heap, -prev_val)\n\n        return True",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1354-construct-target-array-with-multiple-sums/",
      "datePublished": "2022-01-05T00:00:00Z",
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