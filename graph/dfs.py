def dfs(graph, start, visited=None):
    if visited == None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

# Basic undirected graph represented as adjacency dict of lists
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C'],
    'F': []  # isolated node
}

print(dfs(graph, 'B'))