class Student:
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}

    def add_grade(self,course,grade):
        if grade >= 0 and grade <= 20:
            self.grades[course] = grade
        else:
            print("Invalid grade")
            return

    def average(self):
        if self.grades:
            return sum(self.grades.values()) / len(self.grades)
        else:
            return 0

    def best_course(self):
        if not self.grades:
            return None
        return max(self.grades,key=self.grades.get)

    def failed_courses(self):
        list_failed = []
        for course, grade in self.grades.items():
            if grade < 10:
                list_failed.append(course)
    def status(self):
        avg = self.average()
        if avg >= 17:
            return "Excellent"
        elif avg >= 14:
            return "Good"
        elif avg >= 12:
            return "Normal"
        elif avg < 12:
            return "Probation"

    def report(self):
        print(f"Student {self.name}(ID: {self.student_id})")
        for course, grade in self.grades.items():
            print(f"{course}: {grade}")
        print(f"Average: {self.average()}")
        print(f"Best Course: {self.best_course()}")
        print(f"Failed Courses: {self.failed_courses()}")
        print(f"Status: {self.status()}")

student1 = Student("Ali",403644154)
student1.add_grade("Math",18)
student1.add_grade("Data Mining",14)
student1.add_grade("English",20)
student1.add_grade("Data Structure",8)
student1.report()

print("=================================")
student2 = Student("Sara",403644180)
student2.add_grade("Math",17)
student2.add_grade("Data Mining",19)
student2.add_grade("English",19)
student2.add_grade("Data Structure",15)
student2.report() 

print("=================================")
student1.add_grade("Iot",25)

