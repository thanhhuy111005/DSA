import heapq

graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [],
    'C': [('B', -10)]
}

dist = {'A':0, 'B':float('inf'), 'C':float('inf')}

pq = [(0,'A')]

while pq:
    d,u = heapq.heappop(pq)

    if d > dist[u]:
        continue

    for v,w in graph[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heapq.heappush(pq,(dist[v],v))

print(dist)