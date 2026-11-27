print("\n" + "="*50 + "\n")
# Extract the first and last elements.
# Create a new list containing only the middle three numbers using slicing.
nums = [10, 20, 30, 40, 50]
first = nums[0]
last = nums[-1]
middle_three = nums[1:4]
print(first, last, middle_three)

print("\n" + "="*50 + "\n")
# Combine them into one list.
# Duplicate list a three times.
a = [1, 2, 3]
b = [4, 5]
a.extend(b)
print(a*3)

print("\n" + "="*50 + "\n")
# Replace "green" with "yellow" using indexing only.
# Add "purple" to the end without using append.
colors = ["red", "green", "blue"]
colors.insert(1, "yelow")
colors.extend(["purple"])
print(colors)

print("\n" + "="*50 + "\n")
# Extract the first three items as a new tuple.
# Create a tuple containing only the last two items.
t = ("apple", "banana", "cherry", "date", "kiwi")
first_three = t[:3]
last_two = t[-2:]
print(first_three, last_two)

print("\n" + "="*50 + "\n")
# Unpack values into variables x, y, z.
coords = (10, 20, 30)
x, y, z = coords
print(x, y, z)

print("\n" + "="*50 + "\n")
# Find the intersection.
# Find elements in s1 but not in s2.
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
intersection = s1 & s2       
diff_s1_only = s1 - s2     
print(intersection, diff_s1_only)

print("\n" + "="*50 + "\n")
# remove duplicates from list "items"
items = [1, 2, 2, 3, 4, 4, 4, 5]
unique_items = set(items)
print(unique_items)

print("\n" + "="*50 + "\n")
# Find elements in either set but not both
x = {1, 2, 3, 4}
y = {3, 4, 5, 6}
sym_diff = x.symmetric_difference(y)
print(sym_diff)

print("\n" + "="*50 + "\n")
# Create a set of unique characters.
# Count how many unique characters the word has.
word = "mississippi"
unique_chars = set(word)
print(unique_chars, len(unique_chars))

print("\n" + "="*50 + "\n")
# Check if a is a subset of b.
# Check if b is a superset of a.
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))            
print(b.issuperset(a))

print("\n" + "="*50 + "\n")
# Remove "bird" from the set without using conditionals.
# Remove "turtle" and observe what happens (using .discard()).
animals = {"cat", "dog", "bird", "fish"}
animals.remove("bird")
animals.discard("turtle")       
print(animals)

print("\n" + "="*50 + "\n")
# Combine all sets into one set using a built-in (hint: set.union() can take multiple arguments).
list_of_sets = [{1, 2}, {2, 3, 4}, {4, 5}]
all_combined = set().union(*list_of_sets)
print(all_combined)

print("\n" + "="*50 + "\n")
# Iterate through the numbers list using a for loop.
# Print only the even numbers.
numbers = [12, 7, 34, 23, 45, 66, 89, 90, 102]
for num in numbers:
    if num % 2 == 0:
        print(num)


print("\n" + "="*50 + "\n")
# Iterate through the list of words.
# Print only words that have more than 5 characters.
# Count how many words start with the letter "a" (case-insensitive).
words = ["Apple", "banana", "kiwi", "Avocado", "cherry", "apricot", "pear"]
a_count = 0
for w in words:
    if len(w) > 5:
        print(w)
    if w.lower().startswith("a"):
        a_count += 1
print("Starts with 'a':", a_count)

print("\n" + "="*50 + "\n")
# Iterate through temperatures and separate them into two lists:
# "above_zero" for positive temperatures and "below_zero" for negative ones (ignore 0).
temperatures = [15, -3, 0, 22, -8, 11, -1, 4, -10]
above_zero = []
below_zero = []
for temp in temperatures:
    if temp > 0:
        above_zero.append(temp)
    elif temp < 0:
        below_zero.append(temp)
print("Above zero:", above_zero)
print("Below zero:", below_zero)

print("\n" + "="*50 + "\n")
# Loop through the list of student scores.
# If the score is 90 or above, print "A", if between 70 and 89 print "B", otherwise print "C".
# Count how many students received an "A".
scores = [95, 82, 67, 91, 74, 88, 59, 100]
a_grades = 0
for score in scores:
    if score >= 90:
        print("A")
        a_grades += 1
    elif score >= 70:
        print("B")
    else:
        print("C")
print("Total A grades:", a_grades)

print("\n" + "="*50 + "\n")
# Iterate through the data list.
# Calculate the sum of all positive numbers only.
data = [10, -5, 25, 40, -12, 85, 105, 30, -2]
positive_sum = 0
for value in data:
    if value > 0:
        positive_sum += value
print("Sum of positives:", positive_sum)

print("\n" + "="*50 + "\n")
# Iterate through the list of mixed items.
# Check the type of each item: append integers to int_list and strings to str_list.
mixed_items = [10, "apple", 25, "banana", 42, "cherry", 99]
int_list = []
str_list = []
for item in mixed_items:
    if type(item) is int:
        int_list.append(item)
    elif type(item) is str:
        str_list.append(item)
print("Integers:", int_list)
print("Strings:", str_list)

print("\n" + "="*50 + "\n")