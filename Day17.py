# Loops In Python:- Loops are useful because they help you not write the same code many times.
# While Loop:-is loop me block of code tabtak execute hogajab tak hmara
#code satisfed ho rha hoga.jaise hi condition unsatisfied hua meantime par codehmara execute hona band ho jaayega..
# for example
i = 0                          # pahle variable ko initialsie karenge phir 
while (i< 3):                  # while condition lagayenge
    i = i+ 1                   #isme maine increment kiya hai varible ko 
    print("Hello Suprit is it you") #Print karwadiya ab
# iss code me hmara code bass teen baar hi run hoga..

# Else Statement with while loop(Doubt with this topic)
# Python program to show how to use else statement with the while loop  
j = 0  
  
# Iterating through the while loop  
while (j< 4):      
    j =j+ 1  
    print("Python Loops") # Executed untile condition is met  
# Once the condition of while loop gives False this statement will be executed  
else:  
    print("Code block inside the else statement")
    # doubts ye hai ki Condition true hone par bhi else print ho rha hai aur false par bhi
    
# FOR LOOP :-n Python, a for loop is used to iterate over sequences such as lists, strings, tuples, etc.
# "for loop" in Python is like going through a list of things one by one. It's like saying,
# "Do something (defined by the programmer) with each item in this list..
numbers = [4, 2, 6, 7, 3, 5, 8, 10, 6, 1, 9, 2]  
  
# variable to store the square of the number  
square = 0  
  
# Creating an empty list  
squares = []  
  
# Creating a for loop  
for value in numbers:  
    square = value ** 2  
    squares.append(square)  
print("The list of squares is", squares)
                               # DO WHILE LOOP
#  do while loop ek baar to chalega hi irrespective of condition true hai ya false hai
# Aur agli loop tabhi chalegi jab condition true hoga..
#  To Create a Do while loop in python 
#  We can create do while loop by modifing the WHILE LOOP through a technique 
# by using infinte whileloop with a break statement wrapped in an if statement
# that checks a given condition and breaks the iteration if that condition is true...
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break

                     #   Countiue and Break  Statement
# Break Statement means loop ko chodkar nikal jata hai 
for i in range(15):
 if(i==10):
     print("this itteration is skipped")
     break
 print("5X",i,"=",5*i)#ab isme jaise hi i==10 hua ye loop se hi bahar aagya
# Coutinue Statement Means iteration ko chodkar nikal jaao
# i.e sirf ek hi iteration skip next iteration execute toh hoga hi jitna range diya hoga ..
#  EXAMPLES:-
# for i in range(15):
#  if(i==10):
#      print("this itteration is skipped")
#      continue
#  print("5X",i,"=",5*i)