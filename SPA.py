#Name: corayme sandoval
#Period: 1-3
# Students Performance Analyzer

# Proogram indrodution

print("=====================================================================")
print("                STUDENTS PERFORMANCE ANALYZER                       ")
print("=====================================================================")

print()
student_name = input("what is the student's name?")
grade = int(input("what grade level is the student in?"))
assignment_average = float(input("what is the students's assignment average?"))
quiz_average = float(input("what is the student's quiz average?"))
test_average = float(input("what is the student's test average?"))
attendance_percentage = float(input("what is the students's attendance percentage?"))
missing_assignments = int(input("How many assignments does the student have?"))

print()


#calculate grade 

def calculate_grade(assignment_average, quiz_average, test_average):
    assignment_portion = assignment_average * 0.30
    quiz_portion = quiz_average * 0.30
    test_portion = test_average * 0.40

    overall_grade = assignment_portion + quiz_portion + test_portion


    print("overall Grade:", overall_grade)
    return overall_grade





print()
def letter_grade(overall_grade):
    if letter_grade >= 90:
        print("A")
    elif letter_grade >= 80 and letter_grade < 89:
        print("B")
    elif letter_grade >= 70 and letter_grade < 79:
        print("C")
    elif letter_grade >= 60 and letter_grade < 69:
        print("D")
    else:
        print("F")

    print("letter_grade:", letter_grade)
    return letter_grade




def attendance_status(attendance):
    if attendance >= 95:
        print("Excellent attendance")
    elif attendance >= 90 and attendance < 94:
        print("Good attendance ")
    elif attendance >= 80 and attendance < 89:
        print("Attendance Warning")
    else:
        print("Poor attendance")


    print("Attendance Status:", attendance_status )
    return attendance_status




def assignment_status(missing_assignments):
    if missing_assignments == 0:
        print("Excellent")
    elif missing_assignments <= 2:
        print("Good")
    elif missing_assignments <=4:
        print("Warning")
    else:
        print("Critical")


    print("Missing Assignments:", missing_assignments)
    return missing_assignments




#check for academic eligibility



def check_eligibility(overall_grade, attendance, missing_assignments):
    if overall_grade >= 70:
        if attendance >= 90:
            if missing_assignments <= 2:
                print("Academic eligibility: ELIGIBLE ")
                print("Students passed all three requirements")
            else:    
                print("Academic Eligibility: NOT ELIGIBLE")
                print("Reason: Too many missing assignments")
        else:
             print("Academic Eligibility: NOT ELIGIBLE")
             print("Reason: Attendance is too low")
    else:
         print("Academic Eligibility: NOT ELIGIBLE")
         print("Reason: overall grade is to low")    


# Check for high honors status


def check_high_honors(overall_grade, attendance, missing_assignments):
    if overall_grade >= 90:
        if attendance >= 95:
            if missing_assignments == 0:
                print("High Honors")
            else:
                print("High Honors: NO")
                print("Reason: Student has missing assignments.")
        else:
             print("High Honors: NO")
             print("Reason: Attendance requirement not met.")
    else:
        print("High Honors: NO")
        print("Reason: Grade requirement not met.")



def check_good_standing(overall_grade, attendance):
    if overall_grade >= 70 and attendance >= 90:
        print("Good standing: YES")
    else:
        print("Good standing: NO")



def check_support(overall_grade, attendance):
    if overall_grade <= 70 or attendance <= 80:
        print("Additional support: RECOMMENDED")
    else:
        print("Additional support: NOT NEEDED") 


def strongest_category(assignment_average, quiz_average, test_average):
    if assignment_average > quiz_average and assignment_average > test_average:
        print("Strongest Category: Assignments")
    elif quiz_average > assignment_average and quiz_average > test_average:
        print("Strongest Category: Quizzes")
    else:
        print("Strongest Category: Tests")


#check username and password 


username = input("Enter username:")
pin = input("PIN:")

if username == "student":
    if pin == "1234":
        print("Login Successful!")
    else:
        print("Login Failed: Incorrect PIN.")
else:
    print("Login Failed: Incorrect username.")


#grade level messege 


def grade_level_message(grade_level):
    if grade_level == 9:
        print("Welcome to your freshman year!")
    elif grade_level == 10:
        print("Keep building your skills!")
    elif grade_level == 11:
        print("Junior year — keep pushing!")
    elif grade_level == 12:
        print("Senior year — finish strong!")
    else:
        print("Invalid grade level.")





print("=====================================================================")
print("                STUDENTS PERFORMANCE ANALYZER                       ")
print("=====================================================================")

print("student name:", student_name)
print("grade level:", grade)

print("assignment average:", assignment_average)
print("quiz average:", quiz_average)
print("test average:", test_average)

print("overall grade:", calculate_grade(assignment_average, quiz_average, test_average))
print("attendance percentage:", attendance_percentage)
print("missing assignments:", missing_assignments)

