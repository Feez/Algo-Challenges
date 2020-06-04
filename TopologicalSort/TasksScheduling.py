from collections import deque

def is_scheduling_possible(tasks, prerequisites):
    nodes = [[] for task_index in range(tasks)]
    in_degree = [0 for task_index in range(tasks)]

    for from_node, to_node in prerequisites:
        nodes[from_node].append(to_node)
        in_degree[to_node] += 1

    q = deque()

    for node_index in range(tasks):
        if in_degree[node_index] == 0:
            q.append(node_index)

    while q:
        curr_node = q.popleft()

        for connected_node in nodes[curr_node]:
            in_degree[connected_node] -= 1

            if in_degree[connected_node] == 0:
                q.append(connected_node)

    return sum(in_degree) == 0



def main():
    print("Is scheduling possible: " +
          str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))


main()
