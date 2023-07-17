#!/usr/bin/env python3
import sys
import os
# EAFP - Easy to Ask Forgiveness than Permission

try:
    name = open("names.txt").readlines() # FileNotFoundError
    1 / 0 # ZeroDivisionError
    print(name.banana) # AttibuteError
except FileNotFoundError as e:
    print(f"[Error] {str(e)}.")
    sys.exit(1)
except ZeroDivisionError:
    print("[Error] You can't divide by zero!")
    sys.exit(1)
except AttributeError:
    print("[Error] List doesn't have banana!!!")
    sys.exit(1)
else:
    print("Only execute if there are no Error!!!")
finally:
    print("Always execute this step")

