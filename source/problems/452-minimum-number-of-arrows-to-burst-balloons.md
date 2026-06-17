# 452-minimum-number-of-arrows-to-burst-balloons


Try it on <a href='https://leetcode.com/problems/452-minimum-number-of-arrows-to-burst-balloons'>leetcode</a>

## Description
<div class="description">
<div><p>There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array <code>points</code> where <code>points[i] = [x<sub>start</sub>, x<sub>end</sub>]</code> denotes a balloon whose <strong>horizontal diameter</strong> stretches between <code>x<sub>start</sub></code> and <code>x<sub>end</sub></code>. You do not know the exact y-coordinates of the balloons.</p>

<p>Arrows can be shot up <strong>directly vertically</strong> (in the positive y-direction) from different points along the x-axis. A balloon with <code>x<sub>start</sub></code> and <code>x<sub>end</sub></code> is <strong>burst</strong> by an arrow shot at <code>x</code> if <code>x<sub>start</sub> &lt;= x &lt;= x<sub>end</sub></code>. There is <strong>no limit</strong> to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.</p>

<p>Given the array <code>points</code>, return <em>the <strong>minimum</strong> number of arrows that must be shot to burst all balloons</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> points = [[10,16],[2,8],[1,6],[7,12]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> points = [[1,2],[3,4],[5,6],[7,8]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> One arrow needs to be shot for each balloon for a total of 4 arrows.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> points = [[1,2],[2,3],[3,4],[4,5]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= points.length &lt;= 10<sup>5</sup></code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>-2<sup>31</sup> &lt;= x<sub>start</sub> &lt; x<sub>end</sub> &lt;= 2<sup>31</sup> - 1</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        n, count = len(points), 1
        if n == 0:
            return 0
        curr = points[0]

        for i in range(n):
            if curr[1] < points[i][0]:
                count += 1
                curr = points[i]

        return count

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "452. Minimum Number of Arrows to Burst Balloons",
    "text": "There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.\nArrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.\nGiven the array points, return the minimum number of arrows that must be shot to burst all balloons.\n\u00a0\nExample 1:\nInput: points = [[10,16],[2,8],[1,6],[7,12]]\nOutput: 2\nExplanation: The balloons can be burst by 2 arrows:\n- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].\n- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].\n\nExample 2:\nInput: points = [[1,2],[3,4],[5,6],[7,8]]\nOutput: 4\nExplanation: One arrow needs to be shot for each balloon for a total of 4 arrows.\n\nExample 3:\nInput: points = [[1,2],[2,3],[3,4],[4,5]]\nOutput: 2\nExplanation: The balloons can be burst by 2 arrows:\n- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].\n- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].\n\n\u00a0\nConstraints:\n\n1 <= points.length <= 105\npoints[i].length == 2\n-231 <= xstart < xend <= 231 - 1\n\n",
    "url": "https://leetcode.com/problems/452-minimum-number-of-arrows-to-burst-balloons",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def findMinArrowShots(self, points: List[List[int]]) -> int:\n        points.sort(key=lambda x: x[1])\n        n, count = len(points), 1\n        if n == 0:\n            return 0\n        curr = points[0]\n\n        for i in range(n):\n            if curr[1] < points[i][0]:\n                count += 1\n                curr = points[i]\n\n        return count\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/452-minimum-number-of-arrows-to-burst-balloons/",
      "datePublished": "2026-04-02",
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