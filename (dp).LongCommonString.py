"""
Given two strings. 1143
Find common substring, longest
"""
def longestCommonString(str1, str2):
    # Set a 2D array of zeroes
    # Set a length to keep track of longest substring
    # Find length of each string
    # Go through each string till the end
    # LOOK back
    n, m = len(str1), len(str2)
    scoreTbl = [[0 for _ in range(n+1)] for _ in range(m+1)]

    bestScore = 0
    currentLongest = ""

    for i in range(m+1):
        for j in range(n+1):
            if (i==0) or (j==0):
                scoreTbl[i][j] = 0
            elif str2[i-1] == str1[j-1]:
                # Same last common character
                scoreTbl[i][j] = scoreTbl[i-1][j-1]+1
                currentLongest += str2[i-1]
                bestScore = max(bestScore, scoreTbl[i][j])
            else:
                # Reset to zero
                scoreTbl[i][j] = 0
    return bestScore, currentLongest

### TEST ###
str1, str2 = 'abcdegfh', 'taybcdek'
print(longestCommonString(str1, str2))
    
