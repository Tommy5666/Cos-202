print("=== CGPA CALCULATOR ===")

total_points = 0
total_units = 0

n = int(input("Enter number of courses: "))

for i in range(n):
    print("\nCourse", i + 1)

    unit = int(input("Enter course unit: "))
    score = int(input("Enter score: "))

    if score >= 70:
        gp = 5
    elif score >= 60:
        gp = 4
    elif score >= 50:
        gp = 3
    elif score >= 45:
        gp = 2
    elif score >= 40:
        gp = 1
    else:
        gp = 0

    total_points += gp * unit
    total_units += unit

cgpa = total_points / total_units

print("\nYour CGPA is:", round(cgpa, 2))