#indexing
str = "Darshan soni"
first_char = str[0]
print(first_char)

#Slicing
slice = str[0:7]
print(slice)
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

#find specific word
chai = "Masala Chai Chai Chai"
print(chai.find("Chai"))
print(chai.count("Chai"))


#place holders for variables
message = "Hello {}, I wanna talk with {}"
print(message.format('Darshan', 'kumari'))

#single letter usig for loop
for letter in chai:
    print(letter)
    
#quotes issue resolved for using quotes in string use \
chai = "she said , \"i love coffee then i blocked her\"" 
print(chai)