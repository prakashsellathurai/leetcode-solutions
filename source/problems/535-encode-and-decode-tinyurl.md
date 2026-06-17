# 535-encode-and-decode-tinyurl


Try it on <a href='https://leetcode.com/problems/535-encode-and-decode-tinyurl'>leetcode</a>

## Description
<div class="description">
<div><blockquote>Note: This is a companion problem to the <a href="https://leetcode.com/discuss/interview-question/system-design/" target="_blank">System Design</a> problem: <a href="https://leetcode.com/discuss/interview-question/124658/Design-a-URL-Shortener-(-TinyURL-)-System/" target="_blank">Design TinyURL</a>.</blockquote>

<p>TinyURL is a URL shortening service where you enter a URL such as <code>https://leetcode.com/problems/design-tinyurl</code> and it returns a short URL such as <code>http://tinyurl.com/4e9iAk</code>. Design a class to encode a URL and decode a tiny URL.</p>

<p>There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.</p>

<p>Implement the <code>Solution</code> class:</p>

<ul>
	<li><code>Solution()</code> Initializes the object of the system.</li>
	<li><code>String encode(String longUrl)</code> Returns a tiny URL for the given <code>longUrl</code>.</li>
	<li><code>String decode(String shortUrl)</code> Returns the original long URL for the given <code>shortUrl</code>. It is guaranteed that the given <code>shortUrl</code> was encoded by the same object.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> url = "https://leetcode.com/problems/design-tinyurl"
<strong>Output:</strong> "https://leetcode.com/problems/design-tinyurl"

<strong>Explanation:</strong>
Solution obj = new Solution();
string tiny = obj.encode(url); // returns the encoded tiny url.
string ans = obj.decode(tiny); // returns the original url after deconding it.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= url.length &lt;= 10<sup>4</sup></code></li>
	<li><code>url</code> is guranteed to be a valid URL.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Codec:

    alphabet = string.ascii_letters + "0123456789"

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        while longUrl not in self.url2code:
            code = "".join(random.choice(Codec.alphabet) for _ in range(6))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return "http://tinyurl.com/" + self.url2code[longUrl]

    def decode(self, shortUrl):
        return self.code2url[shortUrl[-6:]]

```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "535. Encode and Decode TinyURL",
    "text": "Note: This is a companion problem to the System Design problem: Design TinyURL.\nTinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.\nThere is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.\nImplement the Solution class:\n\nSolution() Initializes the object of the system.\nString encode(String longUrl) Returns a tiny URL for the given longUrl.\nString decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.\n\n\u00a0\nExample 1:\nInput: url = \"https://leetcode.com/problems/design-tinyurl\"\nOutput: \"https://leetcode.com/problems/design-tinyurl\"\n\nExplanation:\nSolution obj = new Solution();\nstring tiny = obj.encode(url); // returns the encoded tiny url.\nstring ans = obj.decode(tiny); // returns the original url after deconding it.\n\n\u00a0\nConstraints:\n\n1 <= url.length <= 104\nurl is guranteed to be a valid URL.\n\n",
    "url": "https://leetcode.com/problems/535-encode-and-decode-tinyurl",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Codec:\n\n    alphabet = string.ascii_letters + \"0123456789\"\n\n    def __init__(self):\n        self.url2code = {}\n        self.code2url = {}\n\n    def encode(self, longUrl):\n        while longUrl not in self.url2code:\n            code = \"\".join(random.choice(Codec.alphabet) for _ in range(6))\n            if code not in self.code2url:\n                self.code2url[code] = longUrl\n                self.url2code[longUrl] = code\n        return \"http://tinyurl.com/\" + self.url2code[longUrl]\n\n    def decode(self, shortUrl):\n        return self.code2url[shortUrl[-6:]]\n",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/535-encode-and-decode-tinyurl/",
      "datePublished": "2024-02-19",
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