from src import graph_algos, matrix_ops, set_ops, utils

def graph_matrix_analysis(edges, start_node, end_node):
    # 1. Graph Algos: Create a graph and find shortest path
    g = graph_algos.Graph()
    nodes = set()
    for u, v, w in edges:
        g.add_edge(u, v, w)
        nodes.add(u)
        nodes.add(v)
        
    distances = g.dijkstra(start_node)
    shortest_path_dist = distances.get(end_node, float('inf'))
    
    # 2. Matrix Ops: Construct adjacency matrix
    sorted_nodes = sorted(list(nodes))
    node_to_idx = {node: i for i, node in enumerate(sorted_nodes)}
    n = len(nodes)
    adj_matrix = [[0] * n for _ in range(n)]
    
    for u, v, w in edges:
        if u in node_to_idx and v in node_to_idx:
            adj_matrix[node_to_idx[u]][node_to_idx[v]] = w # Unweighted for matrix connectivity
            # Assuming undirected for matrix symmetry or directed? 
            # Graph add_edge is directed in the implementation I saw (u->v). 
            # Let's stick to directed.
            
    # 3. Matrix Ops: Calculate square of adjacency matrix (paths of length 2)
    adj_sq = matrix_ops.matrix_power(adj_matrix, 2)
    
    # 4. Set Ops: Find intersection of neighbors
    # Neighbors of start_node
    neighbors_start = [v for v, w in g.adj_list.get(start_node, [])]
    # Neighbors of end_node
    neighbors_end = [v for v, w in g.adj_list.get(end_node, [])]
    
    common_neighbors = set_ops.set_intersection(neighbors_start, neighbors_end)
    num_common = len(common_neighbors)
    
    # 5. Utils: Check if number of common neighbors is prime
    is_num_common_prime = utils.is_prime(num_common)
    
    return shortest_path_dist, is_num_common_prime, adj_sq
