def print_arr(arr):
    if len(arr) < 1:
        print("Empty list")
    print(*arr)

def max_independent_set(nums):

    # Size of passed in array
    nums_size = len(nums)

    # Base cases
    # No elements in nums array
    if nums_size == 0:
        return []
    
    # Check if all nums are negative
    for num in nums:
        if num > 0:
            break
    
    # Only 1 element (can assume element is positive since we already checked for all negatives above)
    # in which case we can go ahead and return that in a list
    if nums_size == 1:
        single_arr = []
        single_arr.append(nums[0])
        return single_arr

    included_nums = [False] * nums_size
    dp = [0] * nums_size

    # either start from index 1 or 0, but some instances those are negative values so we choose 0 instead
    dp[0] = max(0, nums[0])
    dp[1] = max(dp[0], nums[1])

    if nums[0] > 0:
        included_nums[0] = True

    if nums[1] > dp[0]:
        included_nums[1] = True
    
    # dp[i] holds the current highest sum up til the ith element in nums
    for i in range(2, nums_size):
        include = nums[i] + dp[i - 2]
        exclude = dp[i - 1]

        # See which path/sum is larger from dp[i - 1] and nums[i] + dp[i - 2]

        if include > exclude:
            included_nums[i] = True
            dp[i] = include
        else:
            dp[i] = exclude

    result = []
    i = nums_size - 1
    while i >= 0:
        if included_nums[i] == True:
            result.append(nums[i])
            i -= 2
        else:
            i -= 1
    
    result.reverse()
    return result


def main():

    list1 = [7,2,5,8,6]
    list2 = [-1,-1,0]
    list3 = [-1,-1,-10,-34]
    list4 = [10,-3,0]

    # ans1 = max_independent_set(list1)
    # print_arr(ans1)

    # ans2 = max_independent_set(list2)
    # print_arr(ans2)

    # ans3 = max_independent_set(list3)
    # print_arr(ans3) 

    # ans4 = max_independent_set(list4)
    # print_arr(ans4) 
      
    
main()


