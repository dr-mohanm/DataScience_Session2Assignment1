
# coding: utf-8

# In[2]:


# 1. Write a program which accepts a sequence of comma-separated numbers from console and generate a list

# Accept input from user in the console using input function, split it by comma and store in the variable L.
# print it using list format.

L = input('Enter numbers with commas delimiter').split(',')
print(list(L))


# In[3]:


# 2.  Create the below pattern using nested for loop in Python. 
#         *  
#         * *  
#         * * * 
#         * * * * 
#         * * * * * 
#         * * * * 
#         * * * 
#         * *
#         *

# Declare a variable and assign value as 5. since we need the maximum of 5 stars.
# First for loop in the Top Pattern iterates i for 5 times in incremental order and the inner for loop executes multiple times
# based on the i value.Bottom Pattern decrement by 1 until end of loop.


X = 5;
# TOP Pattern
for i in range(0,X):
    for j in range(0,i):
        print ('* ', end="")
    print('')
# Bottom pattern
for i in range(X,0,-1):
    for j in range(0,i):
        print('* ', end="")
    print('')


# In[4]:


# 3.  Write a Python program to reverse a word after accepting the input from the user.
# [::-1] clones it in reversed order.
word = input("Input a word to reverse: ")
word[::-1]


# In[6]:


# 4.  Write a Python Program to print the given string in the format specified in the ​sample output. 
# WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC 
# REPUBLIC and to secure to all its citizens 
#Sample Output: 
# WE, THE PEOPLE OF INDIA,   
#       having solemnly resolved to constitute India into a SOVEREIGN, !  
#              SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC    
#               and to secure to all its citizens

# print the values using \n for next line and \t for tab.

print("WE, THE PEOPLE OF INDIA, \n\thaving solemnly resolved to constitute India into a SOVEREIGN, !       \n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t\tand to secure to all its citizens")

