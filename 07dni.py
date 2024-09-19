#Interview Programs
'''
1- Bubble Sort
2- Check given number is multiple is of a given number(multiplier) and find multiplicand
'''

#1- Bubble Sort

num = int(input("ENTER THE NUMBER OF ELEMENTS TO BE SORTED: "))
num_list = []

print("Enter the Elements: ")
for i in range(num):
    element = int(input(f"{i + 1} : "))  # Convert input to integer
    num_list.append(element)

# Sorting using bubble sort algorithm
for j in range(num):
    for i in range(num - 1):
        if num_list[i] > num_list[i + 1]:
            num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]

print("Sorted List:", num_list)

#2- Check given number is multiple is of a given number(multiplier) and find multiplicand

n = int(input("Enter the multiplier: "))
multiple_of_n = int(input(f"Enter the number to be checked if it's a multiple of {n}: "))

if multiple_of_n%n==0:
    print(f"{multiple_of_n} is multiple of {n} and the multiplicand is {multiple_of_n/n}")
else:
    print(f"{multiple_of_n} is not a multiple of {n}")
