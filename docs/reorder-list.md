---
id: reorder-list
title: 143. Reorder List
sidebar_label: 143. Reorder List
---

Try it on <a href='https://leetcode.com/problems/reorder-list'>leetcode</a>
## Description
<div class="description">
<h2>143. Reorder List</h2><h3>Medium</h3><hr><div><p>You are given the head of a singly linked-list. The list can be represented as:</p>

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