class Class:
    __students_count = 22

    def __init__(self, name: str):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, student_name: str, grade: float):
        if Class.__students_count > 0:
            self.students.append(student_name)
            self.grades.append(grade)
            Class.__students_count -= 1

    def get_average_grade(self):
        grades_sum = sum(self.grades)

        return float(f"{grades_sum / len(self.students):.2f}")

    def __repr__(self):
        return f"The students in {self.name}: {", ".join(self.students)}. Average grade: {self.get_average_grade()}"

a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)

