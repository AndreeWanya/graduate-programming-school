def even_indexes(nums: list) -> list:
    nums_2 = []
    return even_indexes_cont(nums, nums_2)

def even_indexes_cont(nums: list, nums_2: list) -> list:
    if len(nums_2) * 2 >= len(nums) - 1:
        return nums_2
    nums_2.append(nums[len(nums_2) * 2 + 1])
    return even_indexes_cont(nums, nums_2)

# nums_lists = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 4, 8, 3], [1, 3, 5, 8], [1, 3, 5, 7]]
# for lst in nums_lists:
#     print(even_indexes(lst))
