midterm_grade = float(input("Enter your midterm exam grade (0-100): "))
final_exam_grade = float(input("Enter your final exam grade (0-100): "))
project_grade = float(input("Enter your project grade (0-100): "))

if 0 <= midterm_grade <= 100 and 0 <= final_exam_grade <= 100 and 0 <= project_grade <= 100:
    average_grade = (midterm_grade * 0.2) + (final_exam_grade * 0.4) + (project_grade * 0.4)
    if average_grade >= 70:
        print("Excellent! You passed the course. Your average grade is: ",average_grade)
    else:
        print("Unfortunately, you did not pass the course. Your average grade is: ",average_grade)
else:
    print("Please enter valid grades (0-100).")
    