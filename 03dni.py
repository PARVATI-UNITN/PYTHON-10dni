#!/usr/bin/env python
# coding: utf-8

# Simple temperature converter program in Python that converts temperatures between Celsius and Fahrenheit.

# In[1]:


print('CHOSSE ANY OF THE BELOW OPTION: ')
print('1- Celsius to Fahrenheit\n2- Fahrenheit to Celsius\n3- Exit\n')
while True:
    option=input("My choice is: ")
    print('\n')
    if option=='1':
        print('Celsius to Fahrenheit')
        Cc=int(input('Enter Celsius value: '))
        Fc=(9/5) * Cc + 32
        print(f'For {Cc}C the Fahrenheit value is {Fc}F')
        
    elif option=='2':
        print('Fahrenheit to Celsius')
        Ff=int(input('Enter Fahrenheit value: '))
        Cf=(5/9) * (Ff - 32)
        print(f'For {Ff}F the Celsius value is {Cf}C')
        
    elif option=='3':
        print('Exit')
        break
        
    else:
        print('Invalid Choice :(')


# In[ ]:




