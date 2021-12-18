def minStartValue(nums):
    min_val = 0
    running_sum = 0
    
    for n in nums:
        running_sum += n
        min_val = min(min_val, running_sum)
    
    return -min_val+1