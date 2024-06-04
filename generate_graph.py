import random


# restituisce una lista di adiacenza rappresentante un grafo con num_nodes nodi e archi casuali di peso casuale
def random_connected_graph(num_nodes, max_weight=10):
    if num_nodes <= 1:
        return []

    graph = [[] for _ in range(num_nodes)]
    edges = set()

    # Creiamo un albero di base per garantire che il grafo sia connesso
    for i in range(num_nodes - 1):
        weight = random.randint(1, max_weight)
        graph[i].append((i + 1, weight))
        graph[i + 1].append((i, weight))
        edges.add((min(i, i + 1), max(i, i + 1)))

    # Aggiungiamo ulteriori archi casuali per aumentare la complessità del grafo
    additional_edges = num_nodes * 2  # Arbitrario, possiamo aggiungere più o meno archi
    while len(edges) < num_nodes - 1 + additional_edges:
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        if u != v:
            edge = (min(u, v), max(u, v))
            if edge not in edges:
                weight = random.randint(1, max_weight)
                graph[u].append((v, weight))
                graph[v].append((u, weight))
                edges.add(edge)

    return graph
