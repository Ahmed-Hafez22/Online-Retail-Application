from libs import *

db_connection = connect("storeDatabase.db")
db_cursor = db_connection.cursor()

db_cursor.execute(
    """
                  CREATE TABLE IF NOT EXISTS products (
                  id INTEGER PRIMARY KEY,
                  category TEXT,
                  productID INTEGER,
                  quantity INTEGER,
                  price REAL
                  )
                  """
)

db_cursor.execute(
    """
                 CREATE TABLE IF NOT EXISTS customers (
                 id INTEGER PRIMARY KEY,
                 customerID INTEGER,
                 shippingAddress TEXT,
                 billingAddress TEXT,
                 name TEXT,
                 email TEXT,
                 password TEXT
                 )


"""
)

db_cursor.execute("""
                CREATE TABLE IF NOT EXISTS storeStaff (
                  id INTEGER PRIMARY KEY,
                  name TEXT,
                  role TEXT,
                  email TEXT,
                  password TEXT
                  )

""")

db_cursor.execute("INSERT INTO storeStaff(name, role, email, password) VALUES('Ahmed Mohamed Ali', 'Manager', 'ahmed@gmail.com', 'bestManagerEver')")

db_connection.commit()