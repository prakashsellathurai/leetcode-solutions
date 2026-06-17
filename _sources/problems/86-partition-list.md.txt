# 86-partition-list


Try it on <a href='https://leetcode.com/problems/86-partition-list'>leetcode</a>

## Description
<div class="description">
<div><p>Given the <code>head</code> of a linked list and a value <code>x</code>, partition it such that all nodes <strong>less than</strong> <code>x</code> come before nodes <strong>greater than or equal</strong> to <code>x</code>.</p>

<p>You should <strong>preserve</strong> the original relative order of the nodes in each of the two partitions.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/partition.jpg" style="width: 662px; height: 222px;">
<pre><strong>Input:</strong> head = [1,4,3,2,5,2], x = 3
<strong>Output:</strong> [1,2,2,4,3,5]
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> head = [2,1], x = 2
<strong>Output:</strong> [1,2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 200]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li><code>-200 &lt;= x &lt;= 200</code></li>
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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = before = ListNode()
        after_head = after = ListNode()

        cur = head

        while cur:
            if cur.val < x:
                before.next = cur
                before = before.next
            else:
                after.next = cur
                after = after.next
            cur = cur.next
        after.next = None
        before.next = after_head.next
        return before_head.next

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "86. Partition List",
    "text": "Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.\nYou should preserve the original relative order of the nodes in each of the two partitions.\n\u00a0\nExample 1:\n\nInput: head = [1,4,3,2,5,2], x = 3\nOutput: [1,2,2,4,3,5]\n\nExample 2:\nInput: head = [2,1], x = 2\nOutput: [1,2]\n\n\u00a0\nConstraints:\n\nThe number of nodes in the list is in the range [0, 200].\n-100 <= Node.val <= 100\n-200 <= x <= 200\n\n",
    "url": "https://leetcode.com/problems/86-partition-list",
    "answerCount": 1,
    "datePublished": "2022-07-22T20:53:09+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:\n        before_head = before = ListNode()\n        after_head = after = ListNode()\n\n        cur = head\n\n        while cur:\n            if cur.val < x:\n                before.next = cur\n                before = before.next\n            else:\n                after.next = cur\n                after = after.next\n            cur = cur.next\n        after.next = None\n        before.next = after_head.next\n        return before_head.next\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/86-partition-list/",
      "datePublished": "2022-07-22T20:53:09+05:30",
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