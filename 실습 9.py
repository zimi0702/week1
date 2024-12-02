INF = 9999

def printA(A):
    vsize = len(A)
    print("====================================")
    for i in range(vsize):
        for j in range(vsize):
            if (A[i][j] == INF):
                print(" INF ", end='')
            else:
                print(f"{A[i][j]:4d} ", end='')
        print("")

def reconstruct_path(path, start, end):
    if path[start][end] is None:
        return []
    intermediate = []
    while start != end:
        intermediate.append(start)
        start = path[start][end]
    intermediate.append(end)
    return intermediate

def shortest_path_floyd(vertex, adj):
    vsize = len(vertex)
    A = [row[:] for row in adj]  # 2차원 배열 복사
    
    # 경로 배열 초기화
    path = [[None if i != j else j for j in range(vsize)] for i in range(vsize)]

    for i in range(vsize):
        for j in range(vsize):
            if adj[i][j] != INF and i != j:
                path[i][j] = j  # i에서 j로 가는 직접 경로가 있을 경우

    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
                    path[i][j] = path[i][k]  # 경로 업데이트
        printA(A)  # 진행상황 출력용 

    return path, A  # 경로와 거리 배열 반환

if __name__ == "__main__":
    # Shortest Path를 위한 Weighted Graph
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    weight = [[0, 7, INF, INF, 3, 10, INF],
              [7, 0, 4, 10, 2, 6, INF],
              [INF, 4, 0, 2, INF, INF, INF],
              [INF, 10, 2, 0, 11, 9, 4],
              [3, 2, INF, 11, 0, 13, 5],
              [10, 6, INF, 9, 13, 0, INF],
              [INF, INF, INF, 4, 5, INF, 0]]

    print("Shortest Path By Floyd's Algorithm")
    path, distances = shortest_path_floyd(vertex, weight)

    start_vertex = input("Start Vertex: ").strip()
    end_vertex = input("End Vertex: ").strip()

    start_index = vertex.index(start_vertex)
    end_index = vertex.index(end_vertex)

    shortest_distance = distances[start_index][end_index]
    path_vertices = reconstruct_path(path, start_index, end_index)

    if path_vertices:
        path_str = " -> ".join(vertex[i] for i in path_vertices)
        print(f"최단 경로: {path_str}")
        print(f"최단 경로의 거리: {shortest_distance}")
    else:
        print("지정한 정점 사이에 경로가 없습니다.")
