nums = [int(n) for n in input().split()]
for i in range(1, len(nums)):
    for e in range(i, 0, -1):
        if nums[e-1] > nums[e]:
            nums[e-1], nums[e] = nums[e], nums[e-1]
        else:
            break
print(*nums, sep=" ")


# # INPUT0:
# 5 4 3 2 1
# # OUTPUT0:
# 1 2 3 4 5


# # INPUT1:
# 13 93 37 74 61 65 5 55 17 96 52 70 17 7 89 65 16 38 42 15 86 21 93 10 31 28 36 14 65 7 68 86 97 34 27 32 86 44 51 75 29 64 0 36 33 54 20 40 60 56 51 51 25 77 75 46 47 57 18 12 27 28 29 21 22 37 74 78 34 15 71 75 20 19 76 48 98 36 76 49 83 21 44 12 85 68 24 9 80 41 66 1 54 31 55 33 88 35 32 43
# # OUTPUT1:
# 0 1 5 7 7 9 10 12 12 13 14 15 15 16 17 17 18 19 20 20 21 21 21 22 24 25 27 27 28 28 29 29 31 31 32 32 33 33 34 34 35 36 36 36 37 37 38 40 41 42 43 44 44 46 47 48 49 51 51 51 52 54 54 55 55 56 57 60 61 64 65 65 65 66 68 68 70 71 74 74 75 75 75 76 76 77 78 80 83 85 86 86 86 88 89 93 93 96 97 98


# # AS FUNC:
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         e = i - 1
#         while e >= 0 and key < arr[e]:
#             arr[e + 1] = arr[e]
#             e -= 1
#         arr[e + 1] = key
# my_list = [64, 25, 12, 22, 11]
# insertion_sort(my_list)
# print("Sorted array:", my_list)


# # WITH 'e+1'
# nums = [int(n) for n in input().split()]
# for i in range(0, len(nums)-1):  # -1 za da ne izliza 'idx out of range' pri 'nums[e+1]'
#     for e in range(i, -1, -1):  # 'i' e purvo 0, zatva 'end'=-1 ,'step'=-1
#         if nums[e] > nums[e+1]:
#             nums[e], nums[e+1] = nums[e+1], nums[e]
#             # nums[e+1], nums[e] = nums[e], nums[e+1]  # NEMA RAZLIKA
#         else:
#             break
# print(*nums, sep=' ')


# # WITH WHILE LOOP:
# nums = [int(n) for n in input().split()]
# for i in range(1, len(nums)):
#     e = i
#     while nums[e-1] > nums[e] and 0 < e:
#         nums[e-1], nums[e] = nums[e], nums[e-1]
#         e -= 1
# print(*nums, sep=' ')


# # WHILE loop with [e+1]:
# def insertion_sort(nums: list):
#     for i in range(1, len(nums)):
#         key = nums[i]
#         e = i - 1
#         while e >= 0 and key < nums[e]:
#             nums[e+1] = nums[e]
#             e -= 1
#         nums[e+1] = key
# numbers = [12, 11, 13, 5, 6]
# insertion_sort(numbers)
# print("Sorted array:", numbers)  # Sorted array: [5, 6, 11, 12, 13]
