# 1310-xor-queries-of-a-subarray


Try it on <a href='https://leetcode.com/problems/1310-xor-queries-of-a-subarray'>leetcode</a>

## Description
<div class="description">
<div><p>You are given an array <code>arr</code> of positive integers. You are also given the array <code>queries</code> where <code>queries[i] = [left<sub>i, </sub>right<sub>i</sub>]</code>.</p>

<p>For each query <code>i</code> compute the <strong>XOR</strong> of elements from <code>left<sub>i</sub></code> to <code>right<sub>i</sub></code> (that is, <code>arr[left<sub>i</sub>] XOR arr[left<sub>i</sub> + 1] XOR ... XOR arr[right<sub>i</sub>]</code> ).</p>

<p>Return an array <code>answer</code> where <code>answer[i]</code> is the answer to the <code>i<sup>th</sup></code> query.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
<strong>Output:</strong> [2,7,14,8] 
<strong>Explanation:</strong> 
The binary representation of the elements in the array are:
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
The XOR values for queries are:
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
<strong>Output:</strong> [8,0,4,4]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length, queries.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>queries[i].length == 2</code></li>
	<li><code>0 &lt;= left<sub>i</sub> &lt;= right<sub>i</sub> &lt; arr.length</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class segmentTree:
    def __init__(self, arr, n):
        self.n = n
        self.tree = [0] * ((4 * n) + 1)
        self.build(arr, 1, 0, n - 1)

    def build(self, arr, v, lt, rt):
        if lt == rt:
            self.tree[v] = arr[lt]
        else:
            mt = (lt + rt) >> 1
            self.build(arr, 2 * v, lt, mt)
            self.build(arr, 2 * v + 1, mt + 1, rt)
            self.tree[v] = self.tree[2 * v] ^ self.tree[2 * v + 1]

    def query(self, l, r):
        return self.__query(1, 0, self.n - 1, l, r)

    def __query(self, v, lt, rt, l, r):
        if l > r:
            return 0
        if l == lt and r == rt:
            return self.tree[v]
        mt = (lt + rt) >> 1
        return self.__query(2 * v, lt, mt, l, min(mt, r)) ^ self.__query(
            2 * v + 1, mt + 1, rt, max(mt + 1, l), r
        )


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        return self.sTree(arr, queries)

    # Time Complexoty: O(n)
    # space Complexity: O(n)
    def prexor(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        if not n:
            return []
        prefXOR = [0] * n
        prefXOR[0] = arr[0]
        for i in range(1, n):
            prefXOR[i] = prefXOR[i - 1] ^ arr[i]
        res = []
        for l, r in queries:
            if l > 0:
                res.append(prefXOR[l - 1] ^ prefXOR[r])
            else:
                res.append(prefXOR[r])
        return res

    # Time Complexoty: O(n)
    # space Complexity: O(n)
    def sTree(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        st = segmentTree(arr, n)
        return [st.query(l, r) for l, r in queries]

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1310. XOR Queries of a Subarray",
    "text": "You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].\nFor each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).\nReturn an array answer where answer[i] is the answer to the ith query.\n\u00a0\nExample 1:\nInput: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]\nOutput: [2,7,14,8] \nExplanation: \nThe binary representation of the elements in the array are:\n1 = 0001 \n3 = 0011 \n4 = 0100 \n8 = 1000 \nThe XOR values for queries are:\n[0,1] = 1 xor 3 = 2 \n[1,2] = 3 xor 4 = 7 \n[0,3] = 1 xor 3 xor 4 xor 8 = 14 \n[3,3] = 8\n\nExample 2:\nInput: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]\nOutput: [8,0,4,4]\n\n\u00a0\nConstraints:\n\n1 <= arr.length, queries.length <= 3 * 104\n1 <= arr[i] <= 109\nqueries[i].length == 2\n0 <= lefti <= righti < arr.length\n\n",
    "url": "https://leetcode.com/problems/1310-xor-queries-of-a-subarray",
    "answerCount": 1,
    "datePublished": "2022-06-28T12:31:21+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class segmentTree:\n    def __init__(self, arr, n):\n        self.n = n\n        self.tree = [0] * ((4 * n) + 1)\n        self.build(arr, 1, 0, n - 1)\n\n    def build(self, arr, v, lt, rt):\n        if lt == rt:\n            self.tree[v] = arr[lt]\n        else:\n            mt = (lt + rt) >> 1\n            self.build(arr, 2 * v, lt, mt)\n            self.build(arr, 2 * v + 1, mt + 1, rt)\n            self.tree[v] = self.tree[2 * v] ^ self.tree[2 * v + 1]\n\n    def query(self, l, r):\n        return self.__query(1, 0, self.n - 1, l, r)\n\n    def __query(self, v, lt, rt, l, r):\n        if l > r:\n            return 0\n        if l == lt and r == rt:\n            return self.tree[v]\n        mt = (lt + rt) >> 1\n        return self.__query(2 * v, lt, mt, l, min(mt, r)) ^ self.__query(\n            2 * v + 1, mt + 1, rt, max(mt + 1, l), r\n        )\n\n\nclass Solution:\n    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:\n        return self.sTree(arr, queries)\n\n    # Time Complexoty: O(n)\n    # space Complexity: O(n)\n    def prexor(self, arr: List[int], queries: List[List[int]]) -> List[int]:\n        n = len(arr)\n        if not n:\n            return []\n        prefXOR = [0] * n\n        prefXOR[0] = arr[0]\n        for i in range(1, n):\n            prefXOR[i] = prefXOR[i - 1] ^ arr[i]\n        res = []\n        for l, r in queries:\n            if l > 0:\n                res.append(prefXOR[l - 1] ^ prefXOR[r])\n            else:\n                res.append(prefXOR[r])\n        return res\n\n    # Time Complexoty: O(n)\n    # space Complexity: O(n)\n    def sTree(self, arr: List[int], queries: List[List[int]]) -> List[int]:\n        n = len(arr)\n        st = segmentTree(arr, n)\n        return [st.query(l, r) for l, r in queries]\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1310-xor-queries-of-a-subarray/",
      "datePublished": "2022-06-28T12:31:21+05:30",
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