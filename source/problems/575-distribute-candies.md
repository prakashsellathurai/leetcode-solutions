# 575-distribute-candies


Try it on <a href='https://leetcode.com/problems/575-distribute-candies'>leetcode</a>

## Description
<div class="description">
<div><p>Alice has <code>n</code> candies, where the <code>i<sup>th</sup></code> candy is of type <code>candyType[i]</code>. Alice noticed that she started to gain weight, so she visited a doctor.</p>

<p>The doctor advised Alice to only eat <code>n / 2</code> of the candies she has (<code>n</code> is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.</p>

<p>Given the integer array <code>candyType</code> of length <code>n</code>, return <em>the <strong>maximum</strong> number of different types of candies she can eat if she only eats </em><code>n / 2</code><em> of them</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> candyType = [1,1,2,2,3,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> candyType = [1,1,2,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2], [1,3], or [2,3], she still can only eat 2 different types.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> candyType = [6,6,6,6]
<strong>Output:</strong> 1
<strong>Explanation:</strong> Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only has 1 type.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == candyType.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>n</code>&nbsp;is even.</li>
	<li><code>-10<sup>5</sup> &lt;= candyType[i] &lt;= 10<sup>5</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # Count the number of unique candies by creating a set with
        # candyType, and then taking its length.
        unique_candies = len(set(candyType))
        # And find the answer in the same way as before.
        return min(unique_candies, len(candyType) // 2)
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "575. Distribute Candies",
    "text": "Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor.\nThe doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.\nGiven the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.\n\u00a0\nExample 1:\nInput: candyType = [1,1,2,2,3,3]\nOutput: 3\nExplanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.\n\nExample 2:\nInput: candyType = [1,1,2,3]\nOutput: 2\nExplanation: Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2], [1,3], or [2,3], she still can only eat 2 different types.\n\nExample 3:\nInput: candyType = [6,6,6,6]\nOutput: 1\nExplanation: Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only has 1 type.\n\n\u00a0\nConstraints:\n\nn == candyType.length\n2 <= n <= 104\nn\u00a0is even.\n-105 <= candyType[i] <= 105\n\n",
    "url": "https://leetcode.com/problems/575-distribute-candies",
    "answerCount": 1,
    "datePublished": "2022-07-07T01:33:44+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def distributeCandies(self, candyType: List[int]) -> int:\n        # Count the number of unique candies by creating a set with\n        # candyType, and then taking its length.\n        unique_candies = len(set(candyType))\n        # And find the answer in the same way as before.\n        return min(unique_candies, len(candyType) // 2)",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/575-distribute-candies/",
      "datePublished": "2022-07-07T01:33:44+05:30",
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