def find_index_element_match(arr):

    def binary_search(lo, hi):
        print(f"lo={lo}, hi={hi}")

        if (hi >= lo):
            mid = (lo + hi) // 2

            if (mid + 1) < arr[mid]:
                return binary_search(lo=lo, hi=mid - 1)
            elif (mid + 1) > arr[mid]:
                return binary_search(lo=mid + 1, hi=hi)
            else:
                return binary_search(lo=mid + 1, hi=hi) or (mid + 1)
        
        return None

    return binary_search(lo=0, hi=len(arr) - 1)


print(find_index_element_match([-10, -3, 3, 5, 7]))
print("==============================================")
print(find_index_element_match([2, 3, 4, 5, 6, 7]))
print("==============================================")
print(find_index_element_match([-5, -3, -2, 3, 5, 6]))
print("==============================================")
print(find_index_element_match([x + 1 for x in range(200)]))
