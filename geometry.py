import numpy as np
point_list = []

class Shapes:
    def __init__(self, parallelograms, rectangles, rhombi, squares, isosceles_trapezia, cyclic_quadrilaterals, isosceles_triangles, right_triangles):
        self.parallelograms = parallelograms
        self.rectangles = rectangles
        self.rhombi = rhombi
        self.squares = squares
        self.isosceles_trapezia = isosceles_trapezia
        self.cyclic_quadrilaterals = cyclic_quadrilaterals
        self.isosceles_triangles = isosceles_triangles
        self.right_triangles = right_triangles

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
    cyclic_quadrilateral_list = []
    isosceles_triangle_list = []
    right_triangle_list = []

    len_vectors = len(vectors)

    for i in range(len_vectors):
        for j in range(i + 1, len_vectors):
            v1 = vectors[i]
            v2 = vectors[j]
            
            if v1.x < 0:
                v1 = Vector(v1.point2, v1.point1)
    
            elif v1.x == 0:
                if v1.y < 0:
                    v1 = Vector(v1.point2, v1.point1)

            if v2.x < 0:
                v2 = Vector(v2.point2, v2.point1)

            elif v2.x == 0:
                if v2.y < 0:
                    v2 = Vector(v2.point2, v2.point1)

            x1 = v1.point1[0]
            y1 = v1.point1[1]
            x2 = v1.point2[0]
            y2 = v1.point2[1]
            x3 = v2.point2[0]
            y3 = v2.point2[1]
            x4 = v2.point1[0]
            y4 = v2.point1[1]

            x41 = x4 - x1
            y41 = y4 - y1
            x31 = x3 - x1
            y31 = y3 - y1
            x42 = x4 - x2
            y42 = y4 - y2
            x32 = x3 - x2
            y32 = y3 - y2

            point1 = np.array([x1, y1])
            point2 = np.array([x2, y2])
            point3 = np.array([x3, y3])
            point4 = np.array([x4, y4])

            vector1 = vectors[i].xy
            vector2 = vectors[j].xy
            vector3 = np.array([x41, y41])
            vector4 = np.array([x31, y31])
            vector5 = np.array([x42, y42])
            vector6 = np.array([x32, y32])

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

                if -0.001 < np.linalg.norm(vector1) * np.linalg.norm(vector2) + np.linalg.norm(vector3) * np.linalg.norm(vector6) - np.linalg.norm(vector4) * np.linalg.norm(vector5) < 0.001:
                    add_shape(quadrilateral, cyclic_quadrilateral_list)
    
    square_list = list(set(rectangle_list) & set(rhombus_list))
    
    return Shapes(parallelogram_list, rectangle_list, rhombus_list, square_list,\
        isosceles_trapezium_list, cyclic_quadrilateral_list, isosceles_triangle_list, right_triangle_list)
    
def add_shape(shape, shapes):
    if isinstance(shape, Quadrilateral):
        for s in shapes:
            if {(s.point1[0], s.point1[1]), (s.point2[0], s.point2[1]), (s.point3[0], s.point3[1]), (s.point4[0], s.point4[1])}\
                == {(shape.point1[0], shape.point1[1]), (shape.point2[0], shape.point2[1]), (shape.point3[0], shape.point3[1]), (shape.point4[0], shape.point4[1])}:
                return
    else:
        for s in shapes:
            if {(s.point1[0], s.point1[1]), (s.point2[0], s.point2[1]), (s.point3[0], s.point3[1])}\
                == {(shape.point1[0], shape.point1[1]), (shape.point2[0], shape.point2[1]), (shape.point3[0], shape.point3[1])}:
                return
    shapes.append(shape)

def calculate(points):
    vectors = get_vectors(points)
    shapes = get_shapes(vectors)
    return shapes