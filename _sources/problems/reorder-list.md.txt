# reorder-list


Try it on <a href='https://leetcode.com/problems/reorder-list'>leetcode</a>

## Description
<div class="description">
<div><p>You are given the head of a singly linked-list. The list can be represented as:</p>

<pre>L<sub>0</sub> → L<sub>1</sub> → … → L<sub>n - 1</sub> → L<sub>n</sub>
</pre>

<p><em>Reorder the list to be on the following form:</em></p>

<pre>L<sub>0</sub> → L<sub>n</sub> → L<sub>1</sub> → L<sub>n - 1</sub> → L<sub>2</sub> → L<sub>n - 2</sub> → …
</pre>

<p>You may not modify the values in the list's nodes. Only nodes themselves may be changed.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg" style="width: 422px; height: 222px;">
<pre><strong>Input:</strong> head = [1,2,3,4]
<strong>Output:</strong> [1,4,2,3]
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg" style="width: 542px; height: 222px;">
<pre><strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [1,5,2,4,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 5 * 10<sup>4</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 1000</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle point
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # detach into two lists
        node1 = head
        node2 = slow.next
        slow.next = None
        # reverse the second list
        prev = None
        curr = node2
        next_ = None
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        node2 = prev
        # alternatively attach the two lists
        curr = ListNode(0)

        while node1 or node2:

            if node1:
                curr.next = node1
                node1 = node1.next
                curr = curr.next
            if node2:
                curr.next = node2
                node2 = node2.next
                curr = curr.next
        head = curr.next
        # Time Complexity = O(n)
        # Space Complexity = O(1)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "143. Reorder List",
    "text": "You are given the head of a singly linked-list. The list can be represented as:\nL0 \u2192 L1 \u2192 \u2026 \u2192 Ln - 1 \u2192 Ln\n\nReorder the list to be on the following form:\nL0 \u2192 Ln \u2192 L1 \u2192 Ln - 1 \u2192 L2 \u2192 Ln - 2 \u2192 \u2026\n\nYou may not modify the values in the list's nodes. Only nodes themselves may be changed.\n\u00a0\nExample 1:\n\nInput: head = [1,2,3,4]\nOutput: [1,4,2,3]\n\nExample 2:\n\nInput: head = [1,2,3,4,5]\nOutput: [1,5,2,4,3]\n\n\u00a0\nConstraints:\n\nThe number of nodes in the list is in the range [1, 5 * 104].\n1 <= Node.val <= 1000\n\n",
    "url": "https://leetcode.com/problems/reorder-list",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def reorderList(self, head: Optional[ListNode]) -> None:\n        \"\"\"\n        Do not return anything, modify head in-place instead.\n        \"\"\"\n        # find the middle point\n        slow = head\n        fast = head\n\n        while fast and fast.next:\n            fast = fast.next.next\n            slow = slow.next\n        # detach into two lists\n        node1 = head\n        node2 = slow.next\n        slow.next = None\n        # reverse the second list\n        prev = None\n        curr = node2\n        next_ = None\n        while curr:\n            next_ = curr.next\n            curr.next = prev\n            prev = curr\n            curr = next_\n        node2 = prev\n        # alternatively attach the two lists\n        curr = ListNode(0)\n\n        while node1 or node2:\n\n            if node1:\n                curr.next = node1\n                node1 = node1.next\n                curr = curr.next\n            if node2:\n                curr.next = node2\n                node2 = node2.next\n                curr = curr.next\n        head = curr.next\n        # Time Complexity = O(n)\n        # Space Complexity = O(1)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/reorder-list/",
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