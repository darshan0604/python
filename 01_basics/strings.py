str = "Darshan soni"

first_char = str[0]
print(first_char)

slice = str[0:7]
print(slice)

#Slicing
num_list = "0123456789"
print(num_list[0:8:2])
print(num_list[8:0:-2])

#Strip for extra spaces
name = "    Darshan Soni    "
print(name.strip())

#slipt
chai = "Lemon, Ginger, Masala, Adrak, Choclate"
print(chai.split()) #default split case
print(chai.split(", ")) #on paremeter