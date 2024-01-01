def binary_search(nums: list, target: int):
    start_idx = 0
    end_idx = len(nums)-1
    while start_idx <= end_idx:
        mid_idx = (start_idx+end_idx) // 2
        if target < nums[mid_idx]:
            end_idx = mid_idx-1
        elif target == nums[mid_idx]:
            return mid_idx
        elif target > nums[mid_idx]:
            start_idx = mid_idx+1
    return "Sought number is not present in the list."
sorted_numbers = [int(n) for n in input().split()]
sought_number = int(input())
print(binary_search(sorted_numbers, sought_number))


# # INPUT0:
# -1 0 1 2 4
# 4
# # OUTPUT0:
# 4  # Index of 4 is 4


# def binary_search(nums: list, target: int):
#     left = 0
#     right = len(nums)-1
#     while left <= right:
#         mid_idx = (left+right)//2
#         if nums[mid_idx] == target:
#             return mid_idx
#         elif nums[mid_idx] < target:
#             left = mid_idx+1  # +1 just to skip the middle element,cuz we already saw it
#         else:  # nums[mid_idx] > target:
#             right = mid_idx-1  # -1, we are not checking the middle element
#     return -1
#
# sorted_numbers = [int(n) for n in input().split()]
# sought_number = int(input())
# print(binary_search(sorted_numbers, sought_number))


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


# # WRONG:
# def binary_search(nums: list, target: int):
#     start_idx = 0
#     end_idx = len(nums)
#     current_nums = nums[start_idx:end_idx]
#     while True:
#         current_nums = current_nums[start_idx:end_idx]
#         mid_idx = len(current_nums) // 2
#         if target < nums[mid_idx]:
#             start_idx = 0
#             end_idx = mid_idx
#         elif target == current_nums[mid_idx]:
#             # return f"Index of {target} is {mid_idx}"
#             return mid_idx  # THIS FINDS THE RIGHT NUMBER BUT DOESN"T GIVE THE RIGHT INDEX
#             # cuz its should give the index in nums ,NOT in current_nums,
#             # it creates a relative index that changes according to the changing current_nums list
#         elif target >= nums[mid_idx]:
#             start_idx = mid_idx
#             end_idx = len(current_nums)
# sorted_numbers = [int(n) for n in input().split()]
# sought_number = int(input())
# print(binary_search(sorted_numbers, sought_number))