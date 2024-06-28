# Guess the number given as input by the user, using Bisection Search.

#Doesn't the use user confirmation to give directions
num = int(input("Enter the number to be guessed: "))

low = 0
high = 100

if low <= num <= high:
    while True:
        guess = (low + high) // 2  # Calculate the midpoint as an integer

        if guess == num:
            print(f'The number is {guess}')
            break
        elif guess < num:
            low = guess + 1  # Adjust the lower bound
        else:
            high = guess - 1  # Adjust the upper bound

        if low > high:
            print("Number not found in the range [0-100].")
            break
else:
    print("Out of the range [0-100]")


#Make use of user confirmation to give directions
num = int(input("Enter the number to be guessed: "))

low = 0
high = 100

if low <= num <= high:
    while True:
        guess = (low + high) // 2
        print(f"Is the guessed number {guess} ?")
        optn=input("ENTER:\n 'h' if higher\n 'l' if lower\n 's' if yes\n")
        if optn=='s':
            print(f'The number is {guess}')
            break
        elif optn=='h':
            low = guess + 1
        elif optn=='l':
            high = guess - 1
        else:
            print('INVALID INPUT!')
else:
    print("Out of the range [0-100]")
