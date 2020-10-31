#Proyect by Rosangelica Rivera Hernandez #94243
#Brenda Flores Acevedo #120654

from graphics import *
import random

win = GraphWin("Parchesis" , 500,500)

class Design():
    def Squares():
        #Draw and locate the 4 gamers
        rect = Rectangle(Point(15,15) , Point(485,485))
        rect.setFill('beige')
        rect.setWidth(2)
        rect.draw(win)

        blue = Rectangle(Point(300,200), Point(475,25))
        blue.setFill('sky blue')
        blue.draw(win)
        blueSquare = Rectangle(Point(200,25),Point(300,200))
        blueSquare.draw(win)

        yellow = Rectangle(Point(300,300), Point(475,475))
        yellow.setFill('khaki')
        yellow.draw(win)
        yellowSquare = Rectangle(Point(200,200),Point(475,300))
        yellowSquare.draw(win)

        pink = Rectangle(Point(25,475), Point(200,300))
        pink.setFill('hotpink')
        pink.draw(win)
    
        green = Rectangle(Point(25,25), Point(200,200))
        green.setFill('light green')
        green.draw(win)
        
    def Path():
        #Path between pink and yellow
        ySquare = Rectangle(Point(200,300),Point(300,475))
        ySquare.draw(win)

        ySquare1 = Rectangle(Point(200,300),Point(230,475))
        ySquare1.draw(win)

        ySquare2 = Rectangle(Point(230,300),Point(270,475))
        ySquare2.setFill('khaki')
        ySquare2.draw(win)

        ySquare3 = Rectangle(Point(200,446),Point(300,475))
        ySquare3.draw(win)

        ySquare4 = Rectangle(Point(200,417),Point(300,446))
        ySquare4.draw(win)
    
        ySquare5 = Rectangle(Point(200,388),Point(300,417))
        ySquare5.draw(win)

        ySquare6 = Rectangle(Point(200,359),Point(300,388))
        ySquare6.draw(win) 
        
        ySquare7 = Rectangle(Point(200,330),Point(300,359))
        ySquare7.draw(win)

        ySquare8 = Rectangle(Point(200,300),Point(300,330))
        ySquare8.draw(win)


        ySquare10 = Rectangle(Point(230,446),Point(270,475))
        ySquare10.setFill("yellow")
        ySquare10.draw(win)

        #left squares between green and red
        rSquare = Rectangle(Point(200,200),Point(25,230))
        rSquare.draw(win)

        rSquare1 = Rectangle(Point(200,230),Point(25,270))
        rSquare1.setFill('hot pink')
        rSquare1.draw(win)

        rSquare2 = Rectangle(Point(25,200),Point(54,300))
        rSquare2.draw(win)

        rSquare3 = Rectangle(Point(54,200),Point(83,300))
        rSquare3.draw(win)

        rSquare4 = Rectangle(Point(83,200),Point(112,300))
        rSquare4.draw(win)

        rSquare5 = Rectangle(Point(112,200),Point(141,300))
        rSquare5.draw(win)

        rSquare6 = Rectangle(Point(141,200),Point(170,300))
        rSquare6.draw(win)

        rSquare7 = Rectangle(Point(170,200),Point(200,300))
        rSquare7.draw(win)

        rSquare9 = Rectangle(Point(25,230),Point(54,270))
        rSquare9.setFill('pink')
        rSquare9.draw(win)
        

        #Medium squares between blue and green
        gSquare = Rectangle(Point(200,25),Point(230,200))
        gSquare.draw(win)

        gSquare1 = Rectangle(Point(230,25),Point(270,200))
        gSquare1.setFill('light green')
        gSquare1.draw(win)

        gSquare2 = Rectangle(Point(200,171),Point(300,200))
        gSquare2.draw(win)

        gSquare3 = Rectangle(Point(200,142),Point(300,171))
        gSquare3.draw(win)

        gSquare4 = Rectangle(Point(200,113),Point(300,142))
        gSquare4.draw(win)

        gSquare5 = Rectangle(Point(200,84),Point(300,113))
        gSquare5.draw(win)

        gSquare6 = Rectangle(Point(200,55),Point(300,84))
        gSquare6.draw(win)

        gSquare7 = Rectangle(Point(200,25),Point(300,55))
        gSquare7.draw(win)

        gSquare9 = Rectangle(Point(230,25),Point(270,55))
        gSquare9.setFill('spring green')
        gSquare9.draw(win)

        # Right between yellow and blue
        bSquare = Rectangle(Point(300,200),Point(475,230))
        bSquare.draw(win)

        bSquare1 = Rectangle(Point(300,230),Point(475,270))
        bSquare1.setFill('sky blue')
        bSquare1.draw(win)

        bSquare2 = Rectangle(Point(300,250),Point(329,300))
        bSquare2.draw(win)

        bSquare3 = Rectangle(Point(329,200),Point(358,300))
        bSquare3.draw(win)

        bSquare4 = Rectangle(Point(358,200),Point(387,300))
        bSquare4.draw(win)

        bSquare5 = Rectangle(Point(387,200),Point(416,300))
        bSquare5.draw(win)

        bSquare6 = Rectangle(Point(416,200),Point(445,300))
        bSquare6.draw(win)

        bSquare7 = Rectangle(Point(445,200),Point(475,300))
        bSquare7.draw(win)

        bSquare9 = Rectangle(Point(445,230),Point(475,270))
        bSquare9.setFill('light blue')
        bSquare9.draw(win)

    def Center():
        mainRect = Rectangle(Point(200,200) , Point(300,300))
        mainRect.setFill('khaki')
        mainRect.draw(win)

        center1 = Polygon(Point(235,265),Point(200,300),Point(200,200), Point(235 ,235))
        center1.setFill("hot pink")
        center1.draw(win)

        center2 = Polygon(Point(235,235),Point(200,200),Point(300,200), Point(235,265))
        center2.setFill("light green")
        center2.draw(win)

        center3 = Polygon(Point(300,300),Point(265,265),Point(265,235), Point(300,200))
        center3.setFill("sky blue")
        center3.draw(win)

        center = Rectangle(Point(235,235),Point(265,265))
        center.setFill('light cyan')
        center.draw(win)
        greenSquare = Rectangle(Point(25,300),Point(200,200))
        greenSquare.draw(win)
    
        blueSquare = Rectangle(Point(200,25),Point(300,200))
        blueSquare.draw(win)
    
        yellowSquare = Rectangle(Point(200,200),Point(475,300))
        yellowSquare.draw(win)

        #Inside the squares
        greenCenter = Point(110,110)
        green2 = Circle(greenCenter,75)
        green2.setFill('mediumspringgreen')
        green2.draw(win)

        blueCenter = Point(390,110)
        blue2 = Circle(blueCenter, 75)
        blue2.setFill('cornflowerblue')
        blue2.draw(win)

        yellowCenter = Point(390,390)
        yellow2 = Circle(yellowCenter,75)
        yellow2.setFill('cornsilk')
        yellow2.draw(win)

        pinkCenter = Point(110,390)
        pink2 = Circle(pinkCenter,75)
        pink2.setFill('light pink')
        pink2.draw(win)

        pinkMini = Circle(pinkCenter,40)
        pinkMini.setFill('hot pink')
        pinkMini.draw(win)

        blueMini = Circle(blueCenter,40)
        blueMini.setFill('sky blue')
        blueMini.draw(win)

        yellowMini = Circle(yellowCenter,40)
        yellowMini.setFill('khaki')
        yellowMini.draw(win)

        greenMini = Circle(greenCenter,40)
        greenMini.setFill('light green')
        greenMini.draw(win)
        
    def Fiches():
        #Mini circles movement item
        pinkFiche = Circle(Point(55,350),10)
        pinkFiche.setFill('Deep pink')
        pinkFiche.draw(win)

        pinkFiche2 = Circle(Point(165,350),10)
        pinkFiche2.setFill('Deep pink')
        pinkFiche2.draw(win)

        pinkFiche3 = Circle(Point(55,430),10)
        pinkFiche3.setFill('Deep pink')
        pinkFiche3.draw(win)

        pinkFiche4 = Circle(Point(165,430),10)
        pinkFiche4.setFill('Deep pink')
        pinkFiche4.draw(win)

        blueFiche = Circle(Point(335,70),10)
        blueFiche.setFill('medium blue')
        blueFiche.draw(win)
        blueFiche2 = Circle(Point(445,70),10)
        blueFiche2.setFill('medium blue')
        blueFiche2.draw(win)

        blueFiche3 = Circle(Point(335,150),10)
        blueFiche3.setFill('medium blue')
        blueFiche3.draw(win)

        blueFiche4 = Circle(Point(445,150),10)
        blueFiche4.setFill('medium blue')
        blueFiche4.draw(win)

        greenFiche = Circle(Point(55,70),10)
        greenFiche.setFill('sea green')
        greenFiche.draw(win)
        greenFiche2 = Circle(Point(165,70),10)
        greenFiche2.setFill('sea green')
        greenFiche2.draw(win)

        greenFiche3 = Circle(Point(55,150),10)
        greenFiche3.setFill('sea green')
        greenFiche3.draw(win)

        greenFiche4 = Circle(Point(165,150),10)
        greenFiche4.setFill('sea green')
        greenFiche4.draw(win)

        yellowFiche = Circle(Point(445,350),10)
        yellowFiche.setFill('peach puff')
        yellowFiche.draw(win)
        yellowFiche2 = Circle(Point(335,350),10)
        yellowFiche2.setFill('peach puff')
        yellowFiche2.draw(win)

        yellowFiche3 = Circle(Point(445,430),10)
        yellowFiche3.setFill('peach puff')
        yellowFiche3.draw(win)

        yellowFiche4 = Circle(Point(335,430),10)
        yellowFiche4.setFill('peach puff')
        yellowFiche4.draw(win)

