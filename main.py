import time
from algorithms import prim, kruskal
import generate_graph as gg
from tabulate import tabulate


def measure_time(graph, algorithm):
    start_time = time.time()
    if algorithm == 'prim':
        mst_cost, edges_in_mst = prim(graph)
    elif algorithm == 'kruskal':
        mst_cost, edges_in_mst = kruskal(graph)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time, mst_cost, edges_in_mst


def test_increasing_edges(num_nodes, max_weight=10):
    results = []
    for num_edges in range(num_nodes - 1, num_nodes * (num_nodes - 1) // 2, num_nodes):
        graph = gg.random_graph_with_edges(num_nodes, num_edges, max_weight)
        time_prim, _, _ = measure_time(graph, 'prim')
        time_kruskal, _, _ = measure_time(graph, 'kruskal')
        results.append((num_edges, time_prim, time_kruskal))
    return results


def test_positive_vs_negative_weights(num_nodes, num_edges, max_weight=10):
    graph_positive = gg.random_graph_with_edges(num_nodes, num_edges, max_weight, allow_negative_weights=False)
    graph_negative = gg.random_graph_with_edges(num_nodes, num_edges, max_weight, allow_negative_weights=True)

    time_prim_positive, _, _ = measure_time(graph_positive, 'prim')
    time_kruskal_positive, _, _ = measure_time(graph_positive, 'kruskal')

    time_prim_negative, _, _ = measure_time(graph_negative, 'prim')
    time_kruskal_negative, _, _ = measure_time(graph_negative, 'kruskal')

    return {
        'positive': (time_prim_positive, time_kruskal_positive),
        'negative': (time_prim_negative, time_kruskal_negative)
    }


def test_multiple_connected_components(num_nodes, num_components, max_weight=10):
    component_size = num_nodes // num_components
    graphs = [gg.random_connected_graph(component_size, max_weight) for _ in range(num_components)]

    total_time_prim = 0
    for graph in graphs:
        time_prim, _, _ = measure_time(graph, 'prim')
        total_time_prim += time_prim

    # Merging all components into a single graph
    full_graph = []
    offset = 0
    for graph in graphs:
        for i, edges in enumerate(graph):
            full_graph.append([(v + offset, w) for v, w in edges])
        offset += component_size

    time_kruskal, _, _ = measure_time(full_graph, 'kruskal')

    return total_time_prim, time_kruskal


# Example usage:
num_nodes = 50
results_increasing_edges = test_increasing_edges(num_nodes)
results_positive_vs_negative = test_positive_vs_negative_weights(num_nodes, num_nodes * 2)
results_multiple_components = test_multiple_connected_components(num_nodes, 5)

# Printing results in tabular format using tabulate
headers_increasing_edges = ["Number of Edges", "Prim Time (s)", "Kruskal Time (s)"]
table_increasing_edges = [list(result) for result in results_increasing_edges]
print("\nTempo impiegato all’aumentare del numero di archi:")
print(tabulate(table_increasing_edges, headers=headers_increasing_edges, tablefmt="pretty"))

headers_positive_vs_negative = ["Graph Type", "Prim Time (s)", "Kruskal Time (s)"]
table_positive_vs_negative = [
    ["Positive Weights", results_positive_vs_negative['positive'][0], results_positive_vs_negative['positive'][1]],
    ["Negative Weights", results_positive_vs_negative['negative'][0], results_positive_vs_negative['negative'][1]],
]
print("\nTempo impiegato con pesi positivi vs negativi:")
print(tabulate(table_positive_vs_negative, headers=headers_positive_vs_negative, tablefmt="pretty"))

headers_multiple_components = ["Component", "Time (s)"]
table_multiple_components = [
    ["Prim (Total)", results_multiple_components[0]],
    ["Kruskal", results_multiple_components[1]]
]
print("\nTempo impiegato con più componenti connesse:")
print(tabulate(table_multiple_components, headers=headers_multiple_components, tablefmt="pretty"))
