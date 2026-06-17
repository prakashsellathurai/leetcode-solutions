# 707-design-linked-list


Try it on <a href='https://leetcode.com/problems/707-design-linked-list'>leetcode</a>

## Description
<div class="description">
<div><p>Design your implementation of the linked list. You can choose to use a singly or doubly linked list.<br>
A node in a singly linked list should have two attributes: <code>val</code> and <code>next</code>. <code>val</code> is the value of the current node, and <code>next</code> is a pointer/reference to the next node.<br>
If you want to use the doubly linked list, you will need one more attribute <code>prev</code> to indicate the previous node in the linked list. Assume all nodes in the linked list are <strong>0-indexed</strong>.</p>

<p>Implement the <code>MyLinkedList</code> class:</p>

<ul>
	<li><code>MyLinkedList()</code> Initializes the <code>MyLinkedList</code> object.</li>
	<li><code>int get(int index)</code> Get the value of the <code>index<sup>th</sup></code> node in the linked list. If the index is invalid, return <code>-1</code>.</li>
	<li><code>void addAtHead(int val)</code> Add a node of value <code>val</code> before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.</li>
	<li><code>void addAtTail(int val)</code> Append a node of value <code>val</code> as the last element of the linked list.</li>
	<li><code>void addAtIndex(int index, int val)</code> Add a node of value <code>val</code> before the <code>index<sup>th</sup></code> node in the linked list. If <code>index</code> equals the length of the linked list, the node will be appended to the end of the linked list. If <code>index</code> is greater than the length, the node <strong>will not be inserted</strong>.</li>
	<li><code>void deleteAtIndex(int index)</code> Delete the <code>index<sup>th</sup></code> node in the linked list, if the index is valid.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input</strong>
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
<strong>Output</strong>
[null, null, null, null, 2, null, 3]

