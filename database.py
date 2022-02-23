import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="toor"
# )
# # creating database
# mycursor = mydb.cursor()
# # Creating the database
# #mycursor.execute("CREATE DATABASE vaccine")
# # Deleting the database
# #mycursor.execute("DROP DATABASE mydatabase")




mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="toor",
  database="vaccine"
)
mycursor = mydb.cursor()

# sql = "INSERT INTO records (aadhaar, ) VALUES (%s, %s)"
def create_table():
  query = '''
  CREATE TABLE v_records 
  (aadhaar VARCHAR(255) NOT NULL,
   person VARCHAR(255),
   token INT  not null,
   dose1 BOOLEAN,
   dose2 BOOLEAN, 
    PRIMARY KEY (aadhaar))
    '''
  mycursor.execute(query)

def insert(aadhaar, name,token_num, dose1,dose2):
  sql = "INSERT INTO v_records (aadhaar, person,token, dose1, dose2) VALUES (%s, %s,%s, %s, %s)"
  values = (aadhaar, name, token_num, dose1, dose2)
  mycursor.execute(sql, values)
  mydb.commit()
  print(mycursor.rowcount, 'Record Inserted')

def fetch_res():
  mycursor.execute("SELECT * FROM v_records")
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)

def change_table():
  # query = "ALTER TABLE v_records ADD (dose1 BOOLEAN, dose2 BOOLEAN)"
  query = "DROP TABLE v_records"
  mycursor.execute(query)

