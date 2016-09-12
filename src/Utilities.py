import heapq


# PriorityQueue is based on Amit Patel's tutorial: "Implementation of A*" at:
# http://www.redblobgames.com/pathfinding/a-star/implementation.html
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]
