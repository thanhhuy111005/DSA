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
            
            print(f"Đường đi ngắn nhất từ {src_label} đến {dest_label}: {' -> '.join(map(str, path))}")
            print(f"  > Tổng trọng số (độ dài): {dist[dest]}")

# --- Chương trình chính cho Bài Thực hành 04 ---
print("--- Thực hành 04 - Câu a ---")
# Khởi tạo đồ thị cho Hình 1 (8 đỉnh từ 0 đến 7)
vertices_04a = [0, 1, 2, 3, 4, 5, 6, 7]
g4a = Graph(len(vertices_04a))
g4a.set_vertex_labels(vertices_04a)

# Thêm các cạnh dựa vào mũi tên chỉ hướng (mặc định trọng số = 1 do hình không ghi số)
edges_04a = [
    (0, 1), (0, 3),
    (1, 2), (1, 5),
    (2, 7),
    (3, 4), (3, 5),
    (4, 6), (4, 7),
    (5, 6),
    (6, 2)
]
for u, v in edges_04a:
    g4a.add_edge_by_label(u, v, 1)

print("Ma trận kề từ đồ thị có hướng ở Hình 1:")
g4a.print_matrix()


print("\n--- Thực hành 04 - Câu b ---")
# Khởi tạo đồ thị cho Hình 2
vertices_04b = ['a', 'b', 'c', 'd', 'e', 'z']
g4b = Graph(len(vertices_04b))
g4b.set_vertex_labels(vertices_04b)

# Thêm cạnh và trọng số tương ứng từ Hình 2
g4b.add_edge_by_label('a', 'b', 2)
g4b.add_edge_by_label('a', 'd', 5)
g4b.add_edge_by_label('b', 'c', 7)
g4b.add_edge_by_label('b', 'e', 1)
g4b.add_edge_by_label('d', 'e', 6)
g4b.add_edge_by_label('e', 'c', 3)
g4b.add_edge_by_label('e', 'z', 2)
g4b.add_edge_by_label('c', 'z', 1)

g4b.dijkstra('a', 'z')