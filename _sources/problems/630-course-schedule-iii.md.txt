# 630-course-schedule-iii


Try it on <a href='https://leetcode.com/problems/630-course-schedule-iii'>leetcode</a>

## Description
<div class="description">
<div><p>There are <code>n</code> different online courses numbered from <code>1</code> to <code>n</code>. You are given an array <code>courses</code> where <code>courses[i] = [duration<sub>i</sub>, lastDay<sub>i</sub>]</code> indicate that the <code>i<sup>th</sup></code> course should be taken <b>continuously</b> for <code>duration<sub>i</sub></code> days and must be finished before or on <code>lastDay<sub>i</sub></code>.</p>

<p>You will start on the <code>1<sup>st</sup></code> day and you cannot take two or more courses simultaneously.</p>

<p>Return <em>the maximum number of courses that you can take</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
<strong>Output:</strong> 3
Explanation: 
There are totally 4 courses, but you can take 3 courses at most:
First, take the 1<sup>st</sup> course, it costs 100 days so you will finish it on the 100<sup>th</sup> day, and ready to take the next course on the 101<sup>st</sup> day.
Second, take the 3<sup>rd</sup> course, it costs 1000 days so you will finish it on the 1100<sup>th</sup> day, and ready to take the next course on the 1101<sup>st</sup> day. 
Third, take the 2<sup>nd</sup> course, it costs 200 days so you will finish it on the 1300<sup>th</sup> day. 
The 4<sup>th</sup> course cannot be taken now, since you will finish it on the 3300<sup>th</sup> day, which exceeds the closed date.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> courses = [[1,2]]
<strong>Output:</strong> 1
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> courses = [[3,2],[4,3]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= courses.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= duration<sub>i</sub>, lastDay<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        return self.pq(courses)

    # Time Complexity: O(n*d)
    # Space Complexity: O(n*d)
    def iterative(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda course: course[1])

        @cache
        def schedule(i, time):
            if i == len(courses):
                return 0
            taken = 0
            if time + courses[i][0] <= courses[i][1]:
                taken = 1 + schedule(i + 1, time + courses[i][0])
            not_taken = schedule(i + 1, time)
            return max(taken, not_taken)

        return schedule(0, 0)

    # Time Complexity: O(n*k)
    # Space Complexity: O(1)
    def iterative(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda course: course[1])
        time = 0
        cnt = 0
        schedule = []

        for course in courses:
            if time + course[0] <= course[1]:
                time += course[0]
                schedule.append(course[0])
            else:
                max_i = 0
                for i in range(1, len(schedule)):
                    if schedule[i] > schedule[max_i]:
                        max_i = i

                if schedule[max_i] > course[0]:
                    time += course[0] - schedule[max_i]
                    schedule[max_i] = course[0]

        return len(schedule)

    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
    def pq(self, courses: List[List[int]]) -> int:
        heap, time = [], 0
        for t, end in sorted(courses, key=lambda x: x[1]):
            time += t
            heapq.heappush(heap, -t)
            if time > end:
                nt = heapq.heappop(heap)
                time += nt
        return len(heap)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "630. Course Schedule III",
    "text": "There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.\nYou will start on the 1st day and you cannot take two or more courses simultaneously.\nReturn the maximum number of courses that you can take.\n\u00a0\nExample 1:\nInput: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]\nOutput: 3\nExplanation: \nThere are totally 4 courses, but you can take 3 courses at most:\nFirst, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.\nSecond, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. \nThird, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. \nThe 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.\n\nExample 2:\nInput: courses = [[1,2]]\nOutput: 1\n\nExample 3:\nInput: courses = [[3,2],[4,3]]\nOutput: 0\n\n\u00a0\nConstraints:\n\n1 <= courses.length <= 104\n1 <= durationi, lastDayi <= 104\n\n",
    "url": "https://leetcode.com/problems/630-course-schedule-iii",
    "answerCount": 1,
    "datePublished": "2022-06-23T14:18:05+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def scheduleCourse(self, courses: List[List[int]]) -> int:\n        return self.pq(courses)\n\n    # Time Complexity: O(n*d)\n    # Space Complexity: O(n*d)\n    def iterative(self, courses: List[List[int]]) -> int:\n        courses.sort(key=lambda course: course[1])\n\n        @cache\n        def schedule(i, time):\n            if i == len(courses):\n                return 0\n            taken = 0\n            if time + courses[i][0] <= courses[i][1]:\n                taken = 1 + schedule(i + 1, time + courses[i][0])\n            not_taken = schedule(i + 1, time)\n            return max(taken, not_taken)\n\n        return schedule(0, 0)\n\n    # Time Complexity: O(n*k)\n    # Space Complexity: O(1)\n    def iterative(self, courses: List[List[int]]) -> int:\n        courses.sort(key=lambda course: course[1])\n        time = 0\n        cnt = 0\n        schedule = []\n\n        for course in courses:\n            if time + course[0] <= course[1]:\n                time += course[0]\n                schedule.append(course[0])\n            else:\n                max_i = 0\n                for i in range(1, len(schedule)):\n                    if schedule[i] > schedule[max_i]:\n                        max_i = i\n\n                if schedule[max_i] > course[0]:\n                    time += course[0] - schedule[max_i]\n                    schedule[max_i] = course[0]\n\n        return len(schedule)\n\n    # Time Complexity: O(nlogn)\n    # Space Complexity: O(n)\n    def pq(self, courses: List[List[int]]) -> int:\n        heap, time = [], 0\n        for t, end in sorted(courses, key=lambda x: x[1]):\n            time += t\n            heapq.heappush(heap, -t)\n            if time > end:\n                nt = heapq.heappop(heap)\n                time += nt\n        return len(heap)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/630-course-schedule-iii/",
      "datePublished": "2022-06-23T14:18:05+05:30",
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