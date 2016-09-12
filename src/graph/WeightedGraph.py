from src.graph.Graph import Graph


# GridWithWeights is based on Amit Patel's tutorial: "Implementation of A*" at:
# http://www.redblobgames.com/pathfinding/a-star/implementation.html
class WeightedGraph(Graph):
    """
    Weighted graph representation
    """

    def __init__(self, dimensions):
        """
        Initialize graph
        :param dimensions: list representing the length of each dimension
        """
        super().__init__(dimensions)
        self.weights = {}  # Weight of each node

    def cost(self, from_node, to_node):
        """
        Cost to get to node
        :param from_node: node coming from
        :param to_node: node going to
        :return: cost
        """
        return self.weights.get(to_node, 1)
