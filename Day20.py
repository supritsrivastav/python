# FUNCTIONS AND ARGUMENTS IN PYTHON
# Python Functions is a block of statements that return the specific task. 
# The idea is to put some commonly or repeatedly done tasks together and make 
# a function so that instead of writing the same code again and again ..
# for different inputs, we can do the function calls to reuse code contained 
# in it over and over again..
# Lets take an example :- A function is taking out the geometric mean of two numbers
a=8
b=9
# maanlo hmko function banana hai gmean ko toh 
def CalculateGmean(a,b):
 mean=(a*b)/(a+b)
 print(mean)
 CalculateGmean(a,b)
def isGreater(c,d):
 c=10
 d=5
if(a>b):
     print("First number is Greater ") 
else:
        print("Second number is greater or equal") 

        
     # *args is a function stores all the other variables other than first variable in it as a tuple 
# **kwargs used to store the key values in it i.e Dictionaries 
# Format :- def function name{a,*args,**kwargs}  
        
         