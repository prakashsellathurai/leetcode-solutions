# 173-binary-search-tree-iterator


Try it on <a href='https://leetcode.com/problems/173-binary-search-tree-iterator'>leetcode</a>

## Description
<div class="description">

</div>

## Solution(Python)
```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.itr = OptimalBSTIterator(root)

    def next(self) -> int:
        return self.itr.next()

    def hasNext(self) -> bool:
        return self.itr.hasNext()


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# Time Complexity: O(n)
# Space Complexity: O(n)
class NaiveBSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left

    def next(self) -> int:
        if len(self.stack) > 0:
            cur = self.stack.pop()
            if cur.right is not None:
                next_ = cur.right
                while next_:
                    self.stack.append(next_)
                    next_ = next_.left
            return cur.val
        else:
            return None

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Time Complexity: O(n)
# Space Complexity: O(1)
class OptimalBSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.curr = root

    def next(self) -> int:
        if not self.hasNext():
            return None
        else:
            if self.curr.left is None:
                next_ = self.curr.val
                self.curr = self.curr.right
                return next_
            else:
                pred = self.curr.left

                while pred.right and pred.right != self.curr:
                    pred = pred.right

                if pred.right is None:
                    pred.right = self.curr
                    self.curr = self.curr.left
                else:
                    next_ = self.curr.val
                    pred.right = None
                    self.curr = self.curr.right
                    return next_
        return self.next()

    def hasNext(self) -> bool:
        return self.curr is not None

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "173-binary-search-tree-iterator",
    "text": "",
    "url": "https://leetcode.com/problems/173-binary-search-tree-iterator",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass BSTIterator:\n    def __init__(self, root: Optional[TreeNode]):\n        self.itr = OptimalBSTIterator(root)\n\n    def next(self) -> int:\n        return self.itr.next()\n\n    def hasNext(self) -> bool:\n        return self.itr.hasNext()\n\n\n# Your BSTIterator object will be instantiated and called as such:\n# obj = BSTIterator(root)\n# param_1 = obj.next()\n# param_2 = obj.hasNext()\n\n# Time Complexity: O(n)\n# Space Complexity: O(n)\nclass NaiveBSTIterator:\n    def __init__(self, root: Optional[TreeNode]):\n        self.stack = []\n\n        cur = root\n        while cur:\n            self.stack.append(cur)\n            cur = cur.left\n\n    def next(self) -> int:\n        if len(self.stack) > 0:\n            cur = self.stack.pop()\n            if cur.right is not None:\n                next_ = cur.right\n                while next_:\n                    self.stack.append(next_)\n                    next_ = next_.left\n            return cur.val\n        else:\n            return None\n\n    def hasNext(self) -> bool:\n        return len(self.stack) > 0\n\n\n# Time Complexity: O(n)\n# Space Complexity: O(1)\nclass OptimalBSTIterator:\n    def __init__(self, root: Optional[TreeNode]):\n        self.curr = root\n\n    def next(self) -> int:\n        if not self.hasNext():\n            return None\n        else:\n            if self.curr.left is None:\n                next_ = self.curr.val\n                self.curr = self.curr.right\n                return next_\n            else:\n                pred = self.curr.left\n\n                while pred.right and pred.right != self.curr:\n                    pred = pred.right\n\n                if pred.right is None:\n                    pred.right = self.curr\n                    self.curr = self.curr.left\n                else:\n                    next_ = self.curr.val\n                    pred.right = None\n                    self.curr = self.curr.right\n                    return next_\n        return self.next()\n\n    def hasNext(self) -> bool:\n        return self.curr is not None\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/173-binary-search-tree-iterator/",
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