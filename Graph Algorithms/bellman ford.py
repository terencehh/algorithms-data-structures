
# TAKEN FROM GITHUB - DO NOT USE FOR ASSIGNMENTS
# https://gist.github.com/ngenator/6178728

def bellman_ford(graph, source):
    # Step 1: Prepare the distance and predecessor for each node
    distance, predecessor = dict(), dict()
    for node in graph:
        distance[node], predecessor[node] = float('inf'), None
    distance[source] = 0

    # Step 2: Relax the edges
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour in graph[node]:
                # If the distance between the node and the neighbour is lower than the current, store it
                if distance[neighbour] > distance[node] + graph[node][neighbour]:
                    distance[neighbour], predecessor[neighbour] = distance[node] + graph[node][neighbour], node

    # Step 3: Check for negative weight cycles
    for node in graph:
        for neighbour in graph[node]:
            assert distance[neighbour] <= distance[node] + graph[node][neighbour], "Negative weight cycle."

    return distance, predecessor


if __name__ == '__main__':

    graph = {
            's': {'a': 5, 'b': 6},
            'a': {'c': -1},
            'b': {'a': 4, 'd': -10},
            'c': {'b': -2, 'd': 4, 'e': 3},
            'd': {'f': -6},
            'e': {'d': -5},
            'f': {'e': 10}
            }

    distance, predecessor = bellman_ford(graph, source='s')

    print(distance)



