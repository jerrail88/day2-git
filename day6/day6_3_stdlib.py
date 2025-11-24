# day6_3_stdlib.py

import math
import random
from datetime import datetime

# Math example
num = 16
print(f"Square root of {num} is {math.sqrt(num)}")

# Random example
rand_num = random.randint(1, 100)
print(f"Random number between 1 and 100: {rand_num}")

# Date/Time example
now = datetime.now()
print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
