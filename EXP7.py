def graph_coloring(adj_matrix, num_colors):
    n = len(adj_matrix)
    colors = [0] * n
    solutions = []

    def next_value(k):
        while True:
            colors[k] = (colors[k] + 1) % (num_colors + 1)
            if colors[k] == 0:
                return
            for j in range(n):
                if adj_matrix[k][j] == 1 and colors[k] == colors[j]:
                    break
            else:
                return

    def graph_coloring_util(k):
        while True:
            next_value(k)
            if colors[k] == 0:
                return
            if k == n - 1:
                solutions.append(colors[:])
            else:
                graph_coloring_util(k + 1)

    graph_coloring_util(0)
    return solutions

# Example usage:
n = int(input("Enter the number of vertices: "))
adj_matrix = []

print("Enter the adjacency matrix of the graph (1 for connected, 0 for not connected):")
for _ in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)

num_colors = int(input("Enter the number of colors: "))
solutions = graph_coloring(adj_matrix, num_colors)

if solutions:
    print("Possible colorings of the graph without adjacent vertices having the same color:")
    for solution in solutions:
        print(solution)
else:
    print("No valid colorings found.")
