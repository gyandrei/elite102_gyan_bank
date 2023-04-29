import mysql.connector
import os

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
clear screen
###################################################################
"""

def title(title):
    os.system('cls')
    print(f"""
================================================
                {title}
================================================\n\n\n
    """)



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

def deposit(id, deposit):
    
    connection = connect_to_db()
    
    cursor = connection.cursor()
    
    select_user_balance = (f"SELECT * from user where id={id}")

    cursor.execute(select_user_balance)

    for item in cursor:
        old_balance = [int(balance[id]) for balance in cursor.fetchone()]

    new_balance = old_balance + deposit

    print(*new_balance)

    #sql_deposit_query = (f"UPDATE user set balance = {new_balance} where id={id}")

    connection.commit() 
    
    cursor.close()
    
    connection.close()




"""
########################
Option 3. Withdraw
########################
"""

def withdraw():
    print()



"""
########################
Option 4. Delete Account
########################
"""

def deleteaccount(id):
    print()





"""
(skip option 5)
########################
Option 6. Create Account
########################
"""

def createaccount(firstname, lastname, balance):

    connection = connect_to_db()
    
    cursor = connection.cursor()
    
    sql_create_query = (f"INSERT INTO user (firstname, lastname, balance) VALUES ('{firstname}', '{lastname}', {balance})")
    
    cursor.execute(sql_create_query)
    
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
    os.system('cls')
    
    print("""
================================================
~~~~~~~~~Welcome to Gyan Banking System~~~~~~~~~
================================================  
    """)

    print("""
\n\nThis is Gyan's Banking Project for Elite 102
    """)

    input("Enter y to continue: ")

    print()






"""
###################################################################
This is user tasks function
###################################################################
"""

def usertask():
    
    title("Menu")

    options = [1,2,3,4] 
    
    haveaccount = input('\n\nDo you have an account with us already? Y/N \n')

    if haveaccount == 'Y' or haveaccount == 'y':
        title("Menu")
        id = int(input('\n\nWhat is your id? \n'))
        title("menu")
        print('\n\nWhat would you like to do today?')

        print("""
================================================
<<< 1. Check Balance
<<< 2. Deposit
<<< 3. Withdraw
<<< 4. Delete Account
================================================
    """)

        print()
        
        userchoice = int(input())

        while userchoice not in options:
            title("Menu")
            print("""
====================================================
That is not one of the options. 
Please enter a single digit number to select a task.
====================================================
    """)
            print()
            userchoice = int(input())
    
    if haveaccount == 'N' or haveaccount == 'n':
        title("Menu")
        createaccount = input("""
=================================================
Would like to create an account? Y/N
=================================================
    """)
        
        print()
        title("Create Account")
        if createaccount == 'Y' or createaccount == 'y':
            
            print("\nLet's create a new account\n")
            
            userchoice = 6
            
            id = 0

    return userchoice, id











