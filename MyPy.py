print("Hello, Python!")
name = input("Введите ваше имя: ")
print("Привет,", name)

age = 25
height = 1.64
z = 3 + 4j
is_student = True
name = "Anita"
hobbies = ["art", "music", "computer games"]
grades = (10, 11, 12)
unique_numbers = {1, 2, 3, 3, 2, 1}

student = {
    "name": name,
    "age": age,
    "is_student": is_student,
    "group": 8
}

numbers = range(1, 12)
print("=== VARIABLES AND TYPES ===")
print("age:", age, type(age))
print("height:", height, type(height))
print("z:", z, type(z))
print("is_student:", is_student, type(is_student))
print("name:", name, type(name))
print("hobbies:", hobbies, type(hobbies))
print("grades:", grades, type(grades))
print("unique_numbers:", unique_numbers, type(unique_numbers))
print("student:", student, type(student))
print("numbers:", list(numbers), type(numbers))

print("\n=== CALCULATIONS AND CONVERSIONS ===")
# Simple math
a = 10
b = 3
sum_result = a + b
division = a / b
power = a ** b

print("Sum:", sum_result)
print("Division:", division)
print("Power:", power)

# Type conversions
num_str = "42"
num_int = int(num_str)
print("Before:", num_str, type(num_str))
print("After:", num_int, type(num_int))

float_str = "3.14"
num_float = float(float_str)
print("String to float:", num_float, type(num_float))

# Boolean and casting example
print("bool(0):", bool(0))
print("bool('hello'):", bool("hello"))
print("bool(''):", bool(''))   


print("\nAll basic types and operations executed successfully")

