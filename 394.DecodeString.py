"""
Leetcode hard
"""
def decodeString(self, s: str) -> str:
        # Need a stack
        # stack: [string, number]
        # currentString, prevString
        # go through each character
        # want to return curstring
        stack = []; curNum = 0; curString = ''
        for c in s:
            # four cases
            if c == '[':
                # add string first, then number
                stack.append(curString)
                stack.append(curNum)
                # reset 
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                # jam whatever you had with num*currentString
                curString = prevString + num*curString # add current string
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString