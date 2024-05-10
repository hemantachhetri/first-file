class Person: #parent class 
    #assiging attributes
    def __init__(self, name, age, cid):
        self.name = name 
        self.age = age
        self.cid = cid

    # defining behaviours 
    def walk(self):
        print (self.name, "is walking")

    def talk(self):
        print (self.name, "is talking")

    def sleep(self):
        print (self.name, " is sleeping")

    def eat(self):
        print (self.name, "is eating")

class Teacher(Person): #teacher class is inherit from person class
    def __init__(self, name, age, cid, subject, salary, department, designation):
        super().__init__(name, age, cid) #call my parent class
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

        def teach(self):
            print (self.name, "is teaching")

        def grade_students(self):
            print (self.name, "is grading")

        def attend_meeting(self):
            print (self.name, "is attending meeting")

class Student (Person):
    def __init__(self, name, age, cid, std_id, course, year, gpa):
        super().__init__(name, age, cid)
        self.std_id = std_id
        self.course = course
        self.year = year
        self.gpa = gpa

    #behaviours
    def study(self):
        print (self.name, "is studying")

    def attend_class(self):
        print (self.name, "is attending class") 

    def write_exam(self):
        print (self.name, "is writing exam") 

t1 = Teacher("Tashi", 30, 2003, "bio", 45000, "science", "Teacher")
t2 = Teacher("Sonam", 34, 1102, "physic", 45000, "science", "Teacher")

s1 = Student("Pema", 22, 1109, 1140, "BBI", 1, 3)
s2 = Student("Dorji", 21, 1103, 1173, "BBI", 1, 3.2)

if s1.gpa > s2.gpa:
    print (s1.name, "is better than", s2.name)
    student_information = "year: " + str(s1.year) + "course:"
    print (student_information)

else:
    print (s2.name, "is better than", s1.name)
    student_information = "year: " + str(s2.year) + "course:"
    print (student_information)

student_storage = [s1, s2]

for std in student_storage:
    print (std.name)
    print (std.gpa)
    print(std.course)
    print ('=======')

