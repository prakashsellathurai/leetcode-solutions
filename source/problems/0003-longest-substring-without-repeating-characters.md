# 0003-longest-substring-without-repeating-characters


Try it on <a href='https://leetcode.com/problems/0003-longest-substring-without-repeating-characters'>leetcode</a>

## Description
<div class="description">
<p>Given a string <code>s</code>, find the length of the <strong>longest</strong> <span data-keyword="substring-nonempty"><strong>substring</strong></span> without duplicate characters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcabcbb&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;abc&quot;, with the length of 3. Note that <code>&quot;bca&quot;</code> and <code>&quot;cab&quot;</code> are also correct answers.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bbbbb&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> The answer is &quot;b&quot;, with the length of 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;pwwkew&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;wke&quot;, with the length of 3.
Notice that the answer must be a substring, &quot;pwke&quot; is a subsequence and not a substring.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists of English letters, digits, symbols and spaces.</li>
</ul>

</div>

## Solution(Python)
```Python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.optimal(s)
        
    # Time Complexity: O(n^3)
    # Space Complexity: O(n)
    def bruteforce(self, s: str) -> int:
        n = len(s)
        long_sub_len = 0
        
        def isUnique(st):
            return len(st) == len(set(st))
        
        for i in range(n):
            for j in range(i,n):
                if isUnique(s[i:j]):
                    cur_len = j-i
                    if cur_len > long_sub_len:
                        long_sub_len = cur_len
        return long_sub_len
    
    # Time Complexity: O(n)
    # Space Complexity: O(min(m,n))
    def better(self, s: str) -> int:
        n = len(s)
        left = right = 0
        hashmap = defaultdict(lambda : 0)
        res = 0
        
        while right < n:
            hashmap[s[right]] += 1
            
            while hashmap[s[right]]  > 1:
                hashmap[s[left]] -= 1
                left += 1
                
            cur_width = right - left + 1 
            
            if cur_width > res:
                res = cur_width
            
            right += 1
            
        return res
    
    # Time Complexity: O(n)
    # Space Complexity: O(m)
    def optimal(self, s: str) -> int:
        seen = {}
        start = 0
        res = 0
        for end,c in enumerate(s):
            if c in seen:
                start = max(start,seen[c]+1)
            seen[c] = end
            res = max(res ,end-start+1)
        return res
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "3. Longest Substring Without Repeating Characters",
    "text": "Given a string s, find the length of the longest substring without duplicate characters.\n\u00a0\nExample 1:\n\nInput: s = \"abcabcbb\"\nOutput: 3\nExplanation: The answer is \"abc\", with the length of 3. Note that \"bca\" and \"cab\" are also correct answers.\n\nExample 2:\n\nInput: s = \"bbbbb\"\nOutput: 1\nExplanation: The answer is \"b\", with the length of 1.\n\nExample 3:\n\nInput: s = \"pwwkew\"\nOutput: 3\nExplanation: The answer is \"wke\", with the length of 3.\nNotice that the answer must be a substring, \"pwke\" is a subsequence and not a substring.\n\n\u00a0\nConstraints:\n\n0 <= s.length <= 5 * 104\ns consists of English letters, digits, symbols and spaces.\n\n",
    "url": "https://leetcode.com/problems/0003-longest-substring-without-repeating-characters",
    "answerCount": 1,
    "datePublished": "2023-09-30T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def lengthOfLongestSubstring(self, s: str) -> int:\n        return self.optimal(s)\n        \n    # Time Complexity: O(n^3)\n    # Space Complexity: O(n)\n    def bruteforce(self, s: str) -> int:\n        n = len(s)\n        long_sub_len = 0\n        \n        def isUnique(st):\n            return len(st) == len(set(st))\n        \n        for i in range(n):\n            for j in range(i,n):\n                if isUnique(s[i:j]):\n                    cur_len = j-i\n                    if cur_len > long_sub_len:\n                        long_sub_len = cur_len\n        return long_sub_len\n    \n    # Time Complexity: O(n)\n    # Space Complexity: O(min(m,n))\n    def better(self, s: str) -> int:\n        n = len(s)\n        left = right = 0\n        hashmap = defaultdict(lambda : 0)\n        res = 0\n        \n        while right < n:\n            hashmap[s[right]] += 1\n            \n            while hashmap[s[right]]  > 1:\n                hashmap[s[left]] -= 1\n                left += 1\n                \n            cur_width = right - left + 1 \n            \n            if cur_width > res:\n                res = cur_width\n            \n            right += 1\n            \n        return res\n    \n    # Time Complexity: O(n)\n    # Space Complexity: O(m)\n    def optimal(self, s: str) -> int:\n        seen = {}\n        start = 0\n        res = 0\n        for end,c in enumerate(s):\n            if c in seen:\n                start = max(start,seen[c]+1)\n            seen[c] = end\n            res = max(res ,end-start+1)\n        return res",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/0003-longest-substring-without-repeating-characters/",
      "datePublished": "2023-09-30T00:00:00Z",
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