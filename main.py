from math import sqrt
import triangle as tri
from model import newface, off
from random import randint

def plane_equation(triangle):
    # Ax + By + Cz + D = 0

    A, B, C = triangle.A, triangle.B, triangle.C
    AB = [B.x-A.x, B.y-A.y, B.z-A.z]
    AC = [C.x-A.x, C.y-A.y, C.z-A.z]

    a = AB[1] * AC[2] - AC[1] * AB[2]
    b = AB[2] * AC[0] - AC[2] * AB[0]
    c = AB[0] * AC[1] - AC[0] * AB[1]
    d = - (a * B.x + b * B.y + c * B.z)

    return a, b, c, d


def parametric_equations(A, B):
    direction_vector = [B.x - A.x, B.y - A.y, B.z - A.z]

    # x = x0 + at
    # y = y0 + bt
    # z = z0 + ct

    return A.x, direction_vector[0], A.y, direction_vector[1], A.z, direction_vector[2]

def intersection_point(A, B, C, D, x0, a, y0, b, z0, c):
    # solve for t

    # A(x0 + at) + B(y0 + bt) + C(z0 + ct) + D
    # (A * a + B * b + C * c)t + (A * x0 + B * y0 + C * z0 + D)
    try:
        t = -(A * x0 + B * y0 + C * z0 + D) / (A * a + B * b + C * c)
        # find the intersection point
        x = x0 + a * t
        y = y0 + b * t
        z = z0 + c * t

        return tri.point([x, y, z])
    except ZeroDivisionError:
        return tri.point([None, None, None])

def vector_magnitude(A, B):
    return sqrt((B.x - A.x) ** 2 + (B.y - A.y) ** 2 + (B.z - A.z) ** 2)

def area(A, B, C):
    # Heron's formula
    a = vector_magnitude(A, B)
    b = vector_magnitude(B, C)
    c = vector_magnitude(A, C)
    p = (a + b + c) / 2

    k = p * (p - a) * (p - b) * (p - c)

    return sqrt(k) if k > 0 else 0

def point_in_triangle(triangle, P):
    A, B, C = triangle.A, triangle.B, triangle.C
    triangle_area = area(A, B, C)
    area1 = area(A, B, P)
    area2 = area(A, C, P)
    area3 = area(B, C, P)
    if round(triangle_area, 6) == round(area1+area2+area3, 6):
        return True
    else:
        return False

def verify(P, points, tri1, tri2):
    if P.x:
        if point_in_triangle(tri1, P) and point_in_triangle(tri2, P):
            if [P.x, P.y, P.z] in points:
                points.remove([P.x, P.y, P.z])
            else:
                points.append([P.x, P.y, P.z])

def line_in_plane(A, B, C, D, x0, a, y0, b, z0, c):
    for t in (-100000000, 100000000):
        x = x0 + a * t
        y = y0 + b * t
        z = z0 + c * t
        return A * x + B * y + C * z + D == 0

def triangles_intersect(tri1, tri2):
    points = []
    for tris in ([tri1, tri2], [tri2, tri1]):
        A, B, C, D = plane_equation(tris[0])

        for pt in ([tris[1].A, tris[1].B], [tris[1].A, tris[1].C], [tris[1].B, tris[1].C]):
            x0, a, y0, b, z0, c = parametric_equations(pt[0], pt[1])
            P = intersection_point(A, B, C, D, x0, a, y0, b, z0, c)
            if line_in_plane(A, B, C, D, x0, a, y0, b, z0, c):
                return False
            verify(P, points, tris[0], tris[1])

    if len(points) > 0:
        return True
    else:
        return False

if __name__ == "__main__":
    points1 = [[randint(-10, 10), randint(-10, 10), randint(-10, 10)], [randint(-10, 10), randint(-10, 10), randint(-10, 10)], [randint(-10, 10), randint(-10, 10), randint(-10, 10)]]
    points2 = [[randint(-10, 10), randint(-10, 10), randint(-10, 10)], [randint(-10, 10), randint(-10, 10), randint(-10, 10)], [randint(-10, 10), randint(-10, 10), randint(-10, 10)]]

    # trikampiai lieciasi tiese
    # points1 = [[2, 5, 0], [0, 0, 10], [-2, 0, 0]]
    # points2 = [[0, 0, 0], [5, 0, 0], [0, 5, 0]]

    # trikampiai lieciasi 1 taske
    # points1 = [[0, 0, 0], [1, 2, 0], [3, -1, 0]]
    # points2 = [[4, 1, 1], [1, 1, 5], [1, .5, 0]]

    # trikampiai susikerta
    # points1 = [[0, 0, 2], [1, 2, 2], [3, -1, 2]]
    # points2 = [[4, 1, 1], [1, 1, 5], [1, .5, 0]]

    # points1 = [[0, 0, 0], [1, 2, 0], [3, -1, 0]]
    # points2 = [[2, 0, 1], [1, 1, 1], [1, .5, -1]]

    newface(points1, [255, 0, 0])
    newface(points2, [0, 255, 0])
    off('test.off')

    tri1 = tri.triangle(points1)
    tri2 = tri.triangle(points2)

    print("Triangles intersect" if triangles_intersect(tri1, tri2) else "Triangles do not intersect")