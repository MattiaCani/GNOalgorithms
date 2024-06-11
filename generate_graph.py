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

# Nuova funzione per creare un grafo con un numero specificato di archi
def random_graph_with_edges(num_nodes, num_edges, max_weight=10, allow_negative_weights=False):
    if num_nodes <= 1 or num_edges < num_nodes - 1:
        raise ValueError("Numero di archi insufficiente per garantire un grafo connesso")

    graph = [[] for _ in range(num_nodes)]
    edges = set()

    # Funzione per generare peso casuale, positivo o negativo a seconda del parametro
    def generate_weight():
        if allow_negative_weights:
            return random.randint(-max_weight, max_weight)
        else:
            return random.randint(1, max_weight)

    # Creiamo un albero di base per garantire che il grafo sia connesso
    for i in range(num_nodes - 1):
        weight = generate_weight()
        graph[i].append((i + 1, weight))
        graph[i + 1].append((i, weight))
        edges.add((min(i, i + 1), max(i, i + 1)))

    # Aggiungiamo ulteriori archi casuali per raggiungere il numero desiderato di archi
    while len(edges) < num_edges:
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        if u != v:
            edge = (min(u, v), max(u, v))
            if edge not in edges:
                weight = generate_weight()
                graph[u].append((v, weight))
                graph[v].append((u, weight))
                edges.add(edge)

    return graph

# Esempio di utilizzo
# num_nodes = 5
# num_edges = 7
# max_weight = 10
# allow_negative_weights = True  # Cambiare a False per pesi solo positivi
# graph = random_graph_with_edges(num_nodes, num_edges, max_weight, allow_negative_weights)

# for i, edges in enumerate(graph):
#     print(f"Node {i}: {edges}")
