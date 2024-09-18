#Interview Programs
'''
1- Bubble Sort
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
