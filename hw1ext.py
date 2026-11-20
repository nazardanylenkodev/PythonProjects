# ============================================
# Initial Data
# ============================================

# User info
user_name = input("Enter your name: ")
user_surname = input("Enter your surname: ")

# Years
current_year = int(input("Enter the current year: "))
year_of_birth = int(input("Enter your year of birth: "))

# Secret code parts
code_1 = float(input("Enter the first part of the secret code: "))
code_3 = float(input("Enter the third part of the secret code: "))


# Data for code_2
x = float(input("Enter the value for x for code_2: "))
y = float(input("Enter the value for y for code_2: "))

# ============================================
# Solution
# ============================================

current_age = current_year - year_of_birth
code_2 = int(((int(x) % int(y)*13))**0.5)
secret_code = f"{int(code_1)}-{int(code_2)}-{int(code_3)}"

print(" "*15, "="*15, " "*15, sep="\n")

print("Current age:", current_age)
print("Secret code:", secret_code)
print("Hello", user_name, user_surname, "!", "Your age is", current_age, ",Your secret code is :", secret_code)