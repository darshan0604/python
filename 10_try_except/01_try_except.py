try:
    result = 10 / 2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("This will always run, regardless of exceptions.")