# LIST IN PYTHON
# List is a collection of datatypes it can store different types i.e(integers,Strings,as well as objects) of data in it .
# list is also called sequence data type.
# List are mutables and it can be altered or modified even after its creation 
# In python list are simply created by placing the sequence inside the square brackets[]
# Help command is used to know the class of the list 
# Storing the matrix we have to use the multidimensional list...
# Shallow copy impact the modification of upper level 
# Deep copy impact the modification of lower level
# # var =["Dfffd","gggg","hhh"]
# print(var)
# Creating a list of numbers
# List =[10,20,30,40,50,60,70]
# print(List)
# Creating a list of string and access using it by the index
# list1=["abc","cde","rbc","vbn"]
# print("List items")
# print(List[0])
# print(List[1])
# print(List[2])
# hmm list ke elements ko ek ek karke access kar sakte by simply mentioning the idex number 
# insisde the print(List[index number])..

# Creating a list with mixed type of list
List2=[12,34,"Hello","Shivam",67,87]
print("list2 items ")
print(List2[1])
print(List2[2])
print(List2[4])
print(List2[3])
# Creating a list with mixed type of list and accessing a element from multidimensional list
List =[[1,4,5],["DDD","GGG","HHH"]]
print(List[1][2])
# Negative Indexing
#  In Python, negative sequence indexes represent positions 
# from the end of the List.
# Negative indexing means beginning from the end, -1 refers
# to the last item, -2 refers to the second-last item, etc.
# for Example
List=[1,2,"fff","gg","kk",4]
print(List[-3])# jaise yha par hme last se thesra access karna tha toh indexing me hmm -3 likha aur hme mil bhi gya
print(len(List))
# Finding the length of the List
# So to find the length of the list we use the
# (len) function
# Creating a List
List1 = []
print(len(List1))

# Creating a List of numbers
List2 = [10, 20, 14]
print(len(List2))

# Taking the input in List
# We can take the input of a list of elemnts as a strings,integer float etc
# But the drfault one is string
# input the list as a string
string =input("Enter elements (space-seperated):") 
list =string.split()
print("The list is :", list)


# Adding Elements to List :-Elements are added to thelist by using the append function i.eappend().
# only one elements at a time is added to the list by using the append function and ,for the addition of multiple elements to the list with the append() method loops are used .
# Tuples and List are also can be addedto exiting list by using append () function..
# append method() only works for the adddition of elements at the end of the list ..  
# For Example:-
# Creating a list
List=[]
print("Intialblank List: ")
print(List)

# Addition of Elements in the List
# List.append(1)
# List.append(2)
# List.append(3)
# print("List after adddition of1-3:")
# print(List)

# # Addition elements to the list using iterator 
# for i in range(1,5):
#     List.append(i)
#     print("List after addition elements from 1-4:")
#     print(List)
#     # Adding Tuples to list  (Doubt)
#     # List.append((5,7))
#     # print("\nList after adding the tuple to the list: ")
#     # print(List)
    
#     # Adding of list to a List
#     List2= ['For','Geeks']
#     List.append(List2)
#     print("\nList after addition of a List : ")
#     print(List)

# Using the insert method we can also add
# Whileusing the insert function we can add elements at the desired position 
# insert() method requires two arguments i.e (position,value).
# List=[1,2,3,4]
# print("Starting theList ")
# print(List)
# # Now We insert the list using thew insert method
# List.insert(3,12)
# List.insert(2,"Greek")

# print("Updated list after using the insert method")
# print (List)#ab yha par 3 ke baad12 insert hogya ..

# List.insert(4,"Suprit is goodboy")
# print(List)

# Another method is using extend() method 
# By using this method we can use multiple elements at the same time at the end of the list
# for example
# List=[1,2,3,4,5,6]
# print("This is the intial list:")
# List.extend([8,'Suprit are you good ','Always'])
# print("Updated List: ")
# print(List)

            #   Reversing a list
#In python reversing a list is done by using the reverse() method
  # Reversing a list
# mylist = [1, 2, 3, 4, 5, 'Geek', 'Python']
# mylist.reverse()
# print(mylist)
# # The reversed() function returns a reverse iterator, which can be 
# # converted to a list using the list() function. 
# my_list = [1, 2, 3, 4, 5]
# reversed_list = list(reversed(my_list))
# print(reversed_list)
            #  Removing Elements from the list
# M1:- using the remove()method
# In this elements can be removed from the list by usingthe remove function but it can threough if the element is not present in the list .it removes only one elements at a time to remove the range of the element we haveto use the iterator..
List=[1,3,5,7,9]

print("This is the intial  list")
print(List)
# Removing the element from the list using the remove method
List.remove(5)
List.remove(3)
print("Updated List:")
print(List)
# Removing the range of element by using iterator
# Creating a List
List = [1, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 11, 12]
# Removing elements from List
# using iterator method
# for i in range(1, 5):
#     List.remove(i)
# print("\nList after Removing a range of elements: ")
# print(List)
# # M2:- using the pop()function
# # it removes only the last element of the list,
# # to remove an element from a specific position of the List, the index of the element is passed as an argument to the pop() method.
List = [1, 2, 3, 4, 5]

# Removing element from the
# Set using the pop() method
List.pop()
print("\nList after popping an element: ")
print(List)

# Removing element at a
# specific location from the
# Set using the pop() method
List.pop(2)
print("\nList after popping a specific element: ")
print(List)


#Where are lists used in Python?
# Lists are used in Python to store collections of items, such as numbers, strings, or other objects. They are commonly used for:

# Storing and manipulating sequences of data.
# Aggregating items to iterate over them.
# Collecting multiple items as a single variable.
# Data manipulation and analysis.
# How to create a Python list?
# Lists are created using square brackets [] and separating items with commas.

# my_list = [1, 2, 3, 'apple', 'banana']
# How to call a list in Python?
# You call (access) a list by referencing its variable name and can access elements using index positions.
# Slicing operation in python  through shalow function
# #--------Deep Copy :-It helps in preserving the data.
# import copy
# listA = [2, 4, 6, [1, 3]]
# listB = copy.deepcopy(listA)
# showDetails(listA,listB)
# listB[1] = 44
# listB[3][0] = 55
# showDetails(listA,listB)