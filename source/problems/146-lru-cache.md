# 146-lru-cache


Try it on <a href='https://leetcode.com/problems/146-lru-cache'>leetcode</a>

## Description
<div class="description">
<div><p>Design a data structure that follows the constraints of a <strong><a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU" target="_blank">Least Recently Used (LRU) cache</a></strong>.</p>

<p>Implement the <code>LRUCache</code> class:</p>

<ul>
	<li><code>LRUCache(int capacity)</code> Initialize the LRU cache with <strong>positive</strong> size <code>capacity</code>.</li>
	<li><code>int get(int key)</code> Return the value of the <code>key</code> if the key exists, otherwise return <code>-1</code>.</li>
	<li><code>void put(int key, int value)</code>&nbsp;Update the value of the <code>key</code> if the <code>key</code> exists. Otherwise, add the <code>key-value</code> pair to the cache. If the number of keys exceeds the <code>capacity</code> from this operation, <strong>evict</strong> the least recently used key.</li>
</ul>

<p>The functions&nbsp;<code data-stringify-type="code">get</code>&nbsp;and&nbsp;<code data-stringify-type="code">put</code>&nbsp;must each run in <code>O(1)</code> average time complexity.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input</strong>
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
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
	<li>At most 2<code>&nbsp;* 10<sup>5</sup></code>&nbsp;calls will be made to <code>get</code> and <code>put</code>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class ListNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cnt = 0
    
    def get(self, key: int) -> int:
        if key in  self.hashmap:
            node = self.hashmap[key]
            res = node.val
            self.__deleteNode(node)
            self.__addToHead(node)
            return res
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.__deleteNode(node)
            self.__addToHead(node)
        else:
            node = ListNode(key, value)
            self.hashmap[key] = node
            if self.cnt < self.capacity:
                self.cnt += 1
                self.__addToHead(node)
            else:
                del self.hashmap[self.tail.prev.key]
                self.__deleteNode(self.tail.prev)
                self.__addToHead(node)
    def __deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def __addToHead(self, node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node
    


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
    "text": "Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.\nImplement the LRUCache class:\n\nLRUCache(int capacity) Initialize the LRU cache with positive size capacity.\nint get(int key) Return the value of the key if the key exists, otherwise return -1.\nvoid put(int key, int value)\u00a0Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.\n\nThe functions\u00a0get\u00a0and\u00a0put\u00a0must each run in O(1) average time complexity.\n\u00a0\nExample 1:\nInput\n[\"LRUCache\", \"put\", \"put\", \"get\", \"put\", \"get\", \"put\", \"get\", \"get\", \"get\"]\n[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]\nOutput\n[null, null, null, 1, null, -1, null, -1, 3, 4]\n\nExplanation\nLRUCache lRUCache = new LRUCache(2);\nlRUCache.put(1, 1); // cache is {1=1}\nlRUCache.put(2, 2); // cache is {1=1, 2=2}\nlRUCache.get(1);    // return 1\nlRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}\nlRUCache.get(2);    // returns -1 (not found)\nlRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}\nlRUCache.get(1);    // return -1 (not found)\nlRUCache.get(3);    // return 3\nlRUCache.get(4);    // return 4\n\n\u00a0\nConstraints:\n\n1 <= capacity <= 3000\n0 <= key <= 104\n0 <= value <= 105\nAt most 2\u00a0* 105\u00a0calls will be made to get and put.\n\n",
    "url": "https://leetcode.com/problems/146-lru-cache",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class ListNode:\n    def __init__(self, key, val):\n        self.val = val\n        self.key = key\n        self.prev = None\n        self.next = None\n        \nclass LRUCache:\n\n    def __init__(self, capacity: int):\n        self.capacity = capacity\n        self.hashmap = {}\n        self.head = ListNode(0,0)\n        self.tail = ListNode(0,0)\n        self.head.next = self.tail\n        self.tail.prev = self.head\n        self.cnt = 0\n    \n    def get(self, key: int) -> int:\n        if key in  self.hashmap:\n            node = self.hashmap[key]\n            res = node.val\n            self.__deleteNode(node)\n            self.__addToHead(node)\n            return res\n        return -1\n\n    def put(self, key: int, value: int) -> None:\n        if key in self.hashmap:\n            node = self.hashmap[key]\n            node.val = value\n            self.__deleteNode(node)\n            self.__addToHead(node)\n        else:\n            node = ListNode(key, value)\n            self.hashmap[key] = node\n            if self.cnt < self.capacity:\n                self.cnt += 1\n                self.__addToHead(node)\n            else:\n                del self.hashmap[self.tail.prev.key]\n                self.__deleteNode(self.tail.prev)\n                self.__addToHead(node)\n    def __deleteNode(self, node):\n        node.prev.next = node.next\n        node.next.prev = node.prev\n        \n    def __addToHead(self, node):\n        node.next = self.head.next\n        node.next.prev = node\n        node.prev = self.head\n        self.head.next = node\n    \n\n\n# Your LRUCache object will be instantiated and called as such:\n# obj = LRUCache(capacity)\n# param_1 = obj.get(key)\n# obj.put(key,value)",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/146-lru-cache/",
      "datePublished": "2023-04-25",
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