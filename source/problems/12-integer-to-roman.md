# 12-integer-to-roman


Try it on <a href='https://leetcode.com/problems/12-integer-to-roman'>leetcode</a>

## Description
<div class="description">
<div><p>Roman numerals are represented by seven different symbols:&nbsp;<code>I</code>, <code>V</code>, <code>X</code>, <code>L</code>, <code>C</code>, <code>D</code> and <code>M</code>.</p>

<pre><strong>Symbol</strong>       <strong>Value</strong>
I             1
V             5
X             10
L             50
C             100
D             500
M             1000</pre>

<p>For example,&nbsp;<code>2</code> is written as <code>II</code>&nbsp;in Roman numeral, just two one's added together. <code>12</code> is written as&nbsp;<code>XII</code>, which is simply <code>X + II</code>. The number <code>27</code> is written as <code>XXVII</code>, which is <code>XX + V + II</code>.</p>

<p>Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not <code>IIII</code>. Instead, the number four is written as <code>IV</code>. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as <code>IX</code>. There are six instances where subtraction is used:</p>

<ul>
	<li><code>I</code> can be placed before <code>V</code> (5) and <code>X</code> (10) to make 4 and 9.&nbsp;</li>
	<li><code>X</code> can be placed before <code>L</code> (50) and <code>C</code> (100) to make 40 and 90.&nbsp;</li>
	<li><code>C</code> can be placed before <code>D</code> (500) and <code>M</code> (1000) to make 400 and 900.</li>
</ul>

<p>Given an integer, convert it to a roman numeral.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> num = 3
<strong>Output:</strong> "III"
<strong>Explanation:</strong> 3 is represented as 3 ones.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> num = 58
<strong>Output:</strong> "LVIII"
<strong>Explanation:</strong> L = 50, V = 5, III = 3.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> num = 1994
<strong>Output:</strong> "MCMXCIV"
<strong>Explanation:</strong> M = 1000, CM = 900, XC = 90 and IV = 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 3999</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def intToRoman(self, N: int) -> str:
        hashmap = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        res = []
        for val, sym in hashmap.items():
            res.append(N // val * sym)
            N %= val
        return "".join(res)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "12. Integer to Roman",
    "text": "Roman numerals are represented by seven different symbols:\u00a0I, V, X, L, C, D and M.\nSymbol       Value\nI             1\nV             5\nX             10\nL             50\nC             100\nD             500\nM             1000\nFor example,\u00a02 is written as II\u00a0in Roman numeral, just two one's added together. 12 is written as\u00a0XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.\nRoman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:\n\nI can be placed before V (5) and X (10) to make 4 and 9.\u00a0\nX can be placed before L (50) and C (100) to make 40 and 90.\u00a0\nC can be placed before D (500) and M (1000) to make 400 and 900.\n\nGiven an integer, convert it to a roman numeral.\n\u00a0\nExample 1:\nInput: num = 3\nOutput: \"III\"\nExplanation: 3 is represented as 3 ones.\n\nExample 2:\nInput: num = 58\nOutput: \"LVIII\"\nExplanation: L = 50, V = 5, III = 3.\n\nExample 3:\nInput: num = 1994\nOutput: \"MCMXCIV\"\nExplanation: M = 1000, CM = 900, XC = 90 and IV = 4.\n\n\u00a0\nConstraints:\n\n1 <= num <= 3999\n\n",
    "url": "https://leetcode.com/problems/12-integer-to-roman",
    "answerCount": 1,
    "datePublished": "2022-06-07T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def intToRoman(self, N: int) -> str:\n        hashmap = {\n            1000: \"M\",\n            900: \"CM\",\n            500: \"D\",\n            400: \"CD\",\n            100: \"C\",\n            90: \"XC\",\n            50: \"L\",\n            40: \"XL\",\n            10: \"X\",\n            9: \"IX\",\n            5: \"V\",\n            4: \"IV\",\n            1: \"I\",\n        }\n        res = []\n        for val, sym in hashmap.items():\n            res.append(N // val * sym)\n            N %= val\n        return \"\".join(res)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/12-integer-to-roman/",
      "datePublished": "2022-06-07T00:00:00Z",
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