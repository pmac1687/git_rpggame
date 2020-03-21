import sys
import os
import random
import pdb
import pickle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox, QTextEdit

class Player:
    def __init__(self, name):
        self.name = name

        self.health = 30
        self.attack = 50
        self.gold = 55
        self.pots = 1
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.correctguesses = '012345'
        self.guessesleft = 6
        self.hangmanpic = 'hangman.jpg'
        self.letterguess = ''
        self.wrongguesses = ''
        self.hangman = 'dragon'
        self.hangmanfigure = 0
        self.hangmanfigurepics = ['hangman1.png','hangman2.jpg','hangman3.jpg','hangman4.jpg','hangman5.jpg','hangman6.jpg','hangman7.png']
        self.hasexcalibur = False

class Monster :
    def __init__(self,name,health,attack,gold):
        self.name = name
        self.health = health
        self.attack = attack
        self.gold = gold



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(583, 579)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(16, 20, 431, 51))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(22)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(250, 90, 291, 271))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("opening_image.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(16, 230, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 390, 101, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 390, 101, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(344, 390, 111, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textedit = QtWidgets.QTextEdit(Form)
        self.textedit.setGeometry(QtCore.QRect(20, 200, 241, 31))
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 125, 241, 91))
        self.label_4.setText('Pick a number')
        self.label_4.hide()
        self.textedit.hide()
        self.nums = ''
        self.guesses = []
        self.msg = 'msg'

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

            
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Super Gnar Adventure"))
        self.label_3.setText(_translate("Form", "What would you like to do?"))
        self.pushButton.setText(_translate("Form", "EXPLORE"))
        self.pushButton_2.setText(_translate("Form", "STORE"))
        self.pushButton_3.setText(_translate("Form", "STATUS"))

        self.pushButton.clicked.connect(self.explore)
        self.pushButton_3.clicked.connect(self.status)

    def main(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.label_4.hide()
        self.label.setText(_translate("Form", "Super Gnar Adventure"))
        self.label_3.setText(_translate("Form", "What would you like to do?"))
        self.pushButton_2.show()
        self.pushButton_3.show()
        self.pushButton.setText(_translate("Form", "EXPLORE"))
        self.pushButton_2.setText(_translate("Form", "STORE"))
        self.pushButton_3.setText(_translate("Form", "STATUS"))
        self.label_2.setPixmap(QtGui.QPixmap("opening_image.png"))
        self.label_2.setScaledContents(True)

        self.pushButton.clicked.connect(self.explore)
        

    def explore(self, Form):
        _translate = QtCore.QCoreApplication.translate
        x = random.randint(1, 4)
        if x == 1:
            self.label_3.setText(_translate("Form", "You Found A treasure chest!"))
            self.pushButton.setText(_translate("Form", "CONTINUE"))
            self.pushButton_2.hide()
            self.pushButton_3.hide()
            self.label_2.setPixmap(QtGui.QPixmap("CHEST.jpg"))
            self.label_2.setScaledContents(True)
            self.pushButton.clicked.connect(self.chest)
        if x == 2:
            self.label_3.setText(_translate("Form",'As you walk in the room, bones in the \ncorner of the room jump into the air \nand spring to life!!'))
            self.pushButton.setText(_translate("Form", "CONTINUE"))
            self.pushButton_2.hide()
            self.pushButton_3.hide()
            self.label_2.setPixmap(QtGui.QPixmap("skeletons.jpg"))
            self.label_2.setScaledContents(True)
            self.pushButton.clicked.connect(self.skeletons)
        if x == 3:
            self.label_3.setText(_translate("Form",'In the corridor a head as you hear \ncackling from the shadows out leaps \na hoarde of goblin'))
            self.pushButton.setText(_translate("Form", "CONTINUE"))
            self.pushButton_2.hide()
            self.pushButton_3.hide()
            self.label_2.setPixmap(QtGui.QPixmap("goblin.jpg"))
            self.label_2.setScaledContents(True)
            self.pushButton.clicked.connect(self.goblins)
        if x == 4:
            if name.hasexcalibur == False:
                self.label_3.setText(_translate("Form",'there is some kind of puzzle on the \nwall'))
                self.pushButton.setText(_translate("Form", "CONTINUE"))
                self.pushButton_2.hide()
                self.pushButton_3.hide()
                self.label_2.setPixmap(QtGui.QPixmap("hangman.jpg"))
                self.label_2.setScaledContents(True)
                self.pushButton.clicked.connect(self.bridge)
            else:
                self.label_3.setText(_translate("Form", 'Some creature welcomes you \nfrom the darkness'))
                self.pushButton.setText(_translate("Form", "CONTINUE"))
                self.pushButton_2.hide()
                self.pushButton_3.hide()
                self.label_2.setPixmap(QtGui.QPixmap("dragoneye.jpg"))
                self.label_2.setScaledContents(True)
                self.pushButton.clicked.connect(self.dragon)



    def bridge(self):
        self.main(Form)
        self.hangmangame()


    class hangmangame(QDialog):

        def __init__(self):
            super().__init__()

            self.init_ui()


        def init_ui(self):
            self.msg = QtWidgets.QDialog()
            self.msg.setGeometry(300, 100, 500, 500)
            self.msg.textedit = QTextEdit(self.msg)
            self.msg.textedit.setGeometry(20,300,100,20)
            self.msg.label1 = QtWidgets.QLabel(self.msg)
            self.msg.label1.setText('{}{}{}'.format('available letters:','\n',name.alphabet))
            self.msg.label1.move(20, 80)
            self.msg.label2 = QtWidgets.QLabel(self.msg)
            self.msg.label2.setText('{}{}{}{}'.format('guesses left = ',name.guessesleft,'\n', name.correctguesses))
            self.msg.label2.move(20, 260)
            self.msg.label3 = QtWidgets.QLabel(self.msg)
            self.msg.label3.setText('type a letter and hit enter')
            self.msg.label3.move(20, 360)
            self.msg.b1 = QtWidgets.QPushButton('enter', self.msg)
            self.msg.b1.move(20, 320)
            self.msg.label_2 = QtWidgets.QLabel(self.msg)
            self.msg.label_2.setGeometry(QtCore.QRect(200, 50, 291, 271))
            self.msg.label_2.setPixmap(QtGui.QPixmap(name.hangmanpic))
            self.msg.label_2.setScaledContents(True)
            self.msg.b1.clicked.connect(self.hangmanguess)
            self.msg.exec_()



        def hangmanguess(self):
            name.letterguess = self.msg.textedit.toPlainText()
            self.msg.textedit.clear()
            print(name.letterguess)
            self.msg.exit
            if name.letterguess.isalpha() and len(name.letterguess) == 1:
                print(name.letterguess)
                name.letterguess = name.letterguess.lower()
                if name.letterguess in name.hangman:
                    y = name.hangman.find(name.letterguess)
                    name.correctguesses = name.correctguesses.replace(str(y),name.letterguess,1)
                    name.alphabet = name.alphabet.replace(name.letterguess,' ')
                    if name.hangmanfigure == 0 :
                        name.hangmanpic = name.hangmanfigurepics[name.hangmanfigure]
                    if name.correctguesses == name.hangman:
                        return self.excalibur()
                else:
                    name.alphabet = name.alphabet.replace(name.letterguess, ' ')
                    name.hangmanpic = name.hangmanfigurepics[name.hangmanfigure]
                    name.hangmanfigure += 1
                    name.guessesleft -= 1
                    if name.guessesleft == 0:
                        self.hangmanlose()
                self.init_ui()




        def excalibur(self):
            _translate = QtCore.QCoreApplication.translate
            self.msg.textedit.hide()
            self.msg.label1.setText('click red X to exit hangman')
            self.msg.label2.setText(_translate('msg','The wall opens up and What is it....'))
            self.msg.label3.setText(_translate('msg','You have found EXCALIBUR!!!'))
            self.msg.label_2.setPixmap(QtGui.QPixmap(_translate('msg','excalibur.jpg')))
            self.msg.label_2.setScaledContents(True)
            self.msg.b1.clicked.connect(self.backtomain)

        def backtomain(self):
            self.msg.close()
            self.msg.reject()
            self.msg.destroy()
            ui.main(Form)














    def chest(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("Form", "What would you like to do?"))
        self.pushButton.setText(_translate("Form", "FORCE OPEN"))
        self.pushButton_2.show()
        self.pushButton_2.setText(_translate("Form", "PICK LOCK"))
        self.pushButton_3.setText(_translate("Form", ""))
        self.label_2.setPixmap(QtGui.QPixmap("question.jpg"))
        self.label_2.setScaledContents(True)
        self.pushButton.clicked.connect(self.force)
        self.pushButton_2.clicked.connect(self.checklock)

    def force(self, Form):
        _translate = QtCore.QCoreApplication.translate
        """put randint here"""
        z= random.randint(1,4)  
        if z == 2:
            self.label_3.setText(_translate("Form", "You cleave the chest open with your \n sword and discover 40 gold pieces!!"))
            self.pushButton.setText(_translate("Form", "CONTINUE"))
            self.pushButton_2.setText(_translate("Form", ""))
            self.pushButton_3.setText(_translate("Form", ""))
            self.label_2.setPixmap(QtGui.QPixmap("treasure.png"))
            self.label_2.setScaledContents(True)
            self.pushButton.clicked.connect(self.main)
        else:
            self.label_3.setText(_translate("Form", "You strike the chest but your blow \n glances off the chest"))
            self.pushButton.setText(_translate("Form", "CONTINUE"))
            self.pushButton_2.setText(_translate("Form", ""))
            self.pushButton_3.setText(_translate("Form", ""))
            self.label_2.setPixmap(QtGui.QPixmap("doh.jpg"))
            self.label_2.setScaledContents(True)
            self.pushButton.clicked.connect(self.failedpick)


    def checklock(self, Form):
        
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("Form", "The lock appears to have some kind of \n number dials on it."))
        self.pushButton.setText(_translate("Form", "CONTINUE"))
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.label_4.hide()
        self.textedit.hide()
        self.label_2.setPixmap(QtGui.QPixmap("lock.jpg"))
        self.label_2.setScaledContents(True)
        self.pushButton.clicked.connect(self.pick)


     
    def pick(self, Form):


        _translate = QtCore.QCoreApplication.translate
        self.label_4.show()
        self.textedit.show()
        self.label_4.setText(_translate("Form","Pick a number between 1-20 and click CONTINUE \n< REPEAT 3 TIMES >"))
        self.label_3.setText(_translate("Form", self.nums))
        self.pushButton.setText(_translate("Form", "CONTINUE"))
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.label_2.setPixmap(QtGui.QPixmap("lock.jpg"))
        self.label_2.setScaledContents(True)
        self.pushButton.clicked.connect(self.combos)


    def combos(self, Form):
        _translate = QtCore.QCoreApplication.translate
        guess = self.textedit.toPlainText()
        self.textedit.clear()
        if len(self.guesses) == 3:
            solution = 5
            if solution in self.guesses:
                name.gold += 20
                return self.pickedlock(Form)
            else:
                return self.failedpick(Form)
        elif guess.isdigit():
            if int(guess) <= 20 :
                self.nums = '{}{}{}'.format(self.nums,'  ',guess)
                self.guesses.append(int(guess))
        return self.pick(Form)

                         
                
 

    def failedpick(self, Form):
        _translate = QtCore.QCoreApplication.translate
        
        self.label_4.show()
        self.textedit.hide()
        self.label_4.setText(_translate("Form","As you enter the last number...."))
        self.label_3.setText(_translate("Form", 'A Trap door opens at your feet and \nyou fall through the floor!'))
        self.pushButton.setText(_translate("Form", "CONTINUE"))
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.label_2.setPixmap(QtGui.QPixmap("trapdoor.jpg"))
        self.label_2.setScaledContents(True)
        self.pushButton.clicked.connect(self.main)
        self.textedit.clear()

    def pickedlock(self, Form):
        print('failedpick')
        _translate = QtCore.QCoreApplication.translate
        self.label_4.show()
        self.textedit.hide()
        self.label_4.setText(_translate("Form","As you enter the last digit the lock falls open \n SUCCESS!!!"))
        self.label_3.setText(_translate("Form", 'YOU FIND 20 PIECES OF GOLD'))
        self.pushButton.setText(_translate("Form", "CONTINUE"))
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.label_2.setPixmap(QtGui.QPixmap("treasure.png"))
        self.label_2.setScaledContents(True)
        self.pushButton.clicked.connect(self.main)

    def skeletons(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_2.show()
        self.pushButton_3.show()
        self.label_4.show()
        self.textedit.hide()
        self.label_4.setText(_translate("Form", ""))
        self.label_3.setText(_translate("Form", 'What would you like to do?'))
        self.pushButton.setText(_translate("Form", "ATTACK"))
        self.pushButton_2.setText(_translate('Form','FLEE'))
        self.pushButton_3.setText(_translate('Form','STATUS'))
        self.label_2.setPixmap(QtGui.QPixmap("skeletons.jpg"))
        self.label_2.setScaledContents(True)
        self.pushButton.clicked.connect(self.skeletoncombat)
        self.pushButton_3.clicked.connect(self.status)

    def goblins(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_2.show()
        self.pushButton_3.show()
        self.label_4.show()
        self.textedit.hide()
        self.label_4.setText(_translate("Form", ""))
        self.label_3.setText(_translate("Form", 'What would you like to do?'))
        self.pushButton.setText(_translate("Form", "ATTACK"))
        self.pushButton_2.setText(_translate('Form','FLEE'))
        self.pushButton_3.setText(_translate('Form','STATUS'))
        self.label_2.setPixmap(QtGui.QPixmap("goblin.jpg"))
        self.label_2.setScaledContents(True)
        self.pushButton.clicked.connect(self.goblincombat)
        self.pushButton_3.clicked.connect(self.status)

    def dragon(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.show()
        self.pushButton_2.show()
        self.pushButton_3.show()
        self.label_4.show()
        self.textedit.hide()
        self.label_4.setText(_translate("Form", "THE GREAT AND TERRIBLE SMAUG"))
        self.label_3.setText(_translate("Form", 'What would you like to do?'))
        self.pushButton.setText(_translate("Form", "ATTACK"))
        self.pushButton_2.setText(_translate('Form', 'FLEE'))
        self.pushButton_3.setText(_translate('Form', 'STATUS'))
        self.label_2.setPixmap(QtGui.QPixmap("dragon1.jpg"))
        self.label_2.setScaledContents(True)
        self.pushButton.clicked.connect(self.dragoncombat)
        self.pushButton_3.clicked.connect(self.status)



    def skeletoncombat(self, Form):
        _translate = QtCore.QCoreApplication.translate
        print(skeletons.health)
        if skeletons.health <= 0:
            self.label_4.setText(_translate('Form',"your blow strikes true and the skeleton falls to the \nground decapitated"))
            self.label_3.setText(_translate('Form',"you find 10 gold pieces on the skeletons remains"))
            self.label_2.setPixmap(QtGui.QPixmap("treasure.png"))
            self.pushButton_2.hide()
            self.pushButton_3.hide()
            name.gold += skeletons.gold
            skeletons.health = 80
            self.pushButton.setText(_translate('Form','CONTINUE'))
            self.pushButton.clicked.connect(self.main)
        elif name.health <= 0:
            self.label_3.setText(_translate('Form',"you are tipsy on your feet \nwould you like to drink a potion?"))
            self.pushButton_3.hide()
            self.pushButton_2.show()
            self.label_2.setPixmap(QtGui.QPixmap('potion.jpg'))
            self.pushButton.setText(_translate('Form','YES'))
            self.pushButton_2.setText(_translate('Form','NO'))
            self.pushButton.clicked.connect(self.drinkpotionskel)
            self.pushButton_2.clicked.connect(self.playerdead)
        elif name.health > 0 and skeletons.health > 0 :
            return self.skeletoncombatround(Form)

    def goblincombat(self, Form):
        _translate = QtCore.QCoreApplication.translate
        print(skeletons.health)
        if goblin.health <= 0:
            self.label_4.setText( _translate('Form', "the goblin squeals as you lop its head off"))
            self.label_3.setText(_translate('Form', "you find 10 gold pieces on the skeletons remains"))
            self.label_2.setPixmap(QtGui.QPixmap("treasure.png"))
            self.pushButton_2.hide()
            self.pushButton_3.hide()
            name.gold += goblin.gold
            goblin.health = 80
            self.pushButton.setText(_translate('Form', 'CONTINUE'))
            self.pushButton.clicked.connect(self.main)
        elif name.health <= 0:
            self.label_3.setText(_translate('Form', "you are tipsy on your feet \nwould you like to drink a potion?"))
            self.pushButton_3.hide()
            self.pushButton_2.show()
            self.label_2.setPixmap(QtGui.QPixmap('potion.jpg'))
            self.pushButton.setText(_translate('Form', 'YES'))
            self.pushButton_2.setText(_translate('Form', 'NO'))
            self.pushButton.clicked.connect(self.drinkpotionskel)
            self.pushButton_2.clicked.connect(self.playerdead)
        elif name.health > 0 and goblin.health > 0:
            return self.goblincombatround(Form)

    def dragoncombat(self, Form):
        _translate = QtCore.QCoreApplication.translate
        print(dragon.health)
        if dragon.health <= 0:
            self.pushButton_2.hide()
            self.label_4.setText(_translate('Form', "Your stab pierces Smaugs \nscales and Smaug falls dead \nupon your sword!!!"))
            self.label_3.setText(_translate('Form', "Smaug's treasure hoarde is yours!!\nYOU WIN!!"))
            self.label_2.setPixmap(QtGui.QPixmap("dragongold.jpg"))
            self.pushButton_3.hide()
            self.pushButton_2.clicked.connect(self.finale())
            self.pushButton.hide()


        elif name.health <= 0:
            self.label_3.setText(_translate('Form', "you are tipsy on your feet \nwould you like to drink a potion?"))
            self.pushButton_3.hide()
            self.pushButton_2.show()
            self.label_2.setPixmap(QtGui.QPixmap('potion.jpg'))
            self.pushButton.setText(_translate('Form', 'YES'))
            self.pushButton_2.setText(_translate('Form', 'NO'))
            self.pushButton.clicked.connect(self.drinkpotionskel)
            self.pushButton_2.clicked.connect(self.playerdead)
        elif name.health > 0 and dragon.health > 0:
            return self.dragoncombatround(Form)

    def dragoncombatround(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.pushButton.setText(_translate('Form', 'CONTINUE'))
        self.pushButton.clicked.connect(self.dragon)
        a = random.randint(1, 10)
        if a > 2:
            self.label_3.setText(_translate('Form', "You swing and hit the Dragon"))
            dragon.health = dragon.health - name.attack
        elif a <= 2:
            self.label_3.setText(_translate('Form', "you slice at the dragon and whiff!!"))
        b = random.randint(1, 10)
        if b >= 5:
            self.label_4.setText(_translate('Form', "dragon lunges, but you quickly \ndodge the attack"))
        elif b < 5:
            self.label_4.setText(_translate('Form', 'The dragon attacks and you take the brunt of it'))
            name.health = name.health - dragon.attack


    def skeletoncombatround(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.pushButton.setText(_translate('Form', 'CONTINUE'))
        self.pushButton.clicked.connect(self.skeletons)
        a = random.randint(1, 10)
        if a > 2:
            self.label_3.setText(_translate('Form', "You swing and hit the Skeleton"))
            skeletons.health = skeletons.health - name.attack
        elif a <= 2:
            self.label_3.setText(_translate('Form',"you slice at the skeleton and whiff!!" ))
        b = random.randint(1, 10)
        if b >= 5:
            self.label_4.setText(_translate('Form', "skeleton lunges, but you quickly \ndodge the attack"))
        elif b < 5:
            self.label_4.setText(_translate('Form','The Skeletons attack and you take the brunt of it' ))
            name.health = name.health - skeletons.attack

    def goblincombatround(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.pushButton.setText(_translate('Form', 'CONTINUE'))
        self.pushButton.clicked.connect(self.goblins)
        a = random.randint(1, 10)
        if a > 2:
            self.label_3.setText(_translate('Form', "You swing and hit the goblin"))
            goblin.health = goblin.health - name.attack
        elif a <= 2:
            self.label_3.setText(_translate('Form', "you slice at the goblin and whiff!!"))
        b = random.randint(1, 10)
        if b >= 5:
            self.label_4.setText(_translate('Form', "goblin lunges, but you quickly \ndodge the attack"))
        elif b < 5:
            self.label_4.setText(_translate('Form', 'The goblin attack and you take the brunt of it'))
            name.health = name.health - goblin.attack

    def drinkpotionskel(self, Form):
        _translate = QtCore.QCoreApplication.translate
        if name.pots > 0:
            name.health += 20
            name.pots -= 1
            print(name.health, name.pots)
            self.label_3.setText(_translate('Form', 'You have recovered 20 hp.'))
            self.pushButton_2.hide()
            self.pushButton.setText(_translate('Form', 'CONTINUE'))
            self.label_2.setPixmap(QtGui.QPixmap('heart.png'))

            self.pushButton.clicked.connect(self.skeletons)


        elif name.pots == 0:
            self.label_3.setText(_translate('Form', 'You dont have and potions left.'))
            self.pushButton_2.hide()
            self.label_2.setPixmap(QtGui.QPixmap('fainted.jpg'))
            self.pushButton.setText(_translate('Form', 'CONTINUE'))
            self.pushButton.clicked.connect(self.playerdead)



    def playerdead(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate('Form', 'You fought the good fight but your \njourney ends here.'))
        self.label_2.setPixmap(QtGui.QPixmap('rip.jpg'))
        self.pushButton.setText(_translate('Form', 'EXIT'))
        self.pushButton_2.hide()
        self.pushButton.clicked.connect(exit)

    def finale(self):
        msg = QtWidgets.QDialog()
        msg.setGeometry(100,300,300,300)
        msg.label_2 = QtWidgets.QLabel(msg)
        msg.label_2.setGeometry(QtCore.QRect(10, 10, 291, 271))
        msg.label_2.setPixmap(QtGui.QPixmap('final.jpg'))
        msg.label_2.setScaledContents(True)
        msg.btn2 = QtWidgets.QPushButton(msg)
        msg.btn2.setText('main menu')
        msg.btn2.move(125, 90)
        msg.b1 = QtWidgets.QPushButton('exit',msg)
        msg.b1.move(125,125)
        msg.b1.clicked.connect(exit)
        msg.btn2.clicked.connect(self.main)
        msg.btn2.clicked.connect(msg.close)
        msg.show()
        x = msg.exec_()


    def final(self, Form, msg):
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate('Form', 'Well done young hero you \nhave defeated smaug and brought \npeace to the land'))
        self.label_2.setPixmap(QtGui.QPixmap('final.jpg'))
        self.pushButton.setText(_translate('Form', 'EXIT'))
        self.pushButton_2.hide()
        self.pushButton.clicked.connect(self.bridgetoexit)

    def status(self):
        msg = QtWidgets.QDialog()
        msg.setGeometry(300,300,300,300)
        msg.label1 = QtWidgets.QLabel(msg)
        msg.label1.setText('{}{}'.format('Health = ',str(name.health)))
        msg.label1.move(125,80)
        msg.label2 = QtWidgets.QLabel(msg)
        msg.label2.setText('{}{}'.format('Gold = ', str(name.gold)))
        msg.label2.move(125, 100)
        msg.b1 = QtWidgets.QPushButton('ok',msg)
        msg.b1.move(125,125)
        msg.b1.clicked.connect(msg.close)
        msg.show()
        x = msg.exec_()


    def hidemessage(self,msg):
        msg.hide()



    def bridgetoexit(self):
       if name.hasexcalibur == True :
           self.exiter()

    def exiter(self):
        exit()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    name = Player('pat')
    dragon = Monster('dragon',40,15,100)
    goblin = Monster('goblin',10,6,15)
    skeletons = Monster('skeletons',30,7,15)
    Form = QtWidgets.QWidget()
    box = QMessageBox()
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

