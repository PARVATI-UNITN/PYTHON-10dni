PYTHON-10dni

These are assignments that I undertake after watching tutorials from edX and Code with Harry tutorials on Introduction to Python. Doing so have greatly helped me in self-evaluating my skills and understanding.

1- 01dni: 

Python code for a calculator that does 4 arithematic operations on the basis of user's input and choice. This goes on as a loop until the user inputs the command to exit by choosing option 6.

2- 02dni:

Python code for verifing if the email is Google mail ID and is legit. For a mail to be legit it has to follow some conditions like it shouldn't have space in between, front or at back; it shouldn't 
have "." at end or at begining of username in an email (username@gmail.com); length of username should be between 6-30; if username has 8 charecters then at least one should be an alphabet. If any of 
these aren't true, then It will display "Not a legit ID" and the reason. Above this if the domain itself is not "gmail.com" then it displays "Not a Gmail ID. Maybe from some other Domain" and prints the 
domain given as  this is to verify the Google mail ID.

3- 03dni:

Simple temperature converter program in Python that converts temperatures between Celsius and Fahrenheit. Make use of mathematical formulas and  similar code that of calculater in 01dni.

4- 04dni:

Simple program that prints the number of times the string 'bob' occurs in str. For example, if str= 'azcbobobegghakl' then it shows 'bob' occurred 1 time. It make use of function count.

5- 05dni:

