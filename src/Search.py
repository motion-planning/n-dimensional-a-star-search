from src.a_star_search.AStarSearch import a_star_search, reconstruct_path
from src.graph.WeightedGraph import WeightedGraph

graph = WeightedGraph([5, 5, 5])
start, goal = (0, 0, 0), (5, 5, 5)

for obs in graph.neighbors((3, 3, 3)):
    graph.obstacles.add(obs)

came_from, cost_so_far = a_star_search(graph, start, goal)

path = reconstruct_path(came_from, start, goal)

print(path)
