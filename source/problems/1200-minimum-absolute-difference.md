# 1200-minimum-absolute-difference


Try it on <a href='https://leetcode.com/problems/1200-minimum-absolute-difference'>leetcode</a>

## Description
<div class="description">
<p>Given an array of <strong>distinct</strong> integers <code>arr</code>, find all pairs of elements with the minimum absolute difference of any two elements.</p>

<p>Return a list of pairs in ascending order(with respect to pairs), each pair <code>[a, b]</code> follows</p>

<ul>
	<li><code>a, b</code> are from <code>arr</code></li>
	<li><code>a &lt; b</code></li>
	<li><code>b - a</code> equals to the minimum absolute difference of any two elements in <code>arr</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [4,2,1,3]
<strong>Output:</strong> [[1,2],[2,3],[3,4]]
<strong>Explanation: </strong>The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,3,6,10,15]
<strong>Output:</strong> [[1,3]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,8,-10,23,19,-4,-14,27]
<strong>Output:</strong> [[-14,-10],[19,23],[23,27]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>6</sup> &lt;= arr[i] &lt;= 10<sup>6</sup></code></li>
</ul>

</div>

## Solution(Python)
```Python
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        return self.CountingsortedSolution(arr)
        
        
    # Time Complexity: O(n^2)
    # Space COmplexity: O(1)
    def naiveSolution(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        result = []
        min_diff = inf
        for i in range(n):
            pair = (i, i)
            for j in range(i+1, n):
                if i == j:
                    continue
                if arr[j]-arr[i] < min_diff:
                    min_diff = arr[j]-arr[i]
        for i in range(n):
            for j in range(i+1, n):
                if i == j:
                    continue
                if arr[j]-arr[i] == min_diff:  
                    result.append((arr[i], arr[j]))
        return result
    
    # Time Complexity: O(n^logn)
    # Space COmplexity: O(1)
    def sortedSolution(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []
        mindiff = inf
        n = len(arr)
        for i in range(1, n):
            curdiff =  arr[i] - arr[i-1]

            if curdiff < mindiff:
                mindiff = curdiff
                result = [[arr[i-1], arr[i]]]
            elif curdiff == mindiff:
                result.append([arr[i-1], arr[i]])
        return result
    
    # Time Complexity: O(n+M)
    # Space COmplexity: O(M)
    def CountingsortedSolution(self, arr: List[int]) -> List[List[int]]:
        arr = self.countingSort(arr)
        result = []
        mindiff = inf
        n = len(arr)
        for i in range(1, n):
            curdiff =  arr[i] - arr[i-1]
            
            if curdiff < mindiff:
                mindiff = curdiff
                result = [[arr[i-1], arr[i]]]
            elif curdiff == mindiff:
                result.append([arr[i-1], arr[i]])
        return result
    
    def countingSort(self, nums):
        min_, max_ = min(nums), max(nums)
        count = [0] * (max_-min_+1)
        for num in nums:
            count[num-min_] += 1
        result = []
        for i, c in enumerate(count):
            result.extend([i+min_]*c)
        return result
        
    
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1200. Minimum Absolute Difference",
    "text": "Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.\nReturn a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows\n\na, b are from arr\na < b\nb - a equals to the minimum absolute difference of any two elements in arr\n\n\u00a0\nExample 1:\n\nInput: arr = [4,2,1,3]\nOutput: [[1,2],[2,3],[3,4]]\nExplanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.\nExample 2:\n\nInput: arr = [1,3,6,10,15]\nOutput: [[1,3]]\n\nExample 3:\n\nInput: arr = [3,8,-10,23,19,-4,-14,27]\nOutput: [[-14,-10],[19,23],[23,27]]\n\n\u00a0\nConstraints:\n\n2 <= arr.length <= 105\n-106 <= arr[i] <= 106\n\n",
    "url": "https://leetcode.com/problems/1200-minimum-absolute-difference",
    "answerCount": 1,
    "datePublished": "2026-03-01T16:15:16+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:\n        return self.CountingsortedSolution(arr)\n        \n        \n    # Time Complexity: O(n^2)\n    # Space COmplexity: O(1)\n    def naiveSolution(self, arr: List[int]) -> List[List[int]]:\n        n = len(arr)\n        result = []\n        min_diff = inf\n        for i in range(n):\n            pair = (i, i)\n            for j in range(i+1, n):\n                if i == j:\n                    continue\n                if arr[j]-arr[i] < min_diff:\n                    min_diff = arr[j]-arr[i]\n        for i in range(n):\n            for j in range(i+1, n):\n                if i == j:\n                    continue\n                if arr[j]-arr[i] == min_diff:  \n                    result.append((arr[i], arr[j]))\n        return result\n    \n    # Time Complexity: O(n^logn)\n    # Space COmplexity: O(1)\n    def sortedSolution(self, arr: List[int]) -> List[List[int]]:\n        arr.sort()\n        result = []\n        mindiff = inf\n        n = len(arr)\n        for i in range(1, n):\n            curdiff =  arr[i] - arr[i-1]\n\n            if curdiff < mindiff:\n                mindiff = curdiff\n                result = [[arr[i-1], arr[i]]]\n            elif curdiff == mindiff:\n                result.append([arr[i-1], arr[i]])\n        return result\n    \n    # Time Complexity: O(n+M)\n    # Space COmplexity: O(M)\n    def CountingsortedSolution(self, arr: List[int]) -> List[List[int]]:\n        arr = self.countingSort(arr)\n        result = []\n        mindiff = inf\n        n = len(arr)\n        for i in range(1, n):\n            curdiff =  arr[i] - arr[i-1]\n            \n            if curdiff < mindiff:\n                mindiff = curdiff\n                result = [[arr[i-1], arr[i]]]\n            elif curdiff == mindiff:\n                result.append([arr[i-1], arr[i]])\n        return result\n    \n    def countingSort(self, nums):\n        min_, max_ = min(nums), max(nums)\n        count = [0] * (max_-min_+1)\n        for num in nums:\n            count[num-min_] += 1\n        result = []\n        for i, c in enumerate(count):\n            result.extend([i+min_]*c)\n        return result\n        \n    ",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1200-minimum-absolute-difference/",
      "datePublished": "2026-03-01T16:15:16+05:30",
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