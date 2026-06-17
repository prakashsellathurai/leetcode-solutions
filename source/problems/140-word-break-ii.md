# 140-word-break-ii


Try it on <a href='https://leetcode.com/problems/140-word-break-ii'>leetcode</a>

## Description
<div class="description">
<div><p>Given a string <code>s</code> and a dictionary of strings <code>wordDict</code>, add spaces in <code>s</code> to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in <strong>any order</strong>.</p>

<p><strong>Note</strong> that the same word in the dictionary may be reused multiple times in the segmentation.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
<strong>Output:</strong> ["cats and dog","cat sand dog"]
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
<strong>Output:</strong> ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
<strong>Explanation:</strong> Note that you are allowed to reuse a dictionary word.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 20</code></li>
	<li><code>1 &lt;= wordDict.length &lt;= 1000</code></li>
	<li><code>1 &lt;= wordDict[i].length &lt;= 10</code></li>
	<li><code>s</code> and <code>wordDict[i]</code> consist of only lowercase English letters.</li>
	<li>All the strings of <code>wordDict</code> are <strong>unique</strong>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.memo(s,wordDict)
        
    # Time Complexity: O(n*2^n)
    # Space Complexity: O(n*2^n)
    def bruteforce(self, s: str, wordDict: List[str]) -> List[str]:
        output, words = [], {}
        for word in wordDict:
            words[word] = True
       
        def backtrack(start:int, combo:list[str]) -> None:
            if start == len(s):
                output.append(" ".join(combo))
                return
            for i in range(start, len(s)):
                word = s[start:i+1]
                if word in words:
                    combo.append(word)
                    backtrack(i+1, combo)
                    combo.pop()
       
        backtrack(0, [])
        return output
    
    # Time Complexity: O(n*2)
    # Space Complexity: O(n*2)
    def memo(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        memo = {}
        
        def search(string):
            if string in memo:
                return memo[string]
            else:
                paths = []
                
                # base case
                # we include this in here in the case a word
                # that exists in the dictionary can be further decomposed
                if string in wordDict:
                    paths.append(string)
                
                for i in range(len(string)):
                    # if a prefix exists, then see if remainder can be decomposed
                    if string[:i] in wordDict:
                        path = search(string[i:])
                        # if it can't be decomposed, then it will be empty
                        # for each decomposition, prepend the prefix
                        for p in path:
                            paths.append(string[:i] + " " + "".join(p))
                memo[string] = paths
                return memo[string]
        
        return search(s)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "140. Word Break II",
    "text": "Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.\nNote that the same word in the dictionary may be reused multiple times in the segmentation.\n\u00a0\nExample 1:\nInput: s = \"catsanddog\", wordDict = [\"cat\",\"cats\",\"and\",\"sand\",\"dog\"]\nOutput: [\"cats and dog\",\"cat sand dog\"]\n\nExample 2:\nInput: s = \"pineapplepenapple\", wordDict = [\"apple\",\"pen\",\"applepen\",\"pine\",\"pineapple\"]\nOutput: [\"pine apple pen apple\",\"pineapple pen apple\",\"pine applepen apple\"]\nExplanation: Note that you are allowed to reuse a dictionary word.\n\nExample 3:\nInput: s = \"catsandog\", wordDict = [\"cats\",\"dog\",\"sand\",\"and\",\"cat\"]\nOutput: []\n\n\u00a0\nConstraints:\n\n1 <= s.length <= 20\n1 <= wordDict.length <= 1000\n1 <= wordDict[i].length <= 10\ns and wordDict[i] consist of only lowercase English letters.\nAll the strings of wordDict are unique.\n\n",
    "url": "https://leetcode.com/problems/140-word-break-ii",
    "answerCount": 1,
    "datePublished": "2025-01-05T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:\n        return self.memo(s,wordDict)\n        \n    # Time Complexity: O(n*2^n)\n    # Space Complexity: O(n*2^n)\n    def bruteforce(self, s: str, wordDict: List[str]) -> List[str]:\n        output, words = [], {}\n        for word in wordDict:\n            words[word] = True\n       \n        def backtrack(start:int, combo:list[str]) -> None:\n            if start == len(s):\n                output.append(\" \".join(combo))\n                return\n            for i in range(start, len(s)):\n                word = s[start:i+1]\n                if word in words:\n                    combo.append(word)\n                    backtrack(i+1, combo)\n                    combo.pop()\n       \n        backtrack(0, [])\n        return output\n    \n    # Time Complexity: O(n*2)\n    # Space Complexity: O(n*2)\n    def memo(self, s: str, wordDict: List[str]) -> List[str]:\n        wordDict = set(wordDict)\n        memo = {}\n        \n        def search(string):\n            if string in memo:\n                return memo[string]\n            else:\n                paths = []\n                \n                # base case\n                # we include this in here in the case a word\n                # that exists in the dictionary can be further decomposed\n                if string in wordDict:\n                    paths.append(string)\n                \n                for i in range(len(string)):\n                    # if a prefix exists, then see if remainder can be decomposed\n                    if string[:i] in wordDict:\n                        path = search(string[i:])\n                        # if it can't be decomposed, then it will be empty\n                        # for each decomposition, prepend the prefix\n                        for p in path:\n                            paths.append(string[:i] + \" \" + \"\".join(p))\n                memo[string] = paths\n                return memo[string]\n        \n        return search(s)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/140-word-break-ii/",
      "datePublished": "2025-01-05T00:00:00Z",
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