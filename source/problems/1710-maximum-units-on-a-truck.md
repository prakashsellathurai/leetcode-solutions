# 1710-maximum-units-on-a-truck


Try it on <a href='https://leetcode.com/problems/1710-maximum-units-on-a-truck'>leetcode</a>

## Description
<div class="description">
<div><p>You are assigned to put some amount of boxes onto <strong>one truck</strong>. You are given a 2D array <code>boxTypes</code>, where <code>boxTypes[i] = [numberOfBoxes<sub>i</sub>, numberOfUnitsPerBox<sub>i</sub>]</code>:</p>

<ul>
	<li><code>numberOfBoxes<sub>i</sub></code> is the number of boxes of type <code>i</code>.</li>
	<li><code>numberOfUnitsPerBox<sub>i</sub></code><sub> </sub>is the number of units in each box of the type <code>i</code>.</li>
</ul>

<p>You are also given an integer <code>truckSize</code>, which is the <strong>maximum</strong> number of <strong>boxes</strong> that can be put on the truck. You can choose any boxes to put on the truck as long as the number&nbsp;of boxes does not exceed <code>truckSize</code>.</p>

<p>Return <em>the <strong>maximum</strong> total number of <strong>units</strong> that can be put on the truck.</em></p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
<strong>Output:</strong> 8
<strong>Explanation:</strong> There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
<strong>Output:</strong> 91
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= boxTypes.length &lt;= 1000</code></li>
	<li><code>1 &lt;= numberOfBoxes<sub>i</sub>, numberOfUnitsPerBox<sub>i</sub> &lt;= 1000</code></li>
	<li><code>1 &lt;= truckSize &lt;= 10<sup>6</sup></code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        boxes = 0
        for box, units in boxTypes:
            if truckSize > box:
                truckSize -= box
                boxes += box * units
            else:
                boxes += truckSize * units
                return boxes
        return boxes
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1710. Maximum Units on a Truck",
    "text": "You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:\n\nnumberOfBoxesi is the number of boxes of type i.\nnumberOfUnitsPerBoxi is the number of units in each box of the type i.\n\nYou are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number\u00a0of boxes does not exceed truckSize.\nReturn the maximum total number of units that can be put on the truck.\n\u00a0\nExample 1:\nInput: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4\nOutput: 8\nExplanation: There are:\n- 1 box of the first type that contains 3 units.\n- 2 boxes of the second type that contain 2 units each.\n- 3 boxes of the third type that contain 1 unit each.\nYou can take all the boxes of the first and second types, and one box of the third type.\nThe total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.\n\nExample 2:\nInput: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10\nOutput: 91\n\n\u00a0\nConstraints:\n\n1 <= boxTypes.length <= 1000\n1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000\n1 <= truckSize <= 106\n\n",
    "url": "https://leetcode.com/problems/1710-maximum-units-on-a-truck",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:\n        boxTypes.sort(key=lambda x: -x[1])\n        boxes = 0\n        for box, units in boxTypes:\n            if truckSize > box:\n                truckSize -= box\n                boxes += box * units\n            else:\n                boxes += truckSize * units\n                return boxes\n        return boxes",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1710-maximum-units-on-a-truck/",
      "datePublished": "2026-05-25",
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