# ==============================================================================
# PYTHON COMPLETE CRASH COURSE
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. SYNTAX, OUTPUT, COMMENTS & VARIABLES
# ------------------------------------------------------------------------------
print("=== 1. SYNTAX, OUTPUT, COMMENTS & VARIABLES ===")

# This is a single-line comment

"""
This is a multi-line comment / docstring.
None of this code will run.
"""

# Variable assignment
x = 10
name = "Alice"
is_active = True

print("Hello, World!")
print(f"Name: {name}, Initial X: {x}, Active: {is_active}")

# Dynamic Typing (Variables can change types)
x = "Now I am a string!"
print("Updated X:", x)
print("-" * 50)


# ------------------------------------------------------------------------------
# 2. DATA TYPES, NUMBERS & CASTING
# ------------------------------------------------------------------------------
print("\n=== 2. DATA TYPES, NUMBERS & CASTING ===")

# Numbers
a = 10         # int
b = 3.14       # float
c = 1 + 2j     # complex

print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))

# Type Casting (Converting between types)
float_from_int = float(5)     # Converts 5 to 5.0
int_from_float = int(2.8)     # Converts 2.8 to 2 (truncates decimal)
str_from_int   = str(100)     # Converts 100 to "100"

print("Casting Results:", float_from_int, int_from_float, str_from_int)
print("-" * 50)


# ------------------------------------------------------------------------------
# 3. STRINGS & BOOLEANS
# ------------------------------------------------------------------------------
print("\n=== 3. STRINGS & BOOLEANS ===")

text = "  Python Programming  "

print("Original text:", repr(text))
print("Stripped:", text.strip())              # Removes padding spaces
print("Lowercase:", text.lower())             # Converts to lowercase
print("Replaced:", text.replace("P", "J"))    # Replaces 'P' with 'J'
print("Length:", len(text))                   # Character count

# String Slicing [start:end] (end index is excluded)
clean_text = text.strip()
print("Sliced (0 to 6):", clean_text[0:6])

# Booleans
is_valid = True
print("Comparison (10 > 5):", 10 > 5)
print("Empty string bool:", bool(""))         # Evaluates to False
print("Non-empty list bool:", bool([1, 2]))   # Evaluates to True
print("-" * 50)


# ------------------------------------------------------------------------------
# 4. OPERATORS
# ------------------------------------------------------------------------------
print("\n=== 4. OPERATORS ===")

