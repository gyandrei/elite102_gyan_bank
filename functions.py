import mysql.connector


#################variable###################
name = 0
task = 0

"""
###################################################################
This is where the databse is connected to python
###################################################################
"""

def connect_to_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Aquarius_9789',
        database='gyan_bank'
    )

"""
###################################################################
Option 1. Check Balance
###################################################################
"""

def checkbalance(id):
    connection = connect_to_db()
    cursor = connection.cursor()
    testQuery = (f'')
    cursor.execute(testQuery)
    for item in cursor:
        print(item)
    cursor.close()
    connection.close()

"""
###################################################################
Option 2. Deposit
###################################################################
"""

def deposit(id):
    connection = connect_to_db()
    cursor = connection.cursor()
    testQuery = (f'SELECT * FROM user where ')



"""
###################################################################
Option 3. Withdraw
###################################################################
"""




"""
###################################################################
Option 4. Delete Account
###################################################################
"""




"""
###################################################################
Option 5. Modify Account
###################################################################
"""





"""
###################################################################
Option 6. Create Account
###################################################################
"""

def createaccount(id, firstname, lastname, balance):
    connection = connect_to_db()
    cursor = connection.cursor()
    sql = "INSERT INTO customers VALUES (%s, %s)"
    val = (f"{id}", f"{firstname}", f"{lastname}", f"{balance}")
    cursor.execute(sql, val)
    cursor.close()
    connection.close()
    connect_to_db.commit()



"""
###################################################################
This is where the introduction begins
###################################################################
"""

def introduction():
        
    print("""
    ================================================
    ~~~~~~~~~Welcome to Gyan Banking System~~~~~~~~~
    ================================================  
    """)

    name = input('What is your name: ')

    return name


"""
###################################################################
This is user tasks function
###################################################################
"""

def usertask(user_name):
    name = user_name
    options = [1,2,3,4,5] 
    
    haveaccount = input('Do you have an account with us already? Y/N \n')

    if haveaccount == 'Y':

        id = int(input('What is your id? \n'))

        print(f'\nHello {name}. What would you like to do today?')

        print("""
    ================================================
    <<< 1. Check Balance
    <<< 2. Deposit
    <<< 3. Withdraw
    <<< 4. Delete Account
    <<< 5. Modify Account
    ================================================
    """)
    
        
        userchoice = int(input())

        while userchoice not in options:
            print("""
    ====================================================
    That is not one of the options. 
    Please enter a single digit number to select a task.
    ====================================================
    """)
            userchoice = int(input())
    
    if haveaccount == 'N':
        createaccount = input("""
    ====================================================
    Would like to create an account? Y/N \n
    ====================================================
    """)
        
        if createaccount == 'Y':
            print("Let's create a new account")
            userchoice = 6
            id = 0

    return userchoice, id











