# 745-prefix-and-suffix-search


Try it on <a href='https://leetcode.com/problems/745-prefix-and-suffix-search'>leetcode</a>

## Description
<div class="description">
<div><p>Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.</p>

<p>Implement the <code>WordFilter</code> class:</p>

<ul>
	<li><code>WordFilter(string[] words)</code> Initializes the object with the <code>words</code> in the dictionary.</li>
	<li><code>f(string prefix, string suffix)</code> Returns <em>the index of the word in the dictionary,</em> which has the prefix <code>prefix</code> and the suffix <code>suffix</code>. If there is more than one valid index, return <strong>the largest</strong> of them. If there is no such word in the dictionary, return <code>-1</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input</strong>
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
<strong>Output</strong>
[null, 0]

<strong>Explanation</strong>
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 15000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
	<li><code>1 &lt;= prefix.length, suffix.length &lt;= 10</code></li>
	<li><code>words[i]</code>, <code>prefix</code> and <code>suffix</code> consist of lower-case English letters only.</li>
	<li>At most <code>15000</code> calls will be made to the function <code>f</code>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
def Trie():
    return collections.defaultdict(Trie)


WEIGHT = False


class WordFilter(object):
    def __init__(self, words):
        self.trie = Trie()

        for weight, word in enumerate(words):
            word += "#"
            for i in range(len(word)):
                cur = self.trie
                cur[WEIGHT] = weight
                for j in range(i, 2 * len(word) - 1):
                    cur = cur[word[j % len(word)]]
                    cur[WEIGHT] = weight

    def f(self, prefix, suffix):
        cur = self.trie
        for letter in suffix + "#" + prefix:
            if letter not in cur:
                return -1
            cur = cur[letter]
        return cur[WEIGHT]

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "745. Prefix and Suffix Search",
    "text": "Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.\nImplement the WordFilter class:\n\nWordFilter(string[] words) Initializes the object with the words in the dictionary.\nf(string prefix, string suffix) Returns the index of the word in the dictionary, which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.\n\n\u00a0\nExample 1:\nInput\n[\"WordFilter\", \"f\"]\n[[[\"apple\"]], [\"a\", \"e\"]]\nOutput\n[null, 0]\n\nExplanation\nWordFilter wordFilter = new WordFilter([\"apple\"]);\nwordFilter.f(\"a\", \"e\"); // return 0, because the word at index 0 has prefix = \"a\" and suffix = 'e\".\n\n\u00a0\nConstraints:\n\n1 <= words.length <= 15000\n1 <= words[i].length <= 10\n1 <= prefix.length, suffix.length <= 10\nwords[i], prefix and suffix consist of lower-case English letters only.\nAt most 15000 calls will be made to the function f.\n\n",
    "url": "https://leetcode.com/problems/745-prefix-and-suffix-search",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "def Trie():\n    return collections.defaultdict(Trie)\n\n\nWEIGHT = False\n\n\nclass WordFilter(object):\n    def __init__(self, words):\n        self.trie = Trie()\n\n        for weight, word in enumerate(words):\n            word += \"#\"\n            for i in range(len(word)):\n                cur = self.trie\n                cur[WEIGHT] = weight\n                for j in range(i, 2 * len(word) - 1):\n                    cur = cur[word[j % len(word)]]\n                    cur[WEIGHT] = weight\n\n    def f(self, prefix, suffix):\n        cur = self.trie\n        for letter in suffix + \"#\" + prefix:\n            if letter not in cur:\n                return -1\n            cur = cur[letter]\n        return cur[WEIGHT]\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/745-prefix-and-suffix-search/",
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