# 138-copy-list-with-random-pointer


Try it on <a href='https://leetcode.com/problems/138-copy-list-with-random-pointer'>leetcode</a>

## Description
<div class="description">
<div><p>A linked list of length <code>n</code> is given such that each node contains an additional random pointer, which could point to any node in the list, or <code>null</code>.</p>

<p>Construct a <a href="https://en.wikipedia.org/wiki/Object_copying#Deep_copy" target="_blank"><strong>deep copy</strong></a> of the list. The deep copy should consist of exactly <code>n</code> <strong>brand new</strong> nodes, where each new node has its value set to the value of its corresponding original node. Both the <code>next</code> and <code>random</code> pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. <strong>None of the pointers in the new list should point to nodes in the original list</strong>.</p>

<p>For example, if there are two nodes <code>X</code> and <code>Y</code> in the original list, where <code>X.random --&gt; Y</code>, then for the corresponding two nodes <code>x</code> and <code>y</code> in the copied list, <code>x.random --&gt; y</code>.</p>

<p>Return <em>the head of the copied linked list</em>.</p>

<p>The linked list is represented in the input/output as a list of <code>n</code> nodes. Each node is represented as a pair of <code>[val, random_index]</code> where:</p>

<ul>
	<li><code>val</code>: an integer representing <code>Node.val</code></li>
	<li><code>random_index</code>: the index of the node (range from <code>0</code> to <code>n-1</code>) that the <code>random</code> pointer points to, or <code>null</code> if it does not point to any node.</li>
</ul>

<p>Your code will <strong>only</strong> be given the <code>head</code> of the original linked list.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/12/18/e1.png" style="width: 700px; height: 142px;">
<pre><strong>Input:</strong> head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
<strong>Output:</strong> [[7,null],[13,0],[11,4],[10,2],[1,0]]
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/12/18/e2.png" style="width: 700px; height: 114px;">
<pre><strong>Input:</strong> head = [[1,1],[2,1]]
<strong>Output:</strong> [[1,1],[2,1]]
</pre>

<p><strong>Example 3:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/12/18/e3.png" style="width: 700px; height: 122px;"></strong></p>

<pre><strong>Input:</strong> head = [[3,null],[3,0],[3,null]]
<strong>Output:</strong> [[3,null],[3,0],[3,null]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 1000</code></li>
	<li><code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li><code>Node.random</code> is <code>null</code> or is pointing to some node in the linked list.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        return self.withconstantspace(head)

    """
    uses hashmap to map source Node to copy Node
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def withextraspace(self, head: "Optional[Node]") -> "Optional[Node]":
        copyHead = Node(-1)

        copy = copyHead
        source = head

        mapping = {}

        while source:
            tempcopy = Node(source.val)
            if source not in mapping:
                mapping[source] = tempcopy

            copy.next = tempcopy
            source = source.next
            copy = copy.next

        source = head
        copy = copyHead.next
        while source:
            if source.random in mapping:
                copy.random = mapping[source.random]
            else:
                copy.random = None
            source = source.next
            copy = copy.next

        return copyHead.next

    """
    Idea:
    create copy node and insert it between adjacent source node
    
    then iterate the source node again now random node of copy will be 
    random node of source next
    
    after that unwind the interleaved nodes
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def withconstantspace(self, head: "Optional[Node]") -> "Optional[Node]":
        dummyHead = Node(-1)
        dummyHead.next = head
        curr = head

        while curr:
            tmp = Node(curr.val)
            tmp.next = curr.next
            curr.next = tmp
            curr = tmp.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            else:
                curr.next.random = None
            curr = curr.next.next

        curr = dummyHead
        nxt = head

        while nxt:
            curr.next = nxt.next
            curr = nxt
            nxt = curr.next

        return dummyHead.next

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "138. Copy List with Random Pointer",
    "text": "A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.\nConstruct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.\nFor example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.\nReturn the head of the copied linked list.\nThe linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:\n\nval: an integer representing Node.val\nrandom_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.\n\nYour code will only be given the head of the original linked list.\n\u00a0\nExample 1:\n\nInput: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]\nOutput: [[7,null],[13,0],[11,4],[10,2],[1,0]]\n\nExample 2:\n\nInput: head = [[1,1],[2,1]]\nOutput: [[1,1],[2,1]]\n\nExample 3:\n\nInput: head = [[3,null],[3,0],[3,null]]\nOutput: [[3,null],[3,0],[3,null]]\n\n\u00a0\nConstraints:\n\n0 <= n <= 1000\n-104 <= Node.val <= 104\nNode.random is null or is pointing to some node in the linked list.\n\n",
    "url": "https://leetcode.com/problems/138-copy-list-with-random-pointer",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "\"\"\"\n# Definition for a Node.\nclass Node:\n    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):\n        self.val = int(x)\n        self.next = next\n        self.random = random\n\"\"\"\n\n\nclass Solution:\n    def copyRandomList(self, head: \"Optional[Node]\") -> \"Optional[Node]\":\n        return self.withconstantspace(head)\n\n    \"\"\"\n    uses hashmap to map source Node to copy Node\n    \n    Time Complexity: O(n)\n    Space Complexity: O(n)\n    \"\"\"\n\n    def withextraspace(self, head: \"Optional[Node]\") -> \"Optional[Node]\":\n        copyHead = Node(-1)\n\n        copy = copyHead\n        source = head\n\n        mapping = {}\n\n        while source:\n            tempcopy = Node(source.val)\n            if source not in mapping:\n                mapping[source] = tempcopy\n\n            copy.next = tempcopy\n            source = source.next\n            copy = copy.next\n\n        source = head\n        copy = copyHead.next\n        while source:\n            if source.random in mapping:\n                copy.random = mapping[source.random]\n            else:\n                copy.random = None\n            source = source.next\n            copy = copy.next\n\n        return copyHead.next\n\n    \"\"\"\n    Idea:\n    create copy node and insert it between adjacent source node\n    \n    then iterate the source node again now random node of copy will be \n    random node of source next\n    \n    after that unwind the interleaved nodes\n    \n    Time Complexity: O(n)\n    Space Complexity: O(1)\n    \"\"\"\n\n    def withconstantspace(self, head: \"Optional[Node]\") -> \"Optional[Node]\":\n        dummyHead = Node(-1)\n        dummyHead.next = head\n        curr = head\n\n        while curr:\n            tmp = Node(curr.val)\n            tmp.next = curr.next\n            curr.next = tmp\n            curr = tmp.next\n\n        curr = head\n        while curr:\n            if curr.random:\n                curr.next.random = curr.random.next\n            else:\n                curr.next.random = None\n            curr = curr.next.next\n\n        curr = dummyHead\n        nxt = head\n\n        while nxt:\n            curr.next = nxt.next\n            curr = nxt\n            nxt = curr.next\n\n        return dummyHead.next\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/138-copy-list-with-random-pointer/",
      "datePublished": "2023-05-18",
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