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

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average_grade_fs()} \nКурсы в процессе изучения:{self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'

    def average_grade_fs(self):
        list_grade_st = []  # Список оценок
        for li in self.grades.values():
            list_grade_st += li
        average_grade = round(sum(list_grade_st) / len(list_grade_st))
        return average_grade

    def best_student(self, student2):
        if self.average_grade_fs() < student2.average_grade_fs():
            print(f'Средний балл {self.surname} ниже чем у {student2.surname}')
        else:
            print(f'Средний балл {student2.surname} ниже чем у {self.surname}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \n'


class Lecturer(Mentor):

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.average_grade_fl
        self.best_lekturer

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grade_fl()}'

    def average_grade_fl(self):
        list_grade = []  # Список оценок
        for li in self.grades.values():
            list_grade += li
        average_grade = round(sum(list_grade) / len(list_grade))  # Среднее значение
        return average_grade

    def best_lekturer (self, lecturer2):
        if self.average_grade_fl() < lecturer2.average_grade_fl():
            print(f'Средний балл {self.surname} ниже чем у {lecturer2.surname}')
        else:
            print(f'Средний балл {lecturer2.surname} ниже чем у {self.surname}')

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C++']
best_student.finished_courses += ['Введение в программирование']
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

best_student2 = Student('Arkadiy', 'Ukupnik', 'your_gender')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['C++']
best_student2.finished_courses += ['Введение в программирование']
cool_mentor.rate_hw(best_student2, 'Python', 9)
cool_mentor.rate_hw(best_student2, 'Python', 9)
cool_mentor.rate_hw(best_student2, 'Python', 10)





cool_mentor.rate_hw(best_student, 'Python', 8)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_lecturer = Lecturer('Ivan', 'Ivanov')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['C++']
best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(cool_lecturer, 'C++', 10)
best_student.rate_hw(cool_lecturer, 'C++', 10)

cool_lecturer2 = Lecturer('Peter', 'Petrov')
cool_lecturer2.courses_attached += ['Python']
cool_lecturer2.courses_attached += ['C++']
best_student.rate_hw(cool_lecturer2, 'Python', 9)
best_student.rate_hw(cool_lecturer2, 'Python', 8)
best_student.rate_hw(cool_lecturer2, 'C++', 9)
best_student.rate_hw(cool_lecturer2, 'C++', 9)

cool_lecturer.best_lekturer(cool_lecturer2)
best_student.best_student(best_student2)

print(cool_lecturer)

print(best_student)

print(cool_mentor)
print(cool_mentor)

