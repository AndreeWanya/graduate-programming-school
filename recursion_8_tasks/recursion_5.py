def even_values_second(nums: list, length: int) -> list:
    if length == 0:
        return nums
    if nums[-length] % 2 != 0:
        nums.pop(-length)
    return even_values_second(nums, length - 1)

def even_values(nums: list) -> list:
    return even_values_second(nums, len(nums))


# nums_lists = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 4, 8, 3], [1, 3, 5, 8], [1, 3, 5, 7]]
# for lst in nums_lists:
#     print(even_values(lst))
