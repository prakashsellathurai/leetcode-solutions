# Car-Pooling


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
        stops = [0]*1001
        max_stop = 0
        
        for P,pickup,drop in trips:
            stops[pickup]+=P
            stops[drop]-=P
            if drop > max_stop:
                max_stop = drop
        cur_P = 0      
        for i in range(max_stop+1):
            cur_P += stops[i]
            if cur_P > capacity:
                return False
        return True
            
```