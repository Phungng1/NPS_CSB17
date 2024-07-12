# Bai 1
for i in range(3,13,1):
    print(i)
# Bai 2
n = int(input("Input a number: "))
if n > 0:
    for i in range(n+1):
        print(i)
# Bai 3
n = int(input("Input a number: "))
for i in range(1,n,2):
    print(i)
# Bai 4
import turtle
t = turtle.Turtle()
edge = int(input("Input number of edges: "))
degree = 180*(edge-2)
i = 0
while i<edge:
    t.forward(50)
    t.right(180-(degree/edge))
    i+=1
