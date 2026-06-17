# k-closest-points-to-origin


Try it on <a href='https://leetcode.com/problems/k-closest-points-to-origin'>leetcode</a>

## Description
<div class="description">
<div><p>Given an array of <code>points</code> where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents a point on the <strong>X-Y</strong> plane and an integer <code>k</code>, return the <code>k</code> closest points to the origin <code>(0, 0)</code>.</p>

<p>The distance between two points on the <strong>X-Y</strong> plane is the Euclidean distance (i.e., <code>√(x<sub>1</sub> - x<sub>2</sub>)<sup>2</sup> + (y<sub>1</sub> - y<sub>2</sub>)<sup>2</sup></code>).</p>

<p>You may return the answer in <strong>any order</strong>. The answer is <strong>guaranteed</strong> to be <strong>unique</strong> (except for the order that it is in).</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/closestplane1.jpg" style="width: 400px; height: 400px;">
<pre><strong>Input:</strong> points = [[1,3],[-2,2]], k = 1
<strong>Output:</strong> [[-2,2]]
<strong>Explanation:</strong>
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) &lt; sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> points = [[3,3],[5,-1],[-2,4]], k = 2
<strong>Output:</strong> [[3,3],[-2,4]]
<strong>Explanation:</strong> The answer [[-2,4],[3,3]] would also be accepted.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= points.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt; x<sub>i</sub>, y<sub>i</sub> &lt; 10<sup>4</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sort the list with a custom comparator function
        points.sort(key=self.squared_distance)

        # Return the first k elements of the sorted list
        return points[:k]

    def squared_distance(self, point: List[int]) -> int:
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "973. K Closest Points to Origin",
    "text": "Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).\nThe distance between two points on the X-Y plane is the Euclidean distance (i.e., \u221a(x1 - x2)2 + (y1 - y2)2).\nYou may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).\n\u00a0\nExample 1:\n\nInput: points = [[1,3],[-2,2]], k = 1\nOutput: [[-2,2]]\nExplanation:\nThe distance between (1, 3) and the origin is sqrt(10).\nThe distance between (-2, 2) and the origin is sqrt(8).\nSince sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.\nWe only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].\n\nExample 2:\nInput: points = [[3,3],[5,-1],[-2,4]], k = 2\nOutput: [[3,3],[-2,4]]\nExplanation: The answer [[-2,4],[3,3]] would also be accepted.\n\n\u00a0\nConstraints:\n\n1 <= k <= points.length <= 104\n-104 < xi, yi < 104\n\n",
    "url": "https://leetcode.com/problems/k-closest-points-to-origin",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:\n        # Sort the list with a custom comparator function\n        points.sort(key=self.squared_distance)\n\n        # Return the first k elements of the sorted list\n        return points[:k]\n\n    def squared_distance(self, point: List[int]) -> int:\n        \"\"\"Calculate and return the squared Euclidean distance.\"\"\"\n        return point[0] ** 2 + point[1] ** 2\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/k-closest-points-to-origin/",
      "datePublished": "2022-07-23",
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