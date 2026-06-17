# 341-flatten-nested-list-iterator


Try it on <a href='https://leetcode.com/problems/341-flatten-nested-list-iterator'>leetcode</a>

## Description
<div class="description">
<div><p>You are given a nested list of integers <code>nestedList</code>. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.</p>

<p>Implement the <code>NestedIterator</code> class:</p>

<ul>
	<li><code>NestedIterator(List&lt;NestedInteger&gt; nestedList)</code> Initializes the iterator with the nested list <code>nestedList</code>.</li>
	<li><code>int next()</code> Returns the next integer in the nested list.</li>
	<li><code>boolean hasNext()</code> Returns <code>true</code> if there are still some integers in the nested list and <code>false</code> otherwise.</li>
</ul>

<p>Your code will be tested with the following pseudocode:</p>

<pre>initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
</pre>

<p>If <code>res</code> matches the expected flattened list, then your code will be judged as correct.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nestedList = [[1,1],2,[1,1]]
<strong>Output:</strong> [1,1,2,1,1]
<strong>Explanation:</strong> By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nestedList = [1,[4,[6]]]
<strong>Output:</strong> [1,4,6]
<strong>Explanation:</strong> By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nestedList.length &lt;= 500</code></li>
	<li>The values of the integers in the nested list is in the range <code>[-10<sup>6</sup>, 10<sup>6</sup>]</code>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.itr = OptimalNestedIterator(nestedList)

    def next(self) -> int:
        return self.itr.next()

    def hasNext(self) -> bool:
        return self.itr.hasNext()


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


class NaiveNestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.arr = deque(self.chain(nestedList))

    def chain(self, cur: [NestedInteger]):
        tmp = []
        for val in cur:
            if val.isInteger():
                tmp.append(val.getInteger())
            else:
                tmp.extend(self.chain(val.getList()))
        return tmp

    def next(self) -> int:
        return self.arr.popleft()

    def hasNext(self) -> bool:
        return self.arr


class OptimalNestedIterator:
    def __init__(self, nestedList):
        def gen(nestedList):
            for x in nestedList:
                if x.isInteger():
                    yield x.getInteger()
                else:
                    for y in gen(x.getList()):
                        yield y

        self.gen = gen(nestedList)

    def next(self):
        return self.value

    def hasNext(self):
        try:
            self.value = next(self.gen)
            return True
        except StopIteration:
            return False

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "341. Flatten Nested List Iterator",
    "text": "You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.\nImplement the NestedIterator class:\n\nNestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.\nint next() Returns the next integer in the nested list.\nboolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.\n\nYour code will be tested with the following pseudocode:\ninitialize iterator with nestedList\nres = []\nwhile iterator.hasNext()\n    append iterator.next() to the end of res\nreturn res\n\nIf res matches the expected flattened list, then your code will be judged as correct.\n\u00a0\nExample 1:\nInput: nestedList = [[1,1],2,[1,1]]\nOutput: [1,1,2,1,1]\nExplanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].\n\nExample 2:\nInput: nestedList = [1,[4,[6]]]\nOutput: [1,4,6]\nExplanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].\n\n\u00a0\nConstraints:\n\n1 <= nestedList.length <= 500\nThe values of the integers in the nested list is in the range [-106, 106].\n\n",
    "url": "https://leetcode.com/problems/341-flatten-nested-list-iterator",
    "answerCount": 1,
    "datePublished": "2022-04-27T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "# \"\"\"\n# This is the interface that allows for creating nested lists.\n# You should not implement it, or speculate about its implementation\n# \"\"\"\n# class NestedInteger:\n#    def isInteger(self) -> bool:\n#        \"\"\"\n#        @return True if this NestedInteger holds a single integer, rather than a nested list.\n#        \"\"\"\n#\n#    def getInteger(self) -> int:\n#        \"\"\"\n#        @return the single integer that this NestedInteger holds, if it holds a single integer\n#        Return None if this NestedInteger holds a nested list\n#        \"\"\"\n#\n#    def getList(self) -> [NestedInteger]:\n#        \"\"\"\n#        @return the nested list that this NestedInteger holds, if it holds a nested list\n#        Return None if this NestedInteger holds a single integer\n#        \"\"\"\n\n\nclass NestedIterator:\n    def __init__(self, nestedList: [NestedInteger]):\n        self.itr = OptimalNestedIterator(nestedList)\n\n    def next(self) -> int:\n        return self.itr.next()\n\n    def hasNext(self) -> bool:\n        return self.itr.hasNext()\n\n\n# Your NestedIterator object will be instantiated and called as such:\n# i, v = NestedIterator(nestedList), []\n# while i.hasNext(): v.append(i.next())\n\n\nclass NaiveNestedIterator:\n    def __init__(self, nestedList: [NestedInteger]):\n        self.arr = deque(self.chain(nestedList))\n\n    def chain(self, cur: [NestedInteger]):\n        tmp = []\n        for val in cur:\n            if val.isInteger():\n                tmp.append(val.getInteger())\n            else:\n                tmp.extend(self.chain(val.getList()))\n        return tmp\n\n    def next(self) -> int:\n        return self.arr.popleft()\n\n    def hasNext(self) -> bool:\n        return self.arr\n\n\nclass OptimalNestedIterator:\n    def __init__(self, nestedList):\n        def gen(nestedList):\n            for x in nestedList:\n                if x.isInteger():\n                    yield x.getInteger()\n                else:\n                    for y in gen(x.getList()):\n                        yield y\n\n        self.gen = gen(nestedList)\n\n    def next(self):\n        return self.value\n\n    def hasNext(self):\n        try:\n            self.value = next(self.gen)\n            return True\n        except StopIteration:\n            return False\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/341-flatten-nested-list-iterator/",
      "datePublished": "2022-04-27T00:00:00Z",
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