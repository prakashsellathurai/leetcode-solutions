# decode-string


Try it on <a href='https://leetcode.com/problems/decode-string'>leetcode</a>

## Description
<div class="description">
<div><p>Given an encoded string, return its decoded string.</p>

<p>The encoding rule is: <code>k[encoded_string]</code>, where the <code>encoded_string</code> inside the square brackets is being repeated exactly <code>k</code> times. Note that <code>k</code> is guaranteed to be a positive integer.</p>

<p>You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.</p>

<p>Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, <code>k</code>. For example, there won't be input like <code>3a</code> or <code>2[4]</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "3[a]2[bc]"
<strong>Output:</strong> "aaabcbc"
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "3[a2[c]]"
<strong>Output:</strong> "accaccacc"
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> s = "2[abc]3[cd]ef"
<strong>Output:</strong> "abcabccdcdcdef"
</pre><p><strong>Example 4:</strong></p>
<pre><strong>Input:</strong> s = "abc3[cd]xyz"
<strong>Output:</strong> "abccdcdcdxyz"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 30</code></li>
	<li><code>s</code> consists of lowercase English letters, digits, and square brackets <code>'[]'</code>.</li>
	<li><code>s</code> is guaranteed to be <strong>a valid</strong> input.</li>
	<li>All the integers in <code>s</code> are in the range <code>[1, 300]</code>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def decodeString(self, s):
        it, num, stack = 0, 0, [""]
        while it < len(s):
            if s[it].isdigit():
                num = num * 10 + int(s[it])
            elif s[it] == "[":
                stack.append(num)
                num = 0
                stack.append("")
            elif s[it] == "]":
                str1 = stack.pop()
                rep = stack.pop()
                str2 = stack.pop()
                stack.append(str2 + str1 * rep)
            else:
                stack[-1] += s[it]
            it += 1
        return "".join(stack)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "394. Decode String",
    "text": "Given an encoded string, return its decoded string.\nThe encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.\nYou may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.\nFurthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].\n\u00a0\nExample 1:\nInput: s = \"3[a]2[bc]\"\nOutput: \"aaabcbc\"\nExample 2:\nInput: s = \"3[a2[c]]\"\nOutput: \"accaccacc\"\nExample 3:\nInput: s = \"2[abc]3[cd]ef\"\nOutput: \"abcabccdcdcdef\"\nExample 4:\nInput: s = \"abc3[cd]xyz\"\nOutput: \"abccdcdcdxyz\"\n\n\u00a0\nConstraints:\n\n1 <= s.length <= 30\ns consists of lowercase English letters, digits, and square brackets '[]'.\ns is guaranteed to be a valid input.\nAll the integers in s are in the range [1, 300].\n\n",
    "url": "https://leetcode.com/problems/decode-string",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def decodeString(self, s):\n        it, num, stack = 0, 0, [\"\"]\n        while it < len(s):\n            if s[it].isdigit():\n                num = num * 10 + int(s[it])\n            elif s[it] == \"[\":\n                stack.append(num)\n                num = 0\n                stack.append(\"\")\n            elif s[it] == \"]\":\n                str1 = stack.pop()\n                rep = stack.pop()\n                str2 = stack.pop()\n                stack.append(str2 + str1 * rep)\n            else:\n                stack[-1] += s[it]\n            it += 1\n        return \"\".join(stack)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/decode-string/",
      "datePublished": "2022-06-19T23:02:59+05:30",
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