# IF Else Condinational Satatement
# IF Else Statement  supports the conditional operators. i.e condinational operators checks wheter the given conditon is true or false
# and provides the results accordingly..
# a=int(input("Enter your Age: "))
# print("Your Age is" ,a)
# print(a==18)# Equals: a == b 
# print(a!=18)# Not Equals: a != b
# print(a<18)# Less than: a < b
# print(a<=18)# Less than or equal to: a <= b
# print(a>18)# Greater than: a > b
# print(a>=18)# Greater than or equal to: a >= b

# if(a>18):
#     print("You can Drive")
# else:
#     print("You cannot Drive")

# Python if…elif…else Statement
# The if...else statement is used to execute a block of code among two alternatives.

# However, if we need to make a choice between more than two alternatives, we use the if...elif...else statement.

# Syntax

# if condition1:
#     # code block 1

# elif condition2:
#     # code block 2

# else: 
#     # code block 3
# if condition1 - This checks if condition1 is True. If it is, the program executes code block 1.
# elif condition2 - If condition1 is not True, the program checks condition2. If condition2 is True, it executes code block 2.
# else - If neither condition1 nor condition2 is True, the program defaults to executing code block 3
# b=int(input("Enter the number: " ))
# if(b>0):
#     print("Number is Positive")
# elif(b<0):
#     print("Number is Negative") 
# else:
#    print("Number is Neutral")   
   
# NESTED IF ELSE STATEMENTS
# IN Python the nesting is done by using indentation(blankspace)
# i.e agar hmm koi if statement likh rhe hai toh nested if upar wale if statement ke andar hi aayega
# nested if me ek indentation(blankspace) jyda ho jaayega.
# Python me indentation blank space hota hai whi java me curly braces hota hai{}.

d=int(input("Enter the number: " ))
if(d>5):
    print("d isthe bigger number")
 # inner if statement
    if(d<15):
     print("d is between 5 and 15")
     # inner else statement
    else:
     print("d is between 0 and 5")
# outer else statement     
else:
        print("d is neative")
        
