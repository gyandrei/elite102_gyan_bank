import mysql.connector
import functions as md



""""

git add .
git commit -m “Adding new file”
git push origin main

"""

Game = True

while Game:

    name = md.introduction()
    task, id = md.usertask(name)
    

    
    def mainfunction(task, id):
        if task == 1:
            
            md.checkbalance(id)
        
        """if task == 2:

        if task == 3:

        if task == 4:

        if task == 5:
        """

        if task == 6:

            print("""
================================================
    """)

            firstname = input("What is your legal first name? \n\n")
            lastname = input("\nWhat is your legal last name? \n")
            balance = int(input("\nHow much will you be depositing into your account? \n\n"))

            print("""
================================================
    """)

            md.createaccount(firstname, lastname, balance)
        
    
    
    mainfunction(task, id)




    

    Game = False
