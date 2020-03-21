import sys 
import os
import random
import pickle
import yournamewindow 


class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 10
        self.gold = 55
        self.pots = 0
        
    

    


class Monster :
    def __init__(self,name,health,attack,gold):
        self.name = name
        self.health = health
        self.attack = attack
        self.gold = gold

        
        
dragon = Monster('dragon',40,15,100)
goblin = Monster('goblin',10,6,15)
zombie = Monster('zombie',10,7,15)
        







def explore():
    x = random.randint(1,4)
    if x == 1:
        print('you have found a treasure chest what would you like to do?')
        print("type 'force' to force it open, or 'pick' to pick the lock")
        fop = input('')
        if fop == 'force' :
            z= random.randint(1,10)
            if z == 6:
                print('you cleave the chest open with your sword and discover 40 gold pieces')
                name.gold += 40
                main()
            else:
                print('you swing true but your blow bounces right off the chest')
                print('from the shadows leaps a goblin')
                combat3(goblin)
        if fop == 'pick' :
            print("the lock has some combination of numbers on it pick a number from 1 to 20")
            p1 = input("")
            print("pick another number from 1-20")
            p2 = input("")
            print("pick one final number from 1-20")
            p3 = input("")
            y = random.randint(1,20)
            if p1 == y or p2 == y or p3 == y:
                print('the chest pops open, your intuition prevails again!')
                print("inside the chest you discover 40 gold pieces")
                name.gold += 40
                main()
            else:
                print("as you enter the combination, a trap door opens underfoot and you crash hard into the ground,'ouch!' you exclaim")
                name.health -= 10
                main()
    if x == 2 :
        print('it smells like moldy death in here')
        print('a cohort of goblins emerges from the darkness')
        combat3(goblin)
    if x == 3:
        print('an eerie silence resonates from this wretched place, almost as if it were a tomb')
        print('in the next room you a creature ravenously eating something on the ground')
        print('as you edge closer you come to you now see that its a disfigured humanoid creature feasting on a dead body')
        print('it notices you and turns to come at you, arms out stretched and blood thirsty')
        combat1(zombie)
    
    if x == 4:
        print('from the darkness you sense a presence')
        print('pick a number from 1-4')
        pick = input('')
        if pick == '4' :
            print('you hear an ominous voice beckoning you into the large chamber ahead')
            print('you step into a massive antichamber')
            print('an enourmous dragon looms in the darkness, it begins to speak')
            print("the great and terrible smaug speaks :'whether you come for my treasure or my life, it matters not because you have made a grave mistake, and shall pay with your life!")
            combat2(dragon)
        else:
            main()

def combat1(zombie):
    print('what do you want to do?')
    print('type: "attack" or "flee" or "status"')
    atorfl = input('')
    if atorfl == 'attack' :
        if zombie.health <= 0 :
            print("your blow strikes true and the zombie falls to the ground decapitated")
            print("you find 10 gold pieces on the zombie")
            name.gold += zombie.gold
            zombie.health = 80
            main()
        elif name.health <= 0 :
            print("you are tipsy on your feet, would you like to drink a potion")
            print("'yes' or 'no'")
            yono = input("")
            if yono == 'yes' :
                if name.pots > 0 :
                    name.health = 10
                    name.pots -= 1
                else:
                    print("you fall to the floor dead, your suffering ends here")
                    exit()
                    
            else:
                print("you fall to the floor dead, used and abused your adventure ends here")
                exit()
            
        a = random.randint(1,10)
        if a > 2 :
            print("you swimg and hit the zombie")
            zombie.health = zombie.health - name.attack
        
        elif a <= 2 :
            print("you slice at the zombie and whiff!!")
            
        b = random.randint(1,10)
        if b >= 5:
            print("zombie lunges, but you quickly dodge the attack")
            
        elif b < 5 :
            print("you take damage from the zombie")
            name.health = name.health - zombie.attack
        
    elif atorfl == "status" :
        print("{}{}".format("zombie health= ",zombie.health))
        print("{}{}".format("your health= ",name.health))
        
    elif atorfl == 'flee' :
        m = random.randint(1,4)
        if m == 2:
            print("you successfully evade the zombie")
            main()
        else:
            print("you try to run but the zombie strikes you from behind")
            name.health -= zombie.attack
    else:
        wrongCommand()
    combat1(zombie)

