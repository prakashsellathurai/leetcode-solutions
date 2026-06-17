# 355-design-twitter


Try it on <a href='https://leetcode.com/problems/355-design-twitter'>leetcode</a>

## Description
<div class="description">
<div><p>Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the <code>10</code> most recent tweets in the user's news feed.</p>

<p>Implement the <code>Twitter</code> class:</p>

<ul>
	<li><code>Twitter()</code> Initializes your twitter object.</li>
	<li><code>void postTweet(int userId, int tweetId)</code> Composes a new tweet with ID <code>tweetId</code> by the user <code>userId</code>. Each call to this function will be made with a unique <code>tweetId</code>.</li>
	<li><code>List&lt;Integer&gt; getNewsFeed(int userId)</code> Retrieves the <code>10</code> most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be <strong>ordered from most recent to least recent</strong>.</li>
	<li><code>void follow(int followerId, int followeeId)</code> The user with ID <code>followerId</code> started following the user with ID <code>followeeId</code>.</li>
	<li><code>void unfollow(int followerId, int followeeId)</code> The user with ID <code>followerId</code> started unfollowing the user with ID <code>followeeId</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input</strong>
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
<strong>Output</strong>
[null, null, [5], null, null, [6, 5], null, [5]]

<strong>Explanation</strong>
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -&gt; [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -&gt; [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -&gt; [5], since user 1 is no longer following user 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= userId, followerId, followeeId &lt;= 500</code></li>
	<li><code>0 &lt;= tweetId &lt;= 10<sup>4</sup></code></li>
	<li>All the tweets have <strong>unique</strong> IDs.</li>
	<li>At most <code>3 * 10<sup>4</sup></code> calls will be made to <code>postTweet</code>, <code>getNewsFeed</code>, <code>follow</code>, and <code>unfollow</code>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
from heapq import *
from collections import defaultdict, deque


class Twitter:

    # Each user has a separate min heap
    # if size of heap is lesser than 10 keep pushing tweets and when it's full, poppush
    # use a defaultdict to associate user id's to their heaps
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.following = defaultdict(set)
        self.user_tweets = defaultdict(deque)
        self.post = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        """
        self.post += 1
        tweets = self.user_tweets[userId]
        tweets.append(((self.post), tweetId))
        if len(tweets) > 10:
            tweets.popleft()

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        h = []
        u = self.user_tweets[userId]
        h.extend(u)
        heapify(h)
        for user in self.following[userId]:
            tweets = self.user_tweets[user]
            for x in range(len(tweets) - 1, -1, -1):
                if len(h) < 10:
                    heappush(h, tweets[x])
                else:
                    if h[0][0] < tweets[x][0]:
                        heappushpop(h, tweets[x])
                    else:
                        break
        return [heappop(h)[1] for x in range(len(h))][::-1]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            self.following[followerId].discard(followeeId)

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "355. Design Twitter",
    "text": "Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.\nImplement the Twitter class:\n\nTwitter() Initializes your twitter object.\nvoid postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.\nList<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.\nvoid follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.\nvoid unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.\n\n\u00a0\nExample 1:\nInput\n[\"Twitter\", \"postTweet\", \"getNewsFeed\", \"follow\", \"postTweet\", \"getNewsFeed\", \"unfollow\", \"getNewsFeed\"]\n[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]\nOutput\n[null, null, [5], null, null, [6, 5], null, [5]]\n\nExplanation\nTwitter twitter = new Twitter();\ntwitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).\ntwitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]\ntwitter.follow(1, 2);    // User 1 follows user 2.\ntwitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).\ntwitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.\ntwitter.unfollow(1, 2);  // User 1 unfollows user 2.\ntwitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.\n\n\u00a0\nConstraints:\n\n1 <= userId, followerId, followeeId <= 500\n0 <= tweetId <= 104\nAll the tweets have unique IDs.\nAt most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.\n\n",
    "url": "https://leetcode.com/problems/355-design-twitter",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "from heapq import *\nfrom collections import defaultdict, deque\n\n\nclass Twitter:\n\n    # Each user has a separate min heap\n    # if size of heap is lesser than 10 keep pushing tweets and when it's full, poppush\n    # use a defaultdict to associate user id's to their heaps\n    def __init__(self):\n        \"\"\"\n        Initialize your data structure here.\n        \"\"\"\n        self.following = defaultdict(set)\n        self.user_tweets = defaultdict(deque)\n        self.post = 0\n\n    def postTweet(self, userId, tweetId):\n        \"\"\"\n        Compose a new tweet.\n        \"\"\"\n        self.post += 1\n        tweets = self.user_tweets[userId]\n        tweets.append(((self.post), tweetId))\n        if len(tweets) > 10:\n            tweets.popleft()\n\n    def getNewsFeed(self, userId):\n        \"\"\"\n        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.\n        \"\"\"\n        h = []\n        u = self.user_tweets[userId]\n        h.extend(u)\n        heapify(h)\n        for user in self.following[userId]:\n            tweets = self.user_tweets[user]\n            for x in range(len(tweets) - 1, -1, -1):\n                if len(h) < 10:\n                    heappush(h, tweets[x])\n                else:\n                    if h[0][0] < tweets[x][0]:\n                        heappushpop(h, tweets[x])\n                    else:\n                        break\n        return [heappop(h)[1] for x in range(len(h))][::-1]\n\n    def follow(self, followerId, followeeId):\n        \"\"\"\n        Follower follows a followee. If the operation is invalid, it should be a no-op.\n        \"\"\"\n        if followerId != followeeId:\n            self.following[followerId].add(followeeId)\n\n    def unfollow(self, followerId, followeeId):\n        \"\"\"\n        Follower unfollows a followee. If the operation is invalid, it should be a no-op.\n        \"\"\"\n        if followerId != followeeId:\n            self.following[followerId].discard(followeeId)\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/355-design-twitter/",
      "datePublished": "2024-12-03",
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