import sys

# --- BẮT ĐẦU ĐOẠN ĐỊNH NGHĨA LỚP GRAPH (Phần bị thiếu trong file của bạn) ---
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        # Khởi tạo ma trận kề với toàn bộ giá trị 0
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
        # Ánh xạ nhãn đỉnh
        self.vertex_map = {}
        self.reverse_map = {}

    def set_vertex_labels(self, labels):
        for i, label in enumerate(labels):
            self.vertex_map[label] = i
            self.reverse_map[i] = label

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

        if dest_label is not None:
            dest = self.vertex_map[dest_label]
            if dist[dest] == sys.maxsize:
                print(f"Không có đường đi từ {src_label} đến {dest_label}")
                return
            
            # Khôi phục đường đi ngắn nhất
            path = []
            curr = dest
            while curr != -1:
                path.append(self.reverse_map[curr])
                curr = parent[curr]
            path.reverse()
            
            print(f"Đường đi ngắn nhất từ {src_label} đến {dest_label}: {' -> '.join(map(str, path))}")
            print(f"  > Tổng trọng số (độ dài): {dist[dest]}")
# --- KẾT THÚC ĐOẠN ĐỊNH NGHĨA LỚP GRAPH ---


# Khởi tạo đồ thị có 6 đỉnh (0 đến 5)
g = Graph(6)
g.graph = [
    [0, 3, 0, 4, 0, 0],
    [0, 0, 6, 2, 0, 0],
    [0, 0, 0, 0, 4, 3],
    [0, 0, 1, 0, 4, 0],
    [0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0]
]

# Tạo ánh xạ nhãn số tương ứng
labels = [0, 1, 2, 3, 4, 5]
g.set_vertex_labels(labels)

print("--- Thực hành 02 ---")
# Tìm đường đi ngắn nhất từ đỉnh 0 đến tất cả các đỉnh khác
for i in range(1, 6):
    g.dijkstra(0, i)