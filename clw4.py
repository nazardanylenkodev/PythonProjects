# student = {
#     "name" : "Jack",
#     "surename" : "Smith",
#     "age" : 20,
#     "is_maried" : True,
#     "courses" : [
#         "Math",
#         "Art",
#         "History"
#     ],
#     "Info" : {
#         "height" : 180,
#         "eyes" : "blue",
#         "weight" : 90
#     }
# }

# print(student["Info"]["height"])
# print(student["courses"][1])
# print(len(student["courses"])) 

# print(student.get("name"))


# student.update(name="Simon", phone=["55-55-55-555", "77-77-777-77"])
# print(student)


# from pprint import pp

# pp(student)


# age = 40 

# if age <= 12 and age >= 0:
#     print("Hi there child")
# if age <= 21 and age >= 12:
#     print("you are a teen now")
# if age >= 21 and age <= 60:
#     print("adult")
# if age >= 60 and age <= 120:
#     print("welcome back senior")
# else:
#     "imposible"


# for num in range (101):
#     if num %3 == 0 and num %5 == 0:
#         print(num, "fizzbuzz")
#     if num % 3 == 0:
#         print(num, "fizz")
#     if num % 5 == 0:
#         print(num, "buzz")
    
        
# print("\n" + "="*50 + "\n")

# for num in range(200):
#     if num % 7 == 0:
#         print(num, "bang")
#     if num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
#         print(num, "fizzbuzzbang")
#     if num % 3 == 0 and num % 5 == 0:
#         print(num, "buzzbang")
    


# condition = True
# while condition:
#     id_code = input("enter est idcode")
#     if id_code.isdigit():
#         if len(id_code) == 11:
#             print(id_code, "OK")
#             condition = False
#         else:
#             print(id_code, "NOTOK")
#     else:
#         print("NOK")


# current_try = 1
# max_tries = 5

# while current_try <= max_tries:
#     current_try += 1
#     print(f"Try {current_try}")


# for letter in "python":
#     if letter == "h":
#         continue
#     if letter == "n":
#         break
#     print(letter)


id_code = ""

try:
    int(id_code)
    if len(id_code) != 11:
        raise UserWarning
except ValueError:
    print("id code incorrect")
except UserWarning:
    print("it must be 11 digits")
finally:
    print("well done")