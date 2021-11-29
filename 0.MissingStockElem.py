"""
Stocks

GOOGLE: [('6/23', 500), ('6/25', 1000)]
AMAZON: [('6/23', 500), ('6/24', 900), ('7/1', 1000)]
APPLE: [('6/23', 500)]

2D array
Goal: find the sum of all stocks across each day
1D array: []
6/23...7/1
1500   1000

My approach:
DP: buld a table and access the previous value under certain rule
"""
def missingStock(nums):
    # dateSum = [[None]*len(nums[r]) for r in range(len(nums))]

    # Get date range by finding min and max dates
    minDate, maxDate = int(min(map(min, nums))[0]), int(max(map(max, nums))[0])

    # Generate a stock price access table
    dateSum = []
    for r in range(len(nums)):
        # numCol = len(nums[r])
        numDays = maxDate - minDate + 1
        dateSum.append([0]*numDays)

    # Record each existing finding to the table
    # minDate = 1, maxDate = 4
    # [2: A, 3: B]
    # [1: A, 2: A, 3: B , 4: B]
    for stock in range(len(dateSum)):
        currentDate = minDate
        col, refCol = 0, 0
        while currentDate <= maxDate:
            # Get value at index
            refData = nums[stock][refCol]
            date, volume = int(refData[0]), refData[1]
            # Missing entry is when date mismatches
            if currentDate == date or refCol == 0:
                # Set value in sum table
                dateSum[stock][col] = volume
            else:
                dateSum[stock][col] = dateSum[stock][col-1]
            # Update pointer in the reference table 
            if refCol < len(nums[stock])-1:
                nextDate = int(nums[stock][refCol+1][0])
                # See if next date available matches with expected next date
                if nextDate == currentDate+1:
                    refCol += 1
            # Always fill a new entry in the sum atable
            col += 1
            currentDate += 1
    # Return sum per day in the form of a dictionary
    dailySum = {}
    currentDate = minDate
    for col in range(len(dateSum[0])):
        for row in range(len(dateSum)):
            # Get value at index, else set default value and increment
            dailySum[currentDate] = dailySum.get(currentDate, 0) + dateSum[row][col]
        currentDate += 1
    return dailySum
n = [
[('2', 500), ('3', 1200)],
[('1', 300), ('3', 900), ('5', 1000)],
[('2', 300), ('3', 900)],
[('3', 400), ('4', 600)]
]
print(missingStock(n))
"""
Results are:
{1: 1500, 2: 1500, 3: 3400, 4: 3600, 5: 3700}
"""

# def fib(n):
#     """
#     Iterative
#     n (int): the nth fib number
#     """
#     memo = {0: 0, 1: 1, 2: 1}
#     for i in range(3, n):
#         # Set memo
#         memo[i] = memo[i-2]+memo[i-1]
#     return memo[n]