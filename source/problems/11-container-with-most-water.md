# 11-container-with-most-water


Try it on <a href='https://leetcode.com/problems/11-container-with-most-water'>leetcode</a>

## Description
<div class="description">
<div><p>You are given an integer array <code>height</code> of length <code>n</code>. There are <code>n</code> vertical lines drawn such that the two endpoints of the <code>i<sup>th</sup></code> line are <code>(i, 0)</code> and <code>(i, height[i])</code>.</p>

<p>Find two lines that together with the x-axis form a container, such that the container contains the most water.</p>

<p>Return <em>the maximum amount of water a container can store</em>.</p>

<p><strong>Notice</strong> that you may not slant the container.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg" style="width: 600px; height: 287px;">
<pre><strong>Input:</strong> height = [1,8,6,2,5,4,8,3,7]
<strong>Output:</strong> 49
<strong>Explanation:</strong> The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> height = [1,1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == height.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= height[i] &lt;= 10<sup>4</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        return self.twopointer(height)

    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def bruteforce(self, height: List[int]) -> int:
        n = len(height)
        maxArea = 0

        for i in range(n):
            for j in range(i + 1, n):
                area = (j - i) * min(height[j], height[i])

                if area > maxArea:
                    maxArea = area
        return maxArea

    # Time Complexity: O(n)
    # Space Complexity" O(1)
    def twopointer(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1

        maxArea = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            if area > maxArea:
                maxArea = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "11. Container With Most Water",
    "text": "You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).\nFind two lines that together with the x-axis form a container, such that the container contains the most water.\nReturn the maximum amount of water a container can store.\nNotice that you may not slant the container.\n\u00a0\nExample 1:\n\nInput: height = [1,8,6,2,5,4,8,3,7]\nOutput: 49\nExplanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.\n\nExample 2:\nInput: height = [1,1]\nOutput: 1\n\n\u00a0\nConstraints:\n\nn == height.length\n2 <= n <= 105\n0 <= height[i] <= 104\n\n",
    "url": "https://leetcode.com/problems/11-container-with-most-water",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def maxArea(self, height: List[int]) -> int:\n        return self.twopointer(height)\n\n    # Time Complexity: O(n^2)\n    # Space Complexity: O(1)\n    def bruteforce(self, height: List[int]) -> int:\n        n = len(height)\n        maxArea = 0\n\n        for i in range(n):\n            for j in range(i + 1, n):\n                area = (j - i) * min(height[j], height[i])\n\n                if area > maxArea:\n                    maxArea = area\n        return maxArea\n\n    # Time Complexity: O(n)\n    # Space Complexity\" O(1)\n    def twopointer(self, height: List[int]) -> int:\n        n = len(height)\n        left, right = 0, n - 1\n\n        maxArea = 0\n        while left < right:\n            area = (right - left) * min(height[left], height[right])\n            if area > maxArea:\n                maxArea = area\n\n            if height[left] < height[right]:\n                left += 1\n            else:\n                right -= 1\n\n        return maxArea\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/11-container-with-most-water/",
      "datePublished": "2023-06-11",
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