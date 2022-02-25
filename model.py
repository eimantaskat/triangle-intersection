vertices = []
faces = []

def newface(A, RGB):
    global vertices, faces
    Q = ''
    for i in range (len(A)):
        Q += ' '+str(i+len(vertices))
    faces += [str(len(A))+str(Q)+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
    for i in range (len(A)):
        vertices += [str(A[i][0])+' '+str(A[i][1])+' '+str(A[i][2])]

def off(mesh): # mesh - off file
    global vertices, faces
    file = open(mesh, 'w')
    file.write('%s\n%d %d %d\n' % ('OFF',len(vertices),len(faces),0))
    for i in range (len(vertices)):
        file.write('%s\n' % vertices[i])
    for j in range (len(faces)):
        file.write('%s\n' % faces[j])
    file.close()
    vertices = []
    faces = []