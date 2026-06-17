# 406-queue-reconstruction-by-height


Try it on <a href='https://leetcode.com/problems/406-queue-reconstruction-by-height'>leetcode</a>

## Description
<div class="description">
<div><p>You are given an array of people, <code>people</code>, which are the attributes of some people in a queue (not necessarily in order). Each <code>people[i] = [h<sub>i</sub>, k<sub>i</sub>]</code> represents the <code>i<sup>th</sup></code> person of height <code>h<sub>i</sub></code> with <strong>exactly</strong> <code>k<sub>i</sub></code> other people in front who have a height greater than or equal to <code>h<sub>i</sub></code>.</p>

<p>Reconstruct and return <em>the queue that is represented by the input array </em><code>people</code>. The returned queue should be formatted as an array <code>queue</code>, where <code>queue[j] = [h<sub>j</sub>, k<sub>j</sub>]</code> is the attributes of the <code>j<sup>th</sup></code> person in the queue (<code>queue[0]</code> is the person at the front of the queue).</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
<strong>Output:</strong> [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
<strong>Explanation:</strong>
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
<strong>Output:</strong> [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= people.length &lt;= 2000</code></li>
	<li><code>0 &lt;= h<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
	<li><code>0 &lt;= k<sub>i</sub> &lt; people.length</code></li>
	<li>It is guaranteed that the queue can be reconstructed.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Node:
    def __init__(self, p):
        self.person = p
        self.count = 1
        self.left = None
        self.right = None


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        ln = len(people)
        if ln == 0:
            return []

        people = sorted(people, key=lambda x: (-x[0], x[1]))

        root = Node(people[0])
        for p in people[1:]:
            self.insert(root, p, p[1])

        res = []
        self.inorder(root, res)
        return res

    def insert(self, root, p, count):
        # insert to the left
        if root.count > count:
            if not root.left:
                root.left = Node(p)
            else:
                self.insert(root.left, p, count)
            # because I have now one more node on the left
            root.count += 1
        else:
            if not root.right:
                root.right = Node(p)
            else:
                # I already have count - root.count nodes on the left
                self.insert(root.right, p, count - root.count)

    def inorder(self, root, res):
        if root:
            self.inorder(root.left, res)
            res.append(root.person)
            self.inorder(root.right, res)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "406. Queue Reconstruction by Height",
    "text": "You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.\nReconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).\n\u00a0\nExample 1:\nInput: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]\nOutput: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]\nExplanation:\nPerson 0 has height 5 with no other people taller or the same height in front.\nPerson 1 has height 7 with no other people taller or the same height in front.\nPerson 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.\nPerson 3 has height 6 with one person taller or the same height in front, which is person 1.\nPerson 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.\nPerson 5 has height 7 with one person taller or the same height in front, which is person 1.\nHence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.\n\nExample 2:\nInput: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]\nOutput: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]\n\n\u00a0\nConstraints:\n\n1 <= people.length <= 2000\n0 <= hi <= 106\n0 <= ki < people.length\nIt is guaranteed that the queue can be reconstructed.\n\n",
    "url": "https://leetcode.com/problems/406-queue-reconstruction-by-height",
    "answerCount": 1,
    "datePublished": "2022-06-29T19:37:33+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Node:\n    def __init__(self, p):\n        self.person = p\n        self.count = 1\n        self.left = None\n        self.right = None\n\n\nclass Solution:\n    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:\n\n        ln = len(people)\n        if ln == 0:\n            return []\n\n        people = sorted(people, key=lambda x: (-x[0], x[1]))\n\n        root = Node(people[0])\n        for p in people[1:]:\n            self.insert(root, p, p[1])\n\n        res = []\n        self.inorder(root, res)\n        return res\n\n    def insert(self, root, p, count):\n        # insert to the left\n        if root.count > count:\n            if not root.left:\n                root.left = Node(p)\n            else:\n                self.insert(root.left, p, count)\n            # because I have now one more node on the left\n            root.count += 1\n        else:\n            if not root.right:\n                root.right = Node(p)\n            else:\n                # I already have count - root.count nodes on the left\n                self.insert(root.right, p, count - root.count)\n\n    def inorder(self, root, res):\n        if root:\n            self.inorder(root.left, res)\n            res.append(root.person)\n            self.inorder(root.right, res)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/406-queue-reconstruction-by-height/",
      "datePublished": "2022-06-29T19:37:33+05:30",
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