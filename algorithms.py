import heapq


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def prim(graph):
    # Numero di nodi nel grafo
    n = len(graph)

    # Array per tracciare se un nodo è incluso nell'MST
    in_mst = [False] * n

    # Min-heap per selezionare l'arco con il peso minimo
    min_heap = [(0, 0)]  # (peso, nodo)

    mst_cost = 0  # Costo totale del MST
    edges_in_mst = []  # Archi inclusi nell'MST

    while min_heap:
        weight, u = heapq.heappop(min_heap)

        # Se il nodo è già incluso nel MST, continuiamo
        if in_mst[u]:
            continue

        # Aggiungiamo il costo dell'arco al costo totale del MST
        mst_cost += weight
        in_mst[u] = True

        # Aggiungiamo l'arco alla lista degli archi dell'MST
        if weight != 0:
            edges_in_mst.append((u, weight))

        # Esaminiamo tutti i vicini del nodo corrente
        for v, w in graph[u]:
            if not in_mst[v]:
                heapq.heappush(min_heap, (w, v))

    return mst_cost, edges_in_mst


def kruskal(graph):
    num_nodes = len(graph)
    disjoint_set = DisjointSet(num_nodes)
    mst_cost = 0
    edges_in_mst = []
    edges = []

    # Convertiamo la lista di adiacenza in una lista di archi
    for u in range(num_nodes):
        for v, weight in graph[u]:
            if u < v:  # Per evitare duplicati (in grafi non orientati)
                edges.append((weight, u, v))

    # Ordiniamo gli archi in base al peso
    edges.sort()

    for weight, u, v in edges:
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst_cost += weight
            edges_in_mst.append((u, v, weight))

    return mst_cost, edges_in_mst
