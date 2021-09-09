import mysql.connector
import random
import time
import string  

med_list = ['Corona_Medicine', 'Adol', 'Nose_Drops', 'Sanitizer']
mydb = mysql.connector.connect(user='root', password='root', database='hospital', autocommit=True)

cur = mydb.cursor()

print("Welcome to Hamad Hospital!\n")
run = True
globalName = 0

def random_string(letter_count, digit_count):  
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(letter_count)))  
    str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))  
  
    sam_list = list(str1) # it converts the string to list.  
    random.shuffle(sam_list) # It uses a random.shuffle() function to shuffle the string.  
    final_string = ''.join(sam_list)  
    return final_string  
def getDoctorOrPatientFromInput(activity):
        docOrPatient = int(input(f"[1: Doctor\t2: Patient]\nWould you like to {activity} as a doctor or a patient? "))
        Occupation = 0
        if docOrPatient == 1:
            Occupation = "doctor"
        elif docOrPatient == 2:
            Occupation = "patient"
        return Occupation
            
def checkIfRegisteredUserExists(docOrPatient, name):
    checkingIfNameAlreadyExists = (f"select {docOrPatient} from hos{docOrPatient} where {docOrPatient}= '{name}'")
    cur.execute(checkingIfNameAlreadyExists)
    getUser = cur.fetchone()
    userExists = False
    if getUser is not None:
        userExists = True
        return userExists

def login_to_an_existing_account():
        occupation = getDoctorOrPatientFromInput("login")
        if occupation == "doctor":
            username = input("Please enter your name to validate your details: ")
            globalName = username
            doesExist = checkIfRegisteredUserExists(occupation, username)
            if doesExist == None:
                print("Your login details are nowhere to be found...")
                register = input("Would you like to register? ")
                if register == "y": registration(occupation)
            else:
                commonMenu(occupation)
        elif occupation == "patient":
            username = input("Please enter your name to validate your details: ")
            globalName = username
            doesExist = checkIfRegisteredUserExists(occupation, username)
            if doesExist == None:
                print("Your login details are nowhere to be found...")
                register = input("Would you like to register? ")
                if register == "y": registration(occupation)
            else: 
                commonMenu(occupation)

def registration(docOrPatient):
    print("Beginning registration...")
    time.sleep(random.randrange(0, 3))
    name = input("Enter your name: ")
    globalName = name
    doesExist = checkIfRegisteredUserExists(docOrPatient, name)
    if doesExist == True:
        print("Your data already exists in the database.")
    else:
        print("Your account has been created successfully... Please provide the following details to complete the registration!")
        age = int(input("Enter your age: "))
        phone = int(input("Enter your phone number: (+974) ---------"))
        med = random.choice(med_list)
        if docOrPatient == "doctor":
            print({name, age, phone, med})
            print("Generating your ID")
            time.sleep(1)
            ID = random_string(8, 4)
            print(f"Your randomly generated ID is: [{ID}]")
            command = (f"insert into hosdoctor (doctor, age, id, phone) values('{name}', {age}, '{ID}', {phone})")
            cur.execute(command)
        if docOrPatient == "patient":
            dis = input("Enter your disease: ")
            command = (f"insert into hospatient (patient, age, dis, phone, med) values('{name}', {age}, '{dis}', {phone}, '{med}')")
            cur.execute(command)
        print("Successful Registration...\nYou'll be logged in shortly!")
        login_to_an_existing_account()

