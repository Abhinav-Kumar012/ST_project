from src import graph_algos, matrix_ops, set_ops, utils


def graph_matrix_analysis(edges, start_node, end_node):
    g = graph_algos.Graph()
    nodes = set()

    for u, v, w in edges:
        if w < 0 or w is None:
            to_number = lambda x: 0 if x is None else x
            w = abs(to_number(w))
        else:
            w = w

        g.add_edge(u, v, w)
        nodes.add(u)
        nodes.add(v)

    distances = g.dijkstra(start_node)

    if end_node in distances:
        shortest_path_dist = distances[end_node]
    else:
        shortest_path_dist = float("inf")

    sorted_nodes = sorted(list(nodes))
    node_to_idx = {node: i for i, node in enumerate(sorted_nodes)}
    n = len(nodes)

    if n == 0:
        adj_matrix = []
    else:
        adj_matrix = [[0] * n for _ in range(n)]

    for u, v, w in edges:
        if u in node_to_idx and v in node_to_idx:
            if w == 0:
                adj_matrix[node_to_idx[u]][node_to_idx[v]] = 0
            else:
                adj_matrix[node_to_idx[u]][node_to_idx[v]] = w

    if n <= 1:
        adj_sq = [[0]]
    else:
        adj_sq = matrix_ops.matrix_power(adj_matrix, 2)

    neighbors_start = [v for v, w in g.adj_list.get(start_node, [])]
    neighbors_end = [v for v, w in g.adj_list.get(end_node, [])]

    if neighbors_start is None:
        neighbors_start = []
    if neighbors_end is None:
        neighbors_end = []

    common_neighbors = set_ops.set_intersection(neighbors_start, neighbors_end)
    num_common = len(common_neighbors)

    if num_common < 0:
        is_prime = False
    else:
        is_prime = utils.is_prime(num_common)

    return shortest_path_dist, is_prime, adj_sq
