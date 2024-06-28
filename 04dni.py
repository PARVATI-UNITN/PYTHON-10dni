# Simple program for Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

st=input("INPUT A STRING CONTAINING 'bob' (like-bobis,juhwdhxjbobsiolkwkmbobnjs)\n")

times=st.count("bob")
if times!=0:
    print(f"Number of times the string 'bob' occurs is {times} times")
else:
    print(f"String 'bob' doesn't occur")
