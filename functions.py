import mysql.connector


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
Options start
###################################################################
"""

"""
#######################
Option 1. Check Balance
#######################
"""

def checkbalance(id):
    connection = connect_to_db()
    cursor = connection.cursor()
    testQuery = (f'SELECT * FROM user where id={id}')
    cursor.execute(testQuery)
    for item in cursor:
        print(item)
    cursor.close()
    connection.close()

"""
#######################
Option 2. Deposit
#######################
"""

def deposit(id):
    connection = connect_to_db()
    cursor = connection.cursor()
    testQuery = (f'SELECT * FROM user where ')



"""
########################
Option 3. Withdraw
########################
"""




"""
########################
Option 4. Delete Account
########################
"""




"""
########################
Option 5. Modify Account
########################
"""





"""
########################
Option 6. Create Account
########################
"""

def createaccount(firstname, lastname, balance):
    connection = connect_to_db()
    cursor = connection.cursor()
    sql = (f"INSERT INTO user (firstname, lastname, balance) VALUES ('{firstname}', '{lastname}', {balance})")
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()
    
"""
###################################################################
Option finished
###################################################################




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
    print()
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

        print()
        
        userchoice = int(input())

        while userchoice not in options:
            print("""
    ====================================================
    That is not one of the options. 
    Please enter a single digit number to select a task.
    ====================================================
    """)
            print()
            userchoice = int(input())
    
    if haveaccount == 'N':
        createaccount = input("""
    =================================================
    Would like to create an account? Y/N
    =================================================
    """)
        print()
        if createaccount == 'Y':
            print("Let's create a new account")
            userchoice = 6
            id = 0

    return userchoice, id











