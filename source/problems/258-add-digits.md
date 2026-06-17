# 258-add-digits


Try it on <a href='https://leetcode.com/problems/258-add-digits'>leetcode</a>

## Description
<div class="description">
<div><p>Given an integer <code>num</code>, repeatedly add all its digits until the result has only one digit, and return it.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> num = 38
<strong>Output:</strong> 2
<strong>Explanation:</strong> The process is
38 --&gt; 3 + 8 --&gt; 11
11 --&gt; 1 + 1 --&gt; 2 
Since 2 has only one digit, return it.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> num = 0
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= num &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you do it without any loop/recursion in <code>O(1)</code> runtime?</p>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def addDigits(self, num: int) -> int:
        return self.math(num)

    def trivialSolution(self, num: int) -> int:
        digital_root = 0
        while num > 0:
            digital_root += num % 10
            num = num // 10

            if num == 0 and digital_root > 9:
                num = digital_root
                digital_root = 0
        return digital_root

    def math(self, num: int) -> int:
        if num == 0:
            return num
        elif num % 9 == 0:
            return 9
        else:
            return num % 9

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "258. Add Digits",
    "text": "Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.\n\u00a0\nExample 1:\nInput: num = 38\nOutput: 2\nExplanation: The process is\n38 --> 3 + 8 --> 11\n11 --> 1 + 1 --> 2 \nSince 2 has only one digit, return it.\n\nExample 2:\nInput: num = 0\nOutput: 0\n\n\u00a0\nConstraints:\n\n0 <= num <= 231 - 1\n\n\u00a0\nFollow up: Could you do it without any loop/recursion in O(1) runtime?\n",
    "url": "https://leetcode.com/problems/258-add-digits",
    "answerCount": 1,
    "datePublished": "2022-09-08T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def addDigits(self, num: int) -> int:\n        return self.math(num)\n\n    def trivialSolution(self, num: int) -> int:\n        digital_root = 0\n        while num > 0:\n            digital_root += num % 10\n            num = num // 10\n\n            if num == 0 and digital_root > 9:\n                num = digital_root\n                digital_root = 0\n        return digital_root\n\n    def math(self, num: int) -> int:\n        if num == 0:\n            return num\n        elif num % 9 == 0:\n            return 9\n        else:\n            return num % 9\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/258-add-digits/",
      "datePublished": "2022-09-08T00:00:00Z",
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