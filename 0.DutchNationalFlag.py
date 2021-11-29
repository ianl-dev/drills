"""
Given a list and a pivot point, arrange the array such that 

elements less than pivots appear first
elements equal to pivots appear after
elemenets larger than pivots appear last in the array

Try solving using O(n) time complexity and O(1) space complexity
"""
def dutch(nums, pivot):
    """
    My approach: think of [0,-1,2], pivot being the first element 0
    The correct arrangement is: [-1, 0, 2]
    >>> dutch([0, -1, 2], 0)
    [-1, 0, 2]

    There are 3 groups I keep:
    - smaller: nums[:smaller]
    - equal: nums[smaller:equal]
    - not-yet-classify: nums[equal:larger]
    - larger: nums[larger:]

    In general, when comparing, think, 
    what do I want to be before pivot
    - non zero elements? than != pivot
    - lesser elements? than < pivot

    what is pivot: your baseline, like 0, or pivot in quicksort

    """
    # Keep three pointers
    smaller, equal = 0, 0
    larger = len(nums)-1

    # Loop to classify unclassified loop
    while equal < larger:
        if nums[equal] < pivot:
            # Want large elements to be behind pivot
            nums[equal], nums[smaller] = nums[smaller], nums[equal]
            equal += 1
            smaller += 1
        elif nums[equal] == pivot:
            equal += 1
            # Loop has to end
        else:
            # Larger moves to end
            nums[equal], nums[larger] = nums[larger], nums[equal]
            # Large is now classified, but the other element moved is not
            larger -= 1
    return nums

n = [50, 1, 2, 0, 2, 1, 1]
print(dutch(n, 1))