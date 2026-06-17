# find-the-town-judge


Try it on <a href='https://leetcode.com/problems/find-the-town-judge'>leetcode</a>

## Description
<div class="description">
<div><p>In a town, there are <code>n</code> people labeled from <code>1</code> to <code>n</code>. There is a rumor that one of these people is secretly the town judge.</p>

<p>If the town judge exists, then:</p>

<ol>
	<li>The town judge trusts nobody.</li>
	<li>Everybody (except for the town judge) trusts the town judge.</li>
	<li>There is exactly one person that satisfies properties <strong>1</strong> and <strong>2</strong>.</li>
</ol>

<p>You are given an array <code>trust</code> where <code>trust[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> representing that the person labeled <code>a<sub>i</sub></code> trusts the person labeled <code>b<sub>i</sub></code>.</p>

<p>Return <em>the label of the town judge if the town judge exists and can be identified, or return </em><code>-1</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> n = 2, trust = [[1,2]]
<strong>Output:</strong> 2
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> n = 3, trust = [[1,3],[2,3]]
<strong>Output:</strong> 3
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> n = 3, trust = [[1,3],[2,3],[3,1]]
<strong>Output:</strong> -1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>0 &lt;= trust.length &lt;= 10<sup>4</sup></code></li>
	<li><code>trust[i].length == 2</code></li>
	<li>All the pairs of <code>trust</code> are <strong>unique</strong>.</li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li><code>1 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    # The key idea is to visulaize this problem as grpah of n people with trust as
    # graph problem
    # According to the problem Town judge
    # 1.trusts nobody (i.e zero out going connections)
    # 2.everybody trusts him (i.e n incoiming connections)
    #
    # Instead of creating and traversing graph for finding a node with n-1             # connections
    #
    #  A counter array of size n indicating n people can be used to count
    #  number of outgoing connections by incrementing incoming connetion and
    #  decrementing the out going connection
    #
    # Time Complexity : O(T) ,T = length of trust array since 1<= n<=1000 nis               negligible
    # Space Complexity: O(T)
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        cntr = [0] * (n)

        for (a, b) in trust:
            cntr[a - 1] -= 1
            cntr[b - 1] += 1

        for i, cnt in enumerate(cntr):
            if cnt == n - 1:
                return i + 1

        return -1

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "997. Find the Town Judge",
    "text": "In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.\nIf the town judge exists, then:\n\nThe town judge trusts nobody.\nEverybody (except for the town judge) trusts the town judge.\nThere is exactly one person that satisfies properties 1 and 2.\n\nYou are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.\nReturn the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.\n\u00a0\nExample 1:\nInput: n = 2, trust = [[1,2]]\nOutput: 2\n\nExample 2:\nInput: n = 3, trust = [[1,3],[2,3]]\nOutput: 3\n\nExample 3:\nInput: n = 3, trust = [[1,3],[2,3],[3,1]]\nOutput: -1\n\n\u00a0\nConstraints:\n\n1 <= n <= 1000\n0 <= trust.length <= 104\ntrust[i].length == 2\nAll the pairs of trust are unique.\nai != bi\n1 <= ai, bi <= n\n\n",
    "url": "https://leetcode.com/problems/find-the-town-judge",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    # The key idea is to visulaize this problem as grpah of n people with trust as\n    # graph problem\n    # According to the problem Town judge\n    # 1.trusts nobody (i.e zero out going connections)\n    # 2.everybody trusts him (i.e n incoiming connections)\n    #\n    # Instead of creating and traversing graph for finding a node with n-1             # connections\n    #\n    #  A counter array of size n indicating n people can be used to count\n    #  number of outgoing connections by incrementing incoming connetion and\n    #  decrementing the out going connection\n    #\n    # Time Complexity : O(T) ,T = length of trust array since 1<= n<=1000 nis               negligible\n    # Space Complexity: O(T)\n    def findJudge(self, n: int, trust: List[List[int]]) -> int:\n        cntr = [0] * (n)\n\n        for (a, b) in trust:\n            cntr[a - 1] -= 1\n            cntr[b - 1] += 1\n\n        for i, cnt in enumerate(cntr):\n            if cnt == n - 1:\n                return i + 1\n\n        return -1\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/find-the-town-judge/",
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