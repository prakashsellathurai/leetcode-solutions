# insertion-sort-list


Try it on <a href='https://leetcode.com/problems/insertion-sort-list'>leetcode</a>

## Description
<div class="description">
<div><p>Given the <code>head</code> of a singly linked list, sort the list using <strong>insertion sort</strong>, and return <em>the sorted list's head</em>.</p>

<p>The steps of the <strong>insertion sort</strong> algorithm:</p>

<ol>
	<li>Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.</li>
	<li>At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.</li>
	<li>It repeats until no input elements remain.</li>
</ol>

<p>The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.</p>
<img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif" style="height:180px; width:300px">
<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/04/sort1linked-list.jpg" style="width: 422px; height: 222px;">
<pre><strong>Input:</strong> head = [4,2,1,3]
<strong>Output:</strong> [1,2,3,4]
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/04/sort2linked-list.jpg" style="width: 542px; height: 222px;">
<pre><strong>Input:</strong> head = [-1,5,3,4,0]
<strong>Output:</strong> [-1,0,3,4,5]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 5000]</code>.</li>
	<li><code>-5000 &lt;= Node.val &lt;= 5000</code></li>
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
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = head

        while curr:
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            next_ = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = next_
        return dummy.next

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "147. Insertion Sort List",
    "text": "Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.\nThe steps of the insertion sort algorithm:\n\nInsertion sort iterates, consuming one input element each repetition and growing a sorted output list.\nAt each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.\nIt repeats until no input elements remain.\n\nThe following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.\n\n\u00a0\nExample 1:\n\nInput: head = [4,2,1,3]\nOutput: [1,2,3,4]\n\nExample 2:\n\nInput: head = [-1,5,3,4,0]\nOutput: [-1,0,3,4,5]\n\n\u00a0\nConstraints:\n\nThe number of nodes in the list is in the range [1, 5000].\n-5000 <= Node.val <= 5000\n\n",
    "url": "https://leetcode.com/problems/insertion-sort-list",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:\n        dummy = ListNode()\n        curr = head\n\n        while curr:\n            prev = dummy\n            while prev.next and prev.next.val < curr.val:\n                prev = prev.next\n            next_ = curr.next\n            curr.next = prev.next\n            prev.next = curr\n            curr = next_\n        return dummy.next\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/insertion-sort-list/",
      "datePublished": "2024-10-05",
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