from collections import deque

def topological_sort(vertices, edges):
    if vertices == 0:
        return []

    sortedOrder = []
    
    graph = {i : [] for i in range(vertices)}
    in_degrees = {i : 0 for i in range(vertices)}

    for edge in edges:
        in_node, out_node = edge

        graph[in_node].append(out_node)
        in_degrees[out_node] += 1

    q = deque()

    for node, degree in in_degrees.items():
        if degree == 0:
            q.append(node)

    while q:
        curr = q.popleft()
        sortedOrder.append(curr)

        for to_node in graph[curr]:
            in_degrees[to_node] -= 1
            
            if in_degrees[to_node] == 0:
                q.append(to_node)

    if len(sortedOrder) != vertices:
        print("Cycle detected!")
        return []

    return sortedOrder


def main():
    print("Topological sort: " +
          str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
          str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
          str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))

    # With cycle
    print("Topological sort: " +
          str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [0, 3]])))


main()
