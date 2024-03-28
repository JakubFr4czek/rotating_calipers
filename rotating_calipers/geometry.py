class Rectangle:

    def __init__(self, A, B, C, D):
        self.vertices = [A, B, C, D]
        
    def getEdges(self):

        edges = []

        for i in range(1, len(self.vertices)):
            edges.append( (self.vertices[i - 1], self.vertices[i]) )
        edges.append( (self.vertices[-1], self.vertices[0]) )

        return edges
    
class PointSet:

    @staticmethod
    def getEdges(points):

        edges = []

        for i in range(1, len(points)):
            edges.append( (points[i - 1], points[i]) )
        edges.append( (points[-1], points[0]) )
    
        return edges