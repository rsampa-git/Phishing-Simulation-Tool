def sum_to_n(n):
    total = 0
    for i in range(1, n+1):
        total +=i
    return total

#Example
n = int(input("Enter the number n: "))
print(sum_to_n(n))