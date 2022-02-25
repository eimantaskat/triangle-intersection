class pt:
    pass

class triang:
    pass

def triangle(arr):
    tri = triang()

    tri.A = pt()
    tri.A.x = arr[0][0]
    tri.A.y = arr[0][1]
    tri.A.z = arr[0][2]

    tri.B = pt()
    tri.B.x = arr[1][0]
    tri.B.y = arr[1][1]
    tri.B.z = arr[1][2]

    tri.C = pt()
    tri.C.x = arr[2][0]
    tri.C.y = arr[2][1]
    tri.C.z = arr[2][2]

    return tri

def point(arr):
    pnt = pt()

    pnt.x = arr[0]
    pnt.y = arr[1]
    pnt.z = arr[2]

    return pnt