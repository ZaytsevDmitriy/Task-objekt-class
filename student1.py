def average_score(list):  # Средний балл из списка
    score = 0
    for i in list:
        score = round(sum(list) / len(list))
    return score


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
        average_grade = average_score(list_grade_st)
        return average_grade

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not Student')
            return
        return self.average_grade_fs() < other.average_grade_fs()


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

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grade_fl()}'

    def average_grade_fl(self):
        list_grade = []  # Список оценок
        for li in self.grades.values():
            list_grade += li
        average_grade = average_score(list_grade)  # Среднее значение
        return average_grade

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not Lecturer')
            return
        return self.average_grade_fl() < other.average_grade_fl()


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C++']
best_student.finished_courses += ['Введение в программирование']

best_student2 = Student('Arkadiy', 'Ukupnik', 'your_gender')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['C++']
best_student2.finished_courses += ['Введение в программирование']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.rate_hw(best_student2, 'Python', 9)
cool_mentor.rate_hw(best_student2, 'Python', 9)
cool_mentor.rate_hw(best_student2, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 8)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_mentor2 = Reviewer('Leonid', 'Yakubovich')
cool_mentor2.courses_attached += ['Python']
cool_mentor2.rate_hw(best_student2, 'Python', 8)
cool_mentor2.rate_hw(best_student2, 'Python', 7)
cool_mentor2.rate_hw(best_student2, 'Python', 10)
cool_mentor2.rate_hw(best_student, 'Python', 9)
cool_mentor2.rate_hw(best_student, 'Python', 5)
cool_mentor2.rate_hw(best_student, 'Python', 9)

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

student_list = [best_student, best_student2]


def Overall_GPA_S(student_list, cours_name):  # Средняя оценка студентов по курсу cours_name
    score_list = []
    for i in student_list:
        score_list += i.grades[cours_name]
    GPA = average_score(score_list)
    return GPA


lecturer_list = [cool_lecturer, cool_lecturer2]


def Overall_GPA_L(lecturer_list, cours_name):  # Средняя оценка лекторов по курсу
    score_list = []
    for i in lecturer_list:
        score_list += i.grades[cours_name]
    GPA = average_score(score_list)
    return GPA


print(f'{cool_lecturer}\n')
print(f'{cool_lecturer2}\n')
print(f'{best_student}\n')
print(f'{best_student2}\n')
print(cool_mentor)
print(cool_mentor2)
GPA_1 = Overall_GPA_S(student_list, 'Python')
print(f'Средний балл студентов {GPA_1}')
GPA_2 = Overall_GPA_L(lecturer_list, 'C++')
print(f'Средний балл лекторов  {GPA_2}')
print(best_student < best_student2)
print(cool_lecturer < cool_lecturer2)

