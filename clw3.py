# empty = []

# print(type(empty))


# filed_list = ["apple", 1000, 3.14, True, [11,2,3,4,5]]


# print(filed_list[2:4])
# print(len(filed_list))

# print(filed_list[0:4][1])


# courses = {"History","Math","Art","Programming"}
# numbers = {1,2,3,4,5,6,7,8,9,12,24,-10}
# print(numbers)


# for index, course in enumerate(courses):
#     if course == "Math":
#         print(index)

# courses_str = ", ".join(courses)
# print(courses_str)

# text = "Hello world and people"
# text_lst = text.split()
# print(text_lst)

# print(courses.index("Math"))

# print(courses)

# print(id(courses))

# courses[1]= "Physics"

# print(id(courses))
# print(courses)

# courses += ["Estonian"]  
# courses.append("Lit")
# print(courses)

# courses.pop()
# courses.sort()
# print(courses.count("Math"))
# print(len(courses) + 1)

# courses.reverse

names = ["John", "Jane", "Alice", "Bob"]

for name in names:
    if len(name) > 4:
        print("Long name:", name)
    else:
        print("Short name:", name)

people = ["Sarah", "Bob", "Jack", "Samantha"]

short = []
long = []

for person in people:
    if len(person) > 4:
        long.append(person)
    else:
        short.append(person)

print("Short", short, "Long", long)