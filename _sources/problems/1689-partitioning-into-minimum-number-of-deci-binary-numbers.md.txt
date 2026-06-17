# 1689-partitioning-into-minimum-number-of-deci-binary-numbers


Try it on <a href='https://leetcode.com/problems/1689-partitioning-into-minimum-number-of-deci-binary-numbers'>leetcode</a>

## Description
<div class="description">
<div><p>A decimal number is called <strong>deci-binary</strong> if each of its digits is either <code>0</code> or <code>1</code> without any leading zeros. For example, <code>101</code> and <code>1100</code> are <strong>deci-binary</strong>, while <code>112</code> and <code>3001</code> are not.</p>

<p>Given a string <code>n</code> that represents a positive decimal integer, return <em>the <strong>minimum</strong> number of positive <strong>deci-binary</strong> numbers needed so that they sum up to </em><code>n</code><em>.</em></p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> n = "32"
<strong>Output:</strong> 3
<strong>Explanation:</strong> 10 + 11 + 11 = 32
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> n = "82734"
<strong>Output:</strong> 8
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> n = "27346209830709182346"
<strong>Output:</strong> 9
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n.length &lt;= 10<sup>5</sup></code></li>
	<li><code>n</code> consists of only digits.</li>
	<li><code>n</code> does not contain any leading zeros and represents a positive integer.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def minPartitions(self, n: str) -> int:
        return max(list(n))

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1689. Partitioning Into Minimum Number Of Deci-Binary Numbers",
    "text": "A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.\nGiven a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.\n\u00a0\nExample 1:\nInput: n = \"32\"\nOutput: 3\nExplanation: 10 + 11 + 11 = 32\n\nExample 2:\nInput: n = \"82734\"\nOutput: 8\n\nExample 3:\nInput: n = \"27346209830709182346\"\nOutput: 9\n\n\u00a0\nConstraints:\n\n1 <= n.length <= 105\nn consists of only digits.\nn does not contain any leading zeros and represents a positive integer.\n\n",
    "url": "https://leetcode.com/problems/1689-partitioning-into-minimum-number-of-deci-binary-numbers",
    "answerCount": 1,
    "datePublished": "2022-06-27T08:50:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def minPartitions(self, n: str) -> int:\n        return max(list(n))\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1689-partitioning-into-minimum-number-of-deci-binary-numbers/",
      "datePublished": "2022-06-27T08:50:59+05:30",
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