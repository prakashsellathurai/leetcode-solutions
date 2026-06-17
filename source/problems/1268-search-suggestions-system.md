# 1268-search-suggestions-system


Try it on <a href='https://leetcode.com/problems/1268-search-suggestions-system'>leetcode</a>

## Description
<div class="description">
<div><p>You are given an array of strings <code>products</code> and a string <code>searchWord</code>.</p>

<p>Design a system that suggests at most three product names from <code>products</code> after each character of <code>searchWord</code> is typed. Suggested products should have common prefix with <code>searchWord</code>. If there are more than three products with a common prefix return the three lexicographically minimums products.</p>

<p>Return <em>a list of lists of the suggested products after each character of </em><code>searchWord</code><em> is typed</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
<strong>Output:</strong> [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
<strong>Explanation:</strong> products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> products = ["havana"], searchWord = "havana"
<strong>Output:</strong> [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
<strong>Output:</strong> [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= products.length &lt;= 1000</code></li>
	<li><code>1 &lt;= products[i].length &lt;= 3000</code></li>
	<li><code>1 &lt;= sum(products[i].length) &lt;= 2 * 10<sup>4</sup></code></li>
	<li>All the strings of <code>products</code> are <strong>unique</strong>.</li>
	<li><code>products[i]</code> consists of lowercase English letters.</li>
	<li><code>1 &lt;= searchWord.length &lt;= 1000</code></li>
	<li><code>searchWord</code> consists of lowercase English letters.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        return self.trie_search(products, searchWord)

    # Time complexity: O(n log n+nm)
    # Space complexity: O(n)
    def bruteforce(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        res = []
        for i in range(len(searchWord)):
            cur = []
            prefix = searchWord[: i + 1]
            for i in range(len(products)):
                if prefix in products[i]:
                    cur = products[i: i + 3]
                    break

            res.append(cur)
        return res

    # Time complexity: O(n log n+mlogn)
    # Space complexity: O(n)
    def binarysearch(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        res = []
        prefix = ""
        for i in range(len(searchWord)):
            prefix += searchWord[i]

            start = bisect_left(products, prefix)
            cur = [
                products[j]
                for j in range(start, len(products))
                if j < start + 3 and prefix in products[j]
            ]
            res.append(cur)
        return res

    # Time complexity: O(nlogn +nm+s)
    # Space complexity: O(nkm)
    def trie_search(self, products: List[str], searchWord: str) -> List[List[str]]:
        class TrieNode:
            def __init__(self):
                self.children = collections.defaultdict(TrieNode)
                self.suggestion = []

            def add_suggestion(self, product):
                if len(self.suggestion) < 3:
                    self.suggestion.append(product)

        products = sorted(products)
        root = TrieNode()

        for product in products:
            node = root
            for c in product:
                node = node.children[c]
                node.add_suggestion(product)
        res, node = [], root

        for c in searchWord:
            node = node.children[c]
            res.append(node.suggestion)
        return res

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1268. Search Suggestions System",
    "text": "You are given an array of strings products and a string searchWord.\nDesign a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.\nReturn a list of lists of the suggested products after each character of searchWord is typed.\n\u00a0\nExample 1:\nInput: products = [\"mobile\",\"mouse\",\"moneypot\",\"monitor\",\"mousepad\"], searchWord = \"mouse\"\nOutput: [\n[\"mobile\",\"moneypot\",\"monitor\"],\n[\"mobile\",\"moneypot\",\"monitor\"],\n[\"mouse\",\"mousepad\"],\n[\"mouse\",\"mousepad\"],\n[\"mouse\",\"mousepad\"]\n]\nExplanation: products sorted lexicographically = [\"mobile\",\"moneypot\",\"monitor\",\"mouse\",\"mousepad\"]\nAfter typing m and mo all products match and we show user [\"mobile\",\"moneypot\",\"monitor\"]\nAfter typing mou, mous and mouse the system suggests [\"mouse\",\"mousepad\"]\n\nExample 2:\nInput: products = [\"havana\"], searchWord = \"havana\"\nOutput: [[\"havana\"],[\"havana\"],[\"havana\"],[\"havana\"],[\"havana\"],[\"havana\"]]\n\nExample 3:\nInput: products = [\"bags\",\"baggage\",\"banner\",\"box\",\"cloths\"], searchWord = \"bags\"\nOutput: [[\"baggage\",\"bags\",\"banner\"],[\"baggage\",\"bags\",\"banner\"],[\"baggage\",\"bags\"],[\"bags\"]]\n\n\u00a0\nConstraints:\n\n1 <= products.length <= 1000\n1 <= products[i].length <= 3000\n1 <= sum(products[i].length) <= 2 * 104\nAll the strings of products are unique.\nproducts[i] consists of lowercase English letters.\n1 <= searchWord.length <= 1000\nsearchWord consists of lowercase English letters.\n\n",
    "url": "https://leetcode.com/problems/1268-search-suggestions-system",
    "answerCount": 1,
    "datePublished": "2024-10-11T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def suggestedProducts(\n        self, products: List[str], searchWord: str\n    ) -> List[List[str]]:\n        return self.trie_search(products, searchWord)\n\n    # Time complexity: O(n log n+nm)\n    # Space complexity: O(n)\n    def bruteforce(self, products: List[str], searchWord: str) -> List[List[str]]:\n        products.sort()\n\n        res = []\n        for i in range(len(searchWord)):\n            cur = []\n            prefix = searchWord[: i + 1]\n            for i in range(len(products)):\n                if prefix in products[i]:\n                    cur = products[i: i + 3]\n                    break\n\n            res.append(cur)\n        return res\n\n    # Time complexity: O(n log n+mlogn)\n    # Space complexity: O(n)\n    def binarysearch(self, products: List[str], searchWord: str) -> List[List[str]]:\n        products.sort()\n\n        res = []\n        prefix = \"\"\n        for i in range(len(searchWord)):\n            prefix += searchWord[i]\n\n            start = bisect_left(products, prefix)\n            cur = [\n                products[j]\n                for j in range(start, len(products))\n                if j < start + 3 and prefix in products[j]\n            ]\n            res.append(cur)\n        return res\n\n    # Time complexity: O(nlogn +nm+s)\n    # Space complexity: O(nkm)\n    def trie_search(self, products: List[str], searchWord: str) -> List[List[str]]:\n        class TrieNode:\n            def __init__(self):\n                self.children = collections.defaultdict(TrieNode)\n                self.suggestion = []\n\n            def add_suggestion(self, product):\n                if len(self.suggestion) < 3:\n                    self.suggestion.append(product)\n\n        products = sorted(products)\n        root = TrieNode()\n\n        for product in products:\n            node = root\n            for c in product:\n                node = node.children[c]\n                node.add_suggestion(product)\n        res, node = [], root\n\n        for c in searchWord:\n            node = node.children[c]\n            res.append(node.suggestion)\n        return res\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1268-search-suggestions-system/",
      "datePublished": "2024-10-11T00:00:00Z",
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