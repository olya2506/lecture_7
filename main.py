class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.median_grade = 0

    def rate_lecturer(self, lecturer, course, grade_lecturer):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and lecturer.courses_attached:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade_lecturer]
            else:
                lecturer.grades_lecturer[course] = [grade_lecturer]

    def median_grade(self):
        grades_list = []
        for grades in self.grades.values():
            grades_list.append(grades)
        self.median_grade = sum(grades_list) / len(grades_list)
        return self.median_grade

    def __str__(self):
        return f'Имя: {self.name} Фамилия: {self.surname} Средняя оценка за домашние задания: {self.median_grade} Курсы в процессе изучения: {self.courses_in_progress} Завершенные курсы: {self.finished_courses}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades_lecturer = {}
    median_grade_lecture = 0

    def median_grade_lecture(self):
        grades_list = []
        for grades in self.grades_lecturer.values():
            grades_list.append(grades)
        self.median_grade_lecture = sum(grades_list) / len(grades_list)
        return self.median_grade_lecture

    def __str__(self):
        return f'Имя: {self.name} Фамилия: {self.surname} Средняя оценка за лекции: {self.median_grade_lecture}'


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
        return f'Имя: {self.name} Фамилия: {self.surname}'



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'Python', 2)

print(best_student.grades)

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 8)
best_student.rate_lecturer(cool_lecturer, 'Python', 3)

print(cool_lecturer.grades_lecturer)

print(best_student)
print(cool_lecturer)
print(cool_reviewer)
