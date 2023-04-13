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

        if task == 6:
    """
    
    mainfunction(task, id)




    

    Game = False
