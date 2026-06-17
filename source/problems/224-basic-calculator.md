# 224-basic-calculator


Try it on <a href='https://leetcode.com/problems/224-basic-calculator'>leetcode</a>

## Description
<div class="description">
<div><p>Given a string <code>s</code> representing a valid expression, implement a basic calculator to evaluate it, and return <em>the result of the evaluation</em>.</p>

<p><strong>Note:</strong> You are <strong>not</strong> allowed to use any built-in function which evaluates strings as mathematical expressions, such as <code>eval()</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "1 + 1"
<strong>Output:</strong> 2
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = " 2-1 + 2 "
<strong>Output:</strong> 3
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "(1+(4+5+2)-3)+(6+8)"
<strong>Output:</strong> 23
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists of digits, <code>'+'</code>, <code>'-'</code>, <code>'('</code>, <code>')'</code>, and <code>' '</code>.</li>
	<li><code>s</code> represents a valid expression.</li>
	<li><code>'+'</code> is <strong>not</strong> used as a unary operation (i.e., <code>"+1"</code> and <code>"+(2 + 3)"</code> is invalid).</li>
	<li><code>'-'</code> could be used as a unary operation (i.e., <code>"-1"</code> and <code>"-(2 + 3)"</code> is valid).</li>
	<li>There will be no two consecutive operators in the input.</li>
	<li>Every number and running calculation will fit in a signed 32-bit integer.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        number = 0
        sign = 1

        for c in s:
            if c.isdigit():
                number = 10 * number + int(c)
            elif c == "+":
                result += sign * number
                number = 0
                sign = 1
            elif c == "-":
                result += sign * number
                number = 0
                sign = -1
            elif c == "(":
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif c == ")":
                result += sign * number
                number = 0
                result *= stack.pop()
                result += stack.pop()
        if number != 0:
            result += sign * number
        return result

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "224. Basic Calculator",
    "text": "Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.\nNote: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().\n\u00a0\nExample 1:\nInput: s = \"1 + 1\"\nOutput: 2\n\nExample 2:\nInput: s = \" 2-1 + 2 \"\nOutput: 3\n\nExample 3:\nInput: s = \"(1+(4+5+2)-3)+(6+8)\"\nOutput: 23\n\n\u00a0\nConstraints:\n\n1 <= s.length <= 3 * 105\ns consists of digits, '+', '-', '(', ')', and ' '.\ns represents a valid expression.\n'+' is not used as a unary operation (i.e., \"+1\" and \"+(2 + 3)\" is invalid).\n'-' could be used as a unary operation (i.e., \"-1\" and \"-(2 + 3)\" is valid).\nThere will be no two consecutive operators in the input.\nEvery number and running calculation will fit in a signed 32-bit integer.\n\n",
    "url": "https://leetcode.com/problems/224-basic-calculator",
    "answerCount": 1,
    "datePublished": "2023-07-31T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def calculate(self, s: str) -> int:\n        stack = []\n        result = 0\n        number = 0\n        sign = 1\n\n        for c in s:\n            if c.isdigit():\n                number = 10 * number + int(c)\n            elif c == \"+\":\n                result += sign * number\n                number = 0\n                sign = 1\n            elif c == \"-\":\n                result += sign * number\n                number = 0\n                sign = -1\n            elif c == \"(\":\n                stack.append(result)\n                stack.append(sign)\n                sign = 1\n                result = 0\n            elif c == \")\":\n                result += sign * number\n                number = 0\n                result *= stack.pop()\n                result += stack.pop()\n        if number != 0:\n            result += sign * number\n        return result\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/224-basic-calculator/",
      "datePublished": "2023-07-31T00:00:00Z",
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