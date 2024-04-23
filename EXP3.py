import heapq
import time

def greedy(graph, start):
    vertices = len(graph)
    distance = [float('inf')] * vertices
    distance[start] = 0
    visited = [False] * vertices
    priority_queue = [(0, start)]
    path = [-1] * vertices

    while priority_queue:
        u = heapq.heappop(priority_queue)

        if visited[u]:
            continue

        visited[u] = True

        for v, weight in enumerate(graph[u]):
            if not visited[v] and weight != 0 and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                path[v] = u  # Update the parent vertex for reconstructing the path
                heapq.heappush(priority_queue, (distance[v], v))

    return distance, path

def print_path(source, target, path, distances):
    path_trace = []
    while target != -1:
        path_trace.append(target)
        target = path[target]

    path_trace.reverse()

    path_str = " -> ".join(str(vertex) for vertex in path_trace)
    return f"{source} -> {path_str}"

if __name__ == "__main__":
    vertices = int(input("Enter the number of vertices: "))

    print("Enter the weighted adjacency matrix (row-wise, separate values with spaces):")
    graph = [list(map(int, input().split())) for _ in range(vertices)]

    start_vertex = int(input("Enter the starting vertex: "))

    start_time = time.time()
    time.sleep(1)  # Introduce a delay using time.sleep(1) for demonstration purposes

    result, path = greedy(graph, start_vertex)

    output_vertices = ' '.join(map(str, range(vertices)))
    output_distances = ' '.join(map(str, result))
    output_paths = '\n'.join(print_path(start_vertex, i, path, result) for i in range(vertices))

    print(f'Vertices: {output_vertices}')
    print(f'Distances: {output_distances}')
    print(f'Path:')
    print(output_paths)

    end_time = time.time()

    print(f"\nTotal execution time: {end_time - start_time:.6f} seconds")