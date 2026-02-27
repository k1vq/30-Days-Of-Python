# Day 2: 30 Days of python programming

# Level 1
first_name = "Konstantin"
last_name = "Ivanov"
full_name = first_name + " " + last_name
country = "Estonia"
city = "Valga"
age = 19
year = 2026
is_married = False
is_true = True
is_light_on = False

monday, tuesday, wednesday = 1, 2, 3

# Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(year))
print(type(age))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(monday))

print(len(first_name))
print(len(first_name) > len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

r = 30
area_of_circle = 3.14 * r ** 2
circum_of_circle =\
    2 * 3.14 * r

radius = float(input("Radius? "))
user_area = 3.14 * radius ** 2
print(f"Area: {user_area}")

f_name = input("First name: ")
l_name = input("Last name: ")
c_name = input("Country: ")
age_name = int(input("Age: "))

help('keywords')