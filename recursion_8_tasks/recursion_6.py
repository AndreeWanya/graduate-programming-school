def even_indexes(nums: list) -> list:
    return even_indexes_cont(nums, 1)

def even_indexes_cont(nums: list, ind: int) -> list:
    print(nums[ind])
    if ind + 2 >= len(nums):
        return nums
    return even_indexes_cont(nums, ind + 2)



# nums_lists = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 4, 8, 3], [1, 3, 5, 8], [1, 3, 5, 7]]
# for lst in nums_lists:
#     even_indexes(lst)
#     print()
