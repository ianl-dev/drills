def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    One element is dependent on the other's position
    MEDIUM question
    * I learned that resetting nums = something else is NOT in-place!

    Space complexity: O(1), time O(1)
    """
    if len(nums) <= 1 or len(nums) == k:
        # All elements would stay in the same place
        return

    shift = -1*(k%len(nums))
    # If not matching in length
    diff = len(nums[:shift]) - len(nums[shift:])
    nums[:shift-diff], nums[shift-diff:] = nums[shift:], nums[:shift]

n = [1,2,3,4,5,6,7]
n2 = [1,2]
rotate(n2, 2)
print(n2)