# 682-baseball-game


Try it on <a href='https://leetcode.com/problems/682-baseball-game'>leetcode</a>

## Description
<div class="description">
<div><p>You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.</p>

<p>At the beginning of the game, you start with an empty record. You are given a list of strings <code>ops</code>, where <code>ops[i]</code> is the <code>i<sup>th</sup></code> operation you must apply to the record and is one of the following:</p>

<ol>
	<li>An integer <code>x</code> - Record a new score of <code>x</code>.</li>
	<li><code>"+"</code> - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.</li>
	<li><code>"D"</code> - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.</li>
	<li><code>"C"</code> - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.</li>
</ol>

<p>Return <em>the sum of all the scores on the record</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> ops = ["5","2","C","D","+"]
<strong>Output:</strong> 30
<strong>Explanation:</strong>
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> ops = ["5","-2","4","C","D","9","+","+"]
<strong>Output:</strong> 27
<strong>Explanation:</strong>
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> ops = ["1"]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= ops.length &lt;= 1000</code></li>
	<li><code>ops[i]</code> is <code>"C"</code>, <code>"D"</code>, <code>"+"</code>, or a string representing an integer in the range <code>[-3 * 10<sup>4</sup>, 3 * 10<sup>4</sup>]</code>.</li>
	<li>For operation <code>"+"</code>, there will always be at least two previous scores on the record.</li>
	<li>For operations <code>"C"</code> and <code>"D"</code>, there will always be at least one previous score on the record.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []

        for op in ops:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "C":
                stack.pop()

            elif op == "D":
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))
        return sum(stack)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "682. Baseball Game",
    "text": "You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.\nAt the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:\n\nAn integer x - Record a new score of x.\n\"+\" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.\n\"D\" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.\n\"C\" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.\n\nReturn the sum of all the scores on the record.\n\u00a0\nExample 1:\nInput: ops = [\"5\",\"2\",\"C\",\"D\",\"+\"]\nOutput: 30\nExplanation:\n\"5\" - Add 5 to the record, record is now [5].\n\"2\" - Add 2 to the record, record is now [5, 2].\n\"C\" - Invalidate and remove the previous score, record is now [5].\n\"D\" - Add 2 * 5 = 10 to the record, record is now [5, 10].\n\"+\" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].\nThe total sum is 5 + 10 + 15 = 30.\n\nExample 2:\nInput: ops = [\"5\",\"-2\",\"4\",\"C\",\"D\",\"9\",\"+\",\"+\"]\nOutput: 27\nExplanation:\n\"5\" - Add 5 to the record, record is now [5].\n\"-2\" - Add -2 to the record, record is now [5, -2].\n\"4\" - Add 4 to the record, record is now [5, -2, 4].\n\"C\" - Invalidate and remove the previous score, record is now [5, -2].\n\"D\" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].\n\"9\" - Add 9 to the record, record is now [5, -2, -4, 9].\n\"+\" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].\n\"+\" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].\nThe total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.\n\nExample 3:\nInput: ops = [\"1\"]\nOutput: 1\n\n\u00a0\nConstraints:\n\n1 <= ops.length <= 1000\nops[i] is \"C\", \"D\", \"+\", or a string representing an integer in the range [-3 * 104, 3 * 104].\nFor operation \"+\", there will always be at least two previous scores on the record.\nFor operations \"C\" and \"D\", there will always be at least one previous score on the record.\n\n",
    "url": "https://leetcode.com/problems/682-baseball-game",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def calPoints(self, ops: List[str]) -> int:\n        stack = []\n\n        for op in ops:\n            if op == \"+\":\n                stack.append(stack[-1] + stack[-2])\n            elif op == \"C\":\n                stack.pop()\n\n            elif op == \"D\":\n                stack.append(2 * stack[-1])\n            else:\n                stack.append(int(op))\n        return sum(stack)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/682-baseball-game/",
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