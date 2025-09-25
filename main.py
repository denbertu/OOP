from itertools import chain


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Error"

    @staticmethod
    def __calc_avg_grade(obj):
        overall_grades = list(chain.from_iterable([v for k, v in obj.grades.items()]))
        avg_grades = sum(overall_grades) / len(overall_grades)
        return round(avg_grades, 1)
    
    def __eq__(self, other):
        self_avg_grade = Student.__calc_avg_grade(self)
        other_avg_grade = Student.__calc_avg_grade(other)
        if self_avg_grade == other_avg_grade:
            return True
        else:
            return False
        
    def __gt__(self, other):
        self_avg_grade = Student.__calc_avg_grade(self)
        other_avg_grade = Student.__calc_avg_grade(other)
        if self_avg_grade > other_avg_grade:
            return True
        else:
            return False
        
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {Student.__calc_avg_grade(self)}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    @staticmethod
    def __calc_avg_grade(obj):
        overall_grades = list(chain.from_iterable([v for k, v in obj.grades.items()]))
        avg_grades = sum(overall_grades) / len(overall_grades)
        return avg_grades
    
    def __eq__(self, other):
        self_avg_grade = Lecturer.__calc_avg_grade(self)
        other_avg_grade = Lecturer.__calc_avg_grade(other)
        if self_avg_grade == other_avg_grade:
            return True
        else:
            return False
        
    def __gt__(self, other):
        self_avg_grade = Lecturer.__calc_avg_grade(self)
        other_avg_grade = Lecturer.__calc_avg_grade(other)
        if self_avg_grade > other_avg_grade:
            return True
        else:
            return False
            
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {Lecturer.__calc_avg_grade(self)}")
    

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
        return f"Имя: {self.name}\nФамилия: {self.surname}"


def calc_stud_avg_grade(*students, course):
    overall_grades = []
    for student in students:
        if isinstance(student, Student) and course in student.grades:
            overall_grades.extend(student.grades[course])
    avg_grade = sum(overall_grades) / len(overall_grades)
    return int(avg_grade)

def calc_lect_avg_grade(*lecturers, course):
    overall_grades = []
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.grades:
            overall_grades.extend(lecturer.grades[course])
    avg_grade = sum(overall_grades) / len(overall_grades)
    return int(avg_grade)


lecturer_1 = Lecturer('Иван', 'Иванов')
lecturer_2 = Lecturer('Boris', 'Borisov')
reviewer_1 = Reviewer('Пётр', 'Петров')
reviewer_2 = Reviewer('Пётр', 'Петров')
student_1 = Student('Алёхина', 'Ольга', 'Ж')
student_2 = Student('Алёхина', 'Ольга', 'Ж')
mentor_1 = Mentor('Fedor', 'Fedorov')
mentor_2 = Mentor('Alexei', 'Alexeev')
 
student_1.courses_in_progress += ['Python', 'Java', 'C++']
student_2.courses_in_progress += ['Python', 'Java', 'C++']
lecturer_1.courses_attached += ['Python', 'Java', 'C++']
lecturer_2.courses_attached += ['Python', 'Java', 'C++']
reviewer_1.courses_attached += ['Python', 'Java', 'C++']
reviewer_2.courses_attached += ['Python', 'Java', 'C++']
 
student_1.rate_lecture(lecturer_1, 'Python', 7)
student_1.rate_lecture(lecturer_1, 'Python', 8)
student_1.rate_lecture(lecturer_1, 'Python', 2)
student_1.rate_lecture(lecturer_1, 'Java', 8)
student_1.rate_lecture(lecturer_1, 'C++', 8)  
student_1.rate_lecture(lecturer_1, 'Python', 6)

student_2.rate_lecture(lecturer_2, 'Python', 3)
student_2.rate_lecture(lecturer_2, 'Python', 1)
student_2.rate_lecture(lecturer_2, 'Python', 7)
student_2.rate_lecture(lecturer_2, 'Java', 3)
student_2.rate_lecture(lecturer_2, 'C++', 2)  
student_2.rate_lecture(lecturer_2, 'Python', 2)

reviewer_1.rate_hw(student_1, 'Python', 3)
reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'C++', 4)
reviewer_1.rate_hw(student_1, 'Python', 6)
reviewer_1.rate_hw(student_1, 'Java', 3)

reviewer_2.rate_hw(student_2, 'Python', 2)
reviewer_2.rate_hw(student_2, 'Python', 5)
reviewer_2.rate_hw(student_2, 'Python', 2)
reviewer_2.rate_hw(student_2, 'C++', 4)
reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Java', 3)

# print(lecturer_1 < lecturer_2)
# print(lecturer_1 == lecturer_2)
# print(student_1 > student_2)
# print(student_1 == student_2)

# print(student_1)
# print(lecturer_1)
# print(mentor_1)
# print(reviewer_1)

# print(calc_stud_avg_grade(student_1, student_2, course="Python"))
# print(calc_lect_avg_grade(lecturer_1, lecturer_2, course="Python"))

