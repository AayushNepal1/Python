from random import randint
class Die:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_dice(self):
       roll = 0
       while roll < 10: 
        rand = [randint(1, self.sides)]
        for run in rand:
            print(f"""
                :--------:    
                |___|____|     
                |{run}\t\t  
                |___|____| /
                |___|____|/
            """)
        roll += 1
        
print("For 6 sides Die:")
dice = Die()
dice.roll_dice()
print("------------------------------------")

print("For 10 sides Die:") 
dice = Die(10)
dice.roll_dice()
print("-------------------------------------") 

print("For 20 sides Die:")
dice = Die(20)
dice.roll_dice()
