name = 'Nguyen Phong'
age = 18
address = "Ha Noi"
gender = "male"

print("Xin chao, toi la", name, ", toi", age, "tuoi, toi song o", address, "toi la", gender)
print(f"Xin chao, toi la {name}, toi {age} tuoi, toi song o {address}, toi la {gender} ")

# LENGTH FUNCTION
print(len(name))

# SUB-STRING
print(name[2])
print(name[len(name) - 1])
print(name[::-1])

# INPUT COMMAND
full_name = input("Tell me your name?")
print(f"Hello {full_name}!")

a = int(input("Enter a number"))
print(f"{a} to the power of 2 is {a**2}")




### Nhập 2 số từ bàn phím, tính tổng hiệu tích thương và in ra

a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
add = a + b
minus = a - b
times = a * b
divide = a//b

print(f"The sum of the two numbers is {add}, their 
subtraction is {minus}, multiplication is {times} 
and division is {divide}")
### Nhap mot gia tri string bat ky tu ban phim
# Chuyen string do thanh cac chu viet hoa
# Chuyen thanfh viet thuong
# Thay the tat ca chu "h" bang chu "k"
# Lay cac chu o vi tri 2 - 6

name = input("What is your name: ")
print(name.upper())
print(name.lower())

print(name[2:7])


