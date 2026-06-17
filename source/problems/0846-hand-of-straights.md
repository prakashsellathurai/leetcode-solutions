# 0846-hand-of-straights


Try it on <a href='https://leetcode.com/problems/0846-hand-of-straights'>leetcode</a>

## Description
<div class="description">
<p>Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size <code>groupSize</code>, and consists of <code>groupSize</code> consecutive cards.</p>

<p>Given an integer array <code>hand</code> where <code>hand[i]</code> is the value written on the <code>i<sup>th</sup></code> card and an integer <code>groupSize</code>, return <code>true</code> if she can rearrange the cards, or <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
<strong>Output:</strong> true
<strong>Explanation:</strong> Alice&#39;s hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> hand = [1,2,3,4,5], groupSize = 4
<strong>Output:</strong> false
<strong>Explanation:</strong> Alice&#39;s hand can not be rearranged into groups of 4.

</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= hand.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= hand[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= groupSize &lt;= hand.length</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as 1296: <a href="https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/" target="_blank">https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/</a></p>

</div>

## Solution(Python)
```Python
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        return self.most_optimal(hand, groupSize)
    
    # Time Complexity: O(n logn + NK)
    # Space Complexity: O(n)
    def map(self, hands: List[int], groupSize: int) -> bool:
        # Attempt
        # # 1,2,3,,6,2,3,4,7,8
        # # groupSize = 3
        # # if n% g != 0 False
        # #   b = n//g
        # #   b bcukets
        # #  hashmap = [1,2,2,1,1]
        # #  smallest_cur = min(hashmap)
        # #  [[],[],[]]
        # # smallest_cur = min(hashmap)
        # # 
        # #    [] 1 cur+=1
        # #       2 , 3
        # #      if hashmap[smallest_cur] == 0
        # #         reryurn Fa;se
        # #      hashmap[smallest_cur] -=1
        # # return True
        # #       
        n = len(hands)
        if n% groupSize!= 0:
            return False
        # no_of_buckets = n // groupSize
        # MAX = max(hand)
        # MIN = min(hand)
        # counts = [0] * ( MAX -MIN  +1)
        cardCount  = Counter(hands)
        min_heap = list(cardCount.keys())
        heapq.heapify(min_heap)
        while min_heap:
            current_card = min_heap[0]  
            for i in range(groupSize):
                if cardCount[current_card + i] == 0:
                    return False
                cardCount[current_card + i] -= 1
                if cardCount[current_card + i] <= 0:
                    heapq.heappop(min_heap)
        return True

    def optimal(self, hands: List[int], groupSize: int) -> bool: # hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
        cardCount  = Counter(hands) # {1:1, 2:2, 3:2, 6:1, 4:1,7:1,8:1}
        # Sorted list of card values
        sortedCards = sorted(cardCount.keys()) # 1 2 3 4 6 7 8
        # Queue to keep track of the number of new groups
        # starting with each card value
        groupStartQueue = deque() #  []
        lastCard = -1
        currentOpenGroups = 0
        for currentCard in sortedCards: # 1 2 3 4 6 7 8   -> 6
                        # Check if there are any discrepancies in the sequence
            # or more groups are required than available cards
            if (
                currentOpenGroups > 0 and currentCard > lastCard + 1 # 
            ) or currentOpenGroups > cardCount[currentCard]: # 
                return False

            groupStartQueue.append(cardCount[currentCard] - currentOpenGroups) #  0, 0, 1 
            lastCard = currentCard # 6
            currentOpenGroups = cardCount[currentCard] # 1
            # Maintain the queue size to be equal to groupSize
            if len(groupStartQueue) == groupSize: # 
                currentOpenGroups -= groupStartQueue.popleft() # 0

        return currentOpenGroups == 0


    def most_optimal(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        # Counter to store the count of each card value
        card_count = Counter(hand)

        for card in hand:
            start_card = card
            # Find the start of the potential straight sequence
            while card_count[start_card - 1]:
                start_card -= 1

            # Process the sequence starting from start_card
            while start_card <= card:
                while card_count[start_card]:
                    # Check if we can form a consecutive sequence
                    # of groupSize cards
                    for next_card in range(start_card, start_card + groupSize):
                        if not card_count[next_card]:
                            return False
                        card_count[next_card] -= 1
                start_card += 1

        return True

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "846. Hand of Straights",
    "text": "Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.\nGiven an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.\n\u00a0\nExample 1:\n\nInput: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3\nOutput: true\nExplanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]\n\nExample 2:\n\nInput: hand = [1,2,3,4,5], groupSize = 4\nOutput: false\nExplanation: Alice's hand can not be rearranged into groups of 4.\n\n\n\u00a0\nConstraints:\n\n1 <= hand.length <= 104\n0 <= hand[i] <= 109\n1 <= groupSize <= hand.length\n\n\u00a0\nNote: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/\n",
    "url": "https://leetcode.com/problems/0846-hand-of-straights",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "import heapq\nclass Solution:\n    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:\n        return self.most_optimal(hand, groupSize)\n    \n    # Time Complexity: O(n logn + NK)\n    # Space Complexity: O(n)\n    def map(self, hands: List[int], groupSize: int) -> bool:\n        # Attempt\n        # # 1,2,3,,6,2,3,4,7,8\n        # # groupSize = 3\n        # # if n% g != 0 False\n        # #   b = n//g\n        # #   b bcukets\n        # #  hashmap = [1,2,2,1,1]\n        # #  smallest_cur = min(hashmap)\n        # #  [[],[],[]]\n        # # smallest_cur = min(hashmap)\n        # # \n        # #    [] 1 cur+=1\n        # #       2 , 3\n        # #      if hashmap[smallest_cur] == 0\n        # #         reryurn Fa;se\n        # #      hashmap[smallest_cur] -=1\n        # # return True\n        # #       \n        n = len(hands)\n        if n% groupSize!= 0:\n            return False\n        # no_of_buckets = n // groupSize\n        # MAX = max(hand)\n        # MIN = min(hand)\n        # counts = [0] * ( MAX -MIN  +1)\n        cardCount  = Counter(hands)\n        min_heap = list(cardCount.keys())\n        heapq.heapify(min_heap)\n        while min_heap:\n            current_card = min_heap[0]  \n            for i in range(groupSize):\n                if cardCount[current_card + i] == 0:\n                    return False\n                cardCount[current_card + i] -= 1\n                if cardCount[current_card + i] <= 0:\n                    heapq.heappop(min_heap)\n        return True\n\n    def optimal(self, hands: List[int], groupSize: int) -> bool: # hand = [1,2,3,6,2,3,4,7,8], groupSize = 3\n        cardCount  = Counter(hands) # {1:1, 2:2, 3:2, 6:1, 4:1,7:1,8:1}\n        # Sorted list of card values\n        sortedCards = sorted(cardCount.keys()) # 1 2 3 4 6 7 8\n        # Queue to keep track of the number of new groups\n        # starting with each card value\n        groupStartQueue = deque() #  []\n        lastCard = -1\n        currentOpenGroups = 0\n        for currentCard in sortedCards: # 1 2 3 4 6 7 8   -> 6\n                        # Check if there are any discrepancies in the sequence\n            # or more groups are required than available cards\n            if (\n                currentOpenGroups > 0 and currentCard > lastCard + 1 # \n            ) or currentOpenGroups > cardCount[currentCard]: # \n                return False\n\n            groupStartQueue.append(cardCount[currentCard] - currentOpenGroups) #  0, 0, 1 \n            lastCard = currentCard # 6\n            currentOpenGroups = cardCount[currentCard] # 1\n            # Maintain the queue size to be equal to groupSize\n            if len(groupStartQueue) == groupSize: # \n                currentOpenGroups -= groupStartQueue.popleft() # 0\n\n        return currentOpenGroups == 0\n\n\n    def most_optimal(self, hand: List[int], groupSize: int) -> bool:\n        if len(hand) % groupSize != 0:\n            return False\n\n        # Counter to store the count of each card value\n        card_count = Counter(hand)\n\n        for card in hand:\n            start_card = card\n            # Find the start of the potential straight sequence\n            while card_count[start_card - 1]:\n                start_card -= 1\n\n            # Process the sequence starting from start_card\n            while start_card <= card:\n                while card_count[start_card]:\n                    # Check if we can form a consecutive sequence\n                    # of groupSize cards\n                    for next_card in range(start_card, start_card + groupSize):\n                        if not card_count[next_card]:\n                            return False\n                        card_count[next_card] -= 1\n                start_card += 1\n\n        return True\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/0846-hand-of-straights/",
      "datePublished": "2024-07-31",
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