# # MOITO(for some reason it works, but makes some excessive checks)
# def bubble_sort(nums: list):
#     for i in range(len(nums)):
#         for e in range(0, len(nums)):  # you don't need to check the last 'i' indexes because they have already 'bubbled up', been ordered
#             if nums[i] < nums[e]:
#                 nums[i], nums[e] = nums[e], nums[i]
#     return nums
# numbers = [int(n) for n in input().split()]
# print(*bubble_sort(numbers), sep=' ')


# # BEST WAY SO FAR:
nums = [int(x) for x in input().split()]
for i in range(len(nums)):
    for e in range(0, len(nums)-i-1):  # -i-1 is the optimization for not making unnecessary checks
        # -1 cuz you don't want 'nums[j+1]' to go out of range index-wise
        # -i is because the last 'i' elements int the list are ordered, they've BUBBLED UP
        if nums[e] > nums[e+1]:
            nums[e], nums[e+1] = nums[e+1], nums[e]
        print(*nums, sep=" ")
# print(*nums, sep=" ")


# # 2ND WAY:
# nums = [int(x) for x in input().split()]
# is_sorted = False
# counter = 0
# while not is_sorted:
#     is_sorted = True
#     for i in range(1, len(nums) - counter):
#         if nums[i] < nums[i - 1]:
#             nums[i], nums[i - 1] = nums[i - 1], nums[i]
#             is_sorted = False
#     counter += 1
# print(*nums, sep=" ")



# # Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them until they are in the intended order.
# # Just like the movement of air bubbles in the water that rise up to the surface, each element of the array move to the end in each iteration.
# # Therefore, it is called a bubble sort.
# # You can change > to < to sort in descending order.
# def bubble_sort(lst):
#     for i in range(len(lst)):
#         for j in range(len(lst) - 1 - i):
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#     return lst
# lst = [12, 1, 8, 17, 2]
# print(bubble_sort(lst))