#Create the dice
dice = [1,2,3,4,5,6]
Dice = random.choice(dice)
class Play():
    def DiceGet1():
        c1 = Circle(Point(250,250),2)
        c1.setFill('darkcyan')
        c1.draw(win)
        text = Text(Point(250,40),'1')
        text.setSize(20)
        text.setFill('red')
        text.draw(win)
        
    def DiceGet2():
        c1 = Circle(Point(242,250),2)
        c1.setFill('darkcyan')
        c2 = Circle(Point(258,250),2)
        c2.setFill('darkcyan')
        c1.draw(win)
        c2.draw(win)
        text = Text(Point(250,40),'2')
        text.setSize(20)
        text.setFill('red')
        text.draw(win)

    def DiceGet3():
        c1 = Circle(Point(240,240),2)
        c1.setFill('darkcyan')
        c2 = Circle(Point(250,250),2)
        c2.setFill('darkcyan')
        c3 = Circle(Point(260,260),2)
        c3.setFill('darkcyan')
        c1.draw(win)
        c2.draw(win)
        c3.draw(win)
        text = Text(Point(250,40),'3')
        text.setSize(20)
        text.setFill('red')
        text.draw(win)

    def DiceGet4():
         c1 = Circle(Point(242,242),2)
         c1.setFill('darkcyan')
         c2 = Circle(Point(258,242),2)
         c2.setFill('darkcyan')
         c3 = Circle(Point(242,258),2)
         c3.setFill('darkcyan')
         c4 = Circle(Point(258,258),2)
         c4.setFill('darkcyan')
         c1.draw(win)
         c2.draw(win)
         c3.draw(win)
         c4.draw(win)
         text = Text(Point(250,40),'4')
         text.setSize(20)
         text.setFill('red')
         text.draw(win)

    def DiceGet5():
        c1 = Circle(Point(241,241),2)
        c1.setFill('darkcyan')
        c2 = Circle(Point(259,241),2)
        c2.setFill('darkcyan')
        c3 = Circle(Point(241,259),2)
        c3.setFill('darkcyan')
        c4 = Circle(Point(259,259),2)
        c4.setFill('darkcyan')
        c5 = Circle(Point(250,250),2)
        c5.setFill('darkcyan')
        c1.draw(win)
        c2.draw(win)
        c3.draw(win)
        c4.draw(win)
        c5.draw(win)
        text = Text(Point(250,40),'5')
        text.setSize(20)
        text.setFill('red')
        text.draw(win)

    def DiceGet6():
        c1 = Circle(Point(240,242),2)
        c1.setFill('darkcyan')
        c2 = Circle(Point(250,242),2)
        c2.setFill('darkcyan')
        c3 = Circle(Point(260,242),2)
        c3.setFill('darkcyan')
        c4 = Circle(Point(240,257),2)
        c4.setFill('darkcyan')
        c5 = Circle(Point(250,257),2)
        c5.setFill('darkcyan')
        c6 = Circle(Point(260,257),2)
        c6.setFill('darkcyan')
        c1.draw(win)
        c2.draw(win)
        c3.draw(win)
        c4.draw(win)
        c5.draw(win)
        c6.draw(win)
        text = Text(Point(250,40),'6')
        text.setSize(20)
        text.setFill('red')
        text.draw(win)

    def reset():
        center = Rectangle(Point(235,235),Point(265,265))
        center.setFill('light cyan')
        center.draw(win)
        center1 = Rectangle(Point(230,25),Point(270,55))
        center1.setFill('darkblue')
        center1.draw(win)

def main():
    Design.Squares()
    Design.Path()
    Design.Center()
    Design.Fiches()
    while True:
        win.getMouse()
        Dice = random.choice(dice)
        if Dice == 1:
            Play.DiceGet1()
        if Dice == 2:
            Play.DiceGet2()
        if Dice == 3:
            Play.DiceGet3()
        if Dice == 4:
            Play.DiceGet4()
        if Dice == 5:
            Play.DiceGet5()
        if Dice == 6:
            Play.DiceGet6()
            
        win.getMouse()
        Play.reset()
        Dice = random.choice(dice)
if __name__=='__main__':
    main()
