# 1472-design-browser-history


Try it on <a href='https://leetcode.com/problems/1472-design-browser-history'>leetcode</a>

## Description
<div class="description">
<div><p>You have a <strong>browser</strong> of one tab where you start on the <code>homepage</code> and you can visit another <code>url</code>, get back in the history number of <code>steps</code> or move forward in the history number of <code>steps</code>.</p>

<p>Implement the <code>BrowserHistory</code> class:</p>

<ul>
	<li><code>BrowserHistory(string homepage)</code> Initializes the object with the <code>homepage</code>&nbsp;of the browser.</li>
	<li><code>void visit(string url)</code>&nbsp;Visits&nbsp;<code>url</code> from the current page. It clears up all the forward history.</li>
	<li><code>string back(int steps)</code>&nbsp;Move <code>steps</code> back in history. If you can only return <code>x</code> steps in the history and <code>steps &gt; x</code>, you will&nbsp;return only <code>x</code> steps. Return the current <code>url</code>&nbsp;after moving back in history <strong>at most</strong> <code>steps</code>.</li>
	<li><code>string forward(int steps)</code>&nbsp;Move <code>steps</code> forward in history. If you can only forward <code>x</code> steps in the history and <code>steps &gt; x</code>, you will&nbsp;forward only&nbsp;<code>x</code> steps. Return the current <code>url</code>&nbsp;after forwarding in history <strong>at most</strong> <code>steps</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example:</strong></p>

<pre><b>Input:</b>
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
<b>Output:</b>
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

<b>Explanation:</b>
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= homepage.length &lt;= 20</code></li>
	<li><code>1 &lt;= url.length &lt;= 20</code></li>
	<li><code>1 &lt;= steps &lt;= 100</code></li>
	<li><code>homepage</code> and <code>url</code> consist of&nbsp; '.' or lower case English letters.</li>
	<li>At most <code>5000</code>&nbsp;calls will be made to <code>visit</code>, <code>back</code>, and <code>forward</code>.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        self.bound = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        if self.curr == len(self.history):
            self.history.append(url)
        else:
            self.history[self.curr] = url
        self.bound = self.curr

    def back(self, steps: int) -> str:
        self.curr = max(self.curr - steps, 0)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.curr + steps, self.bound)
        return self.history[self.curr]

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1472. Design Browser History",
    "text": "You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.\nImplement the BrowserHistory class:\n\nBrowserHistory(string homepage) Initializes the object with the homepage\u00a0of the browser.\nvoid visit(string url)\u00a0Visits\u00a0url from the current page. It clears up all the forward history.\nstring back(int steps)\u00a0Move steps back in history. If you can only return x steps in the history and steps > x, you will\u00a0return only x steps. Return the current url\u00a0after moving back in history at most steps.\nstring forward(int steps)\u00a0Move steps forward in history. If you can only forward x steps in the history and steps > x, you will\u00a0forward only\u00a0x steps. Return the current url\u00a0after forwarding in history at most steps.\n\n\u00a0\nExample:\nInput:\n[\"BrowserHistory\",\"visit\",\"visit\",\"visit\",\"back\",\"back\",\"forward\",\"visit\",\"forward\",\"back\",\"back\"]\n[[\"leetcode.com\"],[\"google.com\"],[\"facebook.com\"],[\"youtube.com\"],[1],[1],[1],[\"linkedin.com\"],[2],[2],[7]]\nOutput:\n[null,null,null,null,\"facebook.com\",\"google.com\",\"facebook.com\",null,\"linkedin.com\",\"google.com\",\"leetcode.com\"]\n\nExplanation:\nBrowserHistory browserHistory = new BrowserHistory(\"leetcode.com\");\nbrowserHistory.visit(\"google.com\");       // You are in \"leetcode.com\". Visit \"google.com\"\nbrowserHistory.visit(\"facebook.com\");     // You are in \"google.com\". Visit \"facebook.com\"\nbrowserHistory.visit(\"youtube.com\");      // You are in \"facebook.com\". Visit \"youtube.com\"\nbrowserHistory.back(1);                   // You are in \"youtube.com\", move back to \"facebook.com\" return \"facebook.com\"\nbrowserHistory.back(1);                   // You are in \"facebook.com\", move back to \"google.com\" return \"google.com\"\nbrowserHistory.forward(1);                // You are in \"google.com\", move forward to \"facebook.com\" return \"facebook.com\"\nbrowserHistory.visit(\"linkedin.com\");     // You are in \"facebook.com\". Visit \"linkedin.com\"\nbrowserHistory.forward(2);                // You are in \"linkedin.com\", you cannot move forward any steps.\nbrowserHistory.back(2);                   // You are in \"linkedin.com\", move back two steps to \"facebook.com\" then to \"google.com\". return \"google.com\"\nbrowserHistory.back(7);                   // You are in \"google.com\", you can move back only one step to \"leetcode.com\". return \"leetcode.com\"\n\n\u00a0\nConstraints:\n\n1 <= homepage.length <= 20\n1 <= url.length <= 20\n1 <= steps <= 100\nhomepage and url consist of\u00a0 '.' or lower case English letters.\nAt most 5000\u00a0calls will be made to visit, back, and forward.\n\n",
    "url": "https://leetcode.com/problems/1472-design-browser-history",
    "answerCount": 1,
    "datePublished": "2022-06-19T23:02:59+05:30",
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class BrowserHistory:\n    def __init__(self, homepage: str):\n        self.history = [homepage]\n        self.curr = 0\n        self.bound = 0\n\n    def visit(self, url: str) -> None:\n        self.curr += 1\n        if self.curr == len(self.history):\n            self.history.append(url)\n        else:\n            self.history[self.curr] = url\n        self.bound = self.curr\n\n    def back(self, steps: int) -> str:\n        self.curr = max(self.curr - steps, 0)\n        return self.history[self.curr]\n\n    def forward(self, steps: int) -> str:\n        self.curr = min(self.curr + steps, self.bound)\n        return self.history[self.curr]\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1472-design-browser-history/",
      "datePublished": "2022-06-19T23:02:59+05:30",
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