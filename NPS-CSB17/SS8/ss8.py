# Function
def say_hello():
    print("Hello World!")
say_hello() # Hello World!

def say_hello():
    print("Hello World!")
print(say_hello()) # Hello World! None

def say_hello():
    return "Hello World!"
    print("Day la noi dung sau lenh return")
print(say_hello()) # Hello World!


def function_a():
    a = 12
print(a) # Error: name 'a' is not defined

# Giai bai tap voi module
import ss8_module
# Viết hàm tìm số lớn hơn trong 2 số 
a = 1
b = 2
print(f"The bigger number is {ss8_module.findNum(a,b)}")

# Định nghĩa hàm có thể chấp nhận input là số nguyên và 
# in ra "Đây là một số chẵn" nếu nó chẵn. Ngược lại in ra "Đây là một số chẵn"
print(f"{b} is a {ss8_module.evenNum(b)}")

# Viết hàm kiểm tra năm được truyền vào có phải là năm nhuận hay không? Yêu cầu kiểm tra năm đầu vào phải > 0.
year = 2024
flag = ss8_module.leapYear(year)
if flag==True:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Viết hàm tính tổng một array cho trước. Nếu trong array 
# tồn tại phần tử không phải là "số" thì bỏ qua phần tử đó.
arr = [1,2,3,4,"hi","hello world", True, 100]
print(f"Tong cua mang la {ss8_module.sumArray(arr)}")

# Viết một chương trình chấp nhập chuỗi từ người dùng nhập vào, phân tách nhau bởi dấu "," 
# và in những từ đó thành chuỗi theo thứ tự bảng chữ cái, phân tách nhau bởi dấu ","
chuoi = "Du, Lam, Vu, Khanh, Phong"
print(f"String after being organised is {ss8_module.sortString(chuoi)}")
    


