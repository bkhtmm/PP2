student = {
    "name": "John",
    "age": 20,
    "major": "Computer Science"
}
print(student)

student["age"] = 21
print(student)

student["year"] = "Sophomore"
print(student)

print(student.get("name"))
print(student.get("graduation_year", "Not Available"))

for key, value in student.items():
    print(key, value)

keys = student.keys()
print(keys)

values = student.values()
print(values)

del student["major"]
print(student)
