# Problem: Count unique email address
# Date:: 11/05/2021

"""
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each email[i], return the number of different addresses that actually receive mails.

 

Example 1:

Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
Example 2:

Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3
"""

# My take-aways
# 1) string.split('delimiter'), return a list, can assign each item in output list to variable
# 2) string.replace("target delimiter", "replace with"), return a string
# 3) set(), add(hashable), len(set) = num. unique elements

# My solution
def numUniqueEmails(emails):
    # Keep track of local and domain names
    localNames, domainNames = set(), set()
    flags = [".", "+"]
    numUnique = 0

    # Split the string by flags
    for email in emails:
        # Get local and domain names by @
        parts = email.split("@")
        local, domain = parts[0], parts[1]
        # Extract substring before first +
        plus_split = local.split(flags[1])
        if plus_split:
            local = plus_split[0]
        # Join each 'space' with ''
        dot_split = local.split(flags[0])
        if dot_split:
            local = "".join(dot_split)
        # Increment if current email local OR domain is unique
        if (local not in localNames) or (domain not in domainNames):
            numUnique += 1
            localNames.add(local)
            domainNames.add(domain)
    return numUnique

# Best solution
def numUniqueEmailsBest(emails):
    addresses = set()
    for email in emails:
        local, domain = email.split("@")
        local = local.split("+")[0].replace(".", "")
        addresses.add(local + "@" + domain)
    return len(addresses)