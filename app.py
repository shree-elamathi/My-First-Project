from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/school'
db = SQLAlchemy(app)


# Define the Student model
class Student(db.Model):
    stud_ID = db.Column(db.Integer, primary_key=True)
    stud_name = db.Column(db.String(100), nullable=False)
    Total_marks = db.Column(db.Integer, nullable=False)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_data')
def get_data():
    students = Student.query.all()
    students_list = [{'stud_ID': student.stud_ID, 'stud_name': student.stud_name, 'Total_marks': student.Total_marks}
                     for student in students]
    return render_template('data.html', students=students_list)


if __name__ == '__main__':
    app.run(debug=True)
