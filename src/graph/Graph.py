# Graph is based on Amit Patel's tutorial: "Implementation of A*" at:
# http://www.redblobgames.com/pathfinding/a-star/implementation.html
class Graph:
    """
    Representation of a graph
    """

    def __init__(self, dimensions):
        """
        Initialize graph
        :param dimensions: list containing the size of each dimension of the graph
        """
        # Sanity checks
        # Check that dimensions are > 0
        for dimension in dimensions:
            if dimension < 0:
                raise Exception("Dimensions must be >= 0.")

        self.dimensions = dimensions
        self.obstacles = set()  # Obstacles

    def in_bounds(self, point):
        """
        Check whether a point is within the bounds of the graph
        :param point: point to check
        :return: boolean (True if within bounds, False otherwise)
        """
        # Sanity checks
        # Check that point has same number of dimensions as graph
        if not len(point) == len(self.dimensions):
            raise Exception("Point has " + str(len(point)) + " dimensions, Coordination Space has " + \
                            str(len(self.dimensions)) + " dimensions.")

        for i, coordinate in enumerate(point):
            if coordinate > self.dimensions[i] or coordinate < 0:
                return False

        return True

    def passable(self, point):
        """
        Check if point collides with an obstacle
        :param point: point to check
        :return: boolean (True if no collisions, False otherwise)
        """
        return point not in self.obstacles

    def point_neighbors_recursion(self, point):
        """
        Find all neighbors of a point (including the point itself)
        :param point: Point for which to find neighbors
        :return: list of lists, each sublist representing a neighbor
        """
        # Sanity checks
        if point is None:
            raise ValueError("Cannot operate on None")

        neighbors = []
        # 1-dimension
        if len(point) == 1:
            neighbors.append([point[0] - 1])  # left
            neighbors.append([point[0]])  # current
            neighbors.append([point[0] + 1])  # right

            return neighbors

        # n-dimensional
        for sub_dimension in self.point_neighbors_recursion(point[1:]):
            neighbors.append([point[0] - 1] + sub_dimension)  # left + (n-1)-dimensional combinations
            neighbors.append([point[0]] + sub_dimension)  # current + (n-1)-dimensional combinations
            neighbors.append([point[0] + 1] + sub_dimension)  # right + (n-1)-dimensional combinations

        return neighbors

    def neighbors(self, point):
        """
        Find all neighbors of a point
        :param point: Point for which to find neighbors
        :return: list of lists, each sublist representing a neighbor
        """
        # Sanity checks
        # Check that point has same number of dimensions as graph
        if not len(point) == len(self.dimensions):
            raise Exception("Point has " + str(len(point)) + " dimensions, Coordination Space has " + \
                            str(len(self.dimensions)) + " dimensions.")

        point_and_neighbors = self.point_neighbors_recursion(point)  # All neighbors, including point
        point_and_neighbors_set = set()
        for i in point_and_neighbors:
            point_and_neighbors_set.add(tuple(i))

        point_and_neighbors_set.remove(point)  # Remove point
        neighbors = point_and_neighbors_set  # Renaming for readability

        neighbors = filter(self.in_bounds, neighbors)  # Remove points that are out-of-bounds
        neighbors = filter(self.passable, neighbors)  # Remove points that are not neighbors

        return neighbors
