# 0146-lru-cache


Try it on <a href='https://leetcode.com/problems/0146-lru-cache'>leetcode</a>

## Description
<div class="description">
<p>Design a data structure that follows the constraints of a <strong><a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU" target="_blank">Least Recently Used (LRU) cache</a></strong>.</p>

<p>Implement the <code>LRUCache</code> class:</p>

<ul>
	<li><code>LRUCache(int capacity)</code> Initialize the LRU cache with <strong>positive</strong> size <code>capacity</code>.</li>
	<li><code>int get(int key)</code> Return the value of the <code>key</code> if the key exists, otherwise return <code>-1</code>.</li>
	<li><code>void put(int key, int value)</code> Update the value of the <code>key</code> if the <code>key</code> exists. Otherwise, add the <code>key-value</code> pair to the cache. If the number of keys exceeds the <code>capacity</code> from this operation, <strong>evict</strong> the least recently used key.</li>
</ul>

<p>The functions <code>get</code> and <code>put</code> must each run in <code>O(1)</code> average time complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;LRUCache&quot;, &quot;put&quot;, &quot;put&quot;, &quot;get&quot;, &quot;put&quot;, &quot;get&quot;, &quot;put&quot;, &quot;get&quot;, &quot;get&quot;, &quot;get&quot;]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
<strong>Output</strong>
[null, null, null, 1, null, -1, null, -1, 3, 4]

<strong>Explanation</strong>
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= capacity &lt;= 3000</code></li>
	<li><code>0 &lt;= key &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= value &lt;= 10<sup>5</sup></code></li>
	<li>At most <code>2 * 10<sup>5</sup></code> calls will be made to <code>get</code> and <code>put</code>.</li>
</ul>

</div>

## Solution(Python)
```Python
from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = deque()
        

    def get(self, key: int) -> int:
        # if key is presnet in cache iremove the key in orderque and append in left
        if key in self.cache:

            # Move the accessed key to 
            # the front of the deque
            self.order.remove(key)
            self.order.appendleft(key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:

              # if key is presnet in cache iremove the key in orderque and append in left
            # if capcity is greyer pop
            # apped new key

        if key in self.cache:

            # Update the value and move
            # the key to the front
            self.cache[key] = value
            self.order.remove(key)
            self.order.appendleft(key)
        else:
            if len(self.cache) >= self.capacity:

                # Remove the least recently used item
                lru_key = self.order.pop()
                del self.cache[lru_key]

            # Add the new key-value pair
            self.cache[key] = value
            self.order.appendleft(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "146. LRU Cache",
    "text": "Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.\nImplement the LRUCache class:\n\nLRUCache(int capacity) Initialize the LRU cache with positive size capacity.\nint get(int key) Return the value of the key if the key exists, otherwise return -1.\nvoid put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.\n\nThe functions get and put must each run in O(1) average time complexity.\n\u00a0\nExample 1:\n\nInput\n[\"LRUCache\", \"put\", \"put\", \"get\", \"put\", \"get\", \"put\", \"get\", \"get\", \"get\"]\n[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]\nOutput\n[null, null, null, 1, null, -1, null, -1, 3, 4]\n\nExplanation\nLRUCache lRUCache = new LRUCache(2);\nlRUCache.put(1, 1); // cache is {1=1}\nlRUCache.put(2, 2); // cache is {1=1, 2=2}\nlRUCache.get(1);    // return 1\nlRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}\nlRUCache.get(2);    // returns -1 (not found)\nlRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}\nlRUCache.get(1);    // return -1 (not found)\nlRUCache.get(3);    // return 3\nlRUCache.get(4);    // return 4\n\n\u00a0\nConstraints:\n\n1 <= capacity <= 3000\n0 <= key <= 104\n0 <= value <= 105\nAt most 2 * 105 calls will be made to get and put.\n\n",
    "url": "https://leetcode.com/problems/0146-lru-cache",
    "answerCount": 1,
    "datePublished": "2026-01-05T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "from collections import deque\nclass LRUCache:\n\n    def __init__(self, capacity: int):\n        self.capacity = capacity\n        self.cache = {}\n        self.order = deque()\n        \n\n    def get(self, key: int) -> int:\n        # if key is presnet in cache iremove the key in orderque and append in left\n        if key in self.cache:\n\n            # Move the accessed key to \n            # the front of the deque\n            self.order.remove(key)\n            self.order.appendleft(key)\n            return self.cache[key]\n        else:\n            return -1\n        \n\n    def put(self, key: int, value: int) -> None:\n\n              # if key is presnet in cache iremove the key in orderque and append in left\n            # if capcity is greyer pop\n            # apped new key\n\n        if key in self.cache:\n\n            # Update the value and move\n            # the key to the front\n            self.cache[key] = value\n            self.order.remove(key)\n            self.order.appendleft(key)\n        else:\n            if len(self.cache) >= self.capacity:\n\n                # Remove the least recently used item\n                lru_key = self.order.pop()\n                del self.cache[lru_key]\n\n            # Add the new key-value pair\n            self.cache[key] = value\n            self.order.appendleft(key)\n\n\n# Your LRUCache object will be instantiated and called as such:\n# obj = LRUCache(capacity)\n# param_1 = obj.get(key)\n# obj.put(key,value)",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/0146-lru-cache/",
      "datePublished": "2026-01-05T00:00:00Z",
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