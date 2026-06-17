# 80-remove-duplicates-from-sorted-array-ii


Try it on <a href='https://leetcode.com/problems/80-remove-duplicates-from-sorted-array-ii'>leetcode</a>

## Description
<div class="description">
<div><p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing order</strong>, remove some duplicates <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a> such that each unique element appears <strong>at most twice</strong>. The <strong>relative order</strong> of the elements should be kept the <strong>same</strong>.</p>

<p>Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the <strong>first part</strong> of the array <code>nums</code>. More formally, if there are <code>k</code> elements after removing the duplicates, then the first <code>k</code> elements of <code>nums</code>&nbsp;should hold the final result. It does not matter what you leave beyond the first&nbsp;<code>k</code>&nbsp;elements.</p>

<p>Return <code>k</code><em> after placing the final result in the first </em><code>k</code><em> slots of </em><code>nums</code>.</p>

<p>Do <strong>not</strong> allocate extra space for another array. You must do this by <strong>modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></strong> with O(1) extra memory.</p>

<p><strong>Custom Judge:</strong></p>

<p>The judge will test your solution with the following code:</p>

<pre>int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i &lt; k; i++) {
    assert nums[i] == expectedNums[i];
}
</pre>

<p>If all assertions pass, then your solution will be <strong>accepted</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,1,1,2,2,3]
<strong>Output:</strong> 5, nums = [1,1,2,2,3,_]
<strong>Explanation:</strong> Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [0,0,1,1,1,1,2,3,3]
<strong>Output:</strong> 7, nums = [0,0,1,1,2,3,3,_,_]
<strong>Explanation:</strong> Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        if len(nums) <= 2:
            return n
        i = 2

        for j in range(2, n):
            if nums[i - 2] != nums[j]:
                nums[i] = nums[j]
                i += 1

        return i

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "80. Remove Duplicates from Sorted Array II",
    "text": "Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.\nSince it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums\u00a0should hold the final result. It does not matter what you leave beyond the first\u00a0k\u00a0elements.\nReturn k after placing the final result in the first k slots of nums.\nDo not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.\nCustom Judge:\nThe judge will test your solution with the following code:\nint[] nums = [...]; // Input array\nint[] expectedNums = [...]; // The expected answer with correct length\n\nint k = removeDuplicates(nums); // Calls your implementation\n\nassert k == expectedNums.length;\nfor (int i = 0; i < k; i++) {\n    assert nums[i] == expectedNums[i];\n}\n\nIf all assertions pass, then your solution will be accepted.\n\u00a0\nExample 1:\nInput: nums = [1,1,1,2,2,3]\nOutput: 5, nums = [1,1,2,2,3,_]\nExplanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.\nIt does not matter what you leave beyond the returned k (hence they are underscores).\n\nExample 2:\nInput: nums = [0,0,1,1,1,1,2,3,3]\nOutput: 7, nums = [0,0,1,1,2,3,3,_,_]\nExplanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.\nIt does not matter what you leave beyond the returned k (hence they are underscores).\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 3 * 104\n-104 <= nums[i] <= 104\nnums is sorted in non-decreasing order.\n\n",
    "url": "https://leetcode.com/problems/80-remove-duplicates-from-sorted-array-ii",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def removeDuplicates(self, nums):\n        n = len(nums)\n        if len(nums) <= 2:\n            return n\n        i = 2\n\n        for j in range(2, n):\n            if nums[i - 2] != nums[j]:\n                nums[i] = nums[j]\n                i += 1\n\n        return i\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/80-remove-duplicates-from-sorted-array-ii/",
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