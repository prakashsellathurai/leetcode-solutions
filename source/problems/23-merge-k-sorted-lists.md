# 23-merge-k-sorted-lists


Try it on <a href='https://leetcode.com/problems/23-merge-k-sorted-lists'>leetcode</a>

## Description
<div class="description">
<div><p>You are given an array of <code>k</code> linked-lists <code>lists</code>, each linked-list is sorted in ascending order.</p>

<p><em>Merge all the linked-lists into one sorted linked-list and return it.</em></p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> lists = [[1,4,5],[1,3,4],[2,6]]
<strong>Output:</strong> [1,1,2,3,4,4,5,6]
<strong>Explanation:</strong> The linked-lists are:
[
  1-&gt;4-&gt;5,
  1-&gt;3-&gt;4,
  2-&gt;6
]
merging them into one sorted list:
1-&gt;1-&gt;2-&gt;3-&gt;4-&gt;4-&gt;5-&gt;6
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> lists = []
<strong>Output:</strong> []
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> lists = [[]]
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>k == lists.length</code></li>
	<li><code>0 &lt;= k &lt;= 10^4</code></li>
	<li><code>0 &lt;= lists[i].length &lt;= 500</code></li>
	<li><code>-10^4 &lt;= lists[i][j] &lt;= 10^4</code></li>
	<li><code>lists[i]</code> is sorted in <strong>ascending order</strong>.</li>
	<li>The sum of <code>lists[i].length</code> won't exceed <code>10^4</code>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
from queue import PriorityQueue

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.spaceoptmized(lists)

    """
    traverse all nodes and store them in array
    sort the array 
    create the sorted linkedlist
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """

    def bruteforce(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sortedvals = []
        for list in lists:
            while list:
                sortedvals.append(list.val)
                list = list.next

        DummyNode = cur = ListNode(-1)
        sortedvals.sort()
        for val in sortedvals:
            cur.next = ListNode(val)
            cur = cur.next
        return DummyNode.next

    """
    we can optmize bruteforce approach if we put our kth node with prioirty of its value in a priority queue and we can access the smallest value in O(1)
    
    Time Complexity: O(nlogk)
    Space Complexity: O(n)
    """

    def timeoptmized(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val
        Res = cur = ListNode(-1)
        q = PriorityQueue()
        for lst in lists:
            if lst:
                q.put((lst.val, lst))

        while not q.empty():
            val, node = q.get()
            cur.next = ListNode(val)
            cur = cur.next
            node = node.next
            if node:
                q.put((node.val, node))

        return Res.next

    """
    merging  a two sorted list can be done with constant space
    
    what if we keep on merging the adjacent pairs until it becomes a single sorted lists
    at each step the count of lists reduced into half atnost atmost log2k of such iterations need for each interation we got n values to traverse 
    
    Time Complexity: O(nlogk)
    Space Complexity: O(1)
    
     """

    def spaceoptmized(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        interval = 1

        while interval < k:
            for i in range(0, k - interval, 2 * interval):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0] if k > 0 else None

    def mergeTwoLists(self, lst1, lst2):
        sortedlst = cur = ListNode(-1)

        while lst1 and lst2:
            if lst1.val <= lst2.val:
                cur.next = lst1
                lst1 = lst1.next
            else:
                cur.next = lst2
                lst2 = lst2.next
            cur = cur.next
        if not lst1:
            cur.next = lst2
        else:
            cur.next = lst1
        return sortedlst.next

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "23. Merge k Sorted Lists",
    "text": "You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.\nMerge all the linked-lists into one sorted linked-list and return it.\n\u00a0\nExample 1:\nInput: lists = [[1,4,5],[1,3,4],[2,6]]\nOutput: [1,1,2,3,4,4,5,6]\nExplanation: The linked-lists are:\n[\n  1->4->5,\n  1->3->4,\n  2->6\n]\nmerging them into one sorted list:\n1->1->2->3->4->4->5->6\n\nExample 2:\nInput: lists = []\nOutput: []\n\nExample 3:\nInput: lists = [[]]\nOutput: []\n\n\u00a0\nConstraints:\n\nk == lists.length\n0 <= k <= 10^4\n0 <= lists[i].length <= 500\n-10^4 <= lists[i][j] <= 10^4\nlists[i] is sorted in ascending order.\nThe sum of lists[i].length won't exceed 10^4.\n\n",
    "url": "https://leetcode.com/problems/23-merge-k-sorted-lists",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "from queue import PriorityQueue\n\n# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\n\n\nclass Solution:\n    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:\n        return self.spaceoptmized(lists)\n\n    \"\"\"\n    traverse all nodes and store them in array\n    sort the array \n    create the sorted linkedlist\n    Time Complexity: O(n log n)\n    Space Complexity: O(n)\n    \"\"\"\n\n    def bruteforce(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:\n        sortedvals = []\n        for list in lists:\n            while list:\n                sortedvals.append(list.val)\n                list = list.next\n\n        DummyNode = cur = ListNode(-1)\n        sortedvals.sort()\n        for val in sortedvals:\n            cur.next = ListNode(val)\n            cur = cur.next\n        return DummyNode.next\n\n    \"\"\"\n    we can optmize bruteforce approach if we put our kth node with prioirty of its value in a priority queue and we can access the smallest value in O(1)\n    \n    Time Complexity: O(nlogk)\n    Space Complexity: O(n)\n    \"\"\"\n\n    def timeoptmized(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:\n        ListNode.__lt__ = lambda self, other: self.val < other.val\n        Res = cur = ListNode(-1)\n        q = PriorityQueue()\n        for lst in lists:\n            if lst:\n                q.put((lst.val, lst))\n\n        while not q.empty():\n            val, node = q.get()\n            cur.next = ListNode(val)\n            cur = cur.next\n            node = node.next\n            if node:\n                q.put((node.val, node))\n\n        return Res.next\n\n    \"\"\"\n    merging  a two sorted list can be done with constant space\n    \n    what if we keep on merging the adjacent pairs until it becomes a single sorted lists\n    at each step the count of lists reduced into half atnost atmost log2k of such iterations need for each interation we got n values to traverse \n    \n    Time Complexity: O(nlogk)\n    Space Complexity: O(1)\n    \n     \"\"\"\n\n    def spaceoptmized(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:\n        k = len(lists)\n        interval = 1\n\n        while interval < k:\n            for i in range(0, k - interval, 2 * interval):\n                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])\n            interval *= 2\n\n        return lists[0] if k > 0 else None\n\n    def mergeTwoLists(self, lst1, lst2):\n        sortedlst = cur = ListNode(-1)\n\n        while lst1 and lst2:\n            if lst1.val <= lst2.val:\n                cur.next = lst1\n                lst1 = lst1.next\n            else:\n                cur.next = lst2\n                lst2 = lst2.next\n            cur = cur.next\n        if not lst1:\n            cur.next = lst2\n        else:\n            cur.next = lst1\n        return sortedlst.next\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/23-merge-k-sorted-lists/",
      "datePublished": "2022-08-31",
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