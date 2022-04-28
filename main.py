import math


def function_1(n):
    formula = lambda x: (float(n + 1) - 3) / math.pow(float(n + 1), 2)
    total = 0
    for i in range(n):
        total += formula(n)

    return total


result = 1


def function_2(n):
    global result

    result *= ((float(n) / (float(n) + 2)) - 10)

    if n > 1:
        function_2(n - 1)


number = int(input("Please enter a number to calculate first equation: "))
print(function_1(number))

number = int(input("Please enter a second number to calculate second equation: "))
function_2(number)
print(result)
