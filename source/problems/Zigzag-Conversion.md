# zigzag-conversion


Try it on <a href='https://leetcode.com/problems/zigzag-conversion'>leetcode</a>

## Description
<div class="description">
<div><p>The string <code>"PAYPALISHIRING"</code> is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)</p>

<pre>P   A   H   N
A P L S I I G
Y   I   R
</pre>

<p>And then read line by line: <code>"PAHNAPLSIIGYIR"</code></p>

<p>Write the code that will take a string and make this conversion given a number of rows:</p>

<pre>string convert(string s, int numRows);
</pre>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "PAYPALISHIRING", numRows = 3
<strong>Output:</strong> "PAHNAPLSIIGYIR"
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "PAYPALISHIRING", numRows = 4
<strong>Output:</strong> "PINALSIGYAHRPI"
<strong>Explanation:</strong>
P     I    N
A   L S  I G
Y A   H R
P     I
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "A", numRows = 1
<strong>Output:</strong> "A"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of English letters (lower-case and upper-case), <code>','</code> and <code>'.'</code>.</li>
	<li><code>1 &lt;= numRows &lt;= 1000</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows, direction, i = [[] for _ in range(numRows)], 1, 0
        for ch in s:
            rows[i].append(ch)
            i = min(numRows - 1, max(0, i + direction))
            if i == 0 or i == numRows - 1:
                direction *= -1
        return "".join("".join(row) for row in rows)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "6. Zigzag Conversion",
    "text": "The string \"PAYPALISHIRING\" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)\nP   A   H   N\nA P L S I I G\nY   I   R\n\nAnd then read line by line: \"PAHNAPLSIIGYIR\"\nWrite the code that will take a string and make this conversion given a number of rows:\nstring convert(string s, int numRows);\n\n\u00a0\nExample 1:\nInput: s = \"PAYPALISHIRING\", numRows = 3\nOutput: \"PAHNAPLSIIGYIR\"\n\nExample 2:\nInput: s = \"PAYPALISHIRING\", numRows = 4\nOutput: \"PINALSIGYAHRPI\"\nExplanation:\nP     I    N\nA   L S  I G\nY A   H R\nP     I\n\nExample 3:\nInput: s = \"A\", numRows = 1\nOutput: \"A\"\n\n\u00a0\nConstraints:\n\n1 <= s.length <= 1000\ns consists of English letters (lower-case and upper-case), ',' and '.'.\n1 <= numRows <= 1000\n\n",
    "url": "https://leetcode.com/problems/zigzag-conversion",
    "answerCount": 1,
    "datePublished": "2023-01-08T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def convert(self, s: str, numRows: int) -> str:\n        rows, direction, i = [[] for _ in range(numRows)], 1, 0\n        for ch in s:\n            rows[i].append(ch)\n            i = min(numRows - 1, max(0, i + direction))\n            if i == 0 or i == numRows - 1:\n                direction *= -1\n        return \"\".join(\"\".join(row) for row in rows)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/zigzag-conversion/",
      "datePublished": "2023-01-08T00:00:00Z",
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