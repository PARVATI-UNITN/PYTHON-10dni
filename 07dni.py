#Interview Programs
'''
1- Bubble Sort
2- Check given number is multiple is of a given number(multiplier) and find multiplicand
3- Check the Leap Year
4- Perfect numbers between 100
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


#3- Check the Leap Year 

year=int(input("ENTER THE YEAR TO BE CHECKED (LEAP-YEAR OR NOT): "))
if year%100==0:
    print(f"THE YEAR {year} IS A CENTUARY",end=" ")
    if year%400==0:
        print(f"AND IS A LEAP YEAR.")
    else:
        print(f"AND IS NOT A LEAP YEAR.")
elif year%4==0:
    print(f"THE YEAR {year} IS A LEAP YEAR.")
else:
    print(f"THE YEAR {year} IS NOT LEAP YEAR.")

print(6/2)


#4- Perfect numbers between 100

for i in range(1,100):
    f = 0
    for j in range(1, i):
        if i % j == 0:
            f = f + j
    if i == f:
        print(f"{f} PERFECT NUMBER")
    else:
        print(f'{i} NOT PERFECT NUMBER')
