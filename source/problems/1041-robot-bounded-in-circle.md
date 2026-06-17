# 1041-robot-bounded-in-circle


Try it on <a href='https://leetcode.com/problems/1041-robot-bounded-in-circle'>leetcode</a>

## Description
<div class="description">
<div><p>On an infinite plane, a robot initially stands at <code>(0, 0)</code> and faces north. The robot can receive one of three instructions:</p>

<ul>
	<li><code>"G"</code>: go straight 1 unit;</li>
	<li><code>"L"</code>: turn 90 degrees to the left;</li>
	<li><code>"R"</code>: turn 90 degrees to the right.</li>
</ul>

<p>The robot performs the <code>instructions</code> given in order, and repeats them forever.</p>

<p>Return <code>true</code> if and only if there exists a circle in the plane such that the robot never leaves the circle.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> instructions = "GGLLGG"
<strong>Output:</strong> true
<strong>Explanation:</strong> The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> instructions = "GG"
<strong>Output:</strong> false
<strong>Explanation:</strong> The robot moves north indefinitely.</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> instructions = "GL"
<strong>Output:</strong> true
<strong>Explanation:</strong> The robot moves from (0, 0) -&gt; (0, 1) -&gt; (-1, 1) -&gt; (-1, 0) -&gt; (0, 0) -&gt; ...</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= instructions.length &lt;= 100</code></li>
	<li><code>instructions[i]</code> is <code>'G'</code>, <code>'L'</code> or, <code>'R'</code>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def isRobotBounded(self, instructions):
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == "R":
                dx, dy = dy, -dx
            if i == "L":
                dx, dy = -dy, dx
            if i == "G":
                x, y = x + dx, y + dy
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1041. Robot Bounded In Circle",
    "text": "On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:\n\n\"G\": go straight 1 unit;\n\"L\": turn 90 degrees to the left;\n\"R\": turn 90 degrees to the right.\n\nThe robot performs the instructions given in order, and repeats them forever.\nReturn true if and only if there exists a circle in the plane such that the robot never leaves the circle.\n\u00a0\nExample 1:\nInput: instructions = \"GGLLGG\"\nOutput: true\nExplanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).\nWhen repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.\nExample 2:\nInput: instructions = \"GG\"\nOutput: false\nExplanation: The robot moves north indefinitely.\nExample 3:\nInput: instructions = \"GL\"\nOutput: true\nExplanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...\n\u00a0\nConstraints:\n\n1 <= instructions.length <= 100\ninstructions[i] is 'G', 'L' or, 'R'.\n\n",
    "url": "https://leetcode.com/problems/1041-robot-bounded-in-circle",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def isRobotBounded(self, instructions):\n        x, y, dx, dy = 0, 0, 0, 1\n        for i in instructions:\n            if i == \"R\":\n                dx, dy = dy, -dx\n            if i == \"L\":\n                dx, dy = -dy, dx\n            if i == \"G\":\n                x, y = x + dx, y + dy\n        return (x, y) == (0, 0) or (dx, dy) != (0, 1)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1041-robot-bounded-in-circle/",
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