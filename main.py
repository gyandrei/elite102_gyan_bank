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
    task = md.usertask(name)
    print(name)
    print(task)

    def mainfunction(task):
        if task == 1:
            print("What is your id")
            id = int(input())
            md.checkbalance(id)
    
    mainfunction(task)




    ##md.printuser()

    Game = False
