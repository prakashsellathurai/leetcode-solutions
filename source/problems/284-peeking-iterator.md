# 284-peeking-iterator


Try it on <a href='https://leetcode.com/problems/284-peeking-iterator'>leetcode</a>

## Description
<div class="description">
<div><p>Design an iterator that supports the <code>peek</code> operation on an existing iterator in addition to the <code>hasNext</code> and the <code>next</code> operations.</p>

<p>Implement the <code>PeekingIterator</code> class:</p>

<ul>
	<li><code>PeekingIterator(Iterator&lt;int&gt; nums)</code> Initializes the object with the given integer iterator <code>iterator</code>.</li>
	<li><code>int next()</code> Returns the next element in the array and moves the pointer to the next element.</li>
	<li><code>boolean hasNext()</code> Returns <code>true</code> if there are still elements in the array.</li>
	<li><code>int peek()</code> Returns the next element in the array <strong>without</strong> moving the pointer.</li>
</ul>

<p><strong>Note:</strong> Each language may have a different implementation of the constructor and <code>Iterator</code>, but they all support the <code>int next()</code> and <code>boolean hasNext()</code> functions.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input</strong>
["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
[[[1, 2, 3]], [], [], [], [], []]
<strong>Output</strong>
[null, 1, 2, 2, 3, false]

<strong>Explanation</strong>
PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [<u><strong>1</strong></u>,2,3]
peekingIterator.next();    // return 1, the pointer moves to the next element [1,<u><strong>2</strong></u>,3].
peekingIterator.peek();    // return 2, the pointer does not move [1,<u><strong>2</strong></u>,3].
peekingIterator.next();    // return 2, the pointer moves to the next element [1,2,<u><strong>3</strong></u>]
peekingIterator.next();    // return 3, the pointer moves to the next element [1,2,3]
peekingIterator.hasNext(); // return False
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li>All the calls to <code>next</code> and <code>peek</code> are valid.</li>
	<li>At most <code>1000</code> calls will be made to <code>next</code>, <code>hasNext</code>, and <code>peek</code>.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> How would you extend your design to be generic and work with all types, not just integer?</div>
</div>

## Solution(Python)
```Python
class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.buffer = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        return self.buffer

    def next(self):
        tmp = self.buffer
        self.buffer = self.iterator.next() if self.iterator.hasNext() else None
        return tmp

    def hasNext(self):
        return self.buffer != None

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "284. Peeking Iterator",
    "text": "Design an iterator that supports the peek operation on an existing iterator in addition to the hasNext and the next operations.\nImplement the PeekingIterator class:\n\nPeekingIterator(Iterator<int> nums) Initializes the object with the given integer iterator iterator.\nint next() Returns the next element in the array and moves the pointer to the next element.\nboolean hasNext() Returns true if there are still elements in the array.\nint peek() Returns the next element in the array without moving the pointer.\n\nNote: Each language may have a different implementation of the constructor and Iterator, but they all support the int next() and boolean hasNext() functions.\n\u00a0\nExample 1:\nInput\n[\"PeekingIterator\", \"next\", \"peek\", \"next\", \"next\", \"hasNext\"]\n[[[1, 2, 3]], [], [], [], [], []]\nOutput\n[null, 1, 2, 2, 3, false]\n\nExplanation\nPeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [1,2,3]\npeekingIterator.next();    // return 1, the pointer moves to the next element [1,2,3].\npeekingIterator.peek();    // return 2, the pointer does not move [1,2,3].\npeekingIterator.next();    // return 2, the pointer moves to the next element [1,2,3]\npeekingIterator.next();    // return 3, the pointer moves to the next element [1,2,3]\npeekingIterator.hasNext(); // return False\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 1000\n1 <= nums[i] <= 1000\nAll the calls to next and peek are valid.\nAt most 1000 calls will be made to next, hasNext, and peek.\n\n\u00a0\nFollow up: How would you extend your design to be generic and work with all types, not just integer?",
    "url": "https://leetcode.com/problems/284-peeking-iterator",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class PeekingIterator:\n    def __init__(self, iterator):\n        self.iterator = iterator\n        self.buffer = self.iterator.next() if self.iterator.hasNext() else None\n\n    def peek(self):\n        return self.buffer\n\n    def next(self):\n        tmp = self.buffer\n        self.buffer = self.iterator.next() if self.iterator.hasNext() else None\n        return tmp\n\n    def hasNext(self):\n        return self.buffer != None\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/284-peeking-iterator/",
      "datePublished": "2025-07-05",
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