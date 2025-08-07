from collections import deque

def connected_components(graph):
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            component = []
            queue = deque([node])
            while queue:
                curr = queue.popleft()
                if curr not in visited:
                    visited.add(curr)
                    component.append(curr)
                    queue.extend(n for n in graph[curr] if n not in visited)
            components.append(component)

    return components

graph = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B'],
    'D': ['E'],
    'E': ['D'],
    'F': [],
    'G': ['H'],
    'H': ['G']
}

print(connected_components(graph))