def commonMenu(occupation):
    mainMenu = {}
    def task(task_fn):
        mainMenu[task_fn.__name__] = task_fn
    def delete_account(occupation):
        print("Deleting your account")
        cur.execute(f"DELETE FROM hos{occupation} WHERE {occupation}_name = '" + str(globalName) + "'")
        print("Account has been deleted successfully!")
        

    def view_personal_details(occupation):
        print("Name  Age  Disease  Phone No.  Meds ")        
        command3 = (f"select*from hos{occupation} where {occupation}_name='" + str(globalName) + "'")
        cur.execute(command3)
        result = cur.fetchall()
        for i in result:
            print(f"i[0] i[1] i[2] i[3] i[4]")

    def write_feedback():
        patientName = input("Enter name of the patient: ")
        doesExist = checkIfRegisteredUserExists("patient", patientName)
        if doesExist == None:
            print("Patient records not found!")
        else:
            print(f"Creating a file for {patientName} if it doesn't exist!")
            file = open(f"{patientName} - Doctor's Advice.txt", "w")
            review = input("Enter your review [add a fullstop to split the lines!]: ")
            splitReviews = review.split(".")
            file.writelines(splitReviews)
            print("Review written successfully!")
            print("\n".join(splitReviews))

    def request_consultation_fee():
        patientName = input("Enter name of the patient: ")
        doesExist = checkIfRegisteredUserExists("patient", patientName)
        if doesExist == None:
            print("Patient records not found!")
        else:
            fee = int(input("Enter the fee that you require: "))
            feeQuery = (f"UPDATE hospatient SET fee = {fee} WHERE patient = '{patientName}'")
            cur.execute(feeQuery)
            print(f"Fee required updated!\n{patientName} is now required to pay {fee}")

    def view_all_registered_patients():
        print("Fetching data...")
        cur.execute(f"select * from hospatient")
        records = cur.fetchall()
        time.sleep(random.randrange(0, 3))
        print(f"Records of [{len(records)}] patients found!")
        patientID = 1
        for x in records:
            print(f"---------------- [{patientID}] - Patient Name: {x[0]}\nPatient Age: {x[1]}\nPatient Disease: {x[2]}\nPatient Phone number: {x[3]}\nMedicines used: {x[4]}\nPending fee: {x[5]}")
            patientID+=1
            time.sleep(random.randrange(0, 3))

    def view_all_registered_doctors():
        print("Fetching data...")
        cur.execute(f"select * from hosdoctor")
        records = cur.fetchall()
        time.sleep(random.randrange(0, 3))
        print(f"Records of [{len(records)}] doctors found!")
        doctorID = 1
        for x in records:
            print(f"---------------- [{doctorID}] - Doctor Name: {x[0]}\nDoctor Age: {x[1]}\nDoctor ID: {x[2]}\nDoctor Phone number: {x[3]}")
            Doctor+=1
            time.sleep(random.randrange(0, 3))
    def make_payment():
        name = input("Enter your name: ")
        if name != globalName:
            print("Incorrect details")
        print("Enter payment method ""\n""1:Card only""\n")
        pay = int(input("Enter your choice "))
        if pay == 1:
            card_det = input("Enter card holder's name: ")
            card_pwd = int(input("Enter card pin: "))
            amountToPay = cur.execute(f"SELECT fee FROM hospatient WHERE patient = '{card_det}'")
            print(f"You have {amountToPay} left to pay!")
            card_amount = int(input("Enter amount pending($): "))
            print("Sending...")
            time.sleep(random.randrange(0, 3))
            if card_amount == amountToPay:
                cur.execute(f"UPDATE hospatient SET fee = 0 WHERE patient == '{card_det}'")
                print("Amount Sent! You have $0 left to pay!")
            else:
                print("INVALID_TRANSACTION")
    def read_feedback():
        print("Here is our Doctor's view on your health")
        with open(f"{globalName}", 'r') as file:
            data = file.readlines()
            for j in data:
                print(j, end="")
    
    mainMenu = {'1': delete_account, '2': view_personal_details}
    doctorMenu = {'3': write_feedback, '4': request_consultation_fee, '5': view_all_registered_patients}   
    patientMenu = {'3': make_payment, '4': read_feedback}   
    completeMenu = mainMenu.copy()
    if occupation == "doctor":
        completeMenu.update(doctorMenu)
    if occupation == "patient":
        completeMenu.update(patientMenu)
    for key, value in completeMenu.items():
        print(f"{key} : {value.__name__ }")
    MenuInput = int(input("Make your choice: "))
    try:
        completeMenu[f"{MenuInput}"](occupation)
    except TypeError:
        completeMenu[f"{MenuInput}"]()

def register_new_account():
    try:
        registration(getDoctorOrPatientFromInput("register"))
    except Exception as error:
        print("Error occured! ")
        print(error)

    
while run:
    cur = mydb.cursor()
    #cur.execute("DROP DATABASE hospital")

    #cur.execute("CREATE DATABASE hospital")
    #cur.execute("USE hospital")
    
    cur.execute("CREATE TABLE IF NOT EXISTS hospatient (patient VARCHAR(255), age VARCHAR(255), dis VARCHAR(255), phone VARCHAR(255), med VARCHAR(255), fee VARCHAR(100))")
    cur.execute("CREATE TABLE IF NOT EXISTS hosdoctor (doctor VARCHAR(255), age VARCHAR(255), id VARCHAR(255), phone VARCHAR(255))")
    beginMenu = {'1': register_new_account, '2': login_to_an_existing_account}
    for key, value in beginMenu.items():
        print(f"{key} : {value.__name__ }")
    MenuInput = int(input("Make your choice: "))
    try:
        beginMenu[f"{MenuInput}"](occupation)
    except NameError:
        beginMenu[f"{MenuInput}"]()

