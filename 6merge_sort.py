def merge_sort(nums: list):
    if len(nums) == 1:
        return nums
    mid = len(nums)//2
    return merge_arrs(merge_sort(nums[:mid]), merge_sort(nums[mid:]))


def merge_arrs(left, right):
    new_array = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            new_array.append(left[left_idx])
            left_idx += 1
        else:
            new_array.append(right[right_idx])
            right_idx += 1

    while left_idx < len(left):  # if any elements are left in 'left'
        new_array.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):  # if any elements are left in 'right'
        new_array.append(right[right_idx])
        right_idx += 1

    return new_array


numbers = [int(n) for n in input().split()]
print(*merge_sort(numbers), sep=' ')


# DVOINATA RECURSIQ ZADULBAVA TAKA:
# ako nums = [5, 4, 3, 2, 1] >>> [5, 4] | [3, 2, 1] >>> [5] | [4] i podava tezi dvete kato 'left' i 'right' na merge_arrs([4], [5])
# sled tva se izvurta merge_arrs([4], [5])
# vrushta se na nums = [3, 2, 1] >>> merge_sort([3, 2, 1]) >>> [3] | [2, 1] >>> [2] | [1] >>> podava merge_arrs([2], [1])
# izvurta merge_arrs([2], [1]) i gi podrejda v spisuche [1, 2] koeto podava na merge_arrs() otnovo kato right
# ,a left e [3]
# puska merge_arrs([3], [1, 2]) >>> [1, 2, 3]
# puska merge_arrs([4, 5], [1, 2, 3]) >>> [1, 2, 3, 4, 5]


# def merge_sort(nums):
#     if len(nums) == 1:
#         return nums
#
#     middle = len(nums) // 2
#     return merge_arrs(merge_sort(nums[:middle]), merge_sort(nums[middle:]))
#
#
# numbers = [int(x) for x in input().split()]
# sorted_array = merge_sort(numbers)
# print(*sorted_array)