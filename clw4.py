student = {
    "name" : "Jack",
    "surename" : "Smith",
    "age" : 20,
    "is_maried" : True,
    "courses" : [
        "Math",
        "Art",
        "History"
    ],
    "Info" : {
        "height" : 180,
        "eyes" : "blue",
        "weight" : 90
    }
}

print(student["Info"]["height"])
print(student["courses"][1])
print(len(student["courses"])) 

print(student.get("name"))


student.update(name="Simon", phone=["55-55-55-555", "77-77-777-77"])
print(student)

