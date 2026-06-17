# 0622-design-circular-queue


Try it on <a href='https://leetcode.com/problems/0622-design-circular-queue'>leetcode</a>

## Description
<div class="description">
<p>Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called &quot;Ring Buffer&quot;.</p>

<p>One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.</p>

<p>Implement the <code>MyCircularQueue</code> class:</p>

<ul>
	<li><code>MyCircularQueue(k)</code> Initializes the object with the size of the queue to be <code>k</code>.</li>
	<li><code>int Front()</code> Gets the front item from the queue. If the queue is empty, return <code>-1</code>.</li>
	<li><code>int Rear()</code> Gets the last item from the queue. If the queue is empty, return <code>-1</code>.</li>
	<li><code>boolean enQueue(int value)</code> Inserts an element into the circular queue. Return <code>true</code> if the operation is successful.</li>
	<li><code>boolean deQueue()</code> Deletes an element from the circular queue. Return <code>true</code> if the operation is successful.</li>
	<li><code>boolean isEmpty()</code> Checks whether the circular queue is empty or not.</li>
	<li><code>boolean isFull()</code> Checks whether the circular queue is full or not.</li>
</ul>

<p>You must solve the problem without using the built-in queue data structure in your programming language.&nbsp;</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;MyCircularQueue&quot;, &quot;enQueue&quot;, &quot;enQueue&quot;, &quot;enQueue&quot;, &quot;enQueue&quot;, &quot;Rear&quot;, &quot;isFull&quot;, &quot;deQueue&quot;, &quot;enQueue&quot;, &quot;Rear&quot;]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
<strong>Output</strong>
[null, true, true, true, false, 3, true, true, true, 4]

<strong>Explanation</strong>
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 1000</code></li>
	<li><code>0 &lt;= value &lt;= 1000</code></li>
	<li>At most <code>3000</code> calls will be made to&nbsp;<code>enQueue</code>, <code>deQueue</code>,&nbsp;<code>Front</code>,&nbsp;<code>Rear</code>,&nbsp;<code>isEmpty</code>, and&nbsp;<code>isFull</code>.</li>
</ul>

</div>

## Solution(Python)
```Python
class MyCircularQueue:

    def __init__(self, k: int):
        self.front = 0
        self.arr = [-1] * k 
        self.capsize = k 
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size >= self.capsize:
            return False
        rear = (self.front + self.size) % self.capsize
        self.arr[rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        res = self.arr[self.front]
        self.front = (self.front + 1) % self.capsize
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.arr[self.front]

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        rear = (self.front + self.size - 1) % self.capsize
        return self.arr[rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capsize
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "622. Design Circular Queue",
    "text": "Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called \"Ring Buffer\".\nOne of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.\nImplement the MyCircularQueue class:\n\nMyCircularQueue(k) Initializes the object with the size of the queue to be k.\nint Front() Gets the front item from the queue. If the queue is empty, return -1.\nint Rear() Gets the last item from the queue. If the queue is empty, return -1.\nboolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.\nboolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.\nboolean isEmpty() Checks whether the circular queue is empty or not.\nboolean isFull() Checks whether the circular queue is full or not.\n\nYou must solve the problem without using the built-in queue data structure in your programming language.\u00a0\n\u00a0\nExample 1:\n\nInput\n[\"MyCircularQueue\", \"enQueue\", \"enQueue\", \"enQueue\", \"enQueue\", \"Rear\", \"isFull\", \"deQueue\", \"enQueue\", \"Rear\"]\n[[3], [1], [2], [3], [4], [], [], [], [4], []]\nOutput\n[null, true, true, true, false, 3, true, true, true, 4]\n\nExplanation\nMyCircularQueue myCircularQueue = new MyCircularQueue(3);\nmyCircularQueue.enQueue(1); // return True\nmyCircularQueue.enQueue(2); // return True\nmyCircularQueue.enQueue(3); // return True\nmyCircularQueue.enQueue(4); // return False\nmyCircularQueue.Rear();     // return 3\nmyCircularQueue.isFull();   // return True\nmyCircularQueue.deQueue();  // return True\nmyCircularQueue.enQueue(4); // return True\nmyCircularQueue.Rear();     // return 4\n\n\u00a0\nConstraints:\n\n1 <= k <= 1000\n0 <= value <= 1000\nAt most 3000 calls will be made to\u00a0enQueue, deQueue,\u00a0Front,\u00a0Rear,\u00a0isEmpty, and\u00a0isFull.\n\n",
    "url": "https://leetcode.com/problems/0622-design-circular-queue",
    "answerCount": 1,
    "datePublished": "2026-05-19T13:15:53+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class MyCircularQueue:\n\n    def __init__(self, k: int):\n        self.front = 0\n        self.arr = [-1] * k \n        self.capsize = k \n        self.size = 0\n\n    def enQueue(self, value: int) -> bool:\n        if self.size >= self.capsize:\n            return False\n        rear = (self.front + self.size) % self.capsize\n        self.arr[rear] = value\n        self.size += 1\n        return True\n\n    def deQueue(self) -> bool:\n        if self.size == 0:\n            return False\n        res = self.arr[self.front]\n        self.front = (self.front + 1) % self.capsize\n        self.size -= 1\n        return True\n\n    def Front(self) -> int:\n        if self.size == 0:\n            return -1\n        return self.arr[self.front]\n\n    def Rear(self) -> int:\n        if self.size == 0:\n            return -1\n        rear = (self.front + self.size - 1) % self.capsize\n        return self.arr[rear]\n\n    def isEmpty(self) -> bool:\n        return self.size == 0\n\n    def isFull(self) -> bool:\n        return self.size == self.capsize\n        \n\n\n# Your MyCircularQueue object will be instantiated and called as such:\n# obj = MyCircularQueue(k)\n# param_1 = obj.enQueue(value)\n# param_2 = obj.deQueue()\n# param_3 = obj.Front()\n# param_4 = obj.Rear()\n# param_5 = obj.isEmpty()\n# param_6 = obj.isFull()",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/0622-design-circular-queue/",
      "datePublished": "2026-05-19T13:15:53+05:30",
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