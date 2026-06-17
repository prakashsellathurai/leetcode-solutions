# number-complement


Try it on <a href='https://leetcode.com/problems/number-complement'>leetcode</a>

## Description
<div class="description">
<div><p>The <strong>complement</strong> of an integer is the integer you get when you flip all the <code>0</code>'s to <code>1</code>'s and all the <code>1</code>'s to <code>0</code>'s in its binary representation.</p>

<ul>
	<li>For example, The integer <code>5</code> is <code>"101"</code> in binary and its <strong>complement</strong> is <code>"010"</code> which is the integer <code>2</code>.</li>
</ul>

<p>Given an integer <code>num</code>, return <em>its complement</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> num = 5
<strong>Output:</strong> 2
<strong>Explanation:</strong> The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> num = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num &lt; 2<sup>31</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as 1009: <a href="https://leetcode.com/problems/complement-of-base-10-integer/" target="_blank">https://leetcode.com/problems/complement-of-base-10-integer/</a></p>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def findComplement(self, num: int) -> int:
        mask = (1 << (floor(log2(num) + 1))) - 1
        return num ^ mask

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "476. Number Complement",
    "text": "The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.\n\nFor example, The integer 5 is \"101\" in binary and its complement is \"010\" which is the integer 2.\n\nGiven an integer num, return its complement.\n\u00a0\nExample 1:\nInput: num = 5\nOutput: 2\nExplanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.\n\nExample 2:\nInput: num = 1\nOutput: 0\nExplanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.\n\n\u00a0\nConstraints:\n\n1 <= num < 231\n\n\u00a0\nNote: This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/\n",
    "url": "https://leetcode.com/problems/number-complement",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def findComplement(self, num: int) -> int:\n        mask = (1 << (floor(log2(num) + 1))) - 1\n        return num ^ mask\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/number-complement/",
      "datePublished": "2024-08-20",
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