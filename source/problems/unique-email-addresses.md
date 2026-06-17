# unique-email-addresses


Try it on <a href='https://leetcode.com/problems/unique-email-addresses'>leetcode</a>

## Description
<div class="description">
<div><p>Every <strong>valid email</strong> consists of a <strong>local name</strong> and a <strong>domain name</strong>, separated by the <code>'@'</code> sign. Besides lowercase letters, the email may contain one or more <code>'.'</code> or <code>'+'</code>.</p>

<ul>
	<li>For example, in <code>"alice@leetcode.com"</code>, <code>"alice"</code> is the <strong>local name</strong>, and <code>"leetcode.com"</code> is the <strong>domain name</strong>.</li>
</ul>

<p>If you add periods <code>'.'</code> between some characters in the <strong>local name</strong> part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule <strong>does not apply</strong> to <strong>domain names</strong>.</p>

<ul>
	<li>For example, <code>"alice.z@leetcode.com"</code> and <code>"alicez@leetcode.com"</code> forward to the same email address.</li>
</ul>

<p>If you add a plus <code>'+'</code> in the <strong>local name</strong>, everything after the first plus sign <strong>will be ignored</strong>. This allows certain emails to be filtered. Note that this rule <strong>does not apply</strong> to <strong>domain names</strong>.</p>

<ul>
	<li>For example, <code>"m.y+name@email.com"</code> will be forwarded to <code>"my@email.com"</code>.</li>
</ul>

<p>It is possible to use both of these rules at the same time.</p>

<p>Given an array of strings <code>emails</code> where we send one email to each <code>emails[i]</code>, return <em>the number of different addresses that actually receive mails</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
<strong>Output:</strong> 2
<strong>Explanation:</strong> "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= emails.length &lt;= 100</code></li>
	<li><code>1 &lt;= emails[i].length &lt;= 100</code></li>
	<li><code>emails[i]</code> consist of lowercase English letters, <code>'+'</code>, <code>'.'</code> and <code>'@'</code>.</li>
	<li>Each <code>emails[i]</code> contains exactly one <code>'@'</code> character.</li>
	<li>All local and domain names are non-empty.</li>
	<li>Local names do not start with a <code>'+'</code> character.</li>
	<li>Domain names end with the <code>".com"</code> suffix.</li>
	<li>Domain names must contain at least one character before <code>".com"</code> suffix.</li>
</ul>
</div>
</div>

## Solution(Python)
```Python
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        return self.stringSplitmethod(emails)

    # Time Complexity: O(N * M)
    # Space Complexity: O(N*M) 
    def linearIteration(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            cleanEmail = []

            for currChar in email:
                if currChar == "+" or currChar == "@":
                    break;
                
                if currChar != '.':
                    cleanEmail.append(currChar)
            domainName = []

            for currChar in reversed(email):
                domainName.append(currChar)
                if currChar == "@":
                    break

            domainName  = ''.join(domainName[::-1])
            cleanEmail = ''.join(cleanEmail)
            unique_emails.add(cleanEmail+domainName)
        return len(unique_emails)



    # Time Complexity: O(N * M)
    # Space Complexity: O(N*M) 
    def stringSplitmethod(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            localName, domainName = email.split('@')
            localName = localName.split('+')[0].replace('.','')
            uniqueEmail = localName + "@" +domainName
            unique_emails.add(uniqueEmail)
        return len(unique_emails)
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": " \u00a0Unique Email Addresses",
    "text": "Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.\n\nFor example, in \"alice@leetcode.com\", \"alice\" is the local name, and \"leetcode.com\" is the domain name.\n\nIf you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.\n\nFor example, \"alice.z@leetcode.com\" and \"alicez@leetcode.com\" forward to the same email address.\n\nIf you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.\n\nFor example, \"m.y+name@email.com\" will be forwarded to \"my@email.com\".\n\nIt is possible to use both of these rules at the same time.\nGiven an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.\n\u00a0\nExample 1:\nInput: emails = [\"test.email+alex@leetcode.com\",\"test.e.mail+bob.cathy@leetcode.com\",\"testemail+david@lee.tcode.com\"]\nOutput: 2\nExplanation: \"testemail@leetcode.com\" and \"testemail@lee.tcode.com\" actually receive mails.\n\nExample 2:\nInput: emails = [\"a@leetcode.com\",\"b@leetcode.com\",\"c@leetcode.com\"]\nOutput: 3\n\n\u00a0\nConstraints:\n\n1 <= emails.length <= 100\n1 <= emails[i].length <= 100\nemails[i] consist of lowercase English letters, '+', '.' and '@'.\nEach emails[i] contains exactly one '@' character.\nAll local and domain names are non-empty.\nLocal names do not start with a '+' character.\nDomain names end with the \".com\" suffix.\nDomain names must contain at least one character before \".com\" suffix.\n\n",
    "url": "https://leetcode.com/problems/unique-email-addresses",
    "answerCount": 1,
    "author": {
      "@type": "Organization",
      "name": "LeetCode",
      "url": "https://leetcode.com"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "class Solution:\n    def numUniqueEmails(self, emails: List[str]) -> int:\n        return self.stringSplitmethod(emails)\n\n    # Time Complexity: O(N * M)\n    # Space Complexity: O(N*M) \n    def linearIteration(self, emails: List[str]) -> int:\n        unique_emails = set()\n        \n        for email in emails:\n            cleanEmail = []\n\n            for currChar in email:\n                if currChar == \"+\" or currChar == \"@\":\n                    break;\n                \n                if currChar != '.':\n                    cleanEmail.append(currChar)\n            domainName = []\n\n            for currChar in reversed(email):\n                domainName.append(currChar)\n                if currChar == \"@\":\n                    break\n\n            domainName  = ''.join(domainName[::-1])\n            cleanEmail = ''.join(cleanEmail)\n            unique_emails.add(cleanEmail+domainName)\n        return len(unique_emails)\n\n\n\n    # Time Complexity: O(N * M)\n    # Space Complexity: O(N*M) \n    def stringSplitmethod(self, emails: List[str]) -> int:\n        unique_emails = set()\n        \n        for email in emails:\n            localName, domainName = email.split('@')\n            localName = localName.split('+')[0].replace('.','')\n            uniqueEmail = localName + \"@\" +domainName\n            unique_emails.add(uniqueEmail)\n        return len(unique_emails)",
      "url": "https://prakashsellathurai.com/leetcode-solutions/problems/unique-email-addresses/",
      "datePublished": "2022-03-21",
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