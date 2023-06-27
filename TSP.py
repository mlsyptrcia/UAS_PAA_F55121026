import time
import networkx as nx

def tsp(graph):
    start_time = time.time()

    num_nodes = len(graph.nodes)
    shortest_path = None
    shortest_distance = float('inf')

    all_paths = list(nx.permutations(graph.nodes))

    for path in all_paths:
        distance = 0
        for i in range(num_nodes - 1):
            distance += graph[path[i]][path[i+1]]['weight']

        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = path

        print(f"Path: {path} | Distance: {distance}")

    end_time = time.time()
    execution_time = end_time - start_time

    return shortest_path, shortest_distance, execution_time

def dijkstra(graph, start_node):
    start_time = time.time()

    shortest_path = {}
    shortest_distance = {}
    unvisited_nodes = set(graph.nodes)

    for node in graph.nodes:
        shortest_distance[node] = float('inf')

    shortest_distance[start_node] = 0

    while unvisited_nodes:
        current_node = None
        for node in unvisited_nodes:
            if current_node is None or shortest_distance[node] < shortest_distance[current_node]:
                current_node = node

        unvisited_nodes.remove(current_node)

        for neighbor in graph.neighbors(current_node):
            distance = shortest_distance[current_node] + graph[current_node][neighbor]['weight']

            if distance < shortest_distance[neighbor]:
                shortest_distance[neighbor] = distance
                shortest_path[neighbor] = current_node

        print(f"Node: {current_node} | Distance: {shortest_distance[current_node]}")

    end_time = time.time()
    execution_time = end_time - start_time

    return shortest_path, shortest_distance, execution_time

def main():
    graph = nx.Graph()
    graph.add_edge('A', 'B', weight=1)
    graph.add_edge('A', 'C', weight=4)
    graph.add_edge('A', 'D', weight=2)
    graph.add_edge('B', 'C', weight=3)
    graph.add_edge('B', 'D', weight=2)
    graph.add_edge('C', 'D', weight=1)

    print("Graph:")
    print(graph.edges(data=True))

    while True:
        choice = input("\nPilih algoritma (TSP / Dijkstra): ").lower()

        if choice == "tsp":
            shortest_path, shortest_distance, execution_time = tsp(graph)
            break
        elif choice == "dijkstra":
            start_node = input("Masukkan node awal: ")
            shortest_path, shortest_distance, execution_time = dijkstra(graph, start_node)
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

    print("\nShortest Path:", shortest_path)
    print("Shortest Distance:", shortest_distance)
    print("Waktu komputasi:", execution_time, "detik")

if __name__ == "__main__":
    main()
