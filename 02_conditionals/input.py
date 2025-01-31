# userscore = input("Write Score -> ")
# print(int(userscore)/20)

# userscore = int(input("Write Score -> "))
# print(userscore/20)

age = int(input("Write your age -> "))

if age < 13:
    print("Child")
elif age <= 19 and age >= 13:
    print("Teenager")
elif age <= 60:
    print("Adult")
else:
    print("Senior")
    
