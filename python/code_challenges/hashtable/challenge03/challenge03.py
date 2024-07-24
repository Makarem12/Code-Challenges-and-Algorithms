def sum_of_unique_elements(nums):
    # Create a hashtable to count occurrences of each element
    element_count = {}
    
    for num in nums:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1
    
    # Sum elements that appear exactly once
    unique_sum = 0
    for num, count in element_count.items():
        if count == 1:
            unique_sum += num
    #returning the summation
    return unique_sum

