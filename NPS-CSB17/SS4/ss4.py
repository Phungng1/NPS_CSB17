# For loop
# In ra cac so le trong pham vi 10 den 50
for i in range(11,50):
    if i%2==1:
        print(i)

for i in range(11,50,2):
    print(i)

# While loop
n = 11
while n<50:
    print(n)
    n += 2

# Continue
n = 11
while n<50:
    if n == 19:
        n += 2
        continue
    print(n)
    n += 2
### In ra so le nhung bo 19 ###

# In ra cac day so: 0 1 2 3 4 5 6, 100 101 102 103 104 106, 9 8 7 6 5 10 11 12
for i in range(7):
    print(i)

i = 100
while i<107:
    if i==105:
        i+=1
        continue
    print(i)
    i+=1

for i in range(9,4,-1):
    print(i)
    if i==5:
        for k in range(10,13,1):
            print(k)

# In ra cac so chia het cho 3 tu 0 den 30
for i in range(0,31,3):
    print(i)

# In ra day so tu 0 den n, moi so mot dong va n duoc input vao. Khong duoc nhap so am, so thuc
# kiem tra va yeu cau nguoi dung nhap lai
n = (input("Enter a number: "))

while n>0 or n != float(n):
    for i in range(n):
        print(i)


# Tinh so chu so cua mot so nguyen do nguoi dung nhap vao
n = (int(input("Enter a number: ")))
so_chu_so = 1
while n // 10 > 0:
    n = n // 10
    so_chu_so +=1

print(so_chu_so)


# Ve hinh tron voi ban kinh nguoi dung nhap vao
n = float(input("Enter radius: "))
import turtle
t = turtle.Turtle()
i = 0
while i < 5:
    t.circle(n*2)
    t.left(72)
    i +=1
### Extended mode ###
n = float(input("Enter radius: "))
import turtle
t = turtle.Turtle()
repeat_time = int(input("How many repetitions: "))
i = (360/repeat_time)
for k in range(0,repeat_time,1):
    t.circle(n*2)
    t.left(i)