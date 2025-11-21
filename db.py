from libs import *

db_connection = connect("storeDatabase.db")
db_cursor = db_connection.cursor()

db_cursor.execute(
    """
                  CREATE TABLE IF NOT EXISTS products (
                  id INTEGER PRIMARY KEY,
                  Product TEXT,
                  category TEXT,
                  productID TEXT,
                  quantity INTEGER,
                  price REAL,
                  merchantPrice INTEGER
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
                  password TEXT,
                  salary INTEGER
                  )

""")

db_cursor.execute("""
                CREATE TABLE IF NOT EXISTS pendingRequest(
                  id INTEGER PRIMARY KEY,
                  requestType TEXT,
                  requestDetails TEXT
                  )


""")
db_cursor.execute("""
                CREATE TABLE IF NOT EXISTS financials(
                  id INTEGER PRIMARY KEY,
                  sales INTEGER,
                  spentMoney INTEGER,
                  totalNetWorth INTEGER
                  )



""")
db_cursor.execute("UPDATE products SET merchantPrice = 10 WHERE ProductID = '001'")
db_connection.commit()