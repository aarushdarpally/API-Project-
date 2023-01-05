from flask import Flask, request
import random

app = Flask(__name__)



# API 1: Create User
@app.route('/getuser', methods=['GET'])
def numbers():
    args = request.args
    username = args.get("createusername")
    password = args.get("createpassword")
    teacher_name = args.get("teachername")
    user_pass = [username, password]

    access_data = open("usernamesandpasswords.txt", "r")
    for line in access_data.readlines():
        if line.__contains__(user_pass[0]):
            return "this name already exists."
    else:
        user_data = open("usernamesandpasswords.txt", "a+")
        user_data.write(username + "|" + password + "|" + teacher_name)
        user_data.write("\n")
        return "created successfully"

# API 2: The login APi
@app.route('/login', methods=['GET'])
def login():
    args = request.args
    username = args.get("enterusername")
    password = args.get("enterpassword")
    access_data = open("usernamesandpasswords.txt", "r")
    user_data = []
    for line in access_data.readlines():
        if line == ' ':
            pass
        else:
            user_data.append(line.replace('\n', ''))
    user_names = []
    passwords = []

    for data in user_data:
        data = data.split("|")
        user_names.append(data[0])
        passwords.append(data[1])

    # googled this part only
    usersandpass = {key: value
                   for key, value in zip(user_names, passwords)}

    if username in usersandpass and usersandpass[username] == password:
        return "Login successful"
    elif username not in usersandpass:
        return "username and password don't exist"
    else:
        return "invalid credentials"



# API 3 CreateStudents
@app.route('/createstudents', methods=['POST'])
def students():
    args = request.args
    student_name = args.get("studentname")
    student_grade_level = args.get("classtype")

    teachers = []
    teachers_names = []
    teacher_data = open("usernamesandpasswords.txt", "r")
    for line in teacher_data.readlines():
        if line == ' ':
            pass
        else:
            teachers.append(line.replace("\n", ''))

    for teacher in teachers:
        teacher = teacher.split("|")
        teachers_names.append(teacher[2])


    assign_teacher = random.choice(teachers_names)

    add_students = open("students.txt", "r")
    for line in add_students.readlines():
        if line.__contains__(student_name):
            return "the student name already exists"
    else:
        student_data = open("students.txt", "a+")
        student_data.write(student_name + "|" + student_grade_level + "|" + assign_teacher)
        student_data.write("\n")



    return str(student_name + "|" + student_grade_level + "|" + assign_teacher)

# API 4 add GPA's to the student
@app.route('/addgpa', methods=['GET'])
def add_grades():
    args = request.args
    student_name = args.get("studentname")
    student_gpa = args.get("gpa")
    get_students = []

    student_data = open("students.txt", "r")

    for line in student_data.readlines():
        get_students.append(line.replace('\n',''))

    gpa_data = open("studentsgpa.txt", "r")
    for student in get_students:
        if student.__contains__(student_name):
            for file_line in gpa_data.readlines():
                if file_line.__contains__(student_name):
                    return "the student name already exists"
            else:
                data_gpa = open("studentsgpa.txt", "a+")
                data_gpa.write(student + "|" + student_gpa)
                data_gpa.write("\n")
        else:
            pass



    return str(gpa_data.readlines())


# API 5 retrieve data from gpa file and get data from user based on grade
@app.route('/assortgrades', methods=['GET'])
def assortgrades():
    args = request.args
    retrieve_class = args.get('accessgrade')
    retrieve_data = open("studentsgpa.txt", "r")
    data = []
    grade9_data = []
    grade10_data = []
    grade11_data = []
    grade12_data = []

    for freshman in grade9_data:
        grade_nine_data = open("grade9.txt", "a+")
        grade_nine_data.write(freshman)


    for line in retrieve_data.readlines():
        data.append(line.replace('\n',''))

    for data_line in data:
        if data_line.__contains__('freshman'):
            grade9_data.append(data_line)
        elif data_line.__contains__('sophomore'):
            grade10_data.append(data_line)
        elif data_line.__contains__('junior'):
            grade11_data.append(data_line)
        elif data_line.__contains__('senior'):
            grade12_data.append(data_line)
        else:
            pass

    if retrieve_class == 'freshman':
        return str(grade9_data)
    elif retrieve_class == 'sophomore':
        return str(grade10_data)
    elif retrieve_class == 'junior':
        return str(grade11_data)
    elif retrieve_class == 'senior':
        return str(grade12_data)
    else:
        pass



