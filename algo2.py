from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)

    # Step 1: Fill stack according to finish time
    def fill_order(self, v, visited, stack):
        visited.add(v)
        for neighbour in sorted(self.graph[v]):
            if neighbour not in visited:
                self.fill_order(neighbour, visited, stack)
        stack.append(v)

    # Step 2: Transpose graph
    def transpose(self):
        g = Graph()
        for u in self.graph:
            for v in self.graph[u]:
                g.add_edge(v, u)
        return g

    # Step 3: DFS for SCC
    def dfs_scc(self, v, visited, component):
        visited.add(v)
        component.append(v)
        for neighbour in sorted(self.graph[v]):
            if neighbour not in visited:
                self.dfs_scc(neighbour, visited, component)

    # Main function to find SCCs
    def find_sccs(self):
        stack = []
        visited = set()

        # Fill stack
        for vertex in sorted(self.vertices):
            if vertex not in visited:
                self.fill_order(vertex, visited, stack)

        # Transpose graph
        reversed_graph = self.transpose()

        visited.clear()
        scc_list = []

        # Process all vertices in order defined by Stack
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                component = []
                reversed_graph.dfs_scc(vertex, visited, component)
                scc_list.append(sorted(component))

        return scc_list


# ------------------------
# Construct Graph
# ------------------------
g = Graph()

edges = [
    ('a', 'b'),
    ('c', 'a'),
    ('b', 'c'),
    ('b', 'd'),
    ('c', 'e'),
    ('c', 'd'),
    ('d', 'e'),
    ('f', 'd'),
    ('e', 'f'),
    ('f', 'g'),
    ('g', 'e'),
    ('h', 'f'),
    ('g', 'h')
]

for u, v in edges:
    g.add_edge(u, v)

sccs = g.find_sccs()

# Output formatting
output_lines = []
output_lines.append("Strongly Connected Components (SCCs)")
output_lines.append("Using Kosaraju’s Algorithm\n")
output_lines.append("------------------------------------")

for i, scc in enumerate(sccs, 1):
    output_lines.append(f"SCC {i}: {{ " + ", ".join(scc) + " }}")

output_lines.append("\nTime Complexity: O(V + E)")

# Save to file
with open("scc_results.txt", "w") as f:
    for line in output_lines:
        f.write(line + "\n")

# Display
for line in output_lines:
    print(line)