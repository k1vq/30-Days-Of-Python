# Day 3
lnth = int(input("Length: "))
width = int(input("Width: "))
area = lnth * width
perimeter = 2 * (lnth + width)
print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)

radius = int(input("Radius: "))
area_r = 3.14 * radius ** 2
circum = 2 * 3.14 * radius
print("Area of circle:", area_r)
print("Circumference:", circum)

m = 2
y_intercept = -2
x_intercept = 1
print("slope:", m)
print("y-intercept:", y_intercept)
print("x-intercept:", x_intercept)

m_slope = (10 - 2) / (6 - 2)
distance = ((6 - 2)**2 + (10 - 2)**2) ** 0.5
print("slope between points:", m_slope)
print("distance:", distance)
print("slopes equal:", m == m_slope)

print(("on" in "dragon") and ("on" in "python"))

sentence = "I hope this course is not full of jargon."
print("jargon" in sentence)

print(int(float("9.8")) == 10)

hours = int(input("Enter hours: "))
rph = int(input("Enter rate per hour: "))
print(f"Your weekly earning is {hours * rph}")

years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print(f"You have lived for {seconds} seconds.")

print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")