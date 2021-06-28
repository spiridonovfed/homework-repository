import csv

from homework12.app import *

with open("report.csv", mode="w", newline="") as report_file:
    employee_writer = csv.writer(
        report_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
    )

    employee_writer.writerow(
        [
            "Student name",
            "Creation date of homework_result",
            "Teacher name who created homework",
        ]
    )

    all_accepted_homework_results = HomeworkResult.query.filter_by(accepted=True).all()
    for homework_result in all_accepted_homework_results:
        student = homework_result.author
        student_name = f"{student.first_name} {student.last_name}"

        creation_date = str(homework_result.created)[:10]

        teacher_created = homework_result.homework.teacher
        teacher_name = f"{teacher_created.first_name} {teacher_created.last_name}"

        employee_writer.writerow([student_name, creation_date, teacher_name])
