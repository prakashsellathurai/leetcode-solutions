# 1291-sequential-digits


Try it on <a href='https://leetcode.com/problems/1291-sequential-digits'>leetcode</a>

## Description
<div class="description">
<div><p>An&nbsp;integer has <em>sequential digits</em> if and only if each digit in the number is one more than the previous digit.</p>

<p>Return a <strong>sorted</strong> list of all the integers&nbsp;in the range <code>[low, high]</code>&nbsp;inclusive that have sequential digits.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> low = 100, high = 300
<strong>Output:</strong> [123,234]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> low = 1000, high = 13000
<strong>Output:</strong> [1234,2345,3456,4567,5678,6789,12345]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>10 &lt;= low &lt;= high &lt;= 10^9</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    #     def isSequential(self,num):
    #         candidate = num
    #         candidate,after = divmod(candidate,10)

    #         while  candidate > 0:
    #             candidate,before = divmod(candidate,10)

    #             if after != before+1:
    #                 return False
    #             after = before
    #         return True

    #     def sequentialDigits(self, low: int, high: int) -> List[int]:
    #         res = []

    #         for num in range(low,high):
    #             if self.isSequential(num):
    #                 res.append(num)

    #         return res
    # Time Complexity: O(M-N)

    def sequentialDigits(self, low, high):
        out = []
        string = "123456789"

        for i in range(len(str(low)), len(str(high)) + 1):
            for j in range(10 - i):
                num = int(string[j: j + i])
                if low <= num and num <= high:
                    out.append(num)

        return out


# Time Complexity: O(1)
# Space Complexity: O(1)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1291. Sequential Digits",
    "text": "An\u00a0integer has sequential digits if and only if each digit in the number is one more than the previous digit.\nReturn a sorted list of all the integers\u00a0in the range [low, high]\u00a0inclusive that have sequential digits.\n\u00a0\nExample 1:\nInput: low = 100, high = 300\nOutput: [123,234]\nExample 2:\nInput: low = 1000, high = 13000\nOutput: [1234,2345,3456,4567,5678,6789,12345]\n\n\u00a0\nConstraints:\n\n10 <= low <= high <= 10^9\n\n",
    "url": "https://leetcode.com/problems/1291-sequential-digits",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    #     def isSequential(self,num):\n    #         candidate = num\n    #         candidate,after = divmod(candidate,10)\n\n    #         while  candidate > 0:\n    #             candidate,before = divmod(candidate,10)\n\n    #             if after != before+1:\n    #                 return False\n    #             after = before\n    #         return True\n\n    #     def sequentialDigits(self, low: int, high: int) -> List[int]:\n    #         res = []\n\n    #         for num in range(low,high):\n    #             if self.isSequential(num):\n    #                 res.append(num)\n\n    #         return res\n    # Time Complexity: O(M-N)\n\n    def sequentialDigits(self, low, high):\n        out = []\n        string = \"123456789\"\n\n        for i in range(len(str(low)), len(str(high)) + 1):\n            for j in range(10 - i):\n                num = int(string[j: j + i])\n                if low <= num and num <= high:\n                    out.append(num)\n\n        return out\n\n\n# Time Complexity: O(1)\n# Space Complexity: O(1)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1291-sequential-digits/",
      "datePublished": "2024-10-10",
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