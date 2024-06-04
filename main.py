
import time
from algorithms import prim, kruskal
import generate_graph as gg

# Esempio di grafo rappresentato come lista di adiacenza
# (nodo, peso) per ogni arco uscente dal nodo corrente
# graph = [
#     [(1, 2), (3, 6)], # il nodo 0 è collegato al nodo 1 con peso 2 e al nodo 3 con peso 6
#     [(0, 2), (2, 3), (3, 8), (4, 5)],
#     [(1, 3), (4, 7)],
#     [(0, 6), (1, 8)],
#     [(1, 5), (2, 7)]
# ]

num_nodes = 50
# generazione randomica del grafo per test secondi su larga scala
graph = gg.random_connected_graph(num_nodes)

# Misura del tempo di esecuzione dell'algoritmo di Prim
start_time = time.time()
mst_cost_prim, edges_in_mst_prim = prim(graph)
end_time = time.time()
execution_time_prim = end_time - start_time

print("Algoritmo di Prim")
print("Costo totale del MST:", mst_cost_prim)
print("Archi nell'MST:", edges_in_mst_prim)
print("Tempo di esecuzione:", execution_time_prim, "secondi")

# Misura del tempo di esecuzione dell'algoritmo di Kruskal
start_time = time.time()
mst_cost_kruskal, edges_in_mst_kruskal = kruskal(graph)
end_time = time.time()
execution_time_kruskal = end_time - start_time

print("\nAlgoritmo di Kruskal")
print("Costo totale del MST:", mst_cost_kruskal)
print("Archi nell'MST:", edges_in_mst_kruskal)
print("Tempo di esecuzione:", execution_time_kruskal, "secondi")
