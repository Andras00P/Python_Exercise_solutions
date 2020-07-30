''' Calculate final grade from five subjects '''

def grades(a, b, c, d, e):
    avg_grade = int((a + b + c + d + e) / 5)
    f_grade = ""

    if avg_grade >= 90:
        f_grade = "Grade A"
    elif avg_grade >= 80:
        f_grade = "Grade B"
    elif avg_grade >= 70:
        f_grade = "Grade C"
    elif avg_grade >= 60:
        f_grade = "Grade D"
    else:
        f_grade = "Grade F"

    return f_grade, avg_grade

grade_a = int(input("Enter the subject a grade: \n\n"))
grade_b = int(input("Enter the subject b grade: \n\n"))
grade_c = int(input("Enter the subject c grade: \n\n"))
grade_d = int(input("Enter the subject d grade: \n\n"))
grade_e = int(input("Enter the subject e grade: \n\n"))

final_grade, final_score = grades(grade_a, grade_b, grade_c, grade_d, grade_e)
print(f"Your Final grade is: {final_grade}, {final_score}")
