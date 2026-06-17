# 1192-critical-connections-in-a-network


Try it on <a href='https://leetcode.com/problems/1192-critical-connections-in-a-network'>leetcode</a>

## Description
<div class="description">
<div><p>There are <code>n</code> servers numbered from <code>0</code> to <code>n - 1</code> connected by undirected server-to-server <code>connections</code> forming a network where <code>connections[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> represents a connection between servers <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code>. Any server can reach other servers directly or indirectly through the network.</p>

<p>A <em>critical connection</em> is a connection that, if removed, will make some servers unable to reach some other server.</p>

<p>Return all critical connections in the network in any order.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/09/03/1537_ex1_2.png" style="width: 198px; height: 248px;">
<pre><strong>Input:</strong> n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
<strong>Output:</strong> [[1,3]]
<strong>Explanation:</strong> [[3,1]] is also accepted.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> n = 2, connections = [[0,1]]
<strong>Output:</strong> [[0,1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>n - 1 &lt;= connections.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>There are no repeated connections.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        return self.optmial(n, connections)

    # Time Complexity: O(E*(V+E))
    # Space Complexity: O(V+E)
    def bruteforce(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # create graph adj list
        adjList = defaultdict(set)

        for x, y in connections:
            adjList[x].add(y)
            adjList[y].add(x)

        res = []

        # initial number of connected components
        total_com = 0
        visited = [False] * n
        for i in range(n):
            for j in range(n):
                if visited[i] == False and i != j:
                    total_com += 1
                    self.dfs(adjList, i, visited)

        #   remove each E and see if graph remains connected
        for x, y in connections:
            visited = [False] * n

            adjList[x].remove(y)
            adjList[y].remove(x)
            cur_comp = 0

            for i in range(n):
                if visited[i] == False:
                    cur_comp += 1
                    self.dfs(adjList, i, visited)

            # if removal of E increases number of connected compponents then it's a bridge
            if cur_comp > total_com:
                res.append([x, y])

            adjList[x].add(y)
            adjList[y].add(x)
        return res

    # Time Complexity: O((V+E))
    # Space Complexity: O(V+E)
    def dfs(self, adjList, i, visited):
        if visited[i]:
            return
        visited[i] = True
        for j in adjList[i]:
            if not visited[j]:
                self.dfs(adjList, j, visited)

    # Time Complexity: O(V+E)
    # Space Complexity: O(V+E)
    def optmial(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.low = [0] * n
        self.disc = [0] * n
        self.res = []
        self.time = 1

        self.adjList = defaultdict(set)

        for x, y in connections:
            self.adjList[x].add(y)
            self.adjList[y].add(x)

        for u in range(n):
            if not self.disc[u]:
                self.optimal_df_util(u, u)

        return self.res

    def optimal_df_util(self, u, p):
        self.time += 1
        self.low[u] = self.disc[u] = self.time

        for v in self.adjList[u]:
            if v == p:
                continue

            if not self.disc[v]:
                self.optimal_df_util(v, u)
                if self.disc[u] < self.low[v]:
                    self.res.append([u, v])
                self.low[u] = min(self.low[u], self.low[v])
            else:
                self.low[u] = min(self.low[u], self.disc[v])

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1192. Critical Connections in a Network",
    "text": "There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.\nA critical connection is a connection that, if removed, will make some servers unable to reach some other server.\nReturn all critical connections in the network in any order.\n\u00a0\nExample 1:\n\nInput: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]\nOutput: [[1,3]]\nExplanation: [[3,1]] is also accepted.\n\nExample 2:\nInput: n = 2, connections = [[0,1]]\nOutput: [[0,1]]\n\n\u00a0\nConstraints:\n\n2 <= n <= 105\nn - 1 <= connections.length <= 105\n0 <= ai, bi <= n - 1\nai != bi\nThere are no repeated connections.\n\n",
    "url": "https://leetcode.com/problems/1192-critical-connections-in-a-network",
    "answerCount": 1,
    "datePublished": "2024-10-10T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def criticalConnections(\n        self, n: int, connections: List[List[int]]\n    ) -> List[List[int]]:\n        return self.optmial(n, connections)\n\n    # Time Complexity: O(E*(V+E))\n    # Space Complexity: O(V+E)\n    def bruteforce(self, n: int, connections: List[List[int]]) -> List[List[int]]:\n        # create graph adj list\n        adjList = defaultdict(set)\n\n        for x, y in connections:\n            adjList[x].add(y)\n            adjList[y].add(x)\n\n        res = []\n\n        # initial number of connected components\n        total_com = 0\n        visited = [False] * n\n        for i in range(n):\n            for j in range(n):\n                if visited[i] == False and i != j:\n                    total_com += 1\n                    self.dfs(adjList, i, visited)\n\n        #   remove each E and see if graph remains connected\n        for x, y in connections:\n            visited = [False] * n\n\n            adjList[x].remove(y)\n            adjList[y].remove(x)\n            cur_comp = 0\n\n            for i in range(n):\n                if visited[i] == False:\n                    cur_comp += 1\n                    self.dfs(adjList, i, visited)\n\n            # if removal of E increases number of connected compponents then it's a bridge\n            if cur_comp > total_com:\n                res.append([x, y])\n\n            adjList[x].add(y)\n            adjList[y].add(x)\n        return res\n\n    # Time Complexity: O((V+E))\n    # Space Complexity: O(V+E)\n    def dfs(self, adjList, i, visited):\n        if visited[i]:\n            return\n        visited[i] = True\n        for j in adjList[i]:\n            if not visited[j]:\n                self.dfs(adjList, j, visited)\n\n    # Time Complexity: O(V+E)\n    # Space Complexity: O(V+E)\n    def optmial(self, n: int, connections: List[List[int]]) -> List[List[int]]:\n        self.low = [0] * n\n        self.disc = [0] * n\n        self.res = []\n        self.time = 1\n\n        self.adjList = defaultdict(set)\n\n        for x, y in connections:\n            self.adjList[x].add(y)\n            self.adjList[y].add(x)\n\n        for u in range(n):\n            if not self.disc[u]:\n                self.optimal_df_util(u, u)\n\n        return self.res\n\n    def optimal_df_util(self, u, p):\n        self.time += 1\n        self.low[u] = self.disc[u] = self.time\n\n        for v in self.adjList[u]:\n            if v == p:\n                continue\n\n            if not self.disc[v]:\n                self.optimal_df_util(v, u)\n                if self.disc[u] < self.low[v]:\n                    self.res.append([u, v])\n                self.low[u] = min(self.low[u], self.low[v])\n            else:\n                self.low[u] = min(self.low[u], self.disc[v])\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1192-critical-connections-in-a-network/",
      "datePublished": "2024-10-10T00:00:00Z",
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