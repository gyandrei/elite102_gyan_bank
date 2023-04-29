import mysql.connector
import functions as md
import os 


""""

git add .
git commit -m “Adding new file”
git push origin main

"""

Game = True

while Game:
    md.introduction()
    
    task, id = md.usertask()
    
    def mainfunction(task, id):
        
        if task == 1:
            md.title("Check Balance")
            md.checkbalance(id)
        
        """if task == 2:

        if task == 3:

        if task == 4:

        """

        if task == 6:
            md.title("Create Account")
            print("""
================================================
    """)

            firstname = input("\n\n\nWhat is your legal first name? \n\n\n")
            
            lastname = input("What is your legal last name? \n\n\n")
            
            balance = int(input("How much will you be depositing into your account? \n\n\n"))

            print("""
================================================
    """)

            md.createaccount(firstname, lastname, balance)
        
    mainfunction(task, id)

    Game = False
