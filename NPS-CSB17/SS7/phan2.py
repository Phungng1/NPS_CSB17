colors = ['blue', 'red', 'green']
#Bai 1
i = int(input("Input position: "))
print(colors[i-1])

#Bai 2
a = input("Remove element: ")
if a in colors and a.isalpha()==True:
    colors.remove(a)
elif a not in colors and a.isalpha()==True:
    print("Element not found")
else:
    a = int(a)
    if a>(len(colors)-1):
        print("Element not found")
    else:
        colors.pop(a)
print(colors)
# Bai 3
import turtle
t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
colors = ['blue', 'red', 'green']
for item in colors:
	t.color(item)
	t.forward(50)



