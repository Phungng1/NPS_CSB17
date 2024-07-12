# IF CONDITION

a = 300
b = 400

if a<b:
    print (f"{a}<{b}")
else:
    print(f"{a}>{b}")

# ELIF

a = 300
b = 400

if a<b:
    print (f"{a}<{b}")
elif a>b:
    print(f"{a}>{b}")
else:
    print(f"{a}={b}")

# AND - OR - NOT

age = 20
money = 150

if age>=18 and money>200:
    print("You are allowed to enter")
else:
    print("Must be over 18 and have more than 200 to enter")






# Viet chuong trinh tim so lon hon trong 3 so nhap tu ban phim
x = float(input("Enter num1"))
y = float(input("Enter num2"))
z = float(input("Enter num3"))

if x>y and x>z:
    print(f"Largest number: {x}")
elif y>x and y>z:
    print(f"Largest number: {y}")
else:
    print(f"Largest number: {z}")

# Tinh chi so BMI
height = float(input("What is your height in metre(m)? "))
weight = float(input("What is your weight in kilogram(kg)? "))

BMI = (weight)/(height**2)

print(f"Your BMI is {BMI}")

# Tinh nghiem phuong trinh bac 2
import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
delta = (b**2 - 4*a*c)


if delta > 0:
    deltatr = math.sqrt(b**2 - 4*a*c)
    print(f"Phuong trinh co nghiem: {(-b-deltatr)/(2*a)} va {(-b+deltatr)/(2*a)}")
elif delta==0:
    print(f"Phuong trinh co nghiem kep: {-b/(2*a)}")
else:
    print("Phuong trinh vo nghiem")

# Viet chuong trinh kiem tra so nguoi dung nhap vao la so duong, am hay 0
number = float(input("Enter a number: "))
if number>0:
    print(f"{number} la so duong")
elif number<0:
    print(f"{number} la so am")
else:
    print(f"{number} la 0")

# Viet chuong trinh xac dinh mot nam co phai la nam nhuan hay khong (nam nhuan: chia het cho 4)
# Neu chia het cho 100 thi phai chia het cho 4
year = int(input("Enter a year: "))

if year%100==0:
    if year%400==0:
        print(f"{year} la nam nhuan")
    else:
        print(f"{year} ko la nam nhuan")
elif year%4==0:
    print(f"{year} la nam nhuan")
else:
    print(f"{year} ko la nam nhuan")

# Viet chuong trinh cho phep nguoi dung nhap ten dang nhap va mat khau. Kiem tra xem ten dang nhap va mat
# khau da khop yeu cau hay chua
# - Ten dang nhap: nguoidung
# - Mat khau: matkhau123
name = "nguoidung"
password = "matkhau123"
username = input("Enter your username: ")
userpassword = input("Enter password: ")

if username==name and userpassword==password:
    print("Signed in")
else:
    print("Your username or password is incorrect")

# Cho string ch co do dai 1 chua dung mot ky tu
# Viet dieu kien de kiem tra ch co phai mot chu cai trong bang chu cai hay k

ch = input("Enter a character: ")

if ch.isalpha()==True:
    print(f"{ch} is a letter")
else:
   print(f"{ch} is not a letter")

# Kiem tra mot chuoi co phai la so hay khong. In ra thong bao tuong ung
a = input("Enter a character: ")

if a.isnumeric()==True:
    print(f"{a} is a number")
else:
    print(f"{a} is not a number")

# Tach chuoi tu chuoi con
string = "hello world"

string2 = string.split("world")

print(string2)











