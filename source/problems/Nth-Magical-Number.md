# Nth-Magical-Number


Try it on <a href='https://leetcode.com/problems/nth-magical-number'>leetcode</a>

## Description
<div class="description">
<div><p>A positive integer is <em>magical</em> if it is divisible by either <code>a</code> or <code>b</code>.</p>

<p>Given the three integers <code>n</code>, <code>a</code>, and <code>b</code>, return the <code>n<sup>th</sup></code> magical number. Since the answer may be very large, <strong>return it modulo </strong><code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> n = 1, a = 2, b = 3
<strong>Output:</strong> 2
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> n = 4, a = 2, b = 3
<strong>Output:</strong> 6
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> n = 5, a = 2, b = 4
<strong>Output:</strong> 10
</pre><p><strong>Example 4:</strong></p>
<pre><strong>Input:</strong> n = 3, a = 6, b = 4
<strong>Output:</strong> 8
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
	<li><code>2 &lt;= a, b &lt;= 4 * 10<sup>4</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        from math import gcd
        MOD = 10**9 + 7

        L = A // gcd(A, B) * B
        M = L // A + L // B - 1
        q, r = divmod(N, M)

        if r == 0:
            return q * L % MOD

        heads = [A, B]
        for _ in range(int(r) - 1):
            if heads[0] <= heads[1]:
                heads[0] += A
            else:
                heads[1] += B

        return (q * L + min(heads)) % MOD
```