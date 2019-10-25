def is_overlap(a, b):
    start = max(a[0], b[0])
    end = min(a[1], b[1])

    return end - start >= 0

def get_max_interval(a, b):
    start = min(a[0], b[0])
    end = max(a[1], b[1])

    return [start, end]

def get_min_interval(a, b):
    start = max(a[0], b[0])
    end = min(a[1], b[1])

    return [start, end]

def is_ahead(a, b):
    return a[0] > b[1]


def merge(intervals_a, intervals_b):
    result = []

    a = 0
    b = 0

    while a < len(intervals_a) and b < len(intervals_b):
        int_a = intervals_a[a]
        int_b = intervals_b[b]

        if is_overlap(int_a, int_b):
            result.append(get_min_interval(int_a, int_b))

        if is_ahead(int_a, int_b):
            b += 1
        else:
            a += 1
    
    return result


def main():
    print("Intervals Intersection: " +
          str(merge([[1, 3], [5, 6], [7, 9]], 
                    [[2, 3], [5, 7]])))

    print("Intervals Intersection: " +
          str(merge([[1, 3], [5, 7], [9, 12]], 
                    [[5, 10]])))


main()
