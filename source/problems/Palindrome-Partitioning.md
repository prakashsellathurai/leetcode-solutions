# Palindrome-Partitioning


Try it on <a href='https://leetcode.com/problems/131-palindrome-partitioning'>leetcode</a>

## Description
<div class="description">
<div><p>Given a string <code>s</code>, partition <code>s</code> such that every substring of the partition is a <strong>palindrome</strong>. Return all possible palindrome partitioning of <code>s</code>.</p>

<p>A <strong>palindrome</strong> string is a string that reads the same backward as forward.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aab"
<strong>Output:</strong> [["a","a","b"],["aa","b"]]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "a"
<strong>Output:</strong> [["a"]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 16</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    #  Problem Statement: Given a str s return all possible palindromic
    #  partitions
    #
    #   Input: a string
    #   Output: array of all possible palindromics substring partitions
    #
    #   Example:
    #       1.for s="aaab" return [["a","a","b"],["aa","b"]]
    #   
    #   Constraints: 1<= s.length <= 16
    #
    #   Solution:
    #       1.Bruteforce : use backtracking choose a potential candidate (i.e     
    #       palindromic substring )from the generated substring from given   
    #       constraints
    #       
    #       Pseudo code:
    #           fn bactrack (candidate,res,start)
    #               if start reaches end of string
    #                   res.push(cur)
    #               
    #               for end=start;end<len(s);end++
    #                   if isPalindrome(s,start,end):
    #                       candidate.push_back(s[start:end+1])
    #                       backtrack(candidate,res,end+1)
    #                       candidate.pop()
    #   Time Complexity: O(N.2^N) 
    #   (since our constraint is 1<=n<=16 This is acceptable)
    #   SpaceComplexity: O(n)
    def partition(self, s: str) -> List[List[str]]:
        self.res = []

        
        @cache
        def isPalindrome(low,high):
            while low<high:
                if s[low] != s[high]:
                    return False
                low+=1
                high-=1
            return True
        
        def backtrack(start, cur):
            # candidate selection
            if start>=len(s):
                self.res.append(cur[:])
            # Recursive case
            for end in range(start,len(s)):
                if isPalindrome(start,end):
                    cur.append(s[start:end+1])
                    backtrack(end+1,cur)
                    cur.pop()
        backtrack(0,[])
        return self.res
        
        
```