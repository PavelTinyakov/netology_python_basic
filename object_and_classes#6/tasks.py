from add_data import add_new_courses_students, add_end_courses_students, \
    add_courses_lecturers, add_rate_hw, add_rate_course, average_grades_course_students, \
    average_grades_course_lecturers


class HumanInUniversity:
    def __init__(self, name: str, surname: str, gender: str):
        self.name = name
        self.surname = surname
        self.gender = gender

    def __str__(self):
        return f'Статус: {self._status()}\n' \
               f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Пол: {self.gender}'

    def _status(self) -> str:
        if isinstance(self, Reviewer):
            return 'Преподаватель (проверяющий)'
        if isinstance(self, Lecturer):
            return 'Преподаватель (лектор)'
        if isinstance(self, Student):
            return 'Студент'
        return 'Не определен'


class Lecturer(HumanInUniversity):
    def __init__(self, name: str, surname: str, gender: str):
        super().__init__(name, surname, gender)
        self.courses_attached = []
        self.courses_grades = {}

    def add_courses(self, *courses: str) -> None:
        self.courses_attached.extend(list(courses))

    def _average_courses_grades(self):
        grades = []
        for val in self.courses_grades.values():
            grades.extend(val)
        return round(sum(grades)/len(grades), 1)

    def __str__(self):
        return super().__str__() + \
               f'\nСредняя оценка за лекции: {self._average_courses_grades()}'


class Student(HumanInUniversity):
    def __init__(self, name: str, surname: str, gender: str):
        super().__init__(name, surname, gender)
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, *courses: str) -> None:
        self.courses_in_progress.extend(list(courses))

    def add_finished_courses(self, *courses: str) -> None:
        for course in courses:
            if course in self.courses_in_progress:
                self.courses_in_progress.remove(course)
                self.finished_courses.append(course)

    def rate_course(self, lecturer: Lecturer, course: str, grade: int) -> str | None:
        if not all((isinstance(lecturer, Lecturer), course in self.courses_in_progress,
                    course in lecturer.courses_attached, grade < 11)):
            return 'Ошибка'
        if course in lecturer.courses_grades:
            lecturer.courses_grades[course] += [grade]
        else:
            lecturer.courses_grades[course] = [grade]

    def _average_grades(self):
        grades = []
        for val in self.grades.values():
            grades.extend(val)
        return round(sum(grades)/len(grades), 1)

    def __str__(self):
        return super().__str__() + \
               f'\nСредняя оценка за домашние задания: {self._average_grades()}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return 'не принадлежит классу Lecturer'
        return self._average_grades() <= other._average_courses_grades()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return 'не принадлежит классу Lecturer'
        return self._average_grades() >= other._average_courses_grades()


class Reviewer(Lecturer):
    def rate_hw(self, student: Student, course: str, grade: int) -> str | None:
        if not all((isinstance(student, Student), course in self.courses_attached,
                    course in student.courses_in_progress, grade < 11)):
            return 'Ошибка'
        if course in student.grades:
            student.grades[course] += [grade]
        else:
            student.grades[course] = [grade]

    def __str__(self):
        return HumanInUniversity.__str__(self)


if __name__ == '__main__':
    list_courses = ['Git', 'SQL', 'Django', 'HTML/CSS', 'JavaScript',
                    'PyQT', 'React', 'Python', 'Agile', 'NoSQL']

    student_1 = Student('Иван', 'Иванов', 'М')
    student_2 = Student('Ольга', 'Смирнова', 'Ж')
    student_3 = Student('Роман', 'Ким', 'М')
    student_4 = Student('Сергей', 'Лазарев', 'М')
    student_5 = Student('Светлана', 'Романова', 'Ж')
    lecturer_1 = Lecturer('Александр', 'Лях', 'М')
    lecturer_2 = Lecturer('Константин', 'Власов', 'М')
    reviewer_1 = Reviewer('Евгения', 'Филина', 'Ж')
    reviewer_2 = Reviewer('Юлия', 'Власова', 'Ж')

    # Генерация данных
    add_new_courses_students(list_courses, student_1, student_2, student_3, student_4, student_5)
    add_end_courses_students(student_1, student_2, student_3, student_4, student_5)
    add_courses_lecturers(list_courses, lecturer_1, lecturer_2, reviewer_1, reviewer_2)
    add_rate_hw(reviewer_1, reviewer_2, student_1, student_2, student_3, student_4, student_5)
    add_rate_course(lecturer_1, lecturer_2, student_1, student_2, student_3, student_4, student_5)

    print(student_1, end='\n\n')
    print(student_2, end='\n\n')
    print(student_3, end='\n\n')
    print(student_4, end='\n\n')
    print(student_5, end='\n\n')
    print(lecturer_1, end='\n\n')
    print(lecturer_2, end='\n\n')
    print(reviewer_1, end='\n\n')
    print(reviewer_2, end='\n\n')

    print(student_5 <= lecturer_2)
    print(student_5 >= lecturer_2)
    print(student_5 == lecturer_2, end='\n\n')

    course_ = 'Git'
    print(f'Средняя оценка за домашние задания по всем студентам в рамках курса {course_}:')
    print(average_grades_course_students(course_, student_1, student_2, student_3, student_4, student_5))
    print(f'Средняя оценка за лекции всех лекторов в рамках курса {course_}:')
    print(average_grades_course_lecturers(course_, lecturer_1, lecturer_2))
