import itertools
import networkx as nx


def count_quadrilaterals(N1, N2):
    """
    Count the number of quadrilaterals formed by intersections in a triangular grid.
    """
    # Create a graph
    G = nx.Graph()
    
    # Generate intersection points
    intersections = [f'P{i}{j}' for i in range(1, N1 + 1) for j in range(1, N2 + 1)]
    G.add_nodes_from(intersections)
    
    # Add edges between neighboring intersection points
    for i in range(1, N1 + 1):
        for j in range(1, N2 + 1):
            if i < N1:
                G.add_edge(f'P{i}{j}', f'P{i + 1}{j}')
            if j < N2:
                G.add_edge(f'P{i}{j}', f'P{i}{j + 1}')
            if i < N1 and j < N2:
                G.add_edge(f'P{i}{j}', f'P{i + 1}{j + 1}')
                G.add_edge(f'P{i + 1}{j}', f'P{i}{j + 1}')
    
    # Find all quadrilaterals
    quadrilaterals = set()
    for combination in itertools.combinations(G.nodes, 4):
        subgraph = G.subgraph(combination)
        if nx.is_connected(subgraph) and len(subgraph.edges) == 4:
            quadrilaterals.add(tuple(sorted(combination)))
    
    return len(quadrilaterals)


def count_quadrilaterals2(L, R):
    """Функция для подсчёта количества четырёхугольников в треугольнике"""
    if L < 1 or R < 1:
        return 0
    return (L * R * (L + 1) * (R + 1)) // 4


if __name__ == "__main__":
    # Пример: 3 линии из одного угла и 4 из другого
    l = 2
    r = 2
    print("Количество четырёхугольников (граф):", count_quadrilaterals(l, r))
    print("Количество четырёхугольников (формула):", count_quadrilaterals2(l, r))

