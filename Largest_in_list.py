def Largest_in_list(List):
    Max_num = List[0]

    for num in List:
        if num > Max_num:
            Max_num = num

    return Max_num

List = list(input("Enter a list of numbers: "))
print(f"Largest number = {Largest_in_list(List)}")