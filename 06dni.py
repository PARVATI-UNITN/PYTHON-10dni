#!/usr/bin/env python
# coding: utf-8

# #Interview Programs
# '''
# 1- Fibonacci Series
# 2- Prime Numbers
# 3- Palindrome
# 4- Factorials
# 5- Armstrong Numbers
# 6- Matrix Multiplication
# 7- Alphabet Triangle
# '''

# In[9]:


#1- Fibonacci Series

num=int(input("Enter range to which 'Fibonacci Series' should be printed: "))

i=0
j=1
for l in range(num):
    k=i+j
    print(f"{l+1}- {i}+{j}={k}")
    i=j
    j=k


# In[15]:


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


# In[10]:


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


# In[5]:


#4- Factorials

fact=int(input('ENTER THE NUMBER: '))

ans=1
for i in range(fact):
    ans*=(i+1)
    
print(f'Factorial of {fact} is {ans}')


# In[26]:


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

