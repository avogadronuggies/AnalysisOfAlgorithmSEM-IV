import time

def dijkstra(adj, n, start):
    INF = float('inf')
    dist = [INF] * n
    dist[start-1] = 0
    visited = set()
    paths = {v+1: [] for v in range(n)}
    for _ in range(n):
        min_dist = INF
        u = -1
        for v in range(n):
            if v+1 not in visited and dist[v] < min_dist:
                min_dist = dist[v]
                u = v
        visited.add(u+1)
        for v in range(n):
            if v+1 not in visited and adj[u][v] > 0:
                if dist[u] + adj[u][v] < dist[v]:
                    dist[v] = dist[u] + adj[u][v]
                    paths[v+1] = paths[u+1] + [u+1]
    return dist, paths
def print_paths(start, dist, paths):
    print("Shortest paths from vertex", start, "to other vertices:")
    print("V\tD\t\tPath")
    for v, path in paths.items():
        print(f" {v}\t {dist[v-1]}\t\t{path + [v]}")
def main():
    n = int(input("Enter the number of vertices: "))
    adj = []
    print("Enter the adjacency matrix (enter 0 for no connection):")
    for _ in range(n):
        row = list(map(int, input().split()))
        adj.append(row)
    start = int(input("Enter the start vertex:"))
    t1=time.time()
    result_dist, result_paths = dijkstra(adj, n, start)
    print_paths(start, result_dist, result_paths)
    t2=time.time()
    print("Time Taken:",(t2-t1)," seconds")
if __name__ == "__main__":
    main()
