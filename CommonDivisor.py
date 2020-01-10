def getfirstnumber():
    return int(input("Enter the first positive integer: "))


def getsecondnumber():
    return int(input("Enter the second positive integer: "))


def calculations():
    largestdivisor = 0
    divisor = 1
    largest = 0
    num1 = getfirstnumber()
    num2 = getsecondnumber()
    if num1 > num2:
        largest = num1
    elif num2 > num1:
        largest = num2
    else:
        largest = num1
    for index in range(largest):
        divisor += 1
        if num1 % divisor == 0 and num2 % divisor == 0:
            largestdivisor = divisor
        else:
            continue

    print("The largest common divisor is " + str(largestdivisor))


if __name__ == "__main__":
    calculations()

