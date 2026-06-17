# 1195-fizz-buzz-multithreaded


Try it on <a href='https://leetcode.com/problems/1195-fizz-buzz-multithreaded'>leetcode</a>

## Description
<div class="description">
<div><p>You have the four functions:</p>

<ul>
	<li><code>printFizz</code> that prints the word <code>"fizz"</code> to the console,</li>
	<li><code>printBuzz</code> that prints the word <code>"buzz"</code> to the console,</li>
	<li><code>printFizzBuzz</code> that prints the word <code>"fizzbuzz"</code> to the console, and</li>
	<li><code>printNumber</code> that prints a given integer to the console.</li>
</ul>

<p>You are given an instance of the class <code>FizzBuzz</code> that has four functions: <code>fizz</code>, <code>buzz</code>, <code>fizzbuzz</code> and <code>number</code>. The same instance of <code>FizzBuzz</code> will be passed to four different threads:</p>

<ul>
	<li><strong>Thread A:</strong> calls <code>fizz()</code> that should output the word <code>"fizz"</code>.</li>
	<li><strong>Thread B:</strong> calls <code>buzz()</code> that should output the word <code>"buzz"</code>.</li>
	<li><strong>Thread C:</strong> calls <code>fizzbuzz()</code> that should output the word <code>"fizzbuzz"</code>.</li>
	<li><strong>Thread D:</strong> calls <code>number()</code> that should only output the integers.</li>
</ul>

<p>Modify the given class to output the series <code>[1, 2, "fizz", 4, "buzz", ...]</code> where the <code>i<sup>th</sup></code> token (<strong>1-indexed</strong>) of the series is:</p>

<ul>
	<li><code>"fizzbuzz"</code> if <code>i</code> is divisible by <code>3</code> and <code>5</code>,</li>
	<li><code>"fizz"</code> if <code>i</code> is divisible by <code>3</code> and not <code>5</code>,</li>
	<li><code>"buzz"</code> if <code>i</code> is divisible by <code>5</code> and not <code>3</code>, or</li>
	<li><code>i</code> if <code>i</code> is not divisible by <code>3</code> or <code>5</code>.</li>
</ul>

<p>Implement the <code>FizzBuzz</code> class:</p>

<ul>
	<li><code>FizzBuzz(int n)</code> Initializes the object with the number <code>n</code> that represents the length of the sequence that should be printed.</li>
	<li><code>void fizz(printFizz)</code> Calls <code>printFizz</code> to output <code>"fizz"</code>.</li>
	<li><code>void buzz(printBuzz)</code> Calls <code>printBuzz</code> to output <code>"buzz"</code>.</li>
	<li><code>void fizzbuzz(printFizzBuzz)</code> Calls <code>printFizzBuzz</code> to output <code>"fizzbuzz"</code>.</li>
	<li><code>void number(printNumber)</code> Calls <code>printnumber</code> to output the numbers.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> n = 15
