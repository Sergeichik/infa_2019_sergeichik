from math import sin, cos
def primenum(a):
    l = []
    l.append(2)
    n = 0
    q = True
    for i in range(a):
        for k in range(n):
            if (i + 3) %l[k] == 0:
                q = False
       	if q == True:
            l.append(i + 3)
            n = n + 1     
        else:
            q = True         
    print(l)
    return(l)

def sort(m):
    q = 0
    for i in range (len(m)):
        for k in range(len(m) - i):
            if m[i + k] < m[q]:
                q = k + i
        m[i],m[q] = m[q],m[i]
        q = i + 1
    print(m)

    
def rotate(square, angle):
    sqnew = []
    for i in range(3): 
        sqnew.append((square[i][0]*cos(angle) - square[i][1]*sin(angle)),(square[i][0]*sin(angle) + square[i][1]*cos(angle))
    print(sqnew)
primenum(1000)
sort([2, 7, 16, 1, 21]
rotate(((20 , 10), (20,20), (10,20),(10,10)), 0.7)      
