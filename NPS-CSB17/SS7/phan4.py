# Bai 1
nums = [5, 1, 8, 92, 7, 30]
for item in nums:
    if item%2==0:
        print(item)

# Bai 2
num0 = []
while True:
    i = int(input("Input a number: "))
    num0.append(i)
    if i == 0:
        break
for item in num0:
    if item%2==0:
        print(item)