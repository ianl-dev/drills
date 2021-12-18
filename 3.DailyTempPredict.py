"""
Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
For example, given the list temperatures = 
[73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].
Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""
# O(n) time, o(n) space
# use stack
def findDaysUntilWarmer(temps):
    n = len(temps)
    # Maintain an empty list as stack, and days to record the days until next warmest day
    days, stack = [0]*n, []

    for i in range(n-1, -1, -1): # Reverse till the first element
        if not stack:
            stack.append(i)
        else:
            while stack and temps[stack[-1]] <= temps[i]:
                stack.pop()
            # Set daily values as last warmest value minus current (distance)
            days[i] = 0 if not stack else stack[-1]-i 
            # if suppose 76, 73 (last day). 73 <= 76, meaning 76 is the new warmest day, and there is no warmer day 
            # after 76, no warmer, so 0
            stack.append(i)
    return days
    # We want to pop the stack, when stack is not empty