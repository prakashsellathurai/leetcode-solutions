# 155-min-stack


Try it on <a href='https://leetcode.com/problems/155-min-stack'>leetcode</a>

## Description
<div class="description">
<div><p>Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.</p>

<p>Implement the <code>MinStack</code> class:</p>

<ul>
	<li><code>MinStack()</code> initializes the stack object.</li>
	<li><code>void push(int val)</code> pushes the element <code>val</code> onto the stack.</li>
	<li><code>void pop()</code> removes the element on the top of the stack.</li>
	<li><code>int top()</code> gets the top element of the stack.</li>
	<li><code>int getMin()</code> retrieves the minimum element in the stack.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input</strong>
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

<strong>Output</strong>
[null,null,null,null,-3,null,0,-2]

<strong>Explanation</strong>
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= val &lt;= 2<sup>31</sup> - 1</code></li>
	<li>Methods <code>pop</code>, <code>top</code> and <code>getMin</code> operations will always be called on <strong>non-empty</strong> stacks.</li>
	<li>At most <code>3 * 10<sup>4</sup></code> calls will be made to <code>push</code>, <code>pop</code>, <code>top</code>, and <code>getMin</code>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.min = val
            self.stack.append(val)
        elif val < self.min:
            y = (2 * val) - self.min
            self.min = val
            self.stack.append(y)
        else:
            self.stack.append(val)

    def pop(self) -> None:

        if self.stack:
            y = self.stack[-1]
            if y < self.min:
                self.min = (2 * self.min) - y
            self.stack.pop()

    def top(self) -> int:
        if self.stack[-1] < self.min:
            return self.min
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "155. Min Stack",
    "text": "Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.\nImplement the MinStack class:\n\nMinStack() initializes the stack object.\nvoid push(int val) pushes the element val onto the stack.\nvoid pop() removes the element on the top of the stack.\nint top() gets the top element of the stack.\nint getMin() retrieves the minimum element in the stack.\n\n\u00a0\nExample 1:\nInput\n[\"MinStack\",\"push\",\"push\",\"push\",\"getMin\",\"pop\",\"top\",\"getMin\"]\n[[],[-2],[0],[-3],[],[],[],[]]\n\nOutput\n[null,null,null,null,-3,null,0,-2]\n\nExplanation\nMinStack minStack = new MinStack();\nminStack.push(-2);\nminStack.push(0);\nminStack.push(-3);\nminStack.getMin(); // return -3\nminStack.pop();\nminStack.top();    // return 0\nminStack.getMin(); // return -2\n\n\u00a0\nConstraints:\n\n-231 <= val <= 231 - 1\nMethods pop, top and getMin operations will always be called on non-empty stacks.\nAt most 3 * 104 calls will be made to push, pop, top, and getMin.\n\n",
    "url": "https://leetcode.com/problems/155-min-stack",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class MinStack:\n    def __init__(self):\n        self.stack = []\n        self.min = None\n\n    def push(self, val: int) -> None:\n        if not self.stack:\n            self.min = val\n            self.stack.append(val)\n        elif val < self.min:\n            y = (2 * val) - self.min\n            self.min = val\n            self.stack.append(y)\n        else:\n            self.stack.append(val)\n\n    def pop(self) -> None:\n\n        if self.stack:\n            y = self.stack[-1]\n            if y < self.min:\n                self.min = (2 * self.min) - y\n            self.stack.pop()\n\n    def top(self) -> int:\n        if self.stack[-1] < self.min:\n            return self.min\n        else:\n            return self.stack[-1]\n\n    def getMin(self) -> int:\n        return self.min\n\n\n# Your MinStack object will be instantiated and called as such:\n# obj = MinStack()\n# obj.push(val)\n# obj.pop()\n# param_3 = obj.top()\n# param_4 = obj.getMin()\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/155-min-stack/",
      "datePublished": "2025-04-02",
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