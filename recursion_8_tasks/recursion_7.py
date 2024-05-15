def second_max(nums: list) -> int:
    if nums[0] >= nums[1]:
    	return second_max_cont(nums, nums[0], nums[1], 2)
    return second_max_cont(nums, nums[1], nums[0], 0)

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
