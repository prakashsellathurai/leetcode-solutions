# 0080-remove-duplicates-from-sorted-array-ii


Try it on <a href='https://leetcode.com/problems/0080-remove-duplicates-from-sorted-array-ii'>leetcode</a>

## Description
<div class="description">
<p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing order</strong>, remove some duplicates <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a> such that each unique element appears <strong>at most twice</strong>. The <strong>relative order</strong> of the elements should be kept the <strong>same</strong>.</p>

<p>Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the <strong>first part</strong> of the array <code>nums</code>. More formally, if there are <code>k</code> elements after removing the duplicates, then the first <code>k</code> elements of <code>nums</code>&nbsp;should hold the final result. It does not matter what you leave beyond the first&nbsp;<code>k</code>&nbsp;elements.</p>

<p>Return <code>k</code><em> after placing the final result in the first </em><code>k</code><em> slots of </em><code>nums</code>.</p>

<p>Do <strong>not</strong> allocate extra space for another array. You must do this by <strong>modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></strong> with O(1) extra memory.</p>

<p><strong>Custom Judge:</strong></p>

<p>The judge will test your solution with the following code:</p>

<pre>
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i &lt; k; i++) {
    assert nums[i] == expectedNums[i];
}
</pre>

<p>If all assertions pass, then your solution will be <strong>accepted</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1,2,2,3]
<strong>Output:</strong> 5, nums = [1,1,2,2,3,_]
<strong>Explanation:</strong> Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,0,1,1,1,1,2,3,3]
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

## Solution(Python)
```Python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums = [1,1,1,2,2,3]
        # expected [1,1,2,2,3,_]
        # res = 5
        #  i = 0 , 1 , res = 1
        #  i = 1 , 1 ,  res = 2
        #  i = 2, ignore res = 2
        #    i = 3  2 != 1  copy, 1 1 2 2 2 3
        #         res = 3
        #   i =4  res = 4
        #   i = 5 ignore
        #   i = 6  3 != 2 copy 1 1 2 2 3,_
        #   last res localtion
        
        res = 0

        for i in range(len(nums)):
            if res < 2 or nums[i] != nums[res - 2]:
                nums[res] = nums[i]
                res += 1
        return res 
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "80. Remove Duplicates from Sorted Array II",
    "text": "Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.\nSince it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums\u00a0should hold the final result. It does not matter what you leave beyond the first\u00a0k\u00a0elements.\nReturn k after placing the final result in the first k slots of nums.\nDo not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.\nCustom Judge:\nThe judge will test your solution with the following code:\n\nint[] nums = [...]; // Input array\nint[] expectedNums = [...]; // The expected answer with correct length\n\nint k = removeDuplicates(nums); // Calls your implementation\n\nassert k == expectedNums.length;\nfor (int i = 0; i < k; i++) {\n    assert nums[i] == expectedNums[i];\n}\n\nIf all assertions pass, then your solution will be accepted.\n\u00a0\nExample 1:\n\nInput: nums = [1,1,1,2,2,3]\nOutput: 5, nums = [1,1,2,2,3,_]\nExplanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.\nIt does not matter what you leave beyond the returned k (hence they are underscores).\n\nExample 2:\n\nInput: nums = [0,0,1,1,1,1,2,3,3]\nOutput: 7, nums = [0,0,1,1,2,3,3,_,_]\nExplanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.\nIt does not matter what you leave beyond the returned k (hence they are underscores).\n\n\u00a0\nConstraints:\n\n1 <= nums.length <= 3 * 104\n-104 <= nums[i] <= 104\nnums is sorted in non-decreasing order.\n\n",
    "url": "https://leetcode.com/problems/0080-remove-duplicates-from-sorted-array-ii",
    "answerCount": 1,
    "datePublished": "2024-07-13T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def removeDuplicates(self, nums: List[int]) -> int:\n        # nums = [1,1,1,2,2,3]\n        # expected [1,1,2,2,3,_]\n        # res = 5\n        #  i = 0 , 1 , res = 1\n        #  i = 1 , 1 ,  res = 2\n        #  i = 2, ignore res = 2\n        #    i = 3  2 != 1  copy, 1 1 2 2 2 3\n        #         res = 3\n        #   i =4  res = 4\n        #   i = 5 ignore\n        #   i = 6  3 != 2 copy 1 1 2 2 3,_\n        #   last res localtion\n        \n        res = 0\n\n        for i in range(len(nums)):\n            if res < 2 or nums[i] != nums[res - 2]:\n                nums[res] = nums[i]\n                res += 1\n        return res ",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/0080-remove-duplicates-from-sorted-array-ii/",
      "datePublished": "2024-07-13T00:00:00Z",
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