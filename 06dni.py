# #Interview Programs
'''
1- Fibonacci Series
2- Prime Numbers
3- Palindrome
4- Factorials
5- Armstrong Numbers
6- Denomination of Currency 
'''

#1- Fibonacci Series

num=int(input("Enter range to which 'Fibonacci Series' should be printed: "))

i=0
j=1
for l in range(num):
    k=i+j
    print(f"{l+1}- {i}+{j}={k}")
    i=j
    j=k


#2- Prime Numbers

while True:
    optn=input("CHOOSE ANY ONE OPTION:\n 1- Check a number is prime or not\n 2- Display prime numbers between a range of numbers\n 3- Exit\n")
    if optn=='1':
        num1=int(input("Enter a number to check its prime or not: "))
        count=0
        if num1>0:
            for o in range(num1):
                if num1%(o+1)==0:
                    count+=1
                    
            if count>2:
                print(f'{num1} is not a Prime Number')
            else:
                print(f'{num1} is a prime number')
                
        elif num1==0:
            print('"0" is neither prime nor composite')
            
        else:
            print('Please enter numbers above "0"')
            
    elif optn=='2': 
        num2=int(input("Enter range to which prime numbers should be printed "))
        if num2>0:
            print('PRIME NUMBERS:\n')
            count=0
            for a in range(num2):
                for b in range(num2):
                    if (a+1)%(b+1)==0:
                        count+=1 
                if count==2: 
                    print(a+1)
                count=0
                
        elif num2==0:
            print('"0" is neither prime nor composite')
            
        else:
            print('Please enter numbers above "0"')
            
    elif optn=='3':
        print('Exit')
        break
        
    else:
        print('INVALID CHOICE')


#3- Palindrome

word=input('ENTER THE WORD: ')

r_word=word[::-1]
if word!=r_word:
    if word.lower()==r_word.lower():
        print(f'{word} is palindrome when all its char are converted to lowercase or uppercase')
    else:
        print(f'{word} is not a Palindrome')
        
elif word==r_word:
     print(f'{word} is palindrome')


#4- Factorials

fact=int(input('ENTER THE NUMBER: '))

ans=1
for i in range(fact):
    ans*=(i+1)
    
print(f'Factorial of {fact} is {ans}')


#5- Armstrong Numbers

num3=int(input('ENTER THE NUMBER: '))

num4=0
for i in range(len(str(num3))):
    num3=str(num3)
    num5=num3[i]
    num5=int(num5)
    num4+=(num5**3)
num3=int(num3)

if num3==num4:
    print(f'{num3} is an Armstrong Number')
else:
    print(f'{num3} is not an Armstrong Number')


#6- Denomination of Currency

note=int(input("ENTER THE AMOUNT: "))

n2000=note//2000
n500=(note%2000)//500
n200=((note%2000)%500)//200
n100=(((note%2000)%500)%200)//100
n50=((((note%2000)%500)%200)%100)//50
n20=(((((note%2000)%500)%200)%100)%50)//20
n10=((((((note%2000)%500)%200)%100)%50)%20)//10
n5=(((((((note%2000)%500)%200)%100)%50)%20)%10)//5
n2=((((((((note%2000)%500)%200)%100)%50)%20)%10)%5)//2
n1=(((((((((note%2000)%500)%200)%100)%50)%20)%10)%5)%2)//1

print(f"{note} INR HAS:\n {n2000}- 2000 INR note\n {n500}- 500 INR note\n {n200}- 200 INR note\n {n100}- 100 INR note\n {n50}- 50 INR note\n {n20}- 20 INR note\n {n10}- 10 INR note\n {n5}- 5 INR coin\n {n2}- 2 INR coin\n {n1}- 1 INR coin")
