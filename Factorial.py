def Factorial(number):
    if number < 0:
        return ("False, number must be positive")

    total = 1
    long = range(1, number + 1)
    for i in long:
        total *= i
        return total


try:
    n = int(input("Enter a number: "))
    print(f"Factorial = {Factorial(n)}")
except ValueError:
    print("Input must be an integer")