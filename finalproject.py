#Final project:



#المشروع يتطلب انشاء  فئة للدورة وللطالب
#انشاء دورة
class Course:
    def __init__(self,course_name,course_level):
        self.course_id = None #يتم التعيين بشكل تلقائي
        self.course_name = course_name
        self.course_level = course_level


#انشاء فئة الطالب
class Student:
    def __init__(self, student_name, student_level):
        self.student_id = None  # سيتم تعيينه بشكل تلقائي
        self.student_name = student_name
        self.student_level = student_level
        self.student_courses = []
    def add_course(self,course):
        if course.course_level == self.student_level:
            self.student_courses.append(course)
        else:
            print(f"Cannot add course '{course.course_name}' to the student. Course level does not match student level.")
    def display_student_details(self):
        print(f"Student Name : {self.student_name}")
        print(f"Student Level: {self.student_level}")
        print("Courses Enrolled:")
        for course in self.student_courses:
            print(f"{course.course_name}")


#main page
# تعمل هذه الصفحة الرئيسية  على  قديم قائمة من الخيارات للمستخدم والسماح له بتحديد ما يريد القيام به

students = []  # قائمة لتخزين الطلاب
courses = []   # قائمة لتخزين الدورات

while True:
    print("Select an option:")
    print("1. Add new student")
    print("2. Remove student")
    print("3. Edit student")
    print("4. Display all students")
    print("5. Create new course")
    print("6. Add course to student")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:    # إضافة طالب جديد
        student_name = input("Enter student name: ")
        student_level = input("Enter student level (A/B/C): ")
        student = Student(student_name, student_level)
        students.append(student)
        print(f"Student '{student_name}' added successfully.")

    elif choice == 2:     # إزالة طالب
        student_id = int(input("Enter student ID: "))
        for student in students:
            if student.student_id == student_id:
                students.remove(student)
                print(f"Student '{student.student_name}' removed successfully.")
                break
        else:
            print("Student not found.")

    elif choice == 3:    # تحرير معلومات الطالب
        student_id = int(input("Enter student ID: "))
        for student in students:
            if student.student_id == student_id:
                new_name = input("Enter new student name: ")
                new_level = input("Enter new student level (A/B/C): ")
                student.student_name = new_name
                student.student_level = new_level
                print("Student information updated successfully.")
                break
        else:
            print("Student not found.")

    elif choice == 4:    # عرض جميع الطلاب
        print("All Students:")
        for student in students:
            student.display_student_details()

    elif choice == 5:     # إنشاء دورة جديدة
        course_name = input("Enter course name: ")
        course_level = input("Enter course level (A/B/C): ")
        course = Course(course_name, course_level)
        courses.append(course)
        print(f"Course '{course_name}' created successfully.")

    elif choice == 6:    # إضافة دورة للطالب
        student_id = int(input("Enter student ID: "))
        course_id = int(input("Enter course ID: "))
        student = None
        course = None
        for s in students:
            if s.student_id == student_id:
                student = s
                break
        for c in courses:
            if c.course_id == course_id:
                course = c
                break
        if student and course:
            student.add_course(course)
            print(f"Course '{course.course_name}' added to student '{student.student_name}' successfully.")
        else:
            print("Student or course not found.")

    elif choice == 0:
        # الخروج من البرنامج
        break

    else:
        print("Invalid choice. Please select a valid option.")