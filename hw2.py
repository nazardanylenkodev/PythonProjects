# Tasks

"""
TASK 1: The Receipt Formatter
1. Clean up `raw_item_name` by removing extra spaces and converting it to Title Case.
2. Calculate the total cost (`price * quantity`) and round it to 2 decimal places.
3. Print a summary message: "You bought 3 Coffee Mug(s) for a total of $37.5."
"""

raw_item_name = "   coffee mug  "
price = 12.5
quantity = 3

# Write your code below:

print(f"You bought {int(quantity)} {raw_item_name.strip().title()}(s) for a total of ${price * quantity:.2f}.")


print("\n" + "="*50 + "\n")
"""
TASK 2: Username Generator
Generate a suggested username by combining:
- The first 3 letters of `first_name`
- The first 3 letters of `last_name`
- The last 2 digits of `birth_year`
Ensure the final username is completely lowercase (e.g., "alismi04") and print it.
"""

first_name = "Alice"
last_name = "Smith"
birth_year = "2004"

# Write your code below:
username = (first_name[:3] + last_name[:3] + birth_year[-2:]).lower()
print(username)


print("\n" + "="*50 + "\n")

"""
TASK 3: Loud or Quiet?
Analyze the `sentence` variable and store three boolean (True/False) results:
1. `is_all_caps`: Is the sentence completely uppercase?
2. `has_exclamation`: Does the sentence end with "!"?
3. `mentions_python`: Does the sentence contain the word "python" (case-insensitive)?
Print all three boolean variables with descriptive labels.
(methods: .isupper(), .endswith(), .find())
"""

sentence = "I am learning PYTHON right now!"

# Write your code below:
is_all_caps = bool()
has_exclamation = bool()
mentions_python = bool()
all_caps_python = bool()
all_lower_python = bool()

if sentence.isupper():
    is_all_caps = True  
else:
    is_all_caps = False

print(is_all_caps)

if sentence.endswith("!"):
    has_exclamation = True
else:
    has_exclamation = False

print(has_exclamation)

if sentence.find("python"):
    mentions_python = True 
else:
    mentions_python = False

if sentence.find("python") != -1:
    all_lower_python = True
if sentence.find("PYTHON") != -1:
    all_caps_python = True
if mentions_python and all_caps_python == True:
    print("True")
else:
    print("python mentioned but not for this case")


print("\n" + "="*50 + "\n")
"""
TASK 4: Simple Password Validator
Check if `password` meets both security rules:
1. It is at least 8 characters long.
2. It is NOT equal to "password123" (case-insensitive).
Print "Password accepted" if both pass; otherwise, print which specific rule failed.
"""

password = "Password1234"

# Write your code below:

if len(password) >= 8 and password.lower() != "password123":
    print("Password accepted")
elif len(password) < 8:
    print("Password must be at least 8 characters long.")
elif password.lower() == "password123":
    print("make it more secure.")



print("\n" + "="*50 + "\n")
"""
TASK 5: Even, Odd, or Decimal?
Classify the string stored in `raw_number`:
1. If it contains a decimal point ("."), convert it to a float and print "Decimal number".
2. Otherwise, convert it to an integer and check if it is "Even" or "Odd" using %.
"""

raw_number = "42"

# Write your code below:
if raw_number.find(".") != -1:
    raw_number = float(raw_number)
    print("Decimal number")
    print(raw_number)
else:
    raw_number = int(raw_number)
    if raw_number % 2 == 0:
        print("Even")
        print(raw_number)
    else:
        print("Odd")
        print(raw_number)


print("\n" + "="*50 + "\n")

"""
TASK 6: Email Domain Checker
Validate `email` and classify its domain:
1. If it does NOT contain both "@" and ".", print "Invalid email format."
2. If valid and ends with ".edu", print "Student/Academic account".
3. If valid and ends with ".gov", print "Government account".
4. Otherwise, print "Standard account".
"""

email = "alex.chen@university.gov"

# Write your code below:
print(email)
if email.find("@") == -1 or email.find(".") == -1:
    print("Invalid email format.")
elif email.endswith(".edu"):
    print("Student/Academic account")
elif email.endswith(".gov"):
    print("Government account")
else:
    print("Standard account")


print("\n" + "="*50 + "\n")
"""
TASK 7: Temperature Converter
Convert `temp_value` based on `unit` ("C" for Celsius, "F" for Fahrenheit):
- Clean `unit` so lowercase letters ("c", "f") and accidental spaces still work.
- If Celsius, convert to Fahrenheit: (C * 9/5) + 32
- If Fahrenheit, convert to Celsius: (F - 32) * 5/9
- If `unit` is anything else, print "Invalid unit entered."
Round the converted result to 1 decimal place and print it.
"""

temp_value = 25.0
unit = " c "

unit = unit.strip().upper()
if unit == "C":
    converted_value = (temp_value * 9/5) + 32
    print(f"{temp_value}°C is {converted_value:.1f}°F")
elif unit == "F":
    converted_value = (temp_value - 32) * 5/9
    print(f"{temp_value}°F is {converted_value:.1f}°C")
else:
    print("Invalid unit entered.")


print("\n" + "="*50 + "\n")