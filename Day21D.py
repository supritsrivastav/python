# FUNCTIONS ARGUMENTS 
# Function me information as a arguments pass hoga.Arguments hmm function name ke baad likhte hai 
# parenthesis ke andar hmm jitna chache uthne arguments add kar sakte comma lga kar ..
# So there are 4 types of arguments that we can provide in a function
# Default Aruguments:- In this case we can provide  default value while creating a function
# iss tarah agar hmm agar uss function me koi empty value diya ho ga tab wo defalt valueko assume kar lega 
# For Example:-
# def name(fname, mname="John", lname= "Whatson"):
#     print("Hello,",fname, mname, lname)
# name("Amy","Singh") # ab yha hmne last name nhi dala usne default last name utha liye 
# s middle name use nhi karte to wo default usekar leta same aapka first name ke saath bhi hoga..
# Keyword Arguments(named arguments):-isme hmm arguments ko as a key provide karte hai aur jo interpreter hoga wo argument ko uske parameter name se recognize karega.
# in this we can change the order of the arguments  
#  for example:-
# def name(fname,mname,lname):
#      print("Hello,",fname, mname ,lname)
#      name(mname ="Peter",lname="Wesker",fname ="jade")

# Variable length Argument(Arbitary keyword arguments):-Kabhi kabhi hme pta nhi hota ki kitne number of arguments pass honge 
# function me uss time par hmm arbitary arguments use karte hai . #Arbitary arguments allow us to pass a variying number of values during a fuction call.
 #   hmm *(asteric) use karte parameter name se pahle to denote this kind of arguments  
# Required Argument:- jab hmm koi abhi arguments key ya value ke saath  pass n kare tab ye jaruri ban jata hai ki sabhi arguments ko correct order me pass kare jo fuction ke actual order ko match kare 
# Example :-When number of arguments passed does not match to the actual function definition 
def name(fname,mname="Quill", lname="Singh"):
    print("Hello",fname,mname,lname)
    name("Peter","Quill","Singh")