# API 6: Get student with highest gpa based on their class type
@app.route('/findhighgpa', methods=['GET'])
def findhighgpa():
    args = request.args
    grade_level_val = args.get("gradelevelval")


    student_data_from_file = open("studentsgpa.txt", "r")
    student_data = []

    for line in student_data_from_file.readlines():
        student_data.append(line.replace('\n',''))

    freshman_data = []
    sophomore_data = []
    junior_data = []
    senior_data = []

    for student in student_data:
        if student.__contains__('freshman'):
            freshman_data.append(student)
        elif student.__contains__('sophomore'):
            sophomore_data.append(student)
        elif student.__contains__('junior'):
            junior_data.append(student)
        elif student.__contains__('senior'):
            senior_data.append(student)
        else:
            pass

    if grade_level_val == '9':
        freshman_names = []
        freshman_teachers = []
        freshman_gpas = []
        for freshman in freshman_data:
            freshman = freshman.split('|')
            freshman_names.append(freshman[0])
            freshman_teachers.append(freshman[2])
            freshman_gpas.append(float(freshman[3]))

        freshman_students_andgpas = {key: value
                        for key, value in zip(freshman_names, freshman_gpas)}

        # googled this part only
        freshman_highest_gpa = max(freshman_students_andgpas.values())
        freshman_student_with_high_gpa = max(freshman_students_andgpas, key=freshman_students_andgpas.get)

        return "Student with highest gpa in freshman is " + freshman_student_with_high_gpa + " with gpa of " + str(freshman_highest_gpa)
    elif grade_level_val == '10':
        sophomore_names = []
        sophomore_teachers = []
        sophomore_gpas = []
        for sophomore in sophomore_data:
            sophomore = sophomore.split('|')
            sophomore_names.append(sophomore[0])
            sophomore_teachers.append(sophomore[2])
            sophomore_gpas.append(float(sophomore[3]))

        sophomore_students_gpa = {key: value
                                     for key, value in zip(sophomore_names, sophomore_gpas)}
        sophomore_highest_gpa = max(sophomore_students_gpa.values())
        sophomore_student = max(sophomore_students_gpa, key=sophomore_students_gpa.get)
        return "Student with highest gpa in sophomores is " +sophomore_student + " with gpa of " +str(sophomore_highest_gpa)
    elif grade_level_val == '11':
        junior_names = []
        junior_teachers = []
        junior_gpas = []
        for junior in junior_data:
            junior = junior.split('|')
            junior_names.append(junior[0])
            junior_teachers.append(junior[2])
            junior_gpas.append(float(junior[3]))

        junior_students_gpa = {key: value
                               for key, value in zip(junior_names, junior_gpas)}
        junior_highest_gpa = max(junior_students_gpa.values())
        junior_student = max(junior_students_gpa, key=junior_students_gpa.get)
        return "Student with highest gpa in juniors is "+ junior_student + " with gpa of " + str(junior_highest_gpa)
    elif grade_level_val == '12':
        senior_names = []
        senior_teachers = []
        senior_gpas = []
        for senior in senior_data:
            senior = senior.split('|')
            senior_names.append(senior[0])
            senior_teachers.append(senior[2])
            senior_gpas.append(float(senior[3]))

        senior_students_gpa = {key: value
                               for key, value in zip(senior_names, senior_gpas)}
        senior_highest_gpa = max(senior_students_gpa.values())
        senior_student = max(senior_students_gpa, key=senior_students_gpa.get)
        return "Student with highest gpa in seniors is "+ senior_student + " with gpa of " + str(senior_highest_gpa)
    else:
        pass




app.run(host='0.0.0.0', port=8090)