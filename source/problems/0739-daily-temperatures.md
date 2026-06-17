# 0739-daily-temperatures


Try it on <a href='https://leetcode.com/problems/0739-daily-temperatures'>leetcode</a>

## Description
<div class="description">
<p>Given an array of integers <code>temperatures</code> represents the daily temperatures, return <em>an array</em> <code>answer</code> <em>such that</em> <code>answer[i]</code> <em>is the number of days you have to wait after the</em> <code>i<sup>th</sup></code> <em>day to get a warmer temperature</em>. If there is no future day for which this is possible, keep <code>answer[i] == 0</code> instead.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> temperatures = [73,74,75,71,69,72,76,73]
<strong>Output:</strong> [1,1,4,2,1,1,0,0]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> temperatures = [30,40,50,60]
<strong>Output:</strong> [1,1,1,0]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> temperatures = [30,60,90]
<strong>Output:</strong> [1,1,0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;temperatures.length &lt;= 10<sup>5</sup></code></li>
	<li><code>30 &lt;=&nbsp;temperatures[i] &lt;= 100</code></li>
</ul>

</div>

## Solution(Python)
```Python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return self.monotonic_stack(temperatures)
    # bruteforce
    #   as we read through  each temperature
    #     i will count until something is greater
    # Time Complexity: O(n^2)
    # Space complexity: O(1)

    # montonic stack
    #  use stack to keep track of previous temperature with lower index
    #  once i found that my current temparture is greater then i will store the result
    #
    def monotonic_stack(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        # stack empty
        stack = []
        # result array with zero
        res = [0] * n
        # loop through 
        for i in range(n):
        #   compare the temp index in the stac k with current temperature if greater then update the result of stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
        #    pop it 
                stack.pop()
        #   append my current index to stack
            stack.append(i)
        return res
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "739. Daily Temperatures",
    "text": "Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.\n\u00a0\nExample 1:\nInput: temperatures = [73,74,75,71,69,72,76,73]\nOutput: [1,1,4,2,1,1,0,0]\nExample 2:\nInput: temperatures = [30,40,50,60]\nOutput: [1,1,1,0]\nExample 3:\nInput: temperatures = [30,60,90]\nOutput: [1,1,0]\n\n\u00a0\nConstraints:\n\n1 <=\u00a0temperatures.length <= 105\n30 <=\u00a0temperatures[i] <= 100\n\n",
    "url": "https://leetcode.com/problems/0739-daily-temperatures",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:\n        return self.monotonic_stack(temperatures)\n    # bruteforce\n    #   as we read through  each temperature\n    #     i will count until something is greater\n    # Time Complexity: O(n^2)\n    # Space complexity: O(1)\n\n    # montonic stack\n    #  use stack to keep track of previous temperature with lower index\n    #  once i found that my current temparture is greater then i will store the result\n    #\n    def monotonic_stack(self, temperatures: List[int]) -> List[int]:\n        n = len(temperatures)\n        # stack empty\n        stack = []\n        # result array with zero\n        res = [0] * n\n        # loop through \n        for i in range(n):\n        #   compare the temp index in the stac k with current temperature if greater then update the result of stack\n            while stack and temperatures[i] > temperatures[stack[-1]]:\n                res[stack[-1]] = i - stack[-1]\n        #    pop it \n                stack.pop()\n        #   append my current index to stack\n            stack.append(i)\n        return res",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/0739-daily-temperatures/",
      "datePublished": "2025-05-13",
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