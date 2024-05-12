def even_values_second(nums: list, counter: int) -> list:
    if counter == len(nums):
        return nums
    if nums[counter] % 2 == 0:
        print(nums[counter])
    return even_values_second(nums, counter + 1)

def even_values(nums: list) -> list:
    return even_values_second(nums, 0)


# nums_lists = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 4, 8, 3], [1, 3, 5, 8], [1, 3, 5, 7]]
# for lst in nums_lists:
#     even_values(lst)
