# string_sample1 = "hello world world"
# string_sample2 = "fIrSt LeTTeR. dadsdadas"
# string_sample3 = " !  extra whitespace string  **! "
# string_sample4 = "der fluß"



# print(len(string_sample1))
# print(string_sample3.count(" "))

# print(string_sample2.upper())

# print(string_sample4.lower())
# print(string_sample4.casefold())

# print(string_sample1[6:11].upper()[0].lower())

# print(string_sample2.capitalize())
# print(string_sample2.title())

# print(string_sample3.strip())
# print(string_sample3.strip(" !*"))

# print(string_sample1.replace("world", "planet"))

# print(string_sample1.count("world"))
# print(string_sample1.split(" "))

# print(string_sample1.find("world"))

# print(string_sample1.swapcase())

# text = "My favorite book is 'Metro 2039'"
# print(text)
# print("hello, world", "world", 123, 333, sep="***", end="===\n")

# x = 5
# print(id(x))

# x = x +5
# print(id(x))


# product = "computer"
# price = 1500
# text = "This {prd} costs {prc}$."
# print(text.format(prd=product, prc=price))


x = float(input("Enter a number:"))
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
elif x == 0:
    print("x is zero")
if isinstance(x, float):
    print("x is a float number")
elif isinstance(x, int):
    print("x is an integer")
else:
   print("error")