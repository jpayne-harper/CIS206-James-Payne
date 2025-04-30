"""
Assignment 12 - Class Definitions and Test Cases
This script defines the classes depicted in the class diagram and runs test cases to demonstrate their functionality.
Python Version: 3.7.3
"""

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_contact_info(self):
        return f"{self.name} can be reached at {self.email}"


class Student(Person):
    def __init__(self, name, email, student_id, major):
        super().__init__(name, email)
        self.student_id = student_id
        self.major = major

    def enroll_in_course(self, course_name):
        return f"{self.name} has enrolled in {course_name}"


class Teacher(Person):
    def __init__(self, name, email, employee_id, department):
        super().__init__(name, email)
        self.employee_id = employee_id
        self.department = department

    def assign_grade(self, student_name, grade):
        return f"{self.name} assigned grade {grade} to {student_name}"


class Administrator(Person):
    def __init__(self, name, email, admin_level):
        super().__init__(name, email)
        self.admin_level = admin_level

    def generate_reports(self):
        return f"{self.name} (Admin Level {self.admin_level}) is generating reports."


class Course:
    def __init__(self, course_id, title, credits):
        self.course_id = course_id
        self.title = title
        self.credits = credits
        self.students = []
        self.teacher = None

    def add_student(self, student_name):
        self.students.append(student_name)
        return f"{student_name} added to {self.title}"

    def assign_teacher(self, teacher_name):
        self.teacher = teacher_name
        return f"{teacher_name} assigned to teach {self.title}"


class TeachingAssistant(Student, Teacher):
    def __init__(self, name, email, student_id, major, employee_id, department, ta_hours):
        Student.__init__(self, name, email, student_id, major)
        Teacher.__init__(self, name, email, employee_id, department)
        self.ta_hours = ta_hours

    def hold_office_hours(self):
        return f"{self.name} is holding office hours for {self.ta_hours} hours"


if __name__ == '__main__':
    print("TESTING CLASS INSTANTIATIONS AND METHODS\n")

    # Person
    person = Person("Alice", "alice@example.com")
    print(person.get_contact_info())

    # Student
    student = Student("Bob", "bob@example.com", "S123", "Computer Science")
    print(student.get_contact_info())
    print(student.enroll_in_course("Python Programming"))

    # Teacher
    teacher = Teacher("Dr. Smith", "smith@example.com", "T456", "Engineering")
    print(teacher.get_contact_info())
    print(teacher.assign_grade("Bob", "A"))

    # Administrator
    admin = Administrator("Carol", "carol@example.com", 2)
    print(admin.get_contact_info())
    print(admin.generate_reports())

    # Course
    course = Course("C789", "Intro to Databases", 3)
    print(course.add_student("Bob"))
    print(course.assign_teacher("Dr. Smith"))

    # TeachingAssistant (Multiple Inheritance)
    ta = TeachingAssistant("Dan", "dan@example.com", "S321", "Math", "T321", "Math Dept", 5)
    print(ta.get_contact_info())
    print(ta.enroll_in_course("Algebra"))
    print(ta.assign_grade("Alice", "B+"))
    print(ta.hold_office_hours())
