# Bai 1
nums = [1,3,4,7,12]
input = int(input("Input a number: "))
if input in nums:
    print(nums.index(input) + 1)
else:
    print("Number not found")
# Bai 2
print(sum(nums))
# Bai 3
num0 = []
while True:
    i = int(input("Input a number: "))
    num0.append(i)
    if i == 0:
        break
print("Sum of numbers in list: ", sum(num0))
