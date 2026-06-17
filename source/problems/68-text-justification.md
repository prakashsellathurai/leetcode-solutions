# 68-text-justification


Try it on <a href='https://leetcode.com/problems/68-text-justification'>leetcode</a>

## Description
<div class="description">
<div><p>Given an array of strings <code>words</code> and a width <code>maxWidth</code>, format the text such that each line has exactly <code>maxWidth</code> characters and is fully (left and right) justified.</p>

<p>You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces <code>' '</code> when necessary so that each line has exactly <code>maxWidth</code> characters.</p>

<p>Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.</p>

<p>For the last line of text, it should be left-justified and no extra space is inserted between words.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>A word is defined as a character sequence consisting of non-space characters only.</li>
	<li>Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.</li>
	<li>The input array <code>words</code> contains at least one word.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
<strong>Output:</strong>
[
&nbsp; &nbsp;"This &nbsp; &nbsp;is &nbsp; &nbsp;an",
&nbsp; &nbsp;"example &nbsp;of text",
&nbsp; &nbsp;"justification. &nbsp;"
]</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
<strong>Output:</strong>
[
&nbsp; "What &nbsp; must &nbsp; be",
&nbsp; "acknowledgment &nbsp;",
&nbsp; "shall be &nbsp; &nbsp; &nbsp; &nbsp;"
]
<strong>Explanation:</strong> Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified becase it contains only one word.</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
<strong>Output:</strong>
[
&nbsp; "Science &nbsp;is &nbsp;what we",
  "understand &nbsp; &nbsp; &nbsp;well",
&nbsp; "enough to explain to",
&nbsp; "a &nbsp;computer. &nbsp;Art is",
&nbsp; "everything &nbsp;else &nbsp;we",
&nbsp; "do &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"
]</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 300</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 20</code></li>
	<li><code>words[i]</code> consists of only English letters and symbols.</li>
	<li><code>1 &lt;= maxWidth &lt;= 100</code></li>
	<li><code>words[i].length &lt;= maxWidth</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += " "
                res.append("".join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [" ".join(cur).ljust(maxWidth)]

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "68. Text Justification",
    "text": "Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.\nYou should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.\nExtra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.\nFor the last line of text, it should be left-justified and no extra space is inserted between words.\nNote:\n\nA word is defined as a character sequence consisting of non-space characters only.\nEach word's length is guaranteed to be greater than 0 and not exceed maxWidth.\nThe input array words contains at least one word.\n\n\u00a0\nExample 1:\nInput: words = [\"This\", \"is\", \"an\", \"example\", \"of\", \"text\", \"justification.\"], maxWidth = 16\nOutput:\n[\n\u00a0 \u00a0\"This \u00a0 \u00a0is \u00a0 \u00a0an\",\n\u00a0 \u00a0\"example \u00a0of text\",\n\u00a0 \u00a0\"justification. \u00a0\"\n]\nExample 2:\nInput: words = [\"What\",\"must\",\"be\",\"acknowledgment\",\"shall\",\"be\"], maxWidth = 16\nOutput:\n[\n\u00a0 \"What \u00a0 must \u00a0 be\",\n\u00a0 \"acknowledgment \u00a0\",\n\u00a0 \"shall be \u00a0 \u00a0 \u00a0 \u00a0\"\n]\nExplanation: Note that the last line is \"shall be    \" instead of \"shall     be\", because the last line must be left-justified instead of fully-justified.\nNote that the second line is also left-justified becase it contains only one word.\nExample 3:\nInput: words = [\"Science\",\"is\",\"what\",\"we\",\"understand\",\"well\",\"enough\",\"to\",\"explain\",\"to\",\"a\",\"computer.\",\"Art\",\"is\",\"everything\",\"else\",\"we\",\"do\"], maxWidth = 20\nOutput:\n[\n\u00a0 \"Science \u00a0is \u00a0what we\",\n  \"understand \u00a0 \u00a0 \u00a0well\",\n\u00a0 \"enough to explain to\",\n\u00a0 \"a \u00a0computer. \u00a0Art is\",\n\u00a0 \"everything \u00a0else \u00a0we\",\n\u00a0 \"do \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0\"\n]\n\u00a0\nConstraints:\n\n1 <= words.length <= 300\n1 <= words[i].length <= 20\nwords[i] consists of only English letters and symbols.\n1 <= maxWidth <= 100\nwords[i].length <= maxWidth\n\n",
    "url": "https://leetcode.com/problems/68-text-justification",
    "answerCount": 1,
    "datePublished": "2022-04-14T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:\n        res, cur, num_of_letters = [], [], 0\n        for w in words:\n            if num_of_letters + len(w) + len(cur) > maxWidth:\n                for i in range(maxWidth - num_of_letters):\n                    cur[i % (len(cur) - 1 or 1)] += \" \"\n                res.append(\"\".join(cur))\n                cur, num_of_letters = [], 0\n            cur += [w]\n            num_of_letters += len(w)\n        return res + [\" \".join(cur).ljust(maxWidth)]\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/68-text-justification/",
      "datePublished": "2022-04-14T00:00:00Z",
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