<strong>Output:</strong> [1,2,"fizz",4,"buzz","fizz",7,8,"fizz","buzz",11,"fizz",13,14,"fizzbuzz"]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> n = 5
<strong>Output:</strong> [1,2,"fizz",4,"buzz"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 50</code></li>
</ul>
</div>
</div>

## Solution(Python)
```Python
import threading


class FizzBuzz(object):
    def __init__(self, n):
        self.__n = n
        self.__curr = 0
        self.__cv = threading.Condition()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        """
        :type printFizz: method
        :rtype: void
        """
        for i in range(1, self.__n+1):
            with self.__cv:
                while self.__curr % 4 != 0:
                    self.__cv.wait()
                self.__curr += 1
                if i % 3 == 0 and i % 5 != 0:
                    printFizz()
                self.__cv.notify_all()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        """
        :type printBuzz: method
        :rtype: void
        """
        for i in range(1, self.__n+1):
            with self.__cv:
                while self.__curr % 4 != 1:
                    self.__cv.wait()
                self.__curr += 1
                if i % 3 != 0 and i % 5 == 0:
                    printBuzz()
                self.__cv.notify_all()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        """
        :type printFizzBuzz: method
        :rtype: void
        """
        for i in range(1, self.__n+1):
            with self.__cv:
                while self.__curr % 4 != 2:
                    self.__cv.wait()
                self.__curr += 1
                if i % 3 == 0 and i % 5 == 0:
                    printFizzBuzz()
                self.__cv.notify_all()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.__n+1):
            with self.__cv:
                while self.__curr % 4 != 3:
                    self.__cv.wait()
                self.__curr += 1
                if i % 3 != 0 and i % 5 != 0:
                    printNumber(i)
                self.__cv.notify_all()
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "1195. Fizz Buzz Multithreaded",
    "text": "You have the four functions:\n\nprintFizz that prints the word \"fizz\" to the console,\nprintBuzz that prints the word \"buzz\" to the console,\nprintFizzBuzz that prints the word \"fizzbuzz\" to the console, and\nprintNumber that prints a given integer to the console.\n\nYou are given an instance of the class FizzBuzz that has four functions: fizz, buzz, fizzbuzz and number. The same instance of FizzBuzz will be passed to four different threads:\n\nThread A: calls fizz() that should output the word \"fizz\".\nThread B: calls buzz() that should output the word \"buzz\".\nThread C: calls fizzbuzz() that should output the word \"fizzbuzz\".\nThread D: calls number() that should only output the integers.\n\nModify the given class to output the series [1, 2, \"fizz\", 4, \"buzz\", ...] where the ith token (1-indexed) of the series is:\n\n\"fizzbuzz\" if i is divisible by 3 and 5,\n\"fizz\" if i is divisible by 3 and not 5,\n\"buzz\" if i is divisible by 5 and not 3, or\ni if i is not divisible by 3 or 5.\n\nImplement the FizzBuzz class:\n\nFizzBuzz(int n) Initializes the object with the number n that represents the length of the sequence that should be printed.\nvoid fizz(printFizz) Calls printFizz to output \"fizz\".\nvoid buzz(printBuzz) Calls printBuzz to output \"buzz\".\nvoid fizzbuzz(printFizzBuzz) Calls printFizzBuzz to output \"fizzbuzz\".\nvoid number(printNumber) Calls printnumber to output the numbers.\n\n\u00a0\nExample 1:\nInput: n = 15\nOutput: [1,2,\"fizz\",4,\"buzz\",\"fizz\",7,8,\"fizz\",\"buzz\",11,\"fizz\",13,14,\"fizzbuzz\"]\nExample 2:\nInput: n = 5\nOutput: [1,2,\"fizz\",4,\"buzz\"]\n\n\u00a0\nConstraints:\n\n1 <= n <= 50\n\n",
    "url": "https://leetcode.com/problems/1195-fizz-buzz-multithreaded",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "import threading\n\n\nclass FizzBuzz(object):\n    def __init__(self, n):\n        self.__n = n\n        self.__curr = 0\n        self.__cv = threading.Condition()\n\n    # printFizz() outputs \"fizz\"\n    def fizz(self, printFizz):\n        \"\"\"\n        :type printFizz: method\n        :rtype: void\n        \"\"\"\n        for i in range(1, self.__n+1):\n            with self.__cv:\n                while self.__curr % 4 != 0:\n                    self.__cv.wait()\n                self.__curr += 1\n                if i % 3 == 0 and i % 5 != 0:\n                    printFizz()\n                self.__cv.notify_all()\n\n    # printBuzz() outputs \"buzz\"\n    def buzz(self, printBuzz):\n        \"\"\"\n        :type printBuzz: method\n        :rtype: void\n        \"\"\"\n        for i in range(1, self.__n+1):\n            with self.__cv:\n                while self.__curr % 4 != 1:\n                    self.__cv.wait()\n                self.__curr += 1\n                if i % 3 != 0 and i % 5 == 0:\n                    printBuzz()\n                self.__cv.notify_all()\n\n    # printFizzBuzz() outputs \"fizzbuzz\"\n    def fizzbuzz(self, printFizzBuzz):\n        \"\"\"\n        :type printFizzBuzz: method\n        :rtype: void\n        \"\"\"\n        for i in range(1, self.__n+1):\n            with self.__cv:\n                while self.__curr % 4 != 2:\n                    self.__cv.wait()\n                self.__curr += 1\n                if i % 3 == 0 and i % 5 == 0:\n                    printFizzBuzz()\n                self.__cv.notify_all()\n\n    # printNumber(x) outputs \"x\", where x is an integer.\n    def number(self, printNumber):\n        \"\"\"\n        :type printNumber: method\n        :rtype: void\n        \"\"\"\n        for i in range(1, self.__n+1):\n            with self.__cv:\n                while self.__curr % 4 != 3:\n                    self.__cv.wait()\n                self.__curr += 1\n                if i % 3 != 0 and i % 5 != 0:\n                    printNumber(i)\n                self.__cv.notify_all()",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/1195-fizz-buzz-multithreaded/",
      "datePublished": "2025-06-24",
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