#!/usr/bin/python3
import random

number = random.randint(-10, 10)

if number > 0:
    print(f"{number} musbetdir")
elif number == 0:
    print(f"{number} sifirdir")
else:
    print(f"{number} menfidir")
