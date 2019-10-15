# Quadruple Sum to Target (medium)
# https://www.educative.io/courses/grokking-the-coding-interview/gxDOJJ7xAJl
# 
# Given an array of unsorted numbers and a target number, 
# find all unique quadruplets in it, whose sum is equal to the target number.

def search_pairs(arr, target, low, c, d, quadruplets):
    high = len(arr) - 1

    while low < high:
        curr = arr[low] + arr[high]
        if curr == target:
            quadruplets.append([arr[low], arr[high], c, d])
            low += 1
            high -= 1

            while low < high and arr[low] == arr[low - 1]:
                low += 1

            while low < high and arr[high] == arr[high + 1]:
                high -= 1
        elif curr < target:
            low += 1
        else:
            high -= 1

def search_quadruplets(arr, target):
    arr = sorted(arr)

    quadruplets = []
    for i in range(len(arr)):
        # Skip duplicates
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        for j in range(i + 1, len(arr)):
            # Skip duplicates
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue

            search_pairs(arr, target - arr[i] - arr[j],
                        j + 1, arr[i], arr[j], quadruplets)

    return quadruplets

def pprint(quads):
    for arr in quads:
        print(str(arr).ljust(15), ":", sum(arr))


pprint(search_quadruplets([4, 1, 2, -1, 1, -3], target=-1))
