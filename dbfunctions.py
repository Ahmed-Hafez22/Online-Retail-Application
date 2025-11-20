from libs import *
from db import *

def checkStaffPosition():
    staff_lst = db_cursor.execute("SELECT role, email FROM storeStaff").fetchall()


def validateLogin(enteredEmail, enteredPassword):
    if ("@" in enteredEmail):
        staffInfo_lst = db_cursor.execute("SELECT email, password FROM storeStaff").fetchall()

        for staffInfo in staffInfo_lst:
            if(enteredEmail == staffInfo[0] and enteredPassword == staffInfo[1]):
                print("Login successful")
                return
            else:
                print("Invalid email or password")
    else:
        print("Please enter a valid email")


#--------------------------------------------------------
# Manager Functions
def addEmployee():
    requests = db_cursor.execute("SELECT requestDetails FROM pendingRequest WHERE requestType = 'storeStaff'").fetchall()
    for request in requests:
        potentialRequest = json.loads(request[0])
        for personnelInfo in potentialRequest.items():
            print(f"{personnelInfo[0]} : {personnelInfo[1]}")
        choice = input(f"Will you give the job to {potentialRequest['Name']}: ")

        if choice == "Y":
            role = input(f"Assign the role of {potentialRequest["Name"]}: ")
            potentialRequest["Role"] = role

            finalTuple = tuple(potentialRequest.values())
            db_cursor.executemany("INSERT INTO storeStaff(name, email, password, role) VALUES(?, ?, ?, ?)", (finalTuple,))


            db_connection.commit()
        
        else:
            pass

def registerProduct():
    