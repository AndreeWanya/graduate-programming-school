def second_max(nums: list) -> int:
    return second_max_cont(nums, 0, 0, 0)

def second_max_cont(nums: list, f_max: int, s_max: int, ind: int) -> int:
    if ind == len(nums):
        return s_max
    if nums[ind] >= f_max:
        s_max = f_max
        f_max = nums[ind]
    return second_max_cont(nums, f_max, s_max, ind + 1)


# nums_lists = [[5, 4, 3, 2, 5], [2, 3, 4, 5]]
# for nums in nums_lists:
#     print(second_max(nums))
