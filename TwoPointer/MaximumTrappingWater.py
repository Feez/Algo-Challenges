# Maximum Trapping Water (medium)
# https://www.educative.io/courses/grokking-the-coding-interview/m2OZVLm2oOR
# 
# Suppose you are given an array containing non-negative numbers representing heights of a set of buildings. 
# Because of differences in heights of buildings, water can be trapped between them. 
# 
# Find the two buildings that will trap the most amount of water. 
# Write a function that will return the maximum volume of water that will be 
# trapped between these two buildings.

# O(n^2)
def find_max_water_slow(building_heights):
    # formula = min(building1, building2) * spacing
    # [spacing] = building2_index - building1_index

    max_water = 0

    for i in range(len(building_heights)):
        for j in range(i + 1, len(building_heights)):
            shortest_building = min(building_heights[i], building_heights[j])
            max_water = max(max_water, shortest_building * (j - i))

    return max_water

# O(n)
def find_max_water(building_heights):
    max_water = 0

    left = 0
    right = len(building_heights) - 1

    while left < right:
        shortest_building = min(building_heights[left], building_heights[right])
        max_water = max(max_water, shortest_building * (right - left))

        if building_heights[left] < building_heights[right]:
            left += 1
        else:
            right -= 1

    return max_water

print("Output:")
print(find_max_water([1, 3, 5, 4, 1]))
print(find_max_water([3, 2, 5, 4, 2]))
print(find_max_water([1, 4, 3, 2, 5, 8, 4]))

print("Expected:")
print(find_max_water_slow([1, 3, 5, 4, 1]))
print(find_max_water_slow([3, 2, 5, 4, 2]))
print(find_max_water_slow([1, 4, 3, 2, 5, 8, 4]))