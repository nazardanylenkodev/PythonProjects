# ============================================
# Initial Data
# ============================================

# Years
current_year = 2023
year_of_birth = 1988

# Secret code parts
code_1 = "354"
code_3 = 132

# User info
user_name = "John"
user_surname = "Smith"

# Data for code_2
x = 152
y = 132

# ============================================
# Solution
# ============================================

current_age = current_year - year_of_birth
code_2 = int((((int(code_1) % code_3)*13))**0.5)
secret_code = f"{code_1}-{code_2}-{code_3}"

print("Current age:", current_age)
print("Secret code:", secret_code)
print("Hello", user_name, user_surname, "!", "Your age is", current_age, "Your secret code is :", secret_code)