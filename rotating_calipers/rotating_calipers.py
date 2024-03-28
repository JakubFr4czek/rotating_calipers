from .geometry import Rectangle, PointSet
from .convexhull import Graham


#Metoda zwracająca pole prostokąta
def compare_area(a, b):
    return a * b

#Metoda zwracająca obwód prostokąta
def compare_perimeter(a, b):
    return 2 * a + 2 * b

#Metoda zwracająca prostokąt o najmniejszej wartośći zwracanej przez compare
#zawierający wszystkie punkty z points
def smallest_rectangle(points, compare):

   #Punkty tworzące otoczkę wypukłą, O(nlogn)
    hull_points = Graham.graham_algorithm(points)

    #Krawędzie otoczki wypukłej
    edges = PointSet.getEdges(hull_points)

    #Wektory kierunkowe krawędzi
    dir_vec = []
    for edge in edges:
        dir_vec.append( ( (edge[1][0] - edge[0][0]), (edge[1][1] - edge[0][1]) ) )

    #Długości krawędzi (długości wektorów)
    edges_len = []
    for vec in dir_vec:
        edges_len.append( (vec[0]**2 + vec[1]**2)**(1/2) ) 

    #Normalizacja wektorów => Upraszcza i przyspiesza obliczenia (nie jest konieczna do poprawnego działania algorytmu)
    norm_vec = []
    for i in range(len(dir_vec)):
        norm_vec.append( (dir_vec[i][0] / edges_len[i], dir_vec[i][1] / edges_len[i]) )

    #Wektory prostopadłe
    perp_vec = []
    for i in range(len(norm_vec)):
        perp_vec.append( (-norm_vec[i][1], norm_vec[i][0]) )

    #Dla każdego punktu sprawdzam, względem której krawędzi otoczki jest on najbardziej Wysunięty w lewo lub w prawo
    minX = [] 
    maxX = [] 

    for i in range(len(norm_vec)):

        minXVal = float('inf')
        maxXVal = float('-inf')

        for j in range(len(hull_points)):

            temp = hull_points[j][0] * norm_vec[i][0] + hull_points[j][1] * norm_vec[i][1]

            if temp > maxXVal:
                maxXVal = temp
                
            if temp < minXVal:
                minXVal = temp
            
        minX.append(minXVal)
        maxX.append(maxXVal)

    #Dla każdego punktu sprawdzam, względem której krawędzi otoczki jest on najbardziej Wysunięty w górę lub w dół    
    minY = []
    maxY = []

    for i in range(len(perp_vec)):
            
        minYVal = float('inf')
        minYVal = float('inf')
        maxYVal = float('-inf')

        for j in range(len(hull_points)):

            temp = hull_points[j][0] * perp_vec[i][0] + hull_points[j][1] * perp_vec[i][1]

            if temp > maxYVal:
                maxYVal = temp
                
            if temp < minYVal:
                minYVal = temp
            
        minY.append(minYVal)
        maxY.append(maxYVal)

    #Każda czwórka stworzona z minX[i], maxX[i], minY[i], maxY[i] tworzy prostokąt
    #Szukam prostokąta o najmniejszej wartości zwracanej przez compare
    minResult = float('inf')
    minIdx = -1

    for i in range(len(minX)):

        result = compare(abs(minX[i] - maxX[i]), abs(minY[i] - maxY[i]))

        if result < minResult:
            minResult = result
            minIdx = i

    minRectangle = Rectangle( 
        (minX[minIdx],minY[minIdx]), 
        (maxX[minIdx], minY[minIdx]),
        (maxX[minIdx], maxY[minIdx]), 
        (minX[minIdx], maxY[minIdx]))
        
    for i in range(len(minRectangle.vertices)):

        minRectangle.vertices[i] = (
            minRectangle.vertices[i][0] * norm_vec[minIdx][0] + minRectangle.vertices[i][1] * perp_vec[minIdx][0],
            minRectangle.vertices[i][0] * norm_vec[minIdx][1] + minRectangle.vertices[i][1] * perp_vec[minIdx][1]
            )

    return result, minRectangle.vertices