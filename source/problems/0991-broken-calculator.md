# 0991-broken-calculator


Try it on <a href='https://leetcode.com/problems/0991-broken-calculator'>leetcode</a>

## Description
<div class="description">
<p>There is a broken calculator that has the integer <code>startValue</code> on its display initially. In one operation, you can:</p>

<ul>
	<li>multiply the number on display by <code>2</code>, or</li>
	<li>subtract <code>1</code> from the number on display.</li>
</ul>

<p>Given two integers <code>startValue</code> and <code>target</code>, return <em>the minimum number of operations needed to display </em><code>target</code><em> on the calculator</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> startValue = 2, target = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> Use double operation and then decrement operation {2 -&gt; 4 -&gt; 3}.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> startValue = 5, target = 8
<strong>Output:</strong> 2
<strong>Explanation:</strong> Use decrement and then double {5 -&gt; 4 -&gt; 8}.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> startValue = 3, target = 10
<strong>Output:</strong> 3
<strong>Explanation:</strong> Use double, decrement and double {3 -&gt; 6 -&gt; 5 -&gt; 10}.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= startValue, target &lt;= 10<sup>9</sup></code></li>
</ul>

</div>

## Solution(Python)
```Python
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        cnt = 0
        while target > startValue:
            if startValue == target:
                break
            if not target % 2:
                target//=2
            else:
                target+=1
            cnt+=1

        return cnt + startValue -target
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "991. Broken Calculator",
    "text": "There is a broken calculator that has the integer startValue on its display initially. In one operation, you can:\n\nmultiply the number on display by 2, or\nsubtract 1 from the number on display.\n\nGiven two integers startValue and target, return the minimum number of operations needed to display target on the calculator.\n\u00a0\nExample 1:\n\nInput: startValue = 2, target = 3\nOutput: 2\nExplanation: Use double operation and then decrement operation {2 -> 4 -> 3}.\n\nExample 2:\n\nInput: startValue = 5, target = 8\nOutput: 2\nExplanation: Use decrement and then double {5 -> 4 -> 8}.\n\nExample 3:\n\nInput: startValue = 3, target = 10\nOutput: 3\nExplanation: Use double, decrement and double {3 -> 6 -> 5 -> 10}.\n\n\u00a0\nConstraints:\n\n1 <= startValue, target <= 109\n\n",
    "url": "https://leetcode.com/problems/0991-broken-calculator",
    "answerCount": 1,
    "datePublished": "2022-08-16T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def brokenCalc(self, startValue: int, target: int) -> int:\n        cnt = 0\n        while target > startValue:\n            if startValue == target:\n                break\n            if not target % 2:\n                target//=2\n            else:\n                target+=1\n            cnt+=1\n\n        return cnt + startValue -target",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/0991-broken-calculator/",
      "datePublished": "2022-08-16T00:00:00Z",
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