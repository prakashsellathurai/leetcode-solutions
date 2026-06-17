# pairs-of-songs-with-total-durations-divisible-by-60


Try it on <a href='https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60'>leetcode</a>

## Description
<div class="description">
<div><p>You are given a list of songs where the i<sup>th</sup> song has a duration of <code>time[i]</code> seconds.</p>

<p>Return <em>the number of pairs of songs for which their total duration in seconds is divisible by</em> <code>60</code>. Formally, we want the number of indices <code>i</code>, <code>j</code> such that <code>i &lt; j</code> with <code>(time[i] + time[j]) % 60 == 0</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> time = [30,20,150,100,40]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> time = [60,60,60]
<strong>Output:</strong> 3
<strong>Explanation:</strong> All three pairs have a total duration of 120, which is divisible by 60.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= time.length &lt;= 6 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= time[i] &lt;= 500</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans, cnt = 0, collections.Counter()
        for t in time:
            theOther = -t % 60
            ans += cnt[theOther]
            cnt[t % 60] += 1
        return ans

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1010. Pairs of Songs With Total Durations Divisible by 60",
    "text": "You are given a list of songs where the ith song has a duration of time[i] seconds.\nReturn the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.\n\u00a0\nExample 1:\nInput: time = [30,20,150,100,40]\nOutput: 3\nExplanation: Three pairs have a total duration divisible by 60:\n(time[0] = 30, time[2] = 150): total duration 180\n(time[1] = 20, time[3] = 100): total duration 120\n(time[1] = 20, time[4] = 40): total duration 60\n\nExample 2:\nInput: time = [60,60,60]\nOutput: 3\nExplanation: All three pairs have a total duration of 120, which is divisible by 60.\n\n\u00a0\nConstraints:\n\n1 <= time.length <= 6 * 104\n1 <= time[i] <= 500\n\n",
    "url": "https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def numPairsDivisibleBy60(self, time: List[int]) -> int:\n        ans, cnt = 0, collections.Counter()\n        for t in time:\n            theOther = -t % 60\n            ans += cnt[theOther]\n            cnt[t % 60] += 1\n        return ans\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/pairs-of-songs-with-total-durations-divisible-by-60/",
      "datePublished": "2022-07-03",
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