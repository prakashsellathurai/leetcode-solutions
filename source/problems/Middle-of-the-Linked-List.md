# middle-of-the-linked-list


Try it on <a href='https://leetcode.com/problems/middle-of-the-linked-list'>leetcode</a>

## Description
<div class="description">
<div><p>Given the <code>head</code> of a singly linked list, return <em>the middle node of the linked list</em>.</p>

<p>If there are two middle nodes, return <strong>the second middle</strong> node.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/23/lc-midlist1.jpg" style="width: 544px; height: 65px;">
<pre><strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [3,4,5]
<strong>Explanation:</strong> The middle node of the list is node 3.
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/23/lc-midlist2.jpg" style="width: 664px; height: 65px;">
<pre><strong>Input:</strong> head = [1,2,3,4,5,6]
<strong>Output:</strong> [4,5,6]
<strong>Explanation:</strong> Since the list has two middle nodes with values 3 and 4, we return the second one.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 100]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 100</code></li>
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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "876. Middle of the Linked List",
    "text": "Given the head of a singly linked list, return the middle node of the linked list.\nIf there are two middle nodes, return the second middle node.\n\u00a0\nExample 1:\n\nInput: head = [1,2,3,4,5]\nOutput: [3,4,5]\nExplanation: The middle node of the list is node 3.\n\nExample 2:\n\nInput: head = [1,2,3,4,5,6]\nOutput: [4,5,6]\nExplanation: Since the list has two middle nodes with values 3 and 4, we return the second one.\n\n\u00a0\nConstraints:\n\nThe number of nodes in the list is in the range [1, 100].\n1 <= Node.val <= 100\n\n",
    "url": "https://leetcode.com/problems/middle-of-the-linked-list",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:\n        slow = fast = head\n\n        while fast and fast.next:\n            fast = fast.next.next\n            slow = slow.next\n        return slow\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/middle-of-the-linked-list/",
      "datePublished": "2025-10-16",
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