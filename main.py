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
            firstname = input("What is your legal first name? \n")
            lastname = input("What is your legal last name? \n")
            balance = int(input("How much will you be depositing into your account? \n"))
            md.createaccount(id, firstname, lastname, balance)
        
    
    
    mainfunction(task, id)




    

    Game = False
