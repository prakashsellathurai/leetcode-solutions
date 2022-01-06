# Two-Sum


Try it on <a href='https://leetcode.com/problems/1-two-sum'>leetcode</a>

## Description
<div class="description">
<div><p>Given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Output:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than&nbsp;<code>O(n<sup>2</sup>)&nbsp;</code>time complexity?</div>
</div>

## Solution(Python)
```Python
class Solution:
    # Input: nums array
    # Output: return the index of two numbers in a Tuple
    #
    # Assumption: only one solution exists
    # Constraints:
    #   1.-10^9 <= nums[i],target <= 10^9
    #   2.2<=nums.length<= 10^4
    #    
    #
    # BruteForce: Do exactly what was given in the problems
    #  run two loops to find the numbers that sums to target and
    #   return their target
    #
    #Time Complexity:O(n^2)
    #Space Complexity:O(1)
    #
    #Optimised Approach: we can skip the inside second loop
    # via caching it in the memory i.e a Hashmap
    #
    # since our condition is num1 + num2 = target
    # which implies
    #  num2 = target - num1
    # so if we cache num1 in the hashmap
    # and then later if we found target - num1 
    # then num1 and num2 are our required answer 
    #
    # Time Complexity:O(n) 
    # on average Time Compleixty is 2n so at worst caseit's O(n)
    # 
    #Space Complexity:O(n)
    #   extra space for hashmap of size n here we trade extra space for speed
    #
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}    # Hashmap to store num
        n = len(nums)
        
        for i in range(n):
            num1 = nums[i]
            num2 = target-num1
            
            if num2 in hashmap: # if num2 in found we got the match
                return [i,hashmap[num2]]
            hashmap[num1] = i
            
        
        
```