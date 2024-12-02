from collections import deque, defaultdict

def input_graph():
    # 정점 입력
    vertex = input("vertex (예: A, B, C, D, E, F, G, H): ").strip().split(",")
    # 간선 입력
    edges = input("edge (예: A-B, A-C, B-D, ...): ").strip().split(", ")
    
    # 인접 리스트 초기화
    adjacency_list = defaultdict(list)
    
    # 간선 정보를 기반으로 인접 리스트 구성
    for edge in edges:
        u, v = edge.split("-")
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)  # 무향 그래프이므로 양쪽 모두 추가

    return vertex, adjacency_list

def dfs(vertex, adjacency_list, start, visited, result):
    visited.add(start)
    result.append(start)
    for neighbor in sorted(adjacency_list[start]):
        if neighbor not in visited:
            dfs(vertex, adjacency_list, neighbor, visited, result)

def bfs(vertex, adjacency_list, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []

    while queue:
        current = queue.popleft()
        result.append(current)
        for neighbor in sorted(adjacency_list[current]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result

def connected_components(vertex, adjacency_list):
    visited = set()
    components = []

    for v in vertex:
        if v not in visited:
            component = []
            queue = deque([v])
            visited.add(v)

            while queue:
                current = queue.popleft()
                component.append(current)
                for neighbor in adjacency_list[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            components.append(component)

    return components

def spanning_tree(vertex, adjacency_list, start):
    visited = set()
    tree_edges = []
    queue = deque([start])
    visited.add(start)

    while queue:
        current = queue.popleft()
        for neighbor in sorted(adjacency_list[current]):
            if neighbor not in visited:
                visited.add(neighbor)
                tree_edges.append((current, neighbor))
                queue.append(neighbor)

    return tree_edges

if __name__ == "__main__":
    vertex, adjacency_list = input_graph()

    # DFS
    dfs_result = []
    dfs(vertex, adjacency_list, vertex[0], set(), dfs_result)
    print("DFS:", " - ".join(dfs_result))

    # BFS
    bfs_result = bfs(vertex, adjacency_list, vertex[0])
    print("BFS:", " - ".join(bfs_result))

    # Connected Components
    components = connected_components(vertex, adjacency_list)
    print("Connected Components:")
    for i, component in enumerate(components):
        print(f"Component {i + 1}: " + " - ".join(component))

    # Spanning Tree
    spanning_edges = spanning_tree(vertex, adjacency_list, vertex[0])
    print("Spanning Tree Edges:")
    if spanning_edges:
        for u, v in spanning_edges:
            print(f"{u} - {v}")
    else:
        print("No edges in the spanning tree.")