# Arithmetic
print("Addition (10 + 5):", 10 + 5)
print("Division (10 / 3):", 10 / 3)           # Float division
print("Floor Division (10 // 3):", 10 // 3)   # Truncates decimal
print("Modulus / Remainder (10 % 3):", 10 % 3)
print("Exponentiation (2 ** 3):", 2 ** 3)     # 2 to the power of 3

# Comparison & Logical
num = 7
print("Is num equal to 7?:", num == 7)
print("Logical AND (num > 5 and num < 10):", num > 5 and num < 10)
print("Logical NOT (not(num == 7)):", not (num == 7))
print("-" * 50)


# ------------------------------------------------------------------------------
# 5. CORE DATA STRUCTURES (Lists, Tuples, Sets, Dictionaries)
# ------------------------------------------------------------------------------
print("\n=== 5. CORE DATA STRUCTURES ===")

# LIST (Ordered, Mutable, Allows Duplicates)
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits[1] = "blueberry"
print("List:", fruits)

# TUPLE (Ordered, Immutable, Allows Duplicates)
coordinates = (10.0, 20.0)
print("Tuple item at index 0:", coordinates[0])
# coordinates[0] = 15.0  <-- This would raise a TypeError because tuples cannot change!

# SET (Unordered, Mutable, No Duplicates Allowed)
unique_ids = {101, 102, 103, 101, 101}
unique_ids.add(104)
print("Set (Notice duplicates are removed):", unique_ids)

# DICTIONARY (Key-Value Pairs, Mutable, Ordered in Python 3.7+)
user = {
    "username": "coder123",
    "role": "Admin",
    "level": 5
}
user["level"] = 6              # Update existing value
user["email"] = "user@test.com"# Add new key-value pair
print("Dictionary:", user)
print("User's Role:", user["role"])
print("-" * 50)


# ------------------------------------------------------------------------------
# 6. CONTROL FLOW: IF, ELIF, ELSE
# ------------------------------------------------------------------------------
print("\n=== 6. IF, ELIF, ELSE ===")

score = 85

if score >= 90:
    print("Result: Grade A")
elif score >= 80:
    print("Result: Grade B")
elif score >= 70:
    print("Result: Grade C")
else:
    print("Result: Grade F")

# Short-Hand If...Else (Ternary Operator)
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age status ({age}):", status)
print("-" * 50)

print("\n=== ALL CODE EXECUTED SUCCESSFULLY! ===")

# 7. RANGE FUNCTION
# ------------------------------------------------------------------------------
print("=== 1. RANGE FUNCTION ===")

# range(stop) -> Generates numbers from 0 up to (stop - 1)
print("range(5):", list(range(5)))

# range(start, stop) -> Generates numbers from start up to (stop - 1)
print("range(2, 7):", list(range(2, 7)))

# range(start, stop, step) -> Increment by step
print("range(0, 10, 2):", list(range(0, 10, 2)))
print("range(10, 0, -2) [Counting down]:", list(range(10, 0, -2)))
print("-" * 50)


# ------------------------------------------------------------------------------
# 8. FOR LOOPS
# ------------------------------------------------------------------------------
print("\n=== 2. FOR LOOPS ===")

# Loop over a sequence generated by range()
print("Looping with range:")
for i in range(3):
    print(f"  Iteration {i}")

# Loop over a collection (List)
languages = ["Python", "JavaScript", "C++"]
print("\nLooping through a list:")
for lang in languages:
    print(f"  Language: {lang}")

# Loop with break (exits loop) and continue (skips current turn)
print("\nLoop with break & continue:")
for num in range(1, 6):
    if num == 2:
        continue  # Skip number 2
    if num == 5:
        break     # Stop loop entirely when reaching 5
    print(f"  Number: {num}")
print("-" * 50)


# ------------------------------------------------------------------------------
# 9. WHILE LOOPS
# ------------------------------------------------------------------------------
print("\n=== 3. WHILE LOOPS ===")

# Keeps running as long as the condition is True
counter = 1
while counter <= 3:
    print(f"  While loop count: {counter}")
    counter += 1  # Increment counter (CRITICAL: prevents infinite loops!)

# While loop with break
countdown = 5
print("\nCountdown with break:")
while countdown > 0:
    if countdown == 2:
        print("  Aborting early!")
        break
    print(f"  T-minus {countdown}")
    countdown -= 1
print("-" * 50)


# ------------------------------------------------------------------------------
# 10. FUNCTIONS
# ------------------------------------------------------------------------------
print("\n=== 4. FUNCTIONS ===")

# Basic function definition and execution
def greet_user(name="Guest"):  # "Guest" is a default parameter value
    return f"Hello, {name}!"

print(greet_user("Alex"))      # Output: Hello, Alex!
print(greet_user())            # Output: Hello, Guest!

# Function with multiple positional & keyword arguments
def calculate_total(price, tax_rate=0.05):
    return price + (price * tax_rate)

total = calculate_total(100, tax_rate=0.10)
print(f"Total calculated: ${total:.2f}")

# Returning multiple values (returned as a tuple)
def get_min_max(numbers):
    return min(numbers), max(numbers)

low, high = get_min_max([12, 45, 2, 88, 30])
print(f"Min: {low}, Max: {high}")
print("-" * 50)


# ------------------------------------------------------------------------------
# 11. MATCH / CASE (Structural Pattern Matching - Python 3.10+)
# ------------------------------------------------------------------------------
print("\n=== 5. MATCH / CASE ===")

# Acts like a modern "switch/case" statement
command = "start"

match command:
    case "start":
        print("  System starting up...")
    case "stop":
        print("  System shutting down...")
    case "pause" | "hold":  # Multiple conditions using '|' (OR)
        print("  System paused.")
    case _:                 # Default fallback (wildcard matching anything else)
        print("  Unknown command.")

# Matching with pattern conditions
http_status = 404

match http_status:
    case 200:
        print("  Status: OK")
    case 400 | 404:
        print("  Status: Client Error")
    case code if code >= 500: # Match with guard condition
        print(f"  Status: Server Error ({code})")
    case _:
        print("  Status: Other")
print("-" * 50)


# ------------------------------------------------------------------------------
# 12. ARRAYS (Python standard `array` module)
# ------------------------------------------------------------------------------
print("\n=== 6. ARRAYS ===")

"""
NOTE: Python uses Lists for standard general-purpose collections.
For performance-critical code requiring strict single-type arrays,
Python provides the built-in 'array' module.
"""

import array

# Create an integer array ('i' specifies signed integers)
# Format: array.array(typecode, [elements])
int_array = array.array('i', [10, 20, 30, 40])

# Append items
int_array.append(50)

# Modify items
int_array[0] = 15

print("Array elements:", int_array)
print("Typecode:", int_array.typecode)
print("Item at index 2:", int_array[2])

# Attempting to insert a string into an integer array throws a TypeError!
# int_array.append("hello") <-- INVALID

print("-" * 50)
print("\n=== ALL PART 2 CODE EXECUTED SUCCESSFULLY! ===")

