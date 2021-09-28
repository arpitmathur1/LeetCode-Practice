#def three_sum_closest(nums, target):

'''
INPUTS:
    nums: list of integers
    target: always exist, is an int
Output:
    list of integers from nums which sum up the closest to the target

Approaches:
    1) three for loops, where indexes arent equal
    2) we loop through the inputs, we add the data to a dictionary
        we'll have two pointers which'll iterqate through the system, and
        sum is appended to a list
        list iterated

'''

def three_sum_closest(nums, target):

    
    sums = []
    for left_pointer in range(len(nums)-2):
        for middle_pointer in range(left_pointer+1, len(nums)-1):
            for right_pointer in range(middle_pointer+1, len(nums)):
                sums.append(nums[left_pointer]+nums[middle_pointer]+nums[right_pointer]-target)
    sums.sort()
    print(sums)
    
    #for value in sums:
        



three_sum_closest([2,3,7,6],  13)
#three_sum_closest([2,3,4,5,6], 10)
#three_sum_closest([2,3,4,5,6], 19)
#three_sum_closest([2,3,4,5,6], 14)
#three_sum_closest([2,3,4,5,6], 13)
#three_sum_closest([2,3,4,5,6,3], 25)
