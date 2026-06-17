# 0125-valid-palindrome


Try it on <a href='https://leetcode.com/problems/0125-valid-palindrome'>leetcode</a>

## Description
<div class="description">
<p>A phrase is a <strong>palindrome</strong> if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.</p>

<p>Given a string <code>s</code>, return <code>true</code><em> if it is a <strong>palindrome</strong>, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;A man, a plan, a canal: Panama&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> &quot;amanaplanacanalpanama&quot; is a palindrome.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;race a car&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> &quot;raceacar&quot; is not a palindrome.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot; &quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> s is an empty string &quot;&quot; after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of printable ASCII characters.</li>
</ul>

</div>

## Solution(Python)
```Python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.two_pointers(s)
    # Time Complexity: O(n)
    # Space complexity: O(n)
    def simulation(self, s):
        filtyered_char = filter(lambda ch:ch.isalnum(), s)
        lowercase_chars = map(lambda ch: ch.lower(),s )

        return lowercase_chars == lowercase_chars[::-1]

    # Time Complexity: O(n)
    # Space complexity: O(1)
    def two_pointers(self, s):
        i,j = 0, len(s) - 1
        while i<j:
            while i<j and not s[i].isalnum():
                i+=1

            while j>i and not s[j].isalnum():
                j-=1
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        return True

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "125. Valid Palindrome",
    "text": "A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.\nGiven a string s, return true if it is a palindrome, or false otherwise.\n\u00a0\nExample 1:\n\nInput: s = \"A man, a plan, a canal: Panama\"\nOutput: true\nExplanation: \"amanaplanacanalpanama\" is a palindrome.\n\nExample 2:\n\nInput: s = \"race a car\"\nOutput: false\nExplanation: \"raceacar\" is not a palindrome.\n\nExample 3:\n\nInput: s = \" \"\nOutput: true\nExplanation: s is an empty string \"\" after removing non-alphanumeric characters.\nSince an empty string reads the same forward and backward, it is a palindrome.\n\n\u00a0\nConstraints:\n\n1 <= s.length <= 2 * 105\ns consists only of printable ASCII characters.\n\n",
    "url": "https://leetcode.com/problems/0125-valid-palindrome",
    "answerCount": 1,
    "datePublished": "2025-09-28T18:13:28+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def isPalindrome(self, s: str) -> bool:\n        return self.two_pointers(s)\n    # Time Complexity: O(n)\n    # Space complexity: O(n)\n    def simulation(self, s):\n        filtyered_char = filter(lambda ch:ch.isalnum(), s)\n        lowercase_chars = map(lambda ch: ch.lower(),s )\n\n        return lowercase_chars == lowercase_chars[::-1]\n\n    # Time Complexity: O(n)\n    # Space complexity: O(1)\n    def two_pointers(self, s):\n        i,j = 0, len(s) - 1\n        while i<j:\n            while i<j and not s[i].isalnum():\n                i+=1\n\n            while j>i and not s[j].isalnum():\n                j-=1\n            if s[i].lower() != s[j].lower():\n                return False\n            i+=1\n            j-=1\n        return True\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/0125-valid-palindrome/",
      "datePublished": "2025-09-28T18:13:28+05:30",
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