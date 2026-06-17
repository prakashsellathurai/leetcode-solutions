# 705-design-hashset


Try it on <a href='https://leetcode.com/problems/705-design-hashset'>leetcode</a>

## Description
<div class="description">
<div><p>Design a HashSet without using any built-in hash table libraries.</p>

<p>Implement <code>MyHashSet</code> class:</p>

<ul>
	<li><code>void add(key)</code> Inserts the value <code>key</code> into the HashSet.</li>
	<li><code>bool contains(key)</code> Returns whether the value <code>key</code> exists in the HashSet or not.</li>
	<li><code>void remove(key)</code> Removes the value <code>key</code> in the HashSet. If <code>key</code> does not exist in the HashSet, do nothing.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input</strong>
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
<strong>Output</strong>
[null, null, null, true, false, null, true, null, false]

<strong>Explanation</strong>
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= key &lt;= 10<sup>6</sup></code></li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>add</code>, <code>remove</code>, and <code>contains</code>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class MyHashSet:
    def eval_hash(self, key):
        return key % (1 << 15)

    def __init__(self):
        self.arr = [[] for _ in range(1 << 15)]

    def add(self, key: int) -> None:
        t = self.eval_hash(key)
        if key not in self.arr[t]:
            self.arr[t].append(key)

    def remove(self, key: int) -> None:
        t = self.eval_hash(key)
        if key in self.arr[t]:
            self.arr[t].remove(key)

    def contains(self, key: int) -> bool:
        t = self.eval_hash(key)
        return key in self.arr[t]

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "705. Design HashSet",
    "text": "Design a HashSet without using any built-in hash table libraries.\nImplement MyHashSet class:\n\nvoid add(key) Inserts the value key into the HashSet.\nbool contains(key) Returns whether the value key exists in the HashSet or not.\nvoid remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.\n\n\u00a0\nExample 1:\nInput\n[\"MyHashSet\", \"add\", \"add\", \"contains\", \"contains\", \"add\", \"contains\", \"remove\", \"contains\"]\n[[], [1], [2], [1], [3], [2], [2], [2], [2]]\nOutput\n[null, null, null, true, false, null, true, null, false]\n\nExplanation\nMyHashSet myHashSet = new MyHashSet();\nmyHashSet.add(1);      // set = [1]\nmyHashSet.add(2);      // set = [1, 2]\nmyHashSet.contains(1); // return True\nmyHashSet.contains(3); // return False, (not found)\nmyHashSet.add(2);      // set = [1, 2]\nmyHashSet.contains(2); // return True\nmyHashSet.remove(2);   // set = [1]\nmyHashSet.contains(2); // return False, (already removed)\n\u00a0\nConstraints:\n\n0 <= key <= 106\nAt most 104 calls will be made to add, remove, and contains.\n\n",
    "url": "https://leetcode.com/problems/705-design-hashset",
    "answerCount": 1,
    "datePublished": "2026-05-13T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class MyHashSet:\n    def eval_hash(self, key):\n        return key % (1 << 15)\n\n    def __init__(self):\n        self.arr = [[] for _ in range(1 << 15)]\n\n    def add(self, key: int) -> None:\n        t = self.eval_hash(key)\n        if key not in self.arr[t]:\n            self.arr[t].append(key)\n\n    def remove(self, key: int) -> None:\n        t = self.eval_hash(key)\n        if key in self.arr[t]:\n            self.arr[t].remove(key)\n\n    def contains(self, key: int) -> bool:\n        t = self.eval_hash(key)\n        return key in self.arr[t]\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/705-design-hashset/",
      "datePublished": "2026-05-13T00:00:00Z",
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