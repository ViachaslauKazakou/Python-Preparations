""" Travel sales managegment problem (TSP) """

from itertools import permutations
import numpy as np

def tsp_bruteforce(graph):
    n = len(graph)
    cities = range(n)
    min_path = None
    min_cost = float("inf")

    for perm in permutations(cities):
        cost = sum(graph[perm[i]][perm[i+1]] for i in range(n - 1)) + graph[perm[-1]][perm[0]]
        if cost < min_cost:
            min_cost = cost
            min_path = perm

    return min_path, min_cost


def tsp_nearest_neighbor(graph, start=0):
    n = len(graph)
    unvisited = set(range(n))
    unvisited.remove(start)
    path = [start]
    cost = 0

    while unvisited:
        last = path[-1]
        next_city = min(unvisited, key=lambda city: graph[last][city])
        cost += graph[last][next_city]
        path.append(next_city)
        unvisited.remove(next_city)

    cost += graph[path[-1]][start]
    path.append(start)
    return path, cost


if __name__ == '__main__':
    distances = np.array([
        [0, 10, 15, 20],  
        [10, 0, 35, 25],  
        [15, 35, 0, 30],  
        [20, 25, 30, 0] 
    ])
    best_path, best_cost = tsp_bruteforce(distances)
    print(f"Лучший маршрут: {best_path}, Длина маршрута: {best_cost}")
    
    best_path, best_cost = tsp_nearest_neighbor(distances)
    print(f"Маршрут (жадный): {best_path}, Длина маршрута: {best_cost}")