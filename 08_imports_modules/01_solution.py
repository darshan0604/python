from math import sqrt
import random
from datetime import datetime, timezone, timedelta
import pandas as pd

result = sqrt(20)
print(result)

#random number between 1 and 100
random_number = random.randint(1, 100)
print(random_number)

#random choice from a list
random_choice = random.choice(['apple', 'banana', 'cherry'])
print(random_choice)

#current date and t ime
current_date = datetime.today()
print(current_date)


#pandas dataframe
result = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]})
print(result)
