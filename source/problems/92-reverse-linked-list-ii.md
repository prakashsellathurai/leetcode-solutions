# 92-reverse-linked-list-ii


Try it on <a href='https://leetcode.com/problems/92-reverse-linked-list-ii'>leetcode</a>

## Description
<div class="description">
<div><p>Given the <code>head</code> of a singly linked list and two integers <code>left</code> and <code>right</code> where <code>left &lt;= right</code>, reverse the nodes of the list from position <code>left</code> to position <code>right</code>, and return <em>the reversed list</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg" style="width: 542px; height: 222px;">
<pre><strong>Input:</strong> head = [1,2,3,4,5], left = 2, right = 4
<strong>Output:</strong> [1,4,3,2,5]
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> head = [5], left = 1, right = 1
<strong>Output:</strong> [5]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is <code>n</code>.</li>
	<li><code>1 &lt;= n &lt;= 500</code></li>
	<li><code>-500 &lt;= Node.val &lt;= 500</code></li>
	<li><code>1 &lt;= left &lt;= right &lt;= n</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you do it in one pass?</div>
</div>

## Solution(Python)
```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        return self.recursion(head, left, right)

    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def recursion(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        if m == n:
            return head

        if m > 1:
            newHead = head
            newHead.next = self.recursion(head.next, m - 1, n - 1)
            return newHead
        else:
            next_ = head.next
            newHead = self.recursion(next_, 1, n - 1)
            nextnext_ = next_.next
            next_.next = head
            head.next = nextnext_
            return newHead

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "92. Reverse Linked List II",
    "text": "Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.\n\u00a0\nExample 1:\n\nInput: head = [1,2,3,4,5], left = 2, right = 4\nOutput: [1,4,3,2,5]\n\nExample 2:\nInput: head = [5], left = 1, right = 1\nOutput: [5]\n\n\u00a0\nConstraints:\n\nThe number of nodes in the list is n.\n1 <= n <= 500\n-500 <= Node.val <= 500\n1 <= left <= right <= n\n\n\u00a0\nFollow up: Could you do it in one pass?",
    "url": "https://leetcode.com/problems/92-reverse-linked-list-ii",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def reverseBetween(\n        self, head: Optional[ListNode], left: int, right: int\n    ) -> Optional[ListNode]:\n        return self.recursion(head, left, right)\n\n    # Time Complexity: O(N)\n    # Space Complexity: O(N)\n    def recursion(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:\n        if m == n:\n            return head\n\n        if m > 1:\n            newHead = head\n            newHead.next = self.recursion(head.next, m - 1, n - 1)\n            return newHead\n        else:\n            next_ = head.next\n            newHead = self.recursion(next_, 1, n - 1)\n            nextnext_ = next_.next\n            next_.next = head\n            head.next = nextnext_\n            return newHead\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/92-reverse-linked-list-ii/",
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