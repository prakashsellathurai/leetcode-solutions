# 1094-car-pooling


Try it on <a href='https://leetcode.com/problems/1094-car-pooling'>leetcode</a>

## Description
<div class="description">
<div><p>There is a car with <code>capacity</code> empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).</p>

<p>You are given the integer <code>capacity</code> and an array <code>trips</code> where <code>trip[i] = [numPassengers<sub>i</sub>, from<sub>i</sub>, to<sub>i</sub>]</code> indicates that the <code>i<sup>th</sup></code> trip has <code>numPassengers<sub>i</sub></code> passengers and the locations to pick them up and drop them off are <code>from<sub>i</sub></code> and <code>to<sub>i</sub></code> respectively. The locations are given as the number of kilometers due east from the car's initial location.</p>

<p>Return <code>true</code><em> if it is possible to pick up and drop off all passengers for all the given trips, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> trips = [[2,1,5],[3,3,7]], capacity = 4
<strong>Output:</strong> false
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> trips = [[2,1,5],[3,3,7]], capacity = 5
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= trips.length &lt;= 1000</code></li>
	<li><code>trips[i].length == 3</code></li>
	<li><code>1 &lt;= numPassengers<sub>i</sub> &lt;= 100</code></li>
	<li><code>0 &lt;= from<sub>i</sub> &lt; to<sub>i</sub> &lt;= 1000</code></li>
	<li><code>1 &lt;= capacity &lt;= 10<sup>5</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
import heapq


