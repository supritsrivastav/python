# Taking the user input in Python
# Wecan take user input directly by using input() function
# Input function returns the value as string /character hence we have to typecast them whenever required to another datatype
# Syntax:-variable=input()
a = input()
print(a)
a = input()
print("My name is", a)
a = input("Enter your Name: ")
print("My name is", a)
x = input("Enter first Number:")
y = input("Enter Second Number:")
print(
    int(x) + int(y))  # yha par hmm int lga kar typecast kiye hai warna compiler string ke jaise treat karta NUMBERS ko