<strong>Explanation</strong>
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1-&gt;2-&gt;3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1-&gt;3
myLinkedList.get(1);              // return 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= index, val &lt;= 1000</code></li>
	<li>Please do not use the built-in LinkedList library.</li>
	<li>At most <code>2000</code> calls will be made to <code>get</code>, <code>addAtHead</code>, <code>addAtTail</code>, <code>addAtIndex</code> and <code>deleteAtIndex</code>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """

        if index < 0 or index >= self.length:
            return -1

        cur = self.head

        while index != 0:

            cur = cur.next
            index -= 1

        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """

        new_node = ListNode(val)

        new_node.next = self.head

        if self.head:
            self.head.prev = new_node

        self.head = new_node

        self.length += 1

        if self.length == 1:
            self.tail = new_node

        ### trace and debug
        # self.print_linked_list()

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """

        new_node = ListNode(val)

        new_node.prev = self.tail

        if self.tail:
            self.tail.next = new_node

        self.tail = new_node

        self.length += 1

        if self.length == 1:
            self.head = new_node

        ### trace and debug
        # self.print_linked_list()

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """

        if index < 0 or index > self.length:
            return

        elif index == 0:
            self.addAtHead(val)

        elif index == self.length:
            self.addAtTail(val)

        else:

            cur = self.head
            while index - 1 != 0:

                cur = cur.next
                index -= 1

            new_node = ListNode(val)

            new_node.next = cur.next
            cur.next.prev = new_node

            cur.next = new_node
            new_node.prev = cur

            self.length += 1

        ### trace and debug
        # self.print_linked_list()

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """

        if index < 0 or index >= self.length:
            return

        elif index == 0:

            if self.head.next:
                self.head.next.prev = None

            self.head = self.head.next

            self.length -= 1

            if self.length == 0:
                self.tail = None

        elif index == self.length - 1:

            if self.tail.prev:
                self.tail.prev.next = None

            self.tail = self.tail.prev

            self.length -= 1

            if self.length == 0:
                self.head = None

        else:

            cur = self.head
            while index - 1 != 0:

                cur = cur.next
                index -= 1

            cur.next = cur.next.next
            cur.next.prev = cur

            self.length -= 1

        ### trace and debug
        # self.print_linked_list()

    def print_linked_list(self):

        cur = self.head

        while cur:
            print(f" {cur.val} -> ", end="")
            cur = cur.next

        print("\n")

        return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "707. Design Linked List",
    "text": "Design your implementation of the linked list. You can choose to use a singly or doubly linked list.\nA node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.\nIf you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.\nImplement the MyLinkedList class:\n\nMyLinkedList() Initializes the MyLinkedList object.\nint get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.\nvoid addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.\nvoid addAtTail(int val) Append a node of value val as the last element of the linked list.\nvoid addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.\nvoid deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.\n\n\u00a0\nExample 1:\nInput\n[\"MyLinkedList\", \"addAtHead\", \"addAtTail\", \"addAtIndex\", \"get\", \"deleteAtIndex\", \"get\"]\n[[], [1], [3], [1, 2], [1], [1], [1]]\nOutput\n[null, null, null, null, 2, null, 3]\n\nExplanation\nMyLinkedList myLinkedList = new MyLinkedList();\nmyLinkedList.addAtHead(1);\nmyLinkedList.addAtTail(3);\nmyLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3\nmyLinkedList.get(1);              // return 2\nmyLinkedList.deleteAtIndex(1);    // now the linked list is 1->3\nmyLinkedList.get(1);              // return 3\n\n\u00a0\nConstraints:\n\n0 <= index, val <= 1000\nPlease do not use the built-in LinkedList library.\nAt most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.\n\n",
    "url": "https://leetcode.com/problems/707-design-linked-list",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class ListNode:\n    def __init__(self, val):\n        self.val = val\n        self.prev = None\n        self.next = None\n\n\nclass MyLinkedList:\n    def __init__(self):\n        \"\"\"\n        Initialize your data structure here.\n        \"\"\"\n        self.head = None\n        self.tail = None\n        self.length = 0\n\n    def get(self, index: int) -> int:\n        \"\"\"\n        Get the value of the index-th node in the linked list. If the index is invalid, return -1.\n        \"\"\"\n\n        if index < 0 or index >= self.length:\n            return -1\n\n        cur = self.head\n\n        while index != 0:\n\n            cur = cur.next\n            index -= 1\n\n        return cur.val\n\n    def addAtHead(self, val: int) -> None:\n        \"\"\"\n        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.\n        \"\"\"\n\n        new_node = ListNode(val)\n\n        new_node.next = self.head\n\n        if self.head:\n            self.head.prev = new_node\n\n        self.head = new_node\n\n        self.length += 1\n\n        if self.length == 1:\n            self.tail = new_node\n\n        ### trace and debug\n        # self.print_linked_list()\n\n    def addAtTail(self, val: int) -> None:\n        \"\"\"\n        Append a node of value val to the last element of the linked list.\n        \"\"\"\n\n        new_node = ListNode(val)\n\n        new_node.prev = self.tail\n\n        if self.tail:\n            self.tail.next = new_node\n\n        self.tail = new_node\n\n        self.length += 1\n\n        if self.length == 1:\n            self.head = new_node\n\n        ### trace and debug\n        # self.print_linked_list()\n\n    def addAtIndex(self, index: int, val: int) -> None:\n        \"\"\"\n        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.\n        \"\"\"\n\n        if index < 0 or index > self.length:\n            return\n\n        elif index == 0:\n            self.addAtHead(val)\n\n        elif index == self.length:\n            self.addAtTail(val)\n\n        else:\n\n            cur = self.head\n            while index - 1 != 0:\n\n                cur = cur.next\n                index -= 1\n\n            new_node = ListNode(val)\n\n            new_node.next = cur.next\n            cur.next.prev = new_node\n\n            cur.next = new_node\n            new_node.prev = cur\n\n            self.length += 1\n\n        ### trace and debug\n        # self.print_linked_list()\n\n    def deleteAtIndex(self, index: int) -> None:\n        \"\"\"\n        Delete the index-th node in the linked list, if the index is valid.\n        \"\"\"\n\n        if index < 0 or index >= self.length:\n            return\n\n        elif index == 0:\n\n            if self.head.next:\n                self.head.next.prev = None\n\n            self.head = self.head.next\n\n            self.length -= 1\n\n            if self.length == 0:\n                self.tail = None\n\n        elif index == self.length - 1:\n\n            if self.tail.prev:\n                self.tail.prev.next = None\n\n            self.tail = self.tail.prev\n\n            self.length -= 1\n\n            if self.length == 0:\n                self.head = None\n\n        else:\n\n            cur = self.head\n            while index - 1 != 0:\n\n                cur = cur.next\n                index -= 1\n\n            cur.next = cur.next.next\n            cur.next.prev = cur\n\n            self.length -= 1\n\n        ### trace and debug\n        # self.print_linked_list()\n\n    def print_linked_list(self):\n\n        cur = self.head\n\n        while cur:\n            print(f\" {cur.val} -> \", end=\"\")\n            cur = cur.next\n\n        print(\"\\n\")\n\n        return\n\n\n# Your MyLinkedList object will be instantiated and called as such:\n# obj = MyLinkedList()\n# param_1 = obj.get(index)\n# obj.addAtHead(val)\n# obj.addAtTail(val)\n# obj.addAtIndex(index,val)\n# obj.deleteAtIndex(index)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/707-design-linked-list/",
      "datePublished": "2025-03-08",
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