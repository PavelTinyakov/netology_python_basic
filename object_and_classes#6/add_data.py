from random import shuffle, randint


def add_new_courses_students(courses, *students):
    courses = courses.copy()
    for student in students:
        shuffle(courses)
        student.add_courses(*courses[:randint(1, len(courses) - 1)])


def add_end_courses_students(*students):
    for student in students:
        courses = student.courses_in_progress
        shuffle(courses)
        student.add_finished_courses(*courses[:randint(0, len(courses) - 1)])


def add_courses_lecturers(courses, *lecturers):
    for ind, lecturer in enumerate(lecturers):
        if ind % 2 == 0:
            lecturer.add_courses(*courses[:int(len(courses) / 2)])
        else:
            lecturer.add_courses(*courses[int(len(courses) / 2):])


def add_rate_hw(*humans):
    students = []
    reviewers = []
    for human in humans:
        if human._status() == 'Преподаватель (проверяющий)':
            reviewers.append(human)
        elif human._status() == 'Студент':
            students.append(human)
    for reviewer in reviewers:
        for student in students:
            for course in student.courses_in_progress:
                for _ in range(1, randint(2, 10)):
                    reviewer.rate_hw(student, course, randint(1, 10))


def add_rate_course(*humans):
    students = []
    lecturers = []
    for human in humans:
        if human._status() == 'Преподаватель (лектор)':
            lecturers.append(human)
        elif human._status() == 'Студент':
            students.append(human)
    for student in students:
        for lecturer in lecturers:
            for course in lecturer.courses_attached:
                student.rate_course(lecturer, course, randint(1, 10))


def average_grades_course_students(course, *students):
    result = []
    for student in students:
        if student.grades.get(course):
            result.extend(student.grades[course])
    return round(sum(result)/len(result), 1)


def average_grades_course_lecturers(course, *lecturers):
    result = []
    for lecturer in lecturers:
        if lecturer.courses_grades.get(course):
            result.extend(lecturer.courses_grades[course])
    return round(sum(result)/len(result), 1)
