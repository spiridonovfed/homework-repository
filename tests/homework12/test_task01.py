from homework12.app import *


def test_add_teachers():
    opp_teacher = Teacher(first_name="Daniil", last_name="Shadrin")
    db.session.add(opp_teacher)
    advanced_python_teacher = Teacher(first_name="Aleksandr", last_name="Smetanin")
    db.session.add(advanced_python_teacher)
    db.session.commit()


def test_add_students():
    lazy_student = Student(first_name="Roman", last_name="Petrov")
    db.session.add(lazy_student)
    good_student = Student(first_name="Lev", last_name="Sokolov")
    db.session.add(good_student)
    db.session.commit()


def test_add_homeworks_by_teachers_methods():
    opp_teacher = Teacher.query.get(1)
    opp_teacher.create_homework("Learn OOP", 1)
    opp_teacher.create_homework("Read docs", 5)


def test_add_homework_results():
    lazy_student = Student.query.get(1)
    good_student = Student.query.get(2)
    oop_hw = Homework.query.filter_by(text="Learn OOP").first()
    docs_hw = Homework.query.filter_by(text="Read docs").first()
    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    db.session.add(result_1)
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    db.session.add(result_2)
    result_3 = lazy_student.do_homework(docs_hw, "done")
    db.session.add(result_3)
    db.session.commit()


def test_teacher_checks_results():
    opp_teacher = Teacher.query.get(1)
    result_1 = HomeworkResult.query.get(1)
    assert opp_teacher.check_homework(result_1)
    assert result_1.accepted


def test_teacher_gets_list_of_accepted_homework_results():
    opp_teacher = Teacher.query.get(1)
    accepted_homework_by_teacher_attribute = opp_teacher.homework_done
    accepted_homework_results_by_query_to_db = HomeworkResult.query.filter_by(
        accepted=True
    ).all()
    assert (
        accepted_homework_by_teacher_attribute
        == accepted_homework_results_by_query_to_db
    )


def test_teacher_resets_homework_results_of_first_homework():
    opp_teacher = Teacher.query.get(1)
    oop_hw = Homework.query.get(1)
    opp_teacher.reset_results(oop_hw)
    all_homework_results = HomeworkResult.query.all()
    for homework_result in all_homework_results:
        assert homework_result.homework_id != 1


def test_teacher_resets_all_homework_results():
    advanced_python_teacher = Teacher.query.get(2)
    advanced_python_teacher.reset_results()
    all_homework_results = HomeworkResult.query.all()
    assert not all_homework_results


def test_delete_all_entries_for_repeating_testing():
    db.drop_all()
    db.create_all()
