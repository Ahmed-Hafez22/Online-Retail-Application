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

    dict = {
        "Name" : "", 
        "Category" : "",
        "ProductID": 0,
        "Price" : 0
    }

    for key in dict.keys():
        dict[key] = input(f"Enter the {key} of the product: ")

    finalTuple = tuple(dict.values())
    db_cursor.executemany("INSERT INTO products(Product, category, productID, price) VALUES(?,?,?,?)", (finalTuple,))
    db_connection.commit()


def restockProduct():
    productID = input("Enter the ProdcutID of the product: ")

    productName = db_cursor.execute("SELECT product FROM products WHERE productID = ?" , (productID,)).fetchone()[0]

    newQuantity = int(input(f"Enter the new quantity of the {productName} you want: "))

    productPrice = db_cursor.execute("SELECT merchantPrice FROM products WHERE ProductID = ?", (productID,)).fetchone()[0] 
    currentNetWorth = db_cursor.execute("SELECT totalNetWorth FROM financials").fetchone()[0]

    if (currentNetWorth >= (newQuantity * productPrice)):
        currentNetWorth -= (newQuantity * productPrice)
        sales = (newQuantity * productPrice)
        db_cursor.execute("UPDATE financials SET totalNetWorth = ? WHERE Month = ?", (currentNetWorth, ))
        db_cursor.execute("UPDATE products SET quantity = ? WHERE productID = ?", (newQuantity, productID))
    else:
        print("Insufficient balance")
    
#-----------------------------------------------
def intializeTable():
    currentMonthYear = datetime.now().strftime("%m-%Y")

    registeredMonthYear = db_cursor.execute("SELECT monthYear FROM financials").fetchone()

    

    # if currentMonthYear in registeredMonthYear:
    #     pass
    # else:
    #     db_cursor.execute("INSERT INTO financials(monthYear) Values(?)", (currentMonthYear,))

    # db_connection.commit()

intializeTable()