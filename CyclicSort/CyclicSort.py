def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        curr = (i + 1)

        if curr != nums[i]:
            val = nums[i] - 1
            nums[i], nums[val] = nums[val], nums[i]
        else:
            i += 1

    return nums


print(cyclic_sort([3, 2, 4, 5, 6, 1]))