def combat2(dragon):
    print("what would you like to do: 'attack', 'flee','status'")
    act = input('')
    if act == 'flee' :
        if name.attack > 20 :
            print("the door to the chamber seals shut behind you, you will have to fight your way out")
            combat2(dragon)
        if name.attack <= 20 :
            rint = random.randint(1,2) 
            if rint == 1 :
                print("as you run off the dragon cackles in the darkness")
                main()
            elif rint == 2 :
                print('as you try to escape the dragon whips its tall and sends you flying across the room')
                name.health -= dragon.attack
                combat2(dragon)
    elif act == 'attack' :
        if name.health > 0 and dragon.health > 0 :
            a = random.randint(1,10)
            if a > 5 :
                print('your blow glances off the dragons scales')
            elif a <= 5 :
                print('your attack hurts the dragon')
                dragon.health -= name.attack
            b = random.randint(1,10)
            if b > 4 :
                print('the dragons expels fire from its mouth, but you evade the attack')
            elif b <= 4 :
                print("the dragons attack is powerful and knocks you off your feet")
                name.health -= dragon.attack
            combat2(dragon)
        else:
            if dragon.health <= 0 :
                print("you have defeated the great dragon Smaug! the townsfolk cannot thankyou enough")
                print("congratulations traveler you have vanquished the great evil of this land!")
                exit()
            elif name.health <= 0 :
                print('you have sustained heavy damage and are on the verge of collapse, would you like to drink a potion : "yes" or "no"')
                yono = input('')
                if yono == 'yes' :
                    if name.pots > 0 :
                        name.health += 20
                        combat2(dragon)
                    elif name.pots <= 0 :
                        print("you have no potions and fall to the ground dead! better luck next time traveler")
                        exit()
                elif yono == 'no' :
                    print("you have no potions and fall to the ground dead! better luck next time traveler")
                    exit()
    elif act == 'status' :
        print('{}{}{}'.format("your","health = ",name.health))
        print('{}{}{}'.format('dragon ','health = ',dragon.health))
    else:
        wrongCommand()
    combat2(dragon)


def combat3(goblin) :
    print('what do you want to do?')
    print('choose: "attack", "flee", "status"')
    act = input('')
    if act == 'attack' :
        if name.health <= 0 :
            print('you are on the verge of death')
            print('drink a potion to regain health?("yes" or "no")')
            yono = input('')
            if yono == 'yes' :
                if name.pots > 0 :
                    print('you drink the potion and regain health')
                    name.health += 20
                else:
                    print('you are dead')
                    exit()
            if yono == 'no' :
                print('you are dead')
                exit()
        elif goblin.health <= 0 :
            print('you have defeated the goblin hoarde!')
            name.gold += goblin.gold
            goblin.health = 80
            main()
        a = random.randint(1,10)
        if a >= 5 :
            print('you single out and cleave one of the goblins in half')
            goblin.health -= name.attack
        elif a < 5 :
            print('you attack, but miss')
        b = random.randint(1,10)
        if b > 3 :
            print('you swiftly avoid the goblins attack')
        elif b <= 3:
            print('the goblins attack and knock you back')
            name.health -= goblin.attack
        combat3(goblin)
    elif act == 'flee' :
        rand = random.randint(1,2)
        if rand == 1 :
            print('you successfully escape')
            main()
        if rand == 2 :
            print("you are surrounded and cannot escape, the goblins attack")
            name.health -= goblin.attack
            combat3(goblin)
    elif act == 'status' :
        print('{}{}{}'.format(name,"health = ",name.health))
        print('{}{}{}'.format('goblin','health = ',goblin.health))
    else:
        wrongCommand()
    combat3(goblin)
    
    

def wrongCommand():
    print('I dont know that command, try again')
    
        
            
            
def store():
    print("welcome stranger, what would you like to purchase?")
    print("('greatsword' = 30 gold pieces, +10 attack bonus),('potion' = 10 gold pieces, +10 health),('excalibur' = 50 gold pieces, +20 attack, ice enhancement),(type 'exit' to leave store")
    item = input("")
    if item == 'exit' :
        main()
    print(item)
    print("if correct type 'yes' otherwise type 'no'")
    yono = input("")
    if yono == 'yes' :
        if item == 'greatsword' :
            if name.gold >= 30 :
                name.attack += 10
                name.gold -= 30
                store()
            else:
                print('you dont have eneough gold')
                store()
        if item == 'excalibur' :
            if name.gold >= 50 :
                name.attack += 20
                name.gold -= 50
                store()
            else:
                print('you dont have enough gold')
                store()
        if item == 'potion' :
            if name.gold >= 10 :
                name.pots += 1
                name.gold -= 10
            else:
                print('you dont have enough gold')
                store()
    elif yono == 'no' :
        store()
                
        
        
            
       


def main():
    print("What would you like to do?(type 'help' for list of commands)")
    action = input("")
    if action == 'quit':
        exit()
    elif action == 'help':
        print("commands = quit,help,status,rest,explore,store")
        main()
    elif action == 'explore':
        explore()
    elif action == 'status':
        print("health=")
        print(name.health)
        print("would you like to rest and regain some health?")
        print("type 'y' for yes and 'n' for no")
        yono = input('')
        if yono == 'y' :
              name.health += 10
              print("That was a refreshing nap")
              main()
        elif yono == 'n' :
            main()
    elif action == 'store' :
        store()
    else:
        wrongCommand()
        main()


    
              
              
if __name__ == "__main__" :
    MainWindow.show()
    
    print("Welcome weary traveler what is your name?")
    name = input("")
    name = Player(name)
    main()
