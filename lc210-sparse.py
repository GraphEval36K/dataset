import json
import networkx as nx
import random

def connected_sparse_graph(numCourses):
    G = nx.DiGraph()
    for i in range(1, numCourses):
        G.add_edge(random.randint(0, i-1), i)
    for _ in range(min(5000, numCourses * 2)):
        a, b = random.randint(0, numCourses-1), random.randint(0, numCourses-1)
        if not G.has_edge(a, b):
            G.add_edge(a, b)
    return G

def disconnected_sparse_graph(numCourses):
    G = nx.DiGraph()
    partition_point = random.randint(1, numCourses - 1)
    for i in range(1, partition_point):
        if random.random() > 0.5:
            G.add_edge(random.randint(0, i-1), i)
    for i in range(partition_point + 1, numCourses):
        if random.random() > 0.5:
            G.add_edge(random.randint(partition_point, i-1), i)
    return G

def cyclic_sparse_graph(numCourses):
    G = nx.DiGraph()
    cycle_start = random.randint(0, numCourses-3)
    cycle_end = cycle_start + random.randint(2, min(10, numCourses - cycle_start - 1))
    for i in range(cycle_start, cycle_end):
        G.add_edge(i, i+1)
    G.add_edge(cycle_end, cycle_start)
    for _ in range(min(5000, numCourses * 2) - (cycle_end - cycle_start + 1)):
        a, b = random.randint(0, numCourses-1), random.randint(0, numCourses-1)
        if not G.has_edge(a, b):
            G.add_edge(a, b)
    return G

def acyclic_sparse_graph(numCourses):
    G = nx.DiGraph()
    G.add_nodes_from(range(numCourses))  # Ensure all nodes are added before any operations
    added_edges = 0
    while added_edges < min(5000, numCourses * 2):
        a, b = random.randint(0, numCourses-1), random.randint(0, numCourses-1)
        if a != b and not nx.has_path(G, b, a):
            G.add_edge(a, b)
            added_edges += 1
    return G



def Gen_label(numCourses, prerequisites):
    # 1. create a preMap
    preMap = { i : [] for i in range(numCourses)}
    for crs, pre in prerequisites:
        preMap[crs].append(pre)

    res = []
    visit = set()
    cycle = set()
    
    # 2. DFS
    def dfs(crs):
        if crs in visit: return True                 # visit: 已经加入了 res
        if crs in cycle: return False
        
        cycle.add(crs)
        
        for pre in preMap[crs]:
            if dfs(pre) == False: return False

        cycle.remove(crs)

        res.append(crs)
        visit.add(crs)

        return True
    
    # 3. traverse all crs
    for crs in range(numCourses):
        if dfs(crs) == False:
            return []
    return res


def generate_and_save_graphs(num_graphs, min_n, max_n, filename):
    graph_types = [connected_sparse_graph, disconnected_sparse_graph, cyclic_sparse_graph, acyclic_sparse_graph]
    graph_labels = ["connected", "disconnected", "cyclic", "acyclic"]
    data = {label: {"graphs": [], "numCourse": [], "labels": [], "complexity": []} for label in graph_labels}
    
    for graph_func, label in zip(graph_types, graph_labels):
        for _ in range(num_graphs):
            n = random.randint(min_n, max_n)
            G = graph_func(n)
            edges = list(G.edges())
            label_check = Gen_label(n, edges)
            data[label]["numCourse"].append(n)
            data[label]["graphs"].append(edges)
            data[label]["labels"].append(label_check)
            data[label]["complexity"].append(len(edges))

    with open(filename, 'w') as file:
        for key, value in data.items():
            file.write(json.dumps({key: value}) + '\n')


if __name__ == '__main__':
    generate_and_save_graphs(1, 5, 10, './sparse.jsonl')
