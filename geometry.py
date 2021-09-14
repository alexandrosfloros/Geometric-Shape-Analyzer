import numpy as np
point_list = []

class Quadrilateral:
    def __init__(self, point1, point2, point3, point4):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4

class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

class Vector:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.x = self.point2[0] - self.point1[0]
        self.y = self.point2[1] - self.point1[1]
        self.xy = np.array([self.x, self.y])

def get_vectors(points):
    vector_list = []
    len_points = len(points)

    for i in range(len_points):
        for j in range(i + 1, len_points):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[j][0]
            y2 = points[j][1]
            vector = Vector(points[i], points[j])
    
            if vector.x != 0 or vector.y != 0:                    
                vector_list.append(vector)
    
    return vector_list

def get_shapes(vectors):
    parallelogram_list = []
    rectangle_list = []
    rhombus_list = []
    square_list = []
    isosceles_trapezium_list = []
    isosceles_triangle_list = []
    right_triangle_list = []

    len_vectors = len(vectors)

    for i in range(len_vectors):
        for j in range(i + 1, len_vectors):
            x1 = vectors[i].point1[0]
            y1 = vectors[i].point1[1]
            x2 = vectors[i].point2[0]
            y2 = vectors[i].point2[1]
            x3 = vectors[j].point2[0]
            y3 = vectors[j].point2[1]
            x4 = vectors[j].point1[0]
            y4 = vectors[j].point1[1]

            x41 = x4 - x1
            y41 = y4 - y1
            x31 = x3 - x1
            y31 = y3 - y1
            x42 = x4 - x2
            y42 = y4 - y2

            point1 = np.array([x1, y1])
            point2 = np.array([x2, y2])
            point3 = np.array([x3, y3])
            point4 = np.array([x4, y4])

            vector1 = vectors[i].xy
            vector2 = vectors[j].xy
            vector3 = np.array([x41, y41])
            vector4 = np.array([x31, y31])
            vector5 = np.array([x42, y42])

            #Triangles

            if np.array_equal(point1, point3) or np.array_equal(point2, point3) or np.array_equal(point1, point4) or np.array_equal(point2, point4):
                if np.array_equal(point1, point3) or np.array_equal(point2, point3):
                    triangle = Triangle(point1, point2, point4)
                elif np.array_equal(point1, point4) or np.array_equal(point2, point4):
                    triangle = Triangle(point1, point2, point3)
                if np.linalg.det([vector1, vector2]) != 0:
                    if np.linalg.norm(vector1) == np.linalg.norm(vector2):
                        add_shape(triangle, isosceles_triangle_list)
                    if np.dot(vector1, vector2) == 0:
                        add_shape(triangle, right_triangle_list)

            #Quadrilaterals

            elif np.linalg.det([vector1, vector3]) != 0:
                quadrilateral = Quadrilateral(point1, point2, point3, point4)
                if np.array_equal(vector1, vector2) or np.array_equal(vector1, -1 * vector2):
                    add_shape(quadrilateral, parallelogram_list)
                    if np.dot(vector1, vector3) == 0:
                        add_shape(quadrilateral, rectangle_list)
                    if np.dot(vector4, vector5) == 0:
                        add_shape(quadrilateral, rhombus_list)
                if np.linalg.det([vector1, vector2]) == 0 and np.linalg.norm(vector4) == np.linalg.norm(vector5):
                    add_shape(quadrilateral, isosceles_trapezium_list)
    square_list = list(set(rectangle_list) & set(rhombus_list))
    return parallelogram_list, rectangle_list, rhombus_list, square_list, isosceles_trapezium_list, isosceles_triangle_list, right_triangle_list
    
def add_shape(shape, shapes):
    if isinstance(shape, Quadrilateral):
        for s in shapes:
            if {(s.point1[0], s.point1[1]), (s.point2[0], s.point2[1]), (s.point3[0], s.point3[1]), (s.point4[0], s.point4[1])} == {(shape.point1[0], shape.point1[1]), (shape.point2[0], shape.point2[1]), (shape.point3[0], shape.point3[1]), (shape.point4[0], shape.point4[1])}:
                return
    elif isinstance(shape, Triangle):
        for s in shapes:
            if {(s.point1[0], s.point1[1]), (s.point2[0], s.point2[1]), (s.point3[0], s.point3[1])} == {(shape.point1[0], shape.point1[1]), (shape.point2[0], shape.point2[1]), (shape.point3[0], shape.point3[1])}:
                return
    shapes.append(shape)

def display():
    point_list = [np.array([0, 0]), np.array([2, 0]), np.array([4, 0]), np.array([0, 2]), np.array([2, 2])]
    vector_list = get_vectors(point_list)
    shape_list = get_shapes(vector_list)

    print("\n------Results------\n\nVectors:")
    for v in vector_list:
        print(v.xy)

    print("\nParallelograms:")
    for s in shape_list[0]:
        print(s.point1, s.point2, s.point3, s.point4)

    print("\nRectangles:")
    for s in shape_list[1]:
        print(s.point1, s.point2, s.point3, s.point4)

    print("\nRhombi:")
    for s in shape_list[2]:
        print(s.point1, s.point2, s.point3, s.point4)

    print("\nSquares:")
    for s in shape_list[3]:
        print(s.point1, s.point2, s.point3, s.point4)

    print("\nIsosceles Trapezia:")
    for s in shape_list[4]:
        print(s.point1, s.point2, s.point3, s.point4)

    print("\nIsosceles Triangles:")
    for s in shape_list[5]:
        print(s.point1, s.point2, s.point3)

    print("\nRight Triangles:")
    for s in shape_list[6]:
        print(s.point1, s.point2, s.point3)

display()