:
            runningSum += dateSum[r][c]
        dailySum[currentDate] = runningSum
        currentDate += 1
    return dateSum
    