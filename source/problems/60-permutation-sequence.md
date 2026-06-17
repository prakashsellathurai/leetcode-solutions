# 60-permutation-sequence


Try it on <a href='https://leetcode.com/problems/60-permutation-sequence'>leetcode</a>

## Description
<div class="description">
<div><p>The set <code>[1, 2, 3, ...,&nbsp;n]</code> contains a total of <code>n!</code> unique permutations.</p>

<p>By listing and labeling all of the permutations in order, we get the following sequence for <code>n = 3</code>:</p>

<ol>
	<li><code>"123"</code></li>
	<li><code>"132"</code></li>
	<li><code>"213"</code></li>
	<li><code>"231"</code></li>
	<li><code>"312"</code></li>
	<li><code>"321"</code></li>
</ol>

<p>Given <code>n</code> and <code>k</code>, return the <code>k<sup>th</sup></code> permutation sequence.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> n = 3, k = 3
<strong>Output:</strong> "213"
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> n = 4, k = 9
<strong>Output:</strong> "2314"
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> n = 3, k = 1
<strong>Output:</strong> "123"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 9</code></li>
	<li><code>1 &lt;= k &lt;= n!</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return self.optimal(n, k)

    # Time Complexity: O(n!)
    # Space Complexity: O(n)
    def bruteforce(self, n: int, k: int) -> str:

        res = []
        nums = [i for i in range(1, n + 1)]
        times = reduce(lambda x, y: x * y, nums)
        res.append(nums[:])
        for _ in range(1, times + 1):
            nums[:] = self.nextPermutation(nums)
            res.append(nums[:])
        return "".join(map(str, res[k - 1]))

    def nextPermutation(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2

        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1

        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1

            nums[j], nums[i] = nums[i], nums[j]

        s = i + 1
        e = n - 1

        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1
        return nums

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # there are n! possibilties which means MSB index will be one of n numbers
    # which is n!/n = n-1!  in ascending order
    # so k/(n-1)! gives index of MSB k updates to k%(n-1)!
    # now for next MSB do k /(n-2)! gives index of next MSB and k updates to k%(n-2)!
    # do this until n !=0
    def optimal(self, n: int, k: int) -> str:
        # create nums array
        nums = [i for i in range(1, n + 1)]
        # create set from nums
        s = set(nums)

        # update k tozero indexbased
        k -= 1
        ans = ""

        fact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = i * fact[i - 1]

        while n > 0:
            nums[:] = list(s)
            n -= 1
            # calculate index by k/(n-1)! k= k%(n-1)!
            index, k = divmod(k, fact[n])
            ans += str(nums[index])
            s.remove(nums[index])
        # remove that from sand append to ans
        return ans

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "60. Permutation Sequence",
    "text": "The set [1, 2, 3, ...,\u00a0n] contains a total of n! unique permutations.\nBy listing and labeling all of the permutations in order, we get the following sequence for n = 3:\n\n\"123\"\n\"132\"\n\"213\"\n\"231\"\n\"312\"\n\"321\"\n\nGiven n and k, return the kth permutation sequence.\n\u00a0\nExample 1:\nInput: n = 3, k = 3\nOutput: \"213\"\nExample 2:\nInput: n = 4, k = 9\nOutput: \"2314\"\nExample 3:\nInput: n = 3, k = 1\nOutput: \"123\"\n\n\u00a0\nConstraints:\n\n1 <= n <= 9\n1 <= k <= n!\n\n",
    "url": "https://leetcode.com/problems/60-permutation-sequence",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def getPermutation(self, n: int, k: int) -> str:\n        return self.optimal(n, k)\n\n    # Time Complexity: O(n!)\n    # Space Complexity: O(n)\n    def bruteforce(self, n: int, k: int) -> str:\n\n        res = []\n        nums = [i for i in range(1, n + 1)]\n        times = reduce(lambda x, y: x * y, nums)\n        res.append(nums[:])\n        for _ in range(1, times + 1):\n            nums[:] = self.nextPermutation(nums)\n            res.append(nums[:])\n        return \"\".join(map(str, res[k - 1]))\n\n    def nextPermutation(self, nums: List[int]) -> List[int]:\n        \"\"\"\n        Do not return anything, modify nums in-place instead.\n        \"\"\"\n        n = len(nums)\n        i = n - 2\n\n        while i >= 0 and nums[i + 1] <= nums[i]:\n            i -= 1\n\n        if i >= 0:\n            j = n - 1\n            while nums[j] <= nums[i]:\n                j -= 1\n\n            nums[j], nums[i] = nums[i], nums[j]\n\n        s = i + 1\n        e = n - 1\n\n        while s < e:\n            nums[s], nums[e] = nums[e], nums[s]\n            s += 1\n            e -= 1\n        return nums\n\n    # Time Complexity: O(n)\n    # Space Complexity: O(n)\n    # there are n! possibilties which means MSB index will be one of n numbers\n    # which is n!/n = n-1!  in ascending order\n    # so k/(n-1)! gives index of MSB k updates to k%(n-1)!\n    # now for next MSB do k /(n-2)! gives index of next MSB and k updates to k%(n-2)!\n    # do this until n !=0\n    def optimal(self, n: int, k: int) -> str:\n        # create nums array\n        nums = [i for i in range(1, n + 1)]\n        # create set from nums\n        s = set(nums)\n\n        # update k tozero indexbased\n        k -= 1\n        ans = \"\"\n\n        fact = [1] * (n + 1)\n\n        for i in range(1, n + 1):\n            fact[i] = i * fact[i - 1]\n\n        while n > 0:\n            nums[:] = list(s)\n            n -= 1\n            # calculate index by k/(n-1)! k= k%(n-1)!\n            index, k = divmod(k, fact[n])\n            ans += str(nums[index])\n            s.remove(nums[index])\n        # remove that from sand append to ans\n        return ans\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/60-permutation-sequence/",
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