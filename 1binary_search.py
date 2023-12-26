def binary_search(nums: list, target: int):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid_idx = (left+right)//2
        if nums[mid_idx] == target:
            return mid_idx
        elif nums[mid_idx] < target:
            left = mid_idx+1  # +1 just to skip the middle element,cuz we already saw it
        else:  # nums[mid_idx] > target:
            right = mid_idx-1  # -1, we are not checking the middle element
    return -1

sorted_numbers = [int(n) for n in input().split()]
sought_number = int(input())
print(binary_search(sorted_numbers, sought_number))


# # INPUT1:
# 1 2 3 4 5
# 1
# # OUTPUT1:
# 0  # Index of 1 is 0


# # INPUT2:
# -1 0 1 2 4
# 1
# # OUTPUT2:
# 2  # Index of 1 is 2



# def binary_search(nums, target):
#     left = 0
#     right = len(nums) - 1
#
#     while left <= right:
#         mid_index = (left + right) // 2
#         mid_el = nums[mid_index]
#         if mid_el == target:
#             return mid_index
#         if target > mid_el:
#             left = mid_index + 1
#         else:
#             right = mid_index - 1
#     return -1
# nums = [int(x) for x in input().split()]
# target = int(input())
# print(binary_search(nums, target))