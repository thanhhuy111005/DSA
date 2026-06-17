import sys

# --- Định nghĩa lớp Graph để xử lý thuật toán ---
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.vertex_map = {}
        self.reverse_map = {}

    def set_vertex_labels(self, labels):
        for i, label in enumerate(labels):
            self.vertex_map[label] = i
            self.reverse_map[i] = label

    def add_edge_by_label(self, u_label, v_label, weight):
        u = self.vertex_map[u_label]
        v = self.vertex_map[v_label]
        self.graph[u][v] = weight

    def print_matrix(self):
        print("[")
        for row in self.graph:
            print(f"  {row},")
        print("]")

    def dijkstra(self, src_label, dest_label=None):
        src = self.vertex_map[src_label]
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        parent = [-1] * self.V
        sptSet = [False] * self.V

        for _ in range(self.V):
            min_dist = sys.maxsize
            u = -1
            for v in range(self.V):
                if dist[v] < min_dist and not sptSet[v]:
                    min_dist = dist[v]
                    u = v
            
            if u == -1:
                break
                
            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not sptSet[v]:
                    if dist[u] + self.graph[u][v] < dist[v]:
                        dist[v] = dist[u] + self.graph[u][v]
                        parent[v] = u

        if dest_label:
            dest = self.vertex_map[dest_label]
            if dist[dest] == sys.maxsize:
                print(f"Không có đường đi từ {src_label} đến {dest_label}")
                return
            
            path = []
            curr = dest
            while curr != -1:
                path.append(self.reverse_map[curr])
                curr = parent[curr]
            path.reverse()
            
            print(f"Đường đi ngắn nhất từ {src_label} đến {dest_label}: {' -> '.join(path)}")
            print(f"  > Tổng trọng số (độ dài): {dist[dest]}")

# --- Chương trình chính cho Bài Thực hành 03 ---
print("--- Thực hành 03 ---")
vertices_03 = ['a', 'b', 'c', 'f', 'g', 'z']
g3 = Graph(len(vertices_03))
g3.set_vertex_labels(vertices_03)

# Thêm các cạnh theo Hình 1
g3.add_edge_by_label('a', 'b', 3)
g3.add_edge_by_label('a', 'f', 1)
g3.add_edge_by_label('b', 'c', 7)
g3.add_edge_by_label('f', 'c', 9)
g3.add_edge_by_label('f', 'g', 2)
g3.add_edge_by_label('g', 'c', 3)
g3.add_edge_by_label('g', 'z', 7)
g3.add_edge_by_label('c', 'z', 3)

print("a) Ma trận kề từ đồ thị có hướng:")
g3.print_matrix()

print("\nb) Tìm đường đi ngắn nhất:")
g3.dijkstra('a', 'z')