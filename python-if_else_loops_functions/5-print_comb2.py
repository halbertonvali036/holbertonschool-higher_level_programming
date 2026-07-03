#!/usr/bin/python3
for i in range(100):
    print("{:02d}".format(i), end="")
    if i < 99:
        print(", ", end="")
    if (i + 1) % 18 == 0:
        print("\n", end="")
print()
