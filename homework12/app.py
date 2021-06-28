from datetime import datetime, timedelta

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# -------------Custom Errors------------------- #


class DeadlineError(Exception):
    """You are late"""


class RepeatedResultError(Exception):
    """This homework result has been accepted previously"""


# --------------------------------------------- #


def create_timedelta(days):
    """Creates datetime.timedelta object from number of days passed in"""
    return timedelta(days=days)


# ---------Homework and Homework Result------- #


class Homework(db.Model):
    """Table Model for Flask-SQLalchemy"""

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)  # input
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    deadline = db.Column(db.Integer, nullable=False)  # input
    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"), nullable=False)
    homework_results = db.relationship("HomeworkResult", backref="homework", lazy=True)

    def is_active(self):
        """returns True if deadline is not passed, False otherwise"""
        return datetime.now() < self.created + create_timedelta(self.deadline)


class HomeworkResult(db.Model):
    """Table Model for Flask-SQLalchemy"""

    id = db.Column(db.Integer, primary_key=True)
    homework_id = db.Column(
        db.Integer, db.ForeignKey("homework.id"), nullable=False
    )  # input
    student_id = db.Column(
        db.Integer, db.ForeignKey("student.id"), nullable=False
    )  # input
    solution = db.Column(db.Text, nullable=False)  # input
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    accepted = db.Column(db.BOOLEAN, nullable=False, default=False)


# ------------------People-------------------- #
class Student(db.Model):
    """Table Model for Flask-SQLalchemy"""

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)  # input
    last_name = db.Column(db.String(30), nullable=False)  # input
    homework_results = db.relationship("HomeworkResult", backref="author", lazy=True)

    def do_homework(self, homework, result):
        if homework.is_active():
            homework_result = HomeworkResult(
                homework_id=homework.id, student_id=self.id, solution=result
            )
            repeated_results = HomeworkResult.query.filter_by(
                homework_id=homework.id, student_id=self.id, solution=result
            ).all()
            if repeated_results:
                raise RepeatedResultError(
                    "This homework result has been accepted previously"
                )
            db.session.add(homework_result)
            db.session.commit()
            return homework_result
        else:
            raise DeadlineError("You are late")


class Teacher(db.Model):
    """Table Model for Flask-SQLalchemy"""

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)  # input
    last_name = db.Column(db.String(30), nullable=False)  # input
    created_homeworks = db.relationship("Homework", backref="teacher", lazy=True)

    @property
    def homework_done(self):
        """Returns list of all accepted homeworks"""
        return HomeworkResult.query.filter_by(accepted=True).all()

    def create_homework(self, text: str, deadline: int):
        """Creates homeworks in database"""
        homework = Homework(text=text, deadline=deadline, teacher_id=self.id)
        db.session.add(homework)
        db.session.commit()

    def check_homework(self, homework_result):
        """Checks homework_result - if accepted sets 'accepted' attribute to True"""
        if not isinstance(homework_result, HomeworkResult):
            raise TypeError("You gave a not HomeworkResult object")

        if len(homework_result.solution) > 5:
            homework_result.accepted = True
            db.session.commit()
            return True
        else:
            return False

    @classmethod
    def reset_results(cls, homework=None):
        """Deletes all homework_results of homework passed in, delete all homework_results if nothing has passed"""
        if homework and isinstance(homework, Homework):
            homework_results_to_delete = HomeworkResult.query.filter_by(
                homework_id=homework.id
            ).all()
            for homework_result in homework_results_to_delete:
                db.session.delete(homework_result)
            db.session.commit()

        else:
            homework_results_to_delete = HomeworkResult.query.all()
            for homework_result in homework_results_to_delete:
                db.session.delete(homework_result)
            db.session.commit()


db.create_all()
