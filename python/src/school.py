# Create a person class with a name and age and additional relevant fields
class Person:
    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}, Phone: {self.phone}"


# Create a student class that inherits from person and has a student id and a list of courses
class Student(Person):
    def __init__(self, name, age, address, phone, student_id, courses):
        super().__init__(name, age, address, phone)
        self.student_id = student_id
        self.courses = courses

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}, Phone: {self.phone}, Student ID: {self.student_id}, Courses: {self.courses}"


# Create a teacher class that inherits from person and has a teacher id and a list of courses
class Teacher(Person):
    def __init__(self, name, age, address, phone, teacher_id, courses):
        super().__init__(name, age, address, phone)
        self.teacher_id = teacher_id
        self.courses = courses

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}, Phone: {self.phone}, Teacher ID: {self.teacher_id}, Courses: {self.courses}"


# Create a course class that has a course id, a course name, a teacher id, and a list of students
class Course:
    def __init__(self, course_id, course_name, teacher_id, students):
        self.course_id = course_id
        self.course_name = course_name
        self.teacher_id = teacher_id
        self.students = students

    def __str__(self):
        return f"Course ID: {self.course_id}, Course Name: {self.course_name}, Teacher ID: {self.teacher_id}, Students: {self.students}"


# Create a school class that has a list of courses and a list of students
class School:
    def __init__(self, courses, students):
        self.courses = courses
        self.students = students

    def __str__(self):
        return f"Courses: {self.courses}, Students: {self.students}"


import unittest


class TestSchoolSystem(unittest.TestCase):
    def setUp(self):
        self.student1 = Student(
            "John Doe", 20, "123 St", "1234567890", "s123", ["Math", "Science"]
        )
        self.teacher = Teacher(
            "Mr. Smith", 40, "789 St", "1122334455", "t789", ["Math", "Science"]
        )
        self.course = Course("c101", "Math", "t789", ["s123"])
        self.school = School([self.course], [self.student1])

    # Tests that will pass
    def test_student_pass(self):
        self.assertEqual(self.student1.name, "John Doe")
        self.assertEqual(self.student1.age, 20)
        self.assertEqual(self.student1.student_id, "s123")
        self.assertEqual(self.student1.courses, ["Math", "Science"])

    def test_teacher_pass(self):
        self.assertEqual(self.teacher.name, "Mr. Smith")
        self.assertEqual(self.teacher.age, 40)
        self.assertEqual(self.teacher.teacher_id, "t789")
        self.assertEqual(self.teacher.courses, ["Math", "Science"])

    def test_course_pass(self):
        self.assertEqual(self.course.course_id, "c101")
        self.assertEqual(self.course.course_name, "Math")
        self.assertEqual(self.course.teacher_id, "t789")
        self.assertEqual(self.course.students, ["s123"])

    def test_school_pass(self):
        self.assertEqual(self.school.courses, [self.course])
        self.assertEqual(self.school.students, [self.student1])

    # Tests that will fail
    def test_student_fail(self):
        self.assertEqual(self.student1.name, "Jane Doe")
        self.assertEqual(self.student1.age, 21)
        self.assertEqual(self.student1.student_id, "s124")
        self.assertEqual(self.student1.courses, ["English", "History"])

    def test_teacher_fail(self):
        self.assertEqual(self.teacher.name, "Mrs. Smith")
        self.assertEqual(self.teacher.age, 41)
        self.assertEqual(self.teacher.teacher_id, "t790")
        self.assertEqual(self.teacher.courses, ["English", "History"])

    def test_course_fail(self):
        self.assertEqual(self.course.course_id, "c102")
        self.assertEqual(self.course.course_name, "English")
        self.assertEqual(self.course.teacher_id, "t790")
        self.assertEqual(self.course.students, ["s124"])

    def test_school_fail(self):
        self.assertEqual(
            self.school.courses, [Course("c102", "English", "t790", ["s124"])]
        )
        self.assertEqual(
            self.school.students,
            [
                Student(
                    "Jane Doe",
                    21,
                    "456 St",
                    "0987654321",
                    "s124",
                    ["English", "History"],
                )
            ],
        )


# create a main function that will create a school, add students, add teachers, add courses, and print everything
def main():
    # Create a school
    school = School([], [])

    # Create a list of students
    students = []

    # Create a list of teachers
    teachers = []

    # Create a list of courses
    courses = []

    # Create 3 students
    student1 = Student(
        "John", 20, "123 Main Street", "123-456-7890", 1, ["Math", "Science"]
    )
    student2 = Student(
        "Jane", 21, "456 Main Street", "123-456-7890", 2, ["Math", "Science"]
    )
    student3 = Student(
        "Jack", 22, "789 Main Street", "123-456-7890", 3, ["Math", "Science"]
    )

    # Add the students to the list of students
    students.append(student1)
    students.append(student2)
    students.append(student3)

    # Create 3 teachers
    teacher1 = Teacher(
        "Tom", 30, "123 Main Street", "123-456-7890", 1, ["Math", "Science"]
    )
    teacher2 = Teacher(
        "Tim", 31, "456 Main Street", "123-456-7890", 2, ["Math", "Science"]
    )
    teacher3 = Teacher(
        "Tam", 32, "789 Main Street", "123-456-7890", 3, ["Math", "Science"]
    )

    # Add the teachers to the list of teachers
    teachers.append(teacher1)
    teachers.append(teacher2)
    teachers.append(teacher3)

    # Create 3 courses
    course1 = Course(1, "Math", 1, [student1, student2, student3])
    course2 = Course(2, "Science", 2, [student1, student2, student3])
    course3 = Course(3, "English", 3, [student1, student2, student3])

    # Add the courses to the list of courses
    courses.append(course1)
    courses.append(course2)
    courses.append(course3)

    # Add the students, teachers, and courses to the school
    school.students = students
    school.teachers = teachers
    school.courses = courses

    # display the list of students
    print("Students:")
    for student in school.students:
        print(student)

    # display the list of teachers
    print("Teachers:")
    for teacher in school.teachers:
        print(teacher)


# create the python main function
if __name__ == "__main__":
    # main()
    unittest.main()