Consist of two ways first, doesn't use user confirmation to give directions. This uses an input checks if its with range ([0,100]-low=0, high=100) if not it prints 'Out of range'. If within the range then 
checks if its below or above the median of the range if found high it changes variable low=((low+high)//2)-1 else high=((low+high)//2)+1 and if its equal to the guessed number i.e.((low+high)//2) then 
print the number.

Second asks for user input if guess is the answer (key is 's'), or if if guess is higher than guess (key is 'h'), or if guess is less than guess (key is 'l') and rest, does other functions similar to first 
case.

6- 06dni:

Interview Programs

Fibonacci Series: The python code generates and prints the Fibonacci series up to a specified range entered by the user. It begins by prompting the user to input the range until which the Fibonacci series should 
be printed. Two variables, `i` and `j`, are initialized to 0 and 1 respectively, representing the first two numbers in the Fibonacci sequence. A `for` loop iterates `num` times, where `num` is the user-input range. 
In each iteration, the next Fibonacci number `k` is computed by adding `i` and `j`. The current Fibonacci numbers `i` and `j` are then updated for the next iteration. The Fibonacci numbers are printed in a formatted 
string that shows the sequence index (`l+1`), the current Fibonacci numbers (`i` and `j`), and their sum (`k`). This loop continues until the specified range is reached, effectively displaying the Fibonacci series 
as requested by the user.

Prime Numbers: The python code presents a menu-driven program that continuously prompts the user to choose from three options: checking if a number is prime (`optn=='1'`), displaying prime numbers within a specified 
range (`optn=='2'`), or exiting the program (`optn=='3'`). When the user selects option `1`, they input a number (`num1`) to be checked for primality using a loop that counts its divisors. If `num1` has more than 
two divisors, it prints that it is not prime; otherwise, it declares it as prime. Option `2` prompts for a range (`num2`) and prints all prime numbers within that range using nested loops to count divisors for 
each number in the range. Option `3` exits the program when chosen. Any other input displays "INVALID CHOICE". The program handles edge cases such as checking if zero is entered, stating it is neither prime nor 
composite, and prompts the user to enter numbers above zero if they input a negative number.

Palindrome: The python code checks whether a word entered by the user is a palindrome. It first reads the word input and creates a reversed version of it (`r_word`) using Python's slicing feature (`word[::-1]`). 
It then compares the original word (`word`) with its reversed version (`r_word`). If they are not identical (`word != r_word`), it further checks if they are palindromes when case is ignored (`word.lower() ==
r_word.lower()`). If this condition is true, it prints that the word is a palindrome when considering case insensitivity. If neither condition holds true, it concludes that the word is not a palindrome. If the original
word is identical to its reversed version (`word == r_word`), it directly prints that the word is a palindrome. This script efficiently determines if a word is a palindrome, considering both case-sensitive and case
insensitive criteria.

Factorials: The python code computes the factorial of a number entered by the user. It begins by prompting the user to input a number (`fact`) for which the factorial needs to be calculated. It initializes `ans` to 1,
which will store the factorial result. Using a `for` loop that iterates from 0 to `fact-1`, it repeatedly multiplies `ans` by the current value of `i+1` (which represents the sequence of numbers from 1 to `fact`). After
completing the loop, it prints the computed factorial of `fact` using a formatted string that displays the original number and its factorial value. This script efficiently calculates factorials by iteratively multiplying
values, producing the factorial result for any non-negative integer input by the user.

Armstrong Numbers: In this it checks if a number entered by the user is an Armstrong number. An Armstrong number (or narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of
the number of digits. The script begins by prompting the user to input a number (`num3`). It then converts this number to a string (`num3=str(num3)`) to iterate over each digit using a `for` loop. Within the loop, each 
digit (`num5`) is converted back to an integer and raised to the power of 3 (`num5**3`), accumulating the sum in `num4`. After the loop, `num3` is converted back to an integer and compared to `num4`. If they are equal, 
the script prints that the number is an Armstrong number; otherwise, it states that it is not. This script effectively determines whether a given number satisfies the Armstrong number condition using straightforward 
iteration and arithmetic operations.

Denomination of Currency: This code prompts the user to input an amount in Indian Rupees and calculates how many notes and coins of various denominations (2000, 500, 200, 100, 50, 20, 10, 5, 2, and 1 INR)
are needed to represent that amount. It uses integer division and the modulus operator to determine the number of each denomination step-by-step, breaking down the remaining amount as it processes each note or coin.
Finally, it outputs the total amount alongside the count of each denomination, formatted for clarity, making it easy for users to see how the total is composed.

7- 07dni:

Interview Program

Bubble Sort: The program first asks the user how many elements they want to sort. It then prompts the user to enter each element one by one. Then the program sorts the list using the Bubble Sort algorithm. Bubble Sort
works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order. This process repeats until the list is sorted. The outer loop runs num times to ensure all
elements are sorted. The inner loop runs from the start of the list to the second-last element (num - 1), comparing each element with the next one. If an element is greater than the next one, they are swapped and finally,
the sorted list is printed.

Check given number is multiple is of a given number(multiplier) and find multiplicand: The code is to check whether a given number is a multiple of another specified number, referred to as the multiplier, and, if so,
determine the multiplicand. The user first inputs the multiplier, `n`, and then the number to be checked, `multiple_of_n`. The program then evaluates whether `multiple_of_n` is divisible by `n` without a remainder using
the modulus operator (`%`). If the result is zero, it confirms that `multiple_of_n` is indeed a multiple of `n` and calculates the multiplicand by dividing `multiple_of_n` by `n`. It then prints a message stating that
`multiple_of_n` is a multiple of `n` and displays the multiplicand. If the number is not a multiple, the program outputs a message stating that `multiple_of_n` is not a multiple of `n`. This code effectively checks for
divisibility and provides the factor relationship between the two numbers.

Check the Leap Year: The code checks if a user-inputted year is a leap year and whether it is a century year. First, the user is prompted to enter a year, which is then stored as an integer in the `year` variable. The
code then determines if the year is a century year by checking if it is divisible by 100. If it is, it further checks if it is also divisible by 400. A year divisible by both 100 and 400 is a leap year, while a century
year not divisible by 400 is not a leap year. If the year is not a century year, the code checks if it is divisible by 4, in which case it is a leap year. Otherwise, it is not a leap year. The result is printed
accordingly. The final line of the code performs a simple division, printing the result of `6 / 2`, which is `3.0`.

8- 08dni:

This code calculates the volume of a cube based on user input. It first prompts the user to enter the length of a side of the cube using the `input()` function, which captures the value as a string. The `float()` function
then converts this input to a floating-point number for precision. The volume of the cube is calculated by raising the side length to the power of 3 using the `**` operator. Finally, the result is printed to the console
with the message 'Volume of cube is', followed by the calculated volume.

9- 09dni:

This code calculates the simple interest based on user-provided values for the principal amount, number of years, and rate of interest. It first prompts the user to input the principal amount (`p`), the number of years
(`n`), and the rate of interest (`r`). The principal and number of years are converted to floating-point numbers using `float()` for precision, while the rate of interest is converted to an integer using `int()`. The
simple interest is then calculated using the formula  SI = P × R × T / 100. Finally, the calculated simple interest (`si`) is printed to the console with the message 'Simple Interest is'.

10- 10dni:

i: In the first program prompts the user to enter a time value in seconds and then calculates the equivalent hours, minutes, and remaining seconds. It begins by determining the number of hours using
integer division of the total seconds by 3600, which represents the total seconds in one hour. It then calculates the remaining seconds after extracting the hours, and from these remaining seconds, it computes the number
of minutes using integer division by 60. Finally, it uses the modulus operator to find the leftover seconds that do not form a complete minute. The results are printed in a clear format, indicating how many hours,
minutes, and seconds correspond to the input value.

ii: The second code also converts seconds into hours, minutes, and seconds but takes a slightly different approach. After the user inputs the total time in seconds, it first calculates the total minutes by
performing integer division of the seconds by 60. It then finds the remaining seconds using the modulus operator. Next, it calculates the number of hours by dividing the total minutes by 60 and determines the remaining
minutes using the modulus operator again. The final output is formatted using an f-string, which enhances readability by neatly presenting the calculated hours, minutes, and seconds in a single line. This method also
effectively communicates the time conversion, ensuring clarity for the user.
