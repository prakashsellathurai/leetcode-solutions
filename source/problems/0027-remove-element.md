# 0027-remove-element


Try it on <a href='https://leetcode.com/problems/0027-remove-element'>leetcode</a>

## Description
<div class="description">
<p>Given an integer array <code>nums</code> and an integer <code>val</code>, remove all occurrences of <code>val</code> in <code>nums</code> <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a>. The order of the elements may be changed. Then return <em>the number of elements in </em><code>nums</code><em> which are not equal to </em><code>val</code>.</p>

<p>Consider the number of elements in <code>nums</code> which are not equal to <code>val</code> be <code>k</code>, to get accepted, you need to do the following things:</p>

<ul>
	<li>Change the array <code>nums</code> such that the first <code>k</code> elements of <code>nums</code> contain the elements which are not equal to <code>val</code>. The remaining elements of <code>nums</code> are not important as well as the size of <code>nums</code>.</li>
	<li>Return <code>k</code>.</li>
</ul>

<p><strong>Custom Judge:</strong></p>

<p>The judge will test your solution with the following code:</p>

<pre>
int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i &lt; actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
</pre>

<p>If all assertions pass, then your solution will be <strong>accepted</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,2,3], val = 3
<strong>Output:</strong> 2, nums = [2,2,_,_]
<strong>Explanation:</strong> Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,2,2,3,0,4,2], val = 2
<strong>Output:</strong> 5, nums = [0,1,4,0,3,_,_,_]
<strong>Explanation:</strong> Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 50</code></li>
	<li><code>0 &lt;= val &lt;= 100</code></li>
</ul>

</div>

## Solution(Python)
```Python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 3 2 2 3
        # left  0
        # right  3
        #   if right = 3
        #     move right to inside
        #   elif left = val
        #     swap left and right 
        #     increase left and move right
        #   else:
        #     left += 1
        # 3 2 2 3
        #  3 3 left = 0 right = 3
        #   3 2   left  = 0 right = 2
        #      swap 2 3    2 2 3 3
        #   2 3     left = 1 right = 2
        #    2 2      left = 1 right = 1

        # 0 1 2 2 3 0 4 2 val = 2
        # 0 2 left = 0 right = 7
        #     right = 6
        # 0 4 
        #    left = 1 
        # 1 4 
        #    left  = 2
        # 2 4 
        #    0 1 4 2 3 0 2 2  left = 3 right = 5
        # 2 0 
        #    0 1 4 0 3 2 2 2 left = 4 right = 4
        # stopping condition left < right

        left = 0 
        right = len(nums) - 1

        while left <= right:
            if nums[right] == val:
                right -= 1
            elif nums[left] == val:
                nums[left],nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            else:
                left += 1
        return left 
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "27. Remove Element",
    "text": "Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.\nConsider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:\n\nChange the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.\nReturn k.\n\nCustom Judge:\nThe judge will test your solution with the following code:\n\nint[] nums = [...]; // Input array\nint val = ...; // Value to remove\nint[] expectedNums = [...]; // The expected answer with correct length.\n                            // It is sorted with no values equaling val.\n\nint k = removeElement(nums, val); // Calls your implementation\n\nassert k == expectedNums.length;\nsort(nums, 0, k); // Sort the first k elements of nums\nfor (int i = 0; i < actualLength; i++) {\n    assert nums[i] == expectedNums[i];\n}\n\nIf all assertions pass, then your solution will be accepted.\n\u00a0\nExample 1:\n\nInput: nums = [3,2,2,3], val = 3\nOutput: 2, nums = [2,2,_,_]\nExplanation: Your function should return k = 2, with the first two elements of nums being 2.\nIt does not matter what you leave beyond the returned k (hence they are underscores).\n\nExample 2:\n\nInput: nums = [0,1,2,2,3,0,4,2], val = 2\nOutput: 5, nums = [0,1,4,0,3,_,_,_]\nExplanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.\nNote that the five elements can be returned in any order.\nIt does not matter what you leave beyond the returned k (hence they are underscores).\n\n\u00a0\nConstraints:\n\n0 <= nums.length <= 100\n0 <= nums[i] <= 50\n0 <= val <= 100\n\n",
    "url": "https://leetcode.com/problems/0027-remove-element",
    "answerCount": 1,
    "datePublished": "2024-11-18T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def removeElement(self, nums: List[int], val: int) -> int:\n        # 3 2 2 3\n        # left  0\n        # right  3\n        #   if right = 3\n        #     move right to inside\n        #   elif left = val\n        #     swap left and right \n        #     increase left and move right\n        #   else:\n        #     left += 1\n        # 3 2 2 3\n        #  3 3 left = 0 right = 3\n        #   3 2   left  = 0 right = 2\n        #      swap 2 3    2 2 3 3\n        #   2 3     left = 1 right = 2\n        #    2 2      left = 1 right = 1\n\n        # 0 1 2 2 3 0 4 2 val = 2\n        # 0 2 left = 0 right = 7\n        #     right = 6\n        # 0 4 \n        #    left = 1 \n        # 1 4 \n        #    left  = 2\n        # 2 4 \n        #    0 1 4 2 3 0 2 2  left = 3 right = 5\n        # 2 0 \n        #    0 1 4 0 3 2 2 2 left = 4 right = 4\n        # stopping condition left < right\n\n        left = 0 \n        right = len(nums) - 1\n\n        while left <= right:\n            if nums[right] == val:\n                right -= 1\n            elif nums[left] == val:\n                nums[left],nums[right] = nums[right], nums[left]\n                left += 1\n                right -= 1\n            else:\n                left += 1\n        return left ",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/0027-remove-element/",
      "datePublished": "2024-11-18T00:00:00Z",
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