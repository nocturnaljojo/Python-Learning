import mysql.connector

# Before you start this database, you will need to import 'mysql.connector' like the code above
mydb = mysql.connector.connect(
    host='localhost',                   # not using server, so stick with local
    user='root',                        # mySQL username : user (default)
    password='myDatabasePassword',      # use your actual database password,
    port='3306',                        # im using mySQL database, that's why the port is 3306
    database='pythontut'                # my database schemas (I created this before running this code)
)
myCursor = mydb.cursor()

sql = "INSERT INTO user_table (id,username,password) VALUES (%s,%s,%s)"
val = ("1","Jaesuk","myPassword")

myCursor.execute(sql,val)
# mydb.commit() # << commit() if you want to persist(actually save into your database) use this.

print(myCursor.rowcount, "record inserted")

myCursor = mydb.cursor()
myCursor.execute('select * from user_table')
users = myCursor.fetchall()

for user in users:
    print(user)
    print('Username : ' + user[1])
    print('Password : ' + user[2])
