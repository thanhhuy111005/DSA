# Bài 13. DFS dùng ngăn xếp (khử đệ quy) [cite: 41, 42]
def bai13(graph, start):
    visited = set()
    stack = [start]
    order = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            stack.extend(reversed(graph[vertex]))
    return order

