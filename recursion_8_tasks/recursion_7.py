def second_max(nums: list) -> int:
    if nums[0] >= nums[1]:
    	f_max = nums[0]
    	s_max = nums[1]
    else:
    	f_max = nums[1]
    	s_max = nums[0]
    return second_max_cont(nums, f_max, s_max, 2)

def second_max_cont(nums: list, f_max: int, s_max: int, ind: int) -> int:
    if ind == len(nums):
        return s_max
    if nums[ind] >= f_max:
        s_max = f_max
        f_max = nums[ind]
    elif nums[ind] > s_max:
    	s_max = nums[ind]
    return second_max_cont(nums, f_max, s_max, ind + 1)


# nums_lists = [[5, 4, 3, 2, 5], [2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 8, 7]]
# for nums in nums_lists:
#     print(second_max(nums))
