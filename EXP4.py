def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1


def prims(adj_matrix, start):
    n = len(adj_matrix)
    visited = [False] * n
    min_weight = [float('inf')] * n
    min_weight[start] = 0
    parent = [-1] * n
    total_weight = 0

    for _ in range(n):
        min_vertex = -1
        for v in range(n):
            if not visited[v] and (min_vertex == -1 or min_weight[v] < min_weight[min_vertex]):
                min_vertex = v

        visited[min_vertex] = True
        total_weight += min_weight[min_vertex]

        for v in range(n):
            if adj_matrix[min_vertex][v] != 0 and not visited[v] and adj_matrix[min_vertex][v] < min_weight[v]:
                min_weight[v] = adj_matrix[min_vertex][v]
                parent[v] = min_vertex

    print("Edges of the Minimum Spanning Tree (Prim's Algorithm):")
    for v in range(n):
        if v != start:
            print(f"{parent[v]} - {v} : Weight {min_weight[v]}")
    print("Total weight of the Minimum Spanning Tree:", total_weight)


def kruskals(adj_matrix):
    n = len(adj_matrix)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if adj_matrix[i][j] != 0:
                edges.append((i, j, adj_matrix[i][j]))

    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    rank = [0] * n
    total_weight = 0

    print("Edges of the Minimum Spanning Tree (Kruskal's Algorithm):")
    for edge in edges:
        u, v, weight = edge
        if find(parent, u) != find(parent, v):
            print(f"{u} - {v} : Weight {weight}")
            union(parent, rank, u, v)
            total_weight += weight

    print("Total weight of the Minimum Spanning Tree:", total_weight)


# Example usage:
n = int(input("Enter the number of vertices in the graph: "))
print("Enter the Weighted Matrix row by row (space-separated):")
adj_matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)

start_vertex = int(input("Enter the starting vertex for Prim's algorithm: "))
prims(adj_matrix, start_vertex)
print()
kruskals(adj_matrix)