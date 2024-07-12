def findNum(a, b):
    if a>b:
        return a
    elif a==b:
        return 
    else:
        return b

def evenNum(a):
    if a%int(a)==0:
        if a%2==0:
            return "even number"
        else:
            return "odd number"

def leapYear(a):
    if a>0:
        if a%100==0 and a%400==0:
            return True
        elif a%4==0:
            return True
        else:
            return False
    else:
        return "Undefined"


def sumArray(list):
    sum = 0
    for item in list:
        if type(item)=="int" or type(item)=="float":
            sum += item



def sortString(input_string):
    words = input_string.split(",")
    for i in range(len(words)):
        words[i] = words[i].strip()
    words.sort()
    output_string = ",".join(words)
    return output_string


