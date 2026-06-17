# reverse-words-in-a-string


Try it on <a href='https://leetcode.com/problems/reverse-words-in-a-string'>leetcode</a>

## Description
<div class="description">
<div><p>Given an input string <code>s</code>, reverse the order of the <strong>words</strong>.</p>

<p>A <strong>word</strong> is defined as a sequence of non-space characters. The <strong>words</strong> in <code>s</code> will be separated by at least one space.</p>

<p>Return <em>a string of the words in reverse order concatenated by a single space.</em></p>

<p><b>Note</b> that <code>s</code> may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "the sky is blue"
<strong>Output:</strong> "blue is sky the"
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "  hello world  "
<strong>Output:</strong> "world hello"
<strong>Explanation:</strong> Your reversed string should not contain leading or trailing spaces.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "a good   example"
<strong>Output:</strong> "example good a"
<strong>Explanation:</strong> You need to reduce multiple spaces between two words to a single space in the reversed string.
</pre>

<p><strong>Example 4:</strong></p>

<pre><strong>Input:</strong> s = "  Bob    Loves  Alice   "
<strong>Output:</strong> "Alice Loves Bob"
</pre>

<p><strong>Example 5:</strong></p>

<pre><strong>Input:</strong> s = "Alice does not even like bob"
<strong>Output:</strong> "bob like even not does Alice"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> contains English letters (upper-case and lower-case), digits, and spaces <code>' '</code>.</li>
	<li>There is <strong>at least one</strong> word in <code>s</code>.</li>
</ul>

<p>&nbsp;</p>
<p><b data-stringify-type="bold">Follow-up:&nbsp;</b>If the string data type is mutable in your language, can&nbsp;you solve it&nbsp;<b data-stringify-type="bold">in-place</b>&nbsp;with&nbsp;<code data-stringify-type="code">O(1)</code>&nbsp;extra space?</p>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def reverseWords(self, message: str) -> str:
        result = ""
        current = len(message) - 1

        while current >= 0:
            # move to the start of word
            checkpoint = current + 1
            while current >= 0 and message[current] != " ":
                current -= 1

            for temporal in range(current + 1, checkpoint):
                result += message[temporal]

            # move spaces
            while current >= 0 and message[current] == " ":
                current -= 1

            # add spaces
            if current != -1 and len(result):
                result += " "

        return result

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "151. Reverse Words in a String",
    "text": "Given an input string s, reverse the order of the words.\nA word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.\nReturn a string of the words in reverse order concatenated by a single space.\nNote that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.\n\u00a0\nExample 1:\nInput: s = \"the sky is blue\"\nOutput: \"blue is sky the\"\n\nExample 2:\nInput: s = \"  hello world  \"\nOutput: \"world hello\"\nExplanation: Your reversed string should not contain leading or trailing spaces.\n\nExample 3:\nInput: s = \"a good   example\"\nOutput: \"example good a\"\nExplanation: You need to reduce multiple spaces between two words to a single space in the reversed string.\n\nExample 4:\nInput: s = \"  Bob    Loves  Alice   \"\nOutput: \"Alice Loves Bob\"\n\nExample 5:\nInput: s = \"Alice does not even like bob\"\nOutput: \"bob like even not does Alice\"\n\n\u00a0\nConstraints:\n\n1 <= s.length <= 104\ns contains English letters (upper-case and lower-case), digits, and spaces ' '.\nThere is at least one word in s.\n\n\u00a0\nFollow-up:\u00a0If the string data type is mutable in your language, can\u00a0you solve it\u00a0in-place\u00a0with\u00a0O(1)\u00a0extra space?\n",
    "url": "https://leetcode.com/problems/reverse-words-in-a-string",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def reverseWords(self, message: str) -> str:\n        result = \"\"\n        current = len(message) - 1\n\n        while current >= 0:\n            # move to the start of word\n            checkpoint = current + 1\n            while current >= 0 and message[current] != \" \":\n                current -= 1\n\n            for temporal in range(current + 1, checkpoint):\n                result += message[temporal]\n\n            # move spaces\n            while current >= 0 and message[current] == \" \":\n                current -= 1\n\n            # add spaces\n            if current != -1 and len(result):\n                result += \" \"\n\n        return result\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/reverse-words-in-a-string/",
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