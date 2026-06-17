# 17-letter-combinations-of-a-phone-number


Try it on <a href='https://leetcode.com/problems/17-letter-combinations-of-a-phone-number'>leetcode</a>

## Description
<div class="description">
<div><p>Given a string containing digits from <code>2-9</code> inclusive, return all possible letter combinations that the number could represent. Return the answer in <strong>any order</strong>.</p>

<p>A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.</p>

<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png" style="width: 200px; height: 162px;"></p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> digits = "23"
<strong>Output:</strong> ["ad","ae","af","bd","be","bf","cd","ce","cf"]
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> digits = ""
<strong>Output:</strong> []
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> digits = "2"
<strong>Output:</strong> ["a","b","c"]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= digits.length &lt;= 4</code></li>
	<li><code>digits[i]</code> is a digit in the range <code>['2', '9']</code>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def __init__(self):
        self.hashTable = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        self.hashList = [
            "0",
            "1",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz",
        ]

    def letterCombinations(self, digits: str) -> List[str]:
        return self.dfs(digits)

    # Time Complexity: O(4^n)
    # Space Complexity: O(4^n)
    def bfs(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        res = []
        queue = deque([""])

        while queue:
            s = queue.popleft()

            if len(s) == n:
                res.append(s)
            else:
                for letter in self.hashList[int(digits[len(s)])]:
                    queue.append(s + letter)

        return res

    # Time Complexity: O(4^n*n)
    # Space Complexity: O(n)
    def dfs(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        res = []

        def backtrack(candidate, i):
            if len(candidate) == n:
                res.append(candidate)
                return
            for j in range(i, n):
                for code in self.hashTable[digits[j]]:
                    candidate += code
                    backtrack(candidate, j + 1)
                    candidate = candidate[:-1]

        backtrack("", 0)
        return res

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "17. Letter Combinations of a Phone Number",
    "text": "Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.\nA mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.\n\n\u00a0\nExample 1:\nInput: digits = \"23\"\nOutput: [\"ad\",\"ae\",\"af\",\"bd\",\"be\",\"bf\",\"cd\",\"ce\",\"cf\"]\n\nExample 2:\nInput: digits = \"\"\nOutput: []\n\nExample 3:\nInput: digits = \"2\"\nOutput: [\"a\",\"b\",\"c\"]\n\n\u00a0\nConstraints:\n\n0 <= digits.length <= 4\ndigits[i] is a digit in the range ['2', '9'].\n\n",
    "url": "https://leetcode.com/problems/17-letter-combinations-of-a-phone-number",
    "answerCount": 1,
    "datePublished": "2025-04-23T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def __init__(self):\n        self.hashTable = {\n            \"2\": \"abc\",\n            \"3\": \"def\",\n            \"4\": \"ghi\",\n            \"5\": \"jkl\",\n            \"6\": \"mno\",\n            \"7\": \"pqrs\",\n            \"8\": \"tuv\",\n            \"9\": \"wxyz\",\n        }\n        self.hashList = [\n            \"0\",\n            \"1\",\n            \"abc\",\n            \"def\",\n            \"ghi\",\n            \"jkl\",\n            \"mno\",\n            \"pqrs\",\n            \"tuv\",\n            \"wxyz\",\n        ]\n\n    def letterCombinations(self, digits: str) -> List[str]:\n        return self.dfs(digits)\n\n    # Time Complexity: O(4^n)\n    # Space Complexity: O(4^n)\n    def bfs(self, digits: str) -> List[str]:\n        n = len(digits)\n        if n == 0:\n            return []\n        res = []\n        queue = deque([\"\"])\n\n        while queue:\n            s = queue.popleft()\n\n            if len(s) == n:\n                res.append(s)\n            else:\n                for letter in self.hashList[int(digits[len(s)])]:\n                    queue.append(s + letter)\n\n        return res\n\n    # Time Complexity: O(4^n*n)\n    # Space Complexity: O(n)\n    def dfs(self, digits: str) -> List[str]:\n        n = len(digits)\n        if n == 0:\n            return []\n        res = []\n\n        def backtrack(candidate, i):\n            if len(candidate) == n:\n                res.append(candidate)\n                return\n            for j in range(i, n):\n                for code in self.hashTable[digits[j]]:\n                    candidate += code\n                    backtrack(candidate, j + 1)\n                    candidate = candidate[:-1]\n\n        backtrack(\"\", 0)\n        return res\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/17-letter-combinations-of-a-phone-number/",
      "datePublished": "2025-04-23T00:00:00Z",
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