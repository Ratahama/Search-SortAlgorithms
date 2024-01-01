def binary_recursive_search(nums: list, target: int, left, right):
    mid_idx = (left+right)//2
    mid_num = nums[mid_idx]
    if left > right:
        return -1  # This number doesn't exist
    if mid_num == target:
        return mid_idx
    if target < mid_num:
        right = mid_idx-1  # -1 to ski the mid_num too
    else:
        left = mid_idx+1
    return binary_recursive_search(nums, target, left, right)


numbers = [int(n) for n in input().split()]
num = int(input())
r = len(numbers)-1
print(binary_recursive_search(numbers, num, 0 , r))


# # INPUT0:
# -1 0 1 2 4
# 4
# # OUTPUT0:
# 4  # Index of 4 is 4


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