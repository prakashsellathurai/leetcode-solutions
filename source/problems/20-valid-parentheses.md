# 20-valid-parentheses


Try it on <a href='https://leetcode.com/problems/20-valid-parentheses'>leetcode</a>

## Description
<div class="description">
<div><p>Given a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.</p>

<p>An input string is valid if:</p>

<ol>
	<li>Open brackets must be closed by the same type of brackets.</li>
	<li>Open brackets must be closed in the correct order.</li>
</ol>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "()"
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "()[]{}"
<strong>Output:</strong> true
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "(]"
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of parentheses only <code>'()[]{}'</code>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def __init__(self):
        self.hashmap = {"}": "{", ")": "(", "]": "["}

    def isValid(self, s: str) -> bool:
        return self.constantspace(s)

    # Time Complexity: O(n)
    # Space Comeplxity: O(n)
    def stacksolution(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in self.hashmap.values():
                stack.append(c)
            elif c in self.hashmap.keys():
                if stack and self.hashmap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False

        return len(stack) == 0

    # Time Complexity: O(n^2)
    # Space Comeplxity: O(1)
    def constantspace(self, s: str) -> bool:
        def findmatching(s, expected_open_bracket):
            nonlocal i, j, count
            if j > -1 and s[j] == expected_open_bracket:
                s[i] = "#"
                s[j] = "#"
                while j >= 0 and s[j] == "#":
                    j -= 1
                return True
            else:
                return False

        count = 0  # count of open braces
        i = 0  # cur index
        j = -1  # open bracket index
        s = list(s)
        if len(s) == 0:
            return True
        else:
            while i < len(s):
                if s[i] in self.hashmap.keys():
                    ismatched = findmatching(s, self.hashmap[s[i]])
                    if not ismatched:
                        return False
                    count -= 1
                else:
                    j = i
                    count += 1
                i += 1
            return count == 0

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "20. Valid Parentheses",
    "text": "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.\nAn input string is valid if:\n\nOpen brackets must be closed by the same type of brackets.\nOpen brackets must be closed in the correct order.\n\n\u00a0\nExample 1:\nInput: s = \"()\"\nOutput: true\n\nExample 2:\nInput: s = \"()[]{}\"\nOutput: true\n\nExample 3:\nInput: s = \"(]\"\nOutput: false\n\n\u00a0\nConstraints:\n\n1 <= s.length <= 104\ns consists of parentheses only '()[]{}'.\n\n",
    "url": "https://leetcode.com/problems/20-valid-parentheses",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def __init__(self):\n        self.hashmap = {\"}\": \"{\", \")\": \"(\", \"]\": \"[\"}\n\n    def isValid(self, s: str) -> bool:\n        return self.constantspace(s)\n\n    # Time Complexity: O(n)\n    # Space Comeplxity: O(n)\n    def stacksolution(self, s: str) -> bool:\n        stack = []\n\n        for c in s:\n            if c in self.hashmap.values():\n                stack.append(c)\n            elif c in self.hashmap.keys():\n                if stack and self.hashmap[c] == stack[-1]:\n                    stack.pop()\n                else:\n                    return False\n            else:\n                return False\n\n        return len(stack) == 0\n\n    # Time Complexity: O(n^2)\n    # Space Comeplxity: O(1)\n    def constantspace(self, s: str) -> bool:\n        def findmatching(s, expected_open_bracket):\n            nonlocal i, j, count\n            if j > -1 and s[j] == expected_open_bracket:\n                s[i] = \"#\"\n                s[j] = \"#\"\n                while j >= 0 and s[j] == \"#\":\n                    j -= 1\n                return True\n            else:\n                return False\n\n        count = 0  # count of open braces\n        i = 0  # cur index\n        j = -1  # open bracket index\n        s = list(s)\n        if len(s) == 0:\n            return True\n        else:\n            while i < len(s):\n                if s[i] in self.hashmap.keys():\n                    ismatched = findmatching(s, self.hashmap[s[i]])\n                    if not ismatched:\n                        return False\n                    count -= 1\n                else:\n                    j = i\n                    count += 1\n                i += 1\n            return count == 0\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/20-valid-parentheses/",
      "datePublished": "2025-12-07",
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