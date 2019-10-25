def is_overlap(a, b):
    start = max(a[0], b[0])
    end = min(a[1], b[1])

    return end - start >= 0


def get_max_interval(a, b):
    start = min(a[0], b[0])
    end = max(a[1], b[1])

    return [start, end]


def insert(intervals, new_interval):
    if len(intervals) == 0:
        return []

    merged = []

    start = 0

    while start < len(intervals) and intervals[start][1] < new_interval[0]:
        merged.append(intervals[start])
        start += 1

    merged.append(new_interval)

    for i in range(start, len(intervals)):
        curr = intervals[i]

        if is_overlap(curr, merged[-1]):
            merged[-1] = get_max_interval(curr, merged[-1])
        else:
            merged.append(curr)

    return merged


def main():
    print("Intervals after inserting the new interval: " +
          str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " +
          str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " +
          str(insert([[2, 3], [5, 7]], [1, 4])))


main()