class Solution:
    # @Problem-statement:
    #   given integer capacity and an array of trips in the form of
    #   [numOfPassengers,from,to] at index i
    #   Vechicle only drives east
    #   Return True if it is possible to pick and drop for all trips or False
    ###################################################################
    # @Input: capacity: integer,Array of Trips i;e [numOfPassengers,from,to]
    # @Output: Boolean
    ###################################################################
    # @Simple-Example:
    #   1.trips = [[2,1,5],[3,3,7]], capacity = 4
    #       1------5     curP=2
    #           3-----7  curp = 2+3 = 5
    #                   curP > capacity So,False
    #
    #   2.trips = [[2,1,5],[3,3,7]], capacity = 5
    #       1------5        curP = 2
    #           3------7    curP = 3+2 = 5
    #                       curP == capacity ,So True
    #
    #   3.trips = [[2,1,5],[3,5,7]], capacity = 5
    #       1------5          curP = 2
    #              5---------7 curP = 3
    #                         curP < capacity ,So True
    ###################################################################
    # @Constraints:
    #   1 <= trips.length <= 1000
    #   trips[i].length == 3
    #   1 <= numPassengersi <= 100
    #   0 <= fromi < toi <= 1000
    #   1 <= capacity <= 105
    ###################################################################
    # @Assumptions:
    #   The vehicle only drives east
    ###################################################################
    # @Solution:
    #   1.Sorting/PriorityQueue Solution:
    #      @Pseudocode:
    #       sort by pickup location
    #       maintain two variables curP,curTrip
    #
    #       curTip destination can be  more than onesimultaneously
    #       So PQ data structure is used here
    #       iterate through pick up location
    #           while curTip destination <= tips[start]
    #                     curp -=curTip.topP
    #           curTip.heappush(trip(by destination))
    #           curp+=tripP
    #           if curp > cap: return False
    #       return True
    #      @Analysis:
    #       Time Complexity:O(nlogn)
    #       Space Complexity:O(n)
    #
    #      @Code:
    #       def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    #         trips.sort(key=lambda trip:trip[1])

    #         curP = 0
    #         cur_trips = []
    #         heapq.heapify(cur_trips)
    #         for trip in trips:
    #             while len(cur_trips) > 0 and cur_trips[0][0] <= trip[1]:
    #                 _,P = heapq.heappop(cur_trips)
    #                 curP -= P
    #             heapq.heappush(cur_trips,(trip[2],trip[0]))
    #             curP += trip[0]
    #             if curP > capacity:
    #                 return False
    #         return True
    #
    ###################################################################
    # 2. Simulation:
    #       Lets visualize this as linear timeframe where people aboard at
    # point 'from' and depart at point 'to' If we stored them in a array lets
    # stops with index i denoting number of people aboarded or departed
    # numerically +P or -P.Length of the stops is the maximum among all
    #  the destination.Since our contraint ensures us stops cannot be more than
    #   1001 we can always create stops array of size 1001 that gives us contant
    #   space in worst case
    #
    #
    #       @PesudoCode:
    #           create stops array of size 1001
    #           for each of the trip
    #               add +P to stops at from
    #               add -P to stops at to
    #           instialize cur_Passengers
    #           iterate through stops
    #               cur_Passengers += stops[i]
    #               if cur_Passengers>capapcity:
    #                   return False
    #
    #           return True
    #
    #       @Analysis:
    #       Time Complexity: O(n)
    #       Space Complexity: O(1001) = O(1)
    #

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = [0] * 1001
        max_stop = 0

        for P, pickup, drop in trips:
            stops[pickup] += P
            stops[drop] -= P
            if drop > max_stop:
                max_stop = drop
        cur_P = 0
        for i in range(max_stop + 1):
            cur_P += stops[i]
            if cur_P > capacity:
                return False
        return True

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1094. Car Pooling",
    "text": "There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).\nYou are given the integer capacity and an array trips where trip[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.\nReturn true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.\n\u00a0\nExample 1:\nInput: trips = [[2,1,5],[3,3,7]], capacity = 4\nOutput: false\n\nExample 2:\nInput: trips = [[2,1,5],[3,3,7]], capacity = 5\nOutput: true\n\n\u00a0\nConstraints:\n\n1 <= trips.length <= 1000\ntrips[i].length == 3\n1 <= numPassengersi <= 100\n0 <= fromi < toi <= 1000\n1 <= capacity <= 105\n\n",
    "url": "https://leetcode.com/problems/1094-car-pooling",
    "answerCount": 1,
    "datePublished": "2025-10-22T00:00:00Z",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "import heapq\n\n\nclass Solution:\n    # @Problem-statement:\n    #   given integer capacity and an array of trips in the form of\n    #   [numOfPassengers,from,to] at index i\n    #   Vechicle only drives east\n    #   Return True if it is possible to pick and drop for all trips or False\n    ###################################################################\n    # @Input: capacity: integer,Array of Trips i;e [numOfPassengers,from,to]\n    # @Output: Boolean\n    ###################################################################\n    # @Simple-Example:\n    #   1.trips = [[2,1,5],[3,3,7]], capacity = 4\n    #       1------5     curP=2\n    #           3-----7  curp = 2+3 = 5\n    #                   curP > capacity So,False\n    #\n    #   2.trips = [[2,1,5],[3,3,7]], capacity = 5\n    #       1------5        curP = 2\n    #           3------7    curP = 3+2 = 5\n    #                       curP == capacity ,So True\n    #\n    #   3.trips = [[2,1,5],[3,5,7]], capacity = 5\n    #       1------5          curP = 2\n    #              5---------7 curP = 3\n    #                         curP < capacity ,So True\n    ###################################################################\n    # @Constraints:\n    #   1 <= trips.length <= 1000\n    #   trips[i].length == 3\n    #   1 <= numPassengersi <= 100\n    #   0 <= fromi < toi <= 1000\n    #   1 <= capacity <= 105\n    ###################################################################\n    # @Assumptions:\n    #   The vehicle only drives east\n    ###################################################################\n    # @Solution:\n    #   1.Sorting/PriorityQueue Solution:\n    #      @Pseudocode:\n    #       sort by pickup location\n    #       maintain two variables curP,curTrip\n    #\n    #       curTip destination can be  more than onesimultaneously\n    #       So PQ data structure is used here\n    #       iterate through pick up location\n    #           while curTip destination <= tips[start]\n    #                     curp -=curTip.topP\n    #           curTip.heappush(trip(by destination))\n    #           curp+=tripP\n    #           if curp > cap: return False\n    #       return True\n    #      @Analysis:\n    #       Time Complexity:O(nlogn)\n    #       Space Complexity:O(n)\n    #\n    #      @Code:\n    #       def carPooling(self, trips: List[List[int]], capacity: int) -> bool:\n    #         trips.sort(key=lambda trip:trip[1])\n\n    #         curP = 0\n    #         cur_trips = []\n    #         heapq.heapify(cur_trips)\n    #         for trip in trips:\n    #             while len(cur_trips) > 0 and cur_trips[0][0] <= trip[1]:\n    #                 _,P = heapq.heappop(cur_trips)\n    #                 curP -= P\n    #             heapq.heappush(cur_trips,(trip[2],trip[0]))\n    #             curP += trip[0]\n    #             if curP > capacity:\n    #                 return False\n    #         return True\n    #\n    ###################################################################\n    # 2. Simulation:\n    #       Lets visualize this as linear timeframe where people aboard at\n    # point 'from' and depart at point 'to' If we stored them in a array lets\n    # stops with index i denoting number of people aboarded or departed\n    # numerically +P or -P.Length of the stops is the maximum among all\n    #  the destination.Since our contraint ensures us stops cannot be more than\n    #   1001 we can always create stops array of size 1001 that gives us contant\n    #   space in worst case\n    #\n    #\n    #       @PesudoCode:\n    #           create stops array of size 1001\n    #           for each of the trip\n    #               add +P to stops at from\n    #               add -P to stops at to\n    #           instialize cur_Passengers\n    #           iterate through stops\n    #               cur_Passengers += stops[i]\n    #               if cur_Passengers>capapcity:\n    #                   return False\n    #\n    #           return True\n    #\n    #       @Analysis:\n    #       Time Complexity: O(n)\n    #       Space Complexity: O(1001) = O(1)\n    #\n\n    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:\n        stops = [0] * 1001\n        max_stop = 0\n\n        for P, pickup, drop in trips:\n            stops[pickup] += P\n            stops[drop] -= P\n            if drop > max_stop:\n                max_stop = drop\n        cur_P = 0\n        for i in range(max_stop + 1):\n            cur_P += stops[i]\n            if cur_P > capacity:\n                return False\n        return True\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1094-car-pooling/",
      "datePublished": "2025-10-22T00:00:00Z",
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