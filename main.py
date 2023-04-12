#import functions as md

#md.introduction()



import mysql.connector

 

connection = mysql.connector.connect(user = 'root', database = 'example', password = 'Aquarius_9789')

 

cursor = connection.cursor()

 

testQuery = ('SELECT * FROM student')

 

cursor.execute(testQuery)

 

for item in cursor:

    print(item)

 

cursor.close()

connection.close()

