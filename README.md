PYTHOB-10dni

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
It then compares the original word (`word`) with its reversed version (`r_word`). If they are not identical (`word != r_word`), it further checks if they are palindromes when case is ignored (`word.lower() == r_word.lower()`). 
If this condition is true, it prints that the word is a palindrome when considering case insensitivity. If neither condition holds true, it concludes that the word is not a palindrome. If the original word is identical to 
its reversed version (`word == r_word`), it directly prints that the word is a palindrome. This script efficiently determines if a word is a palindrome, considering both case-sensitive and case-insensitive criteria.

Factorials: The python code computes the factorial of a number entered by the user. It begins by prompting the user to input a number (`fact`) for which the factorial needs to be calculated. It initializes `ans` to 1, which 
will store the factorial result. Using a `for` loop that iterates from 0 to `fact-1`, it repeatedly multiplies `ans` by the current value of `i+1` (which represents the sequence of numbers from 1 to `fact`). After completing 
the loop, it prints the computed factorial of `fact` using a formatted string that displays the original number and its factorial value. This script efficiently calculates factorials by iteratively multiplying values, 
producing the factorial result for any non-negative integer input by the user.

Armstrong Numbers: In this it checks if a number entered by the user is an Armstrong number. An Armstrong number (or narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of
the number of digits. The script begins by prompting the user to input a number (`num3`). It then converts this number to a string (`num3=str(num3)`) to iterate over each digit using a `for` loop. Within the loop, each 
digit (`num5`) is converted back to an integer and raised to the power of 3 (`num5**3`), accumulating the sum in `num4`. After the loop, `num3` is converted back to an integer and compared to `num4`. If they are equal, 
the script prints that the number is an Armstrong number; otherwise, it states that it is not. This script effectively determines whether a given number satisfies the Armstrong number condition using straightforward 
iteration and arithmetic operations.

7- 07dni:

Interview Program

Bubble Sort: The program first asks the user how many elements they want to sort. It then prompts the user to enter each element one by one. Then the program sorts the list using the Bubble Sort algorithm. Bubble Sort works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order. This process repeats until the list is sorted. The outer loop runs num times to ensure all elements are sorted. The inner loop runs from the start of the list to the second-last element (num - 1), comparing each element with the next one. If an element is greater than the next one, they are swapped and finally, the sorted list is printed.

8- 08dni:

9- 09dni:

10- 10dni:
