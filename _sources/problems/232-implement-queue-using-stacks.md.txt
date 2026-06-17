# 232-implement-queue-using-stacks


Try it on <a href='https://leetcode.com/problems/232-implement-queue-using-stacks'>leetcode</a>

## Description
<div class="description">
<div><p>Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (<code>push</code>, <code>peek</code>, <code>pop</code>, and <code>empty</code>).</p>

<p>Implement the <code>MyQueue</code> class:</p>

<ul>
	<li><code>void push(int x)</code> Pushes element x to the back of the queue.</li>
	<li><code>int pop()</code> Removes the element from the front of the queue and returns it.</li>
	<li><code>int peek()</code> Returns the element at the front of the queue.</li>
	<li><code>boolean empty()</code> Returns <code>true</code> if the queue is empty, <code>false</code> otherwise.</li>
</ul>

<p><strong>Notes:</strong></p>

<ul>
	<li>You must use <strong>only</strong> standard operations of a stack, which means only <code>push to top</code>, <code>peek/pop from top</code>, <code>size</code>, and <code>is empty</code> operations are valid.</li>
	<li>Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input</strong>
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
<strong>Output</strong>
[null, null, null, 1, 1, false]

<strong>Explanation</strong>
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= x &lt;= 9</code></li>
	<li>At most <code>100</code>&nbsp;calls will be made to <code>push</code>, <code>pop</code>, <code>peek</code>, and <code>empty</code>.</li>
	<li>All the calls to <code>pop</code> and <code>peek</code> are valid.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow-up:</strong> Can you implement the queue such that each operation is <strong><a href="https://en.wikipedia.org/wiki/Amortized_analysis" target="_blank">amortized</a></strong> <code>O(1)</code> time complexity? In other words, performing <code>n</code> operations will take overall <code>O(n)</code> time even if one of those operations may take longer.</p>
</div>
</div>

## Solution(Python)
```Python
class MyQueue:
    def __init__(self):
        self.stack = []
        self.queue = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        self.move()
        if self.queue:
            popped = self.queue.pop()
        return popped

    def peek(self) -> int:
        self.move()
        return self.queue[-1]

    def empty(self) -> bool:
        return not self.stack and not self.queue

    def move(self) -> None:
        if not self.queue:
            while self.stack:
                self.queue.append(self.stack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "232. Implement Queue using Stacks",
    "text": "Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).\nImplement the MyQueue class:\n\nvoid push(int x) Pushes element x to the back of the queue.\nint pop() Removes the element from the front of the queue and returns it.\nint peek() Returns the element at the front of the queue.\nboolean empty() Returns true if the queue is empty, false otherwise.\n\nNotes:\n\nYou must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.\nDepending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.\n\n\u00a0\nExample 1:\nInput\n[\"MyQueue\", \"push\", \"push\", \"peek\", \"pop\", \"empty\"]\n[[], [1], [2], [], [], []]\nOutput\n[null, null, null, 1, 1, false]\n\nExplanation\nMyQueue myQueue = new MyQueue();\nmyQueue.push(1); // queue is: [1]\nmyQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)\nmyQueue.peek(); // return 1\nmyQueue.pop(); // return 1, queue is [2]\nmyQueue.empty(); // return false\n\n\u00a0\nConstraints:\n\n1 <= x <= 9\nAt most 100\u00a0calls will be made to push, pop, peek, and empty.\nAll the calls to pop and peek are valid.\n\n\u00a0\nFollow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.\n",
    "url": "https://leetcode.com/problems/232-implement-queue-using-stacks",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class MyQueue:\n    def __init__(self):\n        self.stack = []\n        self.queue = []\n\n    def push(self, x: int) -> None:\n        self.stack.append(x)\n\n    def pop(self) -> int:\n        self.move()\n        if self.queue:\n            popped = self.queue.pop()\n        return popped\n\n    def peek(self) -> int:\n        self.move()\n        return self.queue[-1]\n\n    def empty(self) -> bool:\n        return not self.stack and not self.queue\n\n    def move(self) -> None:\n        if not self.queue:\n            while self.stack:\n                self.queue.append(self.stack.pop())\n\n\n# Your MyQueue object will be instantiated and called as such:\n# obj = MyQueue()\n# obj.push(x)\n# param_2 = obj.pop()\n# param_3 = obj.peek()\n# param_4 = obj.empty()\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/232-implement-queue-using-stacks/",
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