# Tuples:-Tuples is a collection of objects which is seperated by commas . difference is tuple is immutable but list is mutable..
# Creating tuples:- There are three ways tocreste the tuple are as given below
# 1- Using round Brackets
# To create a tuple we use the brackets()operator
var=("Suprit","are you ","good")
print(var)
# 2- With one item:-
# this is theanother way to create a tuple
values:tuple[int |str,...]=(1,2,3,4,"Suprit")
print(values)
# 3-Tuple Constructor:- To create a tuple with a tuple constructor , we will pass the elemnts as its parameters
tuple_constructor =tuple(("Suprit","are","you","good"))
print(tuple_constructor)

# Note:- Once the tuple is created we can not add, remove, or cannot extend the tuple
mytuple = (1, 2, 3, 4, 5)

# tuples are indexed
print(mytuple[1])
print(mytuple[4])

# tuples contain duplicate elements
mytuple = (1, 2, 3, 4, 2, 3)
print(mytuple)

# adding an element
# mytuple[1] = 100
# print(mytuple)
# Here can clearly see that error occours because tuple does not allow to add the items in it.

# Accessing the tuple using the positve and negative index 
i =("acv","ggh","hhh","lll")
print("Value in i[2]=",var[2])
print("Value in i[0]=",var[0])
print("Value in i[1]=",var[1])
print("Value in i[-2]=",var[-2])

# Different Operations Related to tuples
# Concatenation
# Nesting
# Repetition
#-------------------------- Slicing-----------------------------------------------------
# Slicing is done in the python by putting the colon and the element is returned by the range of n-1
#  i.e:-(0:2) but the element will be sliced from the 0 to 1...
#-------------------------- Deletion--------------------------------------------------
#----------------------- Finding the length--------------------------------------------
# By using the function     lenstr =len(str)
# --------------------Multiple Data Types With Tuples-----------------------------

# --------------------Conversion of List to the tuples--------------------------------
# ------------------------Tuples in a loop--------------------------------------------





