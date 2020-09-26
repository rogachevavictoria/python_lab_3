import math

class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def distance(self):
        d = math.sqrt(pow(self.x, 2) + pow(self.y, 2))
        return d


A = Point('A', 3, 7)
B = Point('B', -10, 4)
C = Point('C', -2, -11)

print('OA = ' + str(A.distance()))
print('OB = ' + str(B.distance()))
print('OC = ' + str(C.distance()))

if (A.distance() >= B.distance()) and (A.distance() >= C.distance()):
    l = A
elif (B.distance() >= A.distance()) and (B.distance() >= C.distance()):
    l = B
else:
    l = C

print(l.name, 'is furthest')

if (A.distance() <= B.distance()) and (A.distance() <= C.distance()):
    s = A
elif (B.distance() <= A.distance()) and (B.distance() <= C.distance()):
    s = B
else:
    s = C

print(s.name, 'is closest')