#List
tea_varities = ['Masala', 'Adrak', 'Lemon']
print(tea_varities[1])
print(tea_varities[0:3])

#Replace String
tea_varities[0:1] = ['Chochlate']
print(tea_varities[0:3])

# for tea in tea_varities:
#     print(tea, end="-")

#removing
print(tea_varities.pop())
print(tea_varities.remove("Adrak"))

#inserting
tea_varities.insert(1, "green") 
print(tea_varities)


# print(tea_varities.pop())
tea_varities_copy = tea_varities.copy()
tea_varities_copy.insert(4, "black") 

print(tea_varities_copy)

#amazing
squared_num = [x**2 for x in range(10)]
print(squared_num)