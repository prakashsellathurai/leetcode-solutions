# 412-fizz-buzz


Try it on <a href='https://leetcode.com/problems/412-fizz-buzz'>leetcode</a>

## Description
<div class="description">
<div><p>Given an integer <code>n</code>, return <em>a string array </em><code>answer</code><em> (<strong>1-indexed</strong>) where</em>:</p>

<ul>
	<li><code>answer[i] == "FizzBuzz"</code> if <code>i</code> is divisible by <code>3</code> and <code>5</code>.</li>
	<li><code>answer[i] == "Fizz"</code> if <code>i</code> is divisible by <code>3</code>.</li>
	<li><code>answer[i] == "Buzz"</code> if <code>i</code> is divisible by <code>5</code>.</li>
	<li><code>answer[i] == i</code> (as a string) if none of the above conditions are true.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> ["1","2","Fizz"]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> n = 5
<strong>Output:</strong> ["1","2","Fizz","4","Buzz"]
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> n = 15
<strong>Output:</strong> ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            if i % 3 ==0 and  i%5 == 0:
                res.append("FizzBuzz")
            elif i % 3 ==0 :
                res.append("Fizz")
            elif i % 5 ==0 :
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
                
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "412. Fizz Buzz",
    "text": "Given an integer n, return a string array answer (1-indexed) where:\n\nanswer[i] == \"FizzBuzz\" if i is divisible by 3 and 5.\nanswer[i] == \"Fizz\" if i is divisible by 3.\nanswer[i] == \"Buzz\" if i is divisible by 5.\nanswer[i] == i (as a string) if none of the above conditions are true.\n\n\u00a0\nExample 1:\nInput: n = 3\nOutput: [\"1\",\"2\",\"Fizz\"]\nExample 2:\nInput: n = 5\nOutput: [\"1\",\"2\",\"Fizz\",\"4\",\"Buzz\"]\nExample 3:\nInput: n = 15\nOutput: [\"1\",\"2\",\"Fizz\",\"4\",\"Buzz\",\"Fizz\",\"7\",\"8\",\"Fizz\",\"Buzz\",\"11\",\"Fizz\",\"13\",\"14\",\"FizzBuzz\"]\n\n\u00a0\nConstraints:\n\n1 <= n <= 104\n\n",
    "url": "https://leetcode.com/problems/412-fizz-buzz",
    "answerCount": 1,
    "datePublished": "2023-11-26T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def fizzBuzz(self, n: int) -> List[str]:\n        res = []\n        for i in range(1,n+1):\n            if i % 3 ==0 and  i%5 == 0:\n                res.append(\"FizzBuzz\")\n            elif i % 3 ==0 :\n                res.append(\"Fizz\")\n            elif i % 5 ==0 :\n                res.append(\"Buzz\")\n            else:\n                res.append(str(i))\n        return res\n                ",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/412-fizz-buzz/",
      "datePublished": "2023-11-26T00:00:00Z",
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