# 1720-decode-xored-array


Try it on <a href='https://leetcode.com/problems/1720-decode-xored-array'>leetcode</a>

## Description
<div class="description">
<div><p>There is a <strong>hidden</strong> integer array <code>arr</code> that consists of <code>n</code> non-negative integers.</p>

<p>It was encoded into another integer array <code>encoded</code> of length <code>n - 1</code>, such that <code>encoded[i] = arr[i] XOR arr[i + 1]</code>. For example, if <code>arr = [1,0,2,1]</code>, then <code>encoded = [1,2,3]</code>.</p>

<p>You are given the <code>encoded</code> array. You are also given an integer <code>first</code>, that is the first element of <code>arr</code>, i.e. <code>arr[0]</code>.</p>

<p>Return <em>the original array</em> <code>arr</code>. It can be proved that the answer exists and is unique.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> encoded = [1,2,3], first = 1
<strong>Output:</strong> [1,0,2,1]
<strong>Explanation:</strong> If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> encoded = [6,2,7,3], first = 4
<strong>Output:</strong> [4,2,0,7,4]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>encoded.length == n - 1</code></li>
	<li><code>0 &lt;= encoded[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= first &lt;= 10<sup>5</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for i in range(len(encoded)):
            cur = encoded[i] ^ res[-1]
            res.append(cur)
        return res
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1720. Decode XORed Array",
    "text": "There is a hidden integer array arr that consists of n non-negative integers.\nIt was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], then encoded = [1,2,3].\nYou are given the encoded array. You are also given an integer first, that is the first element of arr, i.e. arr[0].\nReturn the original array arr. It can be proved that the answer exists and is unique.\n\u00a0\nExample 1:\nInput: encoded = [1,2,3], first = 1\nOutput: [1,0,2,1]\nExplanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]\n\nExample 2:\nInput: encoded = [6,2,7,3], first = 4\nOutput: [4,2,0,7,4]\n\n\u00a0\nConstraints:\n\n2 <= n <= 104\nencoded.length == n - 1\n0 <= encoded[i] <= 105\n0 <= first <= 105\n\n",
    "url": "https://leetcode.com/problems/1720-decode-xored-array",
    "answerCount": 1,
    "datePublished": "2025-08-27T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def decode(self, encoded: List[int], first: int) -> List[int]:\n        res = [first]\n        for i in range(len(encoded)):\n            cur = encoded[i] ^ res[-1]\n            res.append(cur)\n        return res",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1720-decode-xored-array/",
      "datePublished": "2025-08-27T00:00:00Z",
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