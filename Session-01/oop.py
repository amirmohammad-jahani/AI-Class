class Student:
    def __init__(self,name,student_id,major):
        self.name = name
        self.student_id = student_id
        self.major = major

    def show_name(self):
        print(f"My Name Is {self.name}")

    def show_id(self):
        print(f"ID : {self.student_id}")


n1 = Student("Ali",10,"AI")
n2 = Student("Sara",20,"Network")

print(f"Name : {n1.name} , Id : {n1.student_id} , Major : {n1.major} ")
print(f"Name : {n2.name} , Id : {n2.student_id} , Major : {n2.major} ")

