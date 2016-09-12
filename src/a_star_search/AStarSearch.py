import math

from src.Utilities import PriorityQueue


# AStarSearch is based on Amit Patel's tutorial: "Implementation of A*" at:
# http://www.redblobgames.com/pathfinding/a-star/implementation.html

def heuristic(point_a, point_b):
    """
    Estimated cost of travelling between two points
    :param point_a: start point
    :param point_b: goal point
    :return: Euclidean distance
    """
    # Sanity checks
    # Check that points have same number of dimensions
    len_a = len(point_a)
    len_b = len(point_b)
    if not len_a == len_b:
        raise Exception("a has " + str(len_a) + " dimensions, b has " + str(len_b) + " dimensions.")

    # Euclidean distance
    difference_squared = [(a - b) ** 2 for a, b in zip(point_a, point_b)]
    summed = sum(difference_squared)
    root = math.sqrt(summed)

    return root


def a_star_search(graph, start, goal):
    """
    A* Search
    :param graph: graph to search
    :param start: start point
    :param goal: goal point
    :return: path from start to goal
    """
    # Sanity checks
    # Check that points have same number of dimensions as graph
    len_start = len(start)
    len_goal = len(goal)
    len_graph = len(graph.dimensions)
    if not len_start == len_graph:
        raise Exception("start has " + str(len_start) + " dimensions, graph has " + str(len_graph) + " dimensions.")

    if not len_goal == len_graph:
        raise Exception("goal has " + str(len_goal) + " dimensions, graph has " + str(len_graph) + " dimensions.")

    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far


def reconstruct_path(came_from, start, goal):
    """
    Build path after searching
    :param came_from: node came from
    :param start: starting point
    :param goal: goal point
    :return: list representing path
    """
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    # path.append(start)  # optional
    path.reverse()  # optional

    return path
