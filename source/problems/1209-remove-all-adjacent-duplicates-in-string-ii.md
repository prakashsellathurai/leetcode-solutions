# 1209-remove-all-adjacent-duplicates-in-string-ii


Try it on <a href='https://leetcode.com/problems/1209-remove-all-adjacent-duplicates-in-string-ii'>leetcode</a>

## Description
<div class="description">
<div><p>You are given a string <code>s</code> and an integer <code>k</code>, a <code>k</code> <strong>duplicate removal</strong> consists of choosing <code>k</code> adjacent and equal letters from <code>s</code> and removing them, causing the left and the right side of the deleted substring to concatenate together.</p>

<p>We repeatedly make <code>k</code> <strong>duplicate removals</strong> on <code>s</code> until we no longer can.</p>

<p>Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "abcd", k = 2
<strong>Output:</strong> "abcd"
<strong>Explanation: </strong>There's nothing to delete.</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "deeedbbcccbdaa", k = 3
<strong>Output:</strong> "aa"
<strong>Explanation: 
</strong>First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "pbbcggttciiippooaais", k = 2
<strong>Output:</strong> "ps"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= k &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> only contains lower case English letters.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            if stack and c == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])

            if stack[-1][1] == k:
                stack.pop()

        return "".join(i * j for i, j in stack)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1209. Remove All Adjacent Duplicates in String II",
    "text": "You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.\nWe repeatedly make k duplicate removals on s until we no longer can.\nReturn the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.\n\u00a0\nExample 1:\nInput: s = \"abcd\", k = 2\nOutput: \"abcd\"\nExplanation: There's nothing to delete.\nExample 2:\nInput: s = \"deeedbbcccbdaa\", k = 3\nOutput: \"aa\"\nExplanation: \nFirst delete \"eee\" and \"ccc\", get \"ddbbbdaa\"\nThen delete \"bbb\", get \"dddaa\"\nFinally delete \"ddd\", get \"aa\"\nExample 3:\nInput: s = \"pbbcggttciiippooaais\", k = 2\nOutput: \"ps\"\n\n\u00a0\nConstraints:\n\n1 <= s.length <= 105\n2 <= k <= 104\ns only contains lower case English letters.\n\n",
    "url": "https://leetcode.com/problems/1209-remove-all-adjacent-duplicates-in-string-ii",
    "answerCount": 1,
    "datePublished": "2025-11-03T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def removeDuplicates(self, s: str, k: int) -> str:\n        stack = []\n\n        for c in s:\n            if stack and c == stack[-1][0]:\n                stack[-1][1] += 1\n            else:\n                stack.append([c, 1])\n\n            if stack[-1][1] == k:\n                stack.pop()\n\n        return \"\".join(i * j for i, j in stack)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1209-remove-all-adjacent-duplicates-in-string-ii/",
      "datePublished": "2025-11-03T00:00:00Z",
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