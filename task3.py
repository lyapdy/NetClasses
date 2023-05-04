class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        try:
            average_grade = sum([sum(grade) for grade in self.grades.values()]) / sum([len(grade) for grade in self.grades.values()])
            result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
            return result
        except:
            return 'Недостаточно данных'

    def __lt__(self, other):
        self.average_grade = sum([sum(grade) for grade in self.grades.values()]) / sum([len(grade) for grade in self.grades.values()])
        other.average_grade = sum([sum(grade) for grade in other.grades.values()]) / sum([len(grade) for grade in other.grades.values()])

        if not isinstance(other, Student):
            print('Это не студент')
        else:
            return self.average_grade < other.average_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def __str__(self):

        average_grade = sum([sum(grade) for grade in self.grades.values()]) / sum([len(grade) for grade in lecturer_1.grades.values()])

        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade} '
        return result

    def __lt__(self, other):
        self.average_grade = sum([sum(grade) for grade in self.grades.values()]) / sum([len(grade) for grade in self.grades.values()])
        other.average_grade = sum([sum(grade) for grade in other.grades.values()]) / sum([len(grade) for grade in other.grades.values()])

        if isinstance(other, Student):
            print('Это не лектор')
        else:
            return self.average_grade < other.average_grade

class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result


reviewer_1 = Reviewer('Alla', 'Penkova')
reviewer_1.courses_attached.append('PHP')
reviewer_1.courses_attached.append('Java')
reviewer_1.courses_attached.append('Python')

reviewer_2 = Reviewer('Yuriy', 'Gusev')
reviewer_2.courses_attached.append('Python')
reviewer_2.courses_attached.append('PHP')

lecturer_1 = Lecturer('Ivan', 'Kopylov')
lecturer_1.courses_attached.append('Python')
lecturer_1.courses_attached.append('Java')

lecturer_2 = Lecturer('Alex', 'Karakulov')
lecturer_2.courses_attached.append('Python')

student_1 = Student('Dmitriy', 'Morozov', 'male')
student_1.courses_in_progress.append('PHP')
student_1.courses_in_progress.append('Java')
student_1.courses_in_progress.append('Python')

student_2 = Student('Kseniya', 'Muravleva', 'female')
student_2.courses_in_progress.append('Python')
student_2.finished_courses.append('PHP')

student_1.rate_lecturer(lecturer_1, 'Python', 5)
student_1.rate_lecturer(lecturer_1, 'Java', 10)
student_1.rate_lecturer(lecturer_1, 'Java', 7)
student_1.rate_lecturer(lecturer_1, 'Python', 6)
student_1.rate_lecturer(lecturer_2, 'Python', 3)

student_2.rate_lecturer(lecturer_2, 'Python', 6)
student_1.rate_lecturer(lecturer_1, 'Python', 1)

reviewer_1.rate_student(student_1, 'Python', 5)
reviewer_1.rate_student(student_1, 'PHP', 7)
reviewer_1.rate_student(student_1, 'Java', 10)
reviewer_1.rate_student(student_1, 'Python', 7)
reviewer_1.rate_student(student_1, 'Java', 8)
reviewer_1.rate_student(student_2, 'Python', 3)
reviewer_1.rate_student(student_2, 'Python', 4)

reviewer_2.rate_student(student_1, 'Python', 9)
reviewer_2.rate_student(student_2, 'Java', 10)
reviewer_2.rate_student(student_2, 'Python', 7)


print(lecturer_1)
print()
print(reviewer_1)
print()
print(student_1)
print()
print(student_2)
print()
print(student_1 > student_2)
print(lecturer_1 < lecturer_2)

