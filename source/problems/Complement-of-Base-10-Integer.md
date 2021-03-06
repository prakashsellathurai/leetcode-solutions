# Complement-of-Base-10-Integer


Try it on <a href='https://leetcode.com/problems/1009-complement-of-base-10-integer'>leetcode</a>

## Description
<div class="description">
<div><p>The <strong>complement</strong> of an integer is the integer you get when you flip all the <code>0</code>'s to <code>1</code>'s and all the <code>1</code>'s to <code>0</code>'s in its binary representation.</p>

<ul>
	<li>For example, The integer <code>5</code> is <code>"101"</code> in binary and its <strong>complement</strong> is <code>"010"</code> which is the integer <code>2</code>.</li>
</ul>

<p>Given an integer <code>n</code>, return <em>its complement</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> n = 5
<strong>Output:</strong> 2
<strong>Explanation:</strong> 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> n = 7
<strong>Output:</strong> 0
<strong>Explanation:</strong> 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> n = 10
<strong>Output:</strong> 5
<strong>Explanation:</strong> 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt; 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as 476: <a href="https://leetcode.com/problems/number-complement/" target="_blank">https://leetcode.com/problems/number-complement/</a></p>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    # Question: given n flip al it's bits
    # For Example: for "101" return "010"
    #  
    # Draft:
    # we needed  a bit manipulation technique that flips the 
    # bits 
    #       1.and - not useful here
    #       2.Or - not useful here
    #       3. >> / << - not useful here
    #
    #       4.xor - 1^0 = 1 1^1 = 0 (i.e xor with 1's flips the bits)
    #       5.~ = one' complement 
    #
    # which gives us Xor and complement,
    # 1.xor:
    #       we can use a mask lets say 11111 with bit length same as n
    #        constructing the mask of length log(n) can be done in loop 
    #       by formula mask = (2*mask+1) and then xoring with the n
    #
    # 2.complement:  works by invering each bit of the input
    #        
    #
    # Time Complexity: O(log(n))
    # Space Complexity: O(1)
    def bitwiseComplement(self, n: int) -> int:
        mask = 1
        while mask < n:
            mask = 2*mask+1
        return mask^n
```