def isPalindrome(s):
    """
    My intuition
    left and right element should be the same
    narrow search range by reducing index
    skip over non alphabetic character
    """
    left, right = 0, len(s)-1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -=1 
    return True

# Test case
assert isPalindrome("A man, a plan, a canal: Panama") == True
assert isPalindrome("P0") == False