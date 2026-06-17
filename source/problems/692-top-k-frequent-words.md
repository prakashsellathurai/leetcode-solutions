# 692-top-k-frequent-words


Try it on <a href='https://leetcode.com/problems/692-top-k-frequent-words'>leetcode</a>

## Description
<div class="description">
<div><p>Given an array of strings <code>words</code> and an integer <code>k</code>, return <em>the </em><code>k</code><em> most frequent strings</em>.</p>

<p>Return the answer <strong>sorted</strong> by <strong>the frequency</strong> from highest to lowest. Sort the words with the same frequency by their <strong>lexicographical order</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> words = ["i","love","leetcode","i","love","coding"], k = 2
<strong>Output:</strong> ["i","love"]
<strong>Explanation:</strong> "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
<strong>Output:</strong> ["the","is","sunny","day"]
<strong>Explanation:</strong> "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 500</code></li>
	<li><code>1 &lt;= words[i] &lt;= 10</code></li>
	<li><code>words[i]</code> consists of lowercase English letters.</li>
	<li><code>k</code> is in the range <code>[1, The number of <strong>unique</strong> words[i]]</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow-up:</strong> Could you solve it in <code>O(n log(k))</code> time and <code>O(n)</code> extra space?</p>
</div>
</div>

## Solution(Python)
```Python
class Comparator:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count

    def __eq__(self, other):
        return self.count == other.count and self.word == other.word


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return self.priorityqueue(words, k)

    # Time Complexity: O(nmlogn)
    # Space Compexlity: O(n*m)
    def sorting(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        counter = sorted(counter.keys(), key=counter.get, reverse=True)
        return counter[:k]

    # Time Complexity: O(nmlogk)
    # Space Compexlity: O(k)
    def priorityqueue(self, words: List[str], k: int) -> List[str]:
        heap = []
        counter = Counter(words)
        heapq.heapify(heap)
        for word in counter:
            heapq.heappush(heap, (Comparator(counter[word], word), word))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res[::-1]

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "692. Top K Frequent Words",
    "text": "Given an array of strings words and an integer k, return the k most frequent strings.\nReturn the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.\n\u00a0\nExample 1:\nInput: words = [\"i\",\"love\",\"leetcode\",\"i\",\"love\",\"coding\"], k = 2\nOutput: [\"i\",\"love\"]\nExplanation: \"i\" and \"love\" are the two most frequent words.\nNote that \"i\" comes before \"love\" due to a lower alphabetical order.\n\nExample 2:\nInput: words = [\"the\",\"day\",\"is\",\"sunny\",\"the\",\"the\",\"the\",\"sunny\",\"is\",\"is\"], k = 4\nOutput: [\"the\",\"is\",\"sunny\",\"day\"]\nExplanation: \"the\", \"is\", \"sunny\" and \"day\" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.\n\n\u00a0\nConstraints:\n\n1 <= words.length <= 500\n1 <= words[i] <= 10\nwords[i] consists of lowercase English letters.\nk is in the range [1, The number of unique words[i]]\n\n\u00a0\nFollow-up: Could you solve it in O(n log(k)) time and O(n) extra space?\n",
    "url": "https://leetcode.com/problems/692-top-k-frequent-words",
    "answerCount": 1,
    "datePublished": "2023-11-05T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Comparator:\n    def __init__(self, count, word):\n        self.count = count\n        self.word = word\n\n    def __lt__(self, other):\n        if self.count == other.count:\n            return self.word > other.word\n        return self.count < other.count\n\n    def __eq__(self, other):\n        return self.count == other.count and self.word == other.word\n\n\nclass Solution:\n    def topKFrequent(self, words: List[str], k: int) -> List[str]:\n        return self.priorityqueue(words, k)\n\n    # Time Complexity: O(nmlogn)\n    # Space Compexlity: O(n*m)\n    def sorting(self, words: List[str], k: int) -> List[str]:\n        counter = Counter(words)\n        counter = sorted(counter.keys(), key=counter.get, reverse=True)\n        return counter[:k]\n\n    # Time Complexity: O(nmlogk)\n    # Space Compexlity: O(k)\n    def priorityqueue(self, words: List[str], k: int) -> List[str]:\n        heap = []\n        counter = Counter(words)\n        heapq.heapify(heap)\n        for word in counter:\n            heapq.heappush(heap, (Comparator(counter[word], word), word))\n            if len(heap) > k:\n                heapq.heappop(heap)\n\n        res = []\n        for _ in range(k):\n            res.append(heapq.heappop(heap)[1])\n        return res[::-1]\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/692-top-k-frequent-words/",
      "datePublished": "2023-11-05T00:00:00Z",
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