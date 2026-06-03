student={
    "name":"saksham",
     "age":20,
     "address":"birgunj"
}

print(student["name"])
print(student["age"])
student["university"]="Pokhara"

print(student["university"])
student["class"]="Bachelor 4 semester"
print(student["class"])

del(student["class"])

print(student.keys())
print(student.values())
print(student.items())