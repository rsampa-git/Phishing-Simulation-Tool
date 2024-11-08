#FizzBuzz

#A function to print numbers from 1 to 100
def FizzBuzz():
    numbers = range(1, 101)
    for i in numbers:
        if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

FizzBuzz()
