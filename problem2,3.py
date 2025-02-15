#Problem 2
class PartTimeStudent:
    student_count = 0  
    def __init__(self, min_hour, max_hour):
        self.min_hour = min_hour
        self.max_hour = max_hour
        PartTimeStudent.student_count += 1 
    def count():
        return PartTimeStudent.student_count
Thang = PartTimeStudent(11, 22)
Quynh = PartTimeStudent(11, 24)
Thien = PartTimeStudent(11, 21)
print(PartTimeStudent.count()) 
Vinh= PartTimeStudent(10,20)
print(PartTimeStudent.count())

#Problem3
class SchoolSystem:
    def __init__(self):
        self.students = []  
        self.lecturers = []  
        self.projects = []  

    def add_student(self, student):
        if len(self.students) < 10:
            self.students.append(student)
        else:
            print("Cannot add more students")
    def add_lecturer(self, lecturer):
        if len(self.lecturers) < 10:
            self.lecturers.append(lecturer)
        else:
            print("Cannot add more lecturers")
    def add_project(self, project):
        if len(self.projects) < 10:
            self.projects.append(project)
        else:
            print("Cannot add more projects")
    def display_summary(self):
        print("\nStudents:")
        for student in self.students:
            print(f"- {student}")

        print("\nLecturers:")
        for lecturer in self.lecturers:
            print(f"- {lecturer}")

        print("\nProjects:")
        for project in self.projects:
            print(f"- {project}")
school = SchoolSystem()
school.add_student("Vinh")
school.add_student("Thang")
school.add_lecturer("Dr Anh")
school.add_lecturer("Mrs Nhu")
school.add_project("OOP")
school.add_project("HTML")
school.display_summary()
