# # userscore = input("Write Score -> ")
# # print(int(userscore)/20)

# # userscore = int(input("Write Score -> "))
# # print(userscore/20)

# #Solution 1
# age = int(input("Write your age -> "))

# if age < 13:
#     print("Child")
# elif age <= 19 and age >= 13:
#     print("Teenager")
# elif age <= 60:
#     print("Adult")
# else:
#     print("Senior")
    
# #solution 2
# #ternary operator
# price = 12 if age >= 18 else 8

# day = "Wednesday"
# if day == "Wednesday":
#     # price = price - 2
#     price -= 2

# print("Ticket price for you is $", price)

# #Solution 3
# score = int(input("Enter Percentage -> "))


# if(score >= 100 or score <= 0):    
#     print("Percentage Should be Under 100 and higher 0")
#     exit()
    
# if(score >= 90):
#     print("A Grade")
# elif(score >= 70):
#     print("B Grade")
# elif(score >= 50):
#     print("C Grade")
# elif(score >= 35):
#     print("D Grade")

#solution4
#fruit = "Mango"
#color = "Orange"

#  sure if fruit = "Mango": 'Yes' else: "No"
#Something

# #leap year

year = int(input("Type year -> "))

if(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
    print(year,"Leap Year")
else:
    print(year,"Not a leap year")