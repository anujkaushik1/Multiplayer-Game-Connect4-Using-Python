from typing import Counter
import pygame
from time import sleep
from pygame.draw import circle
import socket
from threading import Thread


pygame.init()

color = (0,0,150)
surface = pygame.display.set_mode((400,300))
surface.fill(color)
pygame.display.set_caption("Pepcoding Connect4")
font = pygame.font.Font("freesansbold.ttf", 40)

font_black = (0,0,0)
font_white = (255,255,255)


black_color = (0,0,0)
player_color = ((0,255,170))
red_color = (255,0,0)
isPlayerColor = True
playerWins = False

redColorXCoordinate = 0
redColorYCoordinate = 0

#cordinate of circle
X = 40
Y = 30

listOfCircles = [
                  [[X,Y] , [X+60,Y], [X+120,Y], [X+180,Y], [X+240,Y],[X+300,Y]],
                  [[X,Y+60] , [X+60,Y+60], [X+120,Y+60], [X+180,Y+60], [X+240,Y+60],[X+300,Y+60]],
                  [[X,Y+120] , [X+60,Y+120], [X+120,Y+120], [X+180,Y+120], [X+240,Y+120],[X+300,Y+120]],
                  [[X,Y+180] , [X+60,Y+180], [X+120,Y+180], [X+180,Y+180], [X+240,Y+180],[X+300,Y+180]],
                  [[X,Y+240] , [X+60,Y+240], [X+120,Y+240], [X+180,Y+240], [X+240,Y+240],[X+300,Y+240]]                 
                  
                ] 

connect4List = []

# Socket =>``



for i in range(len(listOfCircles)):
    col = []
    for j in range(len(listOfCircles[0])):
        col.append(-1)
    connect4List.append(col)


def createCircles():
            
        pygame.draw.circle(surface, black_color, (X,Y), 20,0)
        pygame.draw.circle(surface, black_color, (X + 60 ,Y), 20,0)
        pygame.draw.circle(surface, black_color, (X + 120,Y), 20,0)
        pygame.draw.circle(surface, black_color, (X + 180,Y), 20,0)
        pygame.draw.circle(surface, black_color, (X + 240,Y), 20,0)
        pygame.draw.circle(surface, black_color, (X + 300,Y), 20,0) 

        pygame.draw.circle(surface, black_color, (X,Y + 60), 20,0)
        pygame.draw.circle(surface, black_color, (X + 60 ,Y +60), 20,0)
        pygame.draw.circle(surface, black_color, (X + 120,Y + 60), 20,0)
        pygame.draw.circle(surface, black_color, (X + 180,Y + 60), 20,0)
        pygame.draw.circle(surface, black_color, (X + 240,Y + 60), 20,0)
        pygame.draw.circle(surface, black_color, (X + 300,Y + 60), 20,0)

        pygame.draw.circle(surface, black_color, (X,Y + 120), 20,0)
        pygame.draw.circle(surface, black_color, (X + 60 ,Y + 120), 20,0)
        pygame.draw.circle(surface, black_color, (X + 120,Y + 120), 20,0)
        pygame.draw.circle(surface, black_color, (X + 180,Y + 120), 20,0)
        pygame.draw.circle(surface, black_color, (X + 240,Y + 120), 20,0)
        pygame.draw.circle(surface, black_color, (X + 300,Y + 120), 20,0)

        pygame.draw.circle(surface, black_color, (X,Y + 180), 20,0)
        pygame.draw.circle(surface, black_color, (X + 60 ,Y + 180), 20,0)
        pygame.draw.circle(surface, black_color, (X + 120,Y + 180), 20,0)
        pygame.draw.circle(surface, black_color, (X + 180,Y + 180), 20,0)
        pygame.draw.circle(surface, black_color, (X + 240,Y + 180), 20,0)
        pygame.draw.circle(surface, black_color, (X + 300,Y + 180), 20,0)

        pygame.draw.circle(surface, black_color, (X,Y + 240), 20,0)
        pygame.draw.circle(surface, black_color, (X + 60 ,Y + 240), 20,0)
        pygame.draw.circle(surface, black_color, (X + 120,Y + 240), 20,0)
        pygame.draw.circle(surface, black_color, (X + 180,Y + 240), 20,0)
        pygame.draw.circle(surface, black_color, (X + 240,Y + 240), 20,0)
        pygame.draw.circle(surface, black_color, (X + 300,Y + 240), 20,0)


def isPointInsideCircle(equation_x, equation_y, equation_h, equation_k):

    # h, k are the centre of the given cirle
    # x, y are the points that we have to check

    radius = 20
    circleEquation = (equation_x - equation_h) * (equation_x - equation_h) + (equation_y - equation_k) * (equation_y - equation_k)

    if(circleEquation <= radius * radius):  
        return True 
    
    else:
        return False

def isPointInsideRect(x1, y1, x2, y2, x, y):
 
    if (x > x1 and x < x2 and y < y1 and y > y2) :
        return True
    else :
        return False


def isFourdots0Connected(row, column, player):
    
    dots0 = 0
    dots1 = 0

    dictionary = {
        "player" : -1,
        "dots" : False
    }


    # BOTTOM TO TOP => 
    r = row - 3
    mainRow = row
    mainColumn = column

    while(mainRow >= r and mainRow >= 0):
        element = connect4List[mainRow][mainColumn]
        
        if(element == 0):
            dots0 += 1
            # print(dots0)

        
        if(element == 1):
            dots1 += 1
            # print(dots1)

        mainRow -= 1
    
    if(dots0 == 4):
        dictionary["player"] = 0
        dictionary["dots"] = True
        return dictionary
    
    elif(dots1 == 4):
        dictionary["player"] = 1
        dictionary["dots"] = True
        return dictionary
    
    else:
        dots0 = 0
        dots1 = 0


    # TOP RIGHT =>

    r = row - 3
    c = column + 3
    mainRow = row
    mainColumn = column

    while(mainRow >= r and mainColumn <= c and mainRow >= 0 and mainColumn < len(connect4List[0])):
        element = connect4List[mainRow][mainColumn]

        if(element == 0):
            dots0 += 1

        elif(element == 1):
            dots1 += 1


        mainRow -= 1
        mainColumn += 1
    
    if(dots0 == 4):
        dictionary["player"] = 0
        dictionary["dots"] = True
        return dictionary

    elif(dots1 == 4):
        dictionary["player"] = 1
        dictionary["dots"] = True
        return dictionary
    
    else:
        dots0 = 0
        dots1 = 0




    # TOP LEFT =>
    
    r = row-3
    c = column-3
    mainRow = row
    mainColumn = column

    while(mainRow>=r and mainColumn>=c):
        element = connect4List[mainRow][mainColumn]

        if(element == 0):
            dots0 += 1
        
        elif(element == 1):
            dots1 += 1


        mainRow -= 1
        mainColumn -= 1

    if(dots0 == 4):
        dictionary["player"] = 0
        dictionary["dots"] = True
        return dictionary

    elif(dots1 == 4):
        dictionary["player"] = 1
        dictionary["dots"] = True
        return dictionary
    
    else:
        dots0 = 0
        dots1 = 0

    
    # TO LEFT =>

    mainRow = row
    mainColumn = column
    c = column-3

    while(mainColumn>=c):
        element = connect4List[mainRow][mainColumn]

        if(element == 0):
            dots0 += 1
        
        elif(element == 1):
            dots1 += 1


        mainColumn -= 1

    if(dots0 == 4):
        dictionary["player"] = 0
        dictionary["dots"] = True
        return dictionary

    elif(dots1 == 4):
        dictionary["player"] = 1
        dictionary["dots"] = True
        return dictionary

    else:
        dots0 = 0
        dots1 = 0

    # TO RIGHT =>
    
    mainRow = row
    mainColumn = column
    c = column + 3

    while(mainColumn <= c and mainColumn < len(connect4List[0])):
        element = connect4List[mainRow][mainColumn]
        mainColumn += 1

        if(element == 0):
            dots0 += 1
        
        elif(element == 1):
            dots1 += 1

        
    if(dots0 == 4):
        dictionary["player"] = 0
        dictionary["dots"] = True
        return dictionary
    
    elif(dots1 == 4):
        dictionary["player"] = 1
        dictionary["dots"] = True
        return dictionary

    else:
        dots0 = 0
        dots1 = 0

    
    # TO BOTTOM =>

    mainRow = row
    mainColumn = column
    r = row + 3

    while(mainRow <= r and mainRow < len(connect4List)):
        element = connect4List[mainRow][mainColumn]

        if(element == 0):
            dots0 += 1

        elif(element == 1):
            dots1 += 1

        mainRow += 1
    
    if(dots0 == 4):
        dictionary["player"] = 0
        dictionary["dots"] = True
        return dictionary
    
    elif(dots1 == 4):
        dictionary["player"] = 1
        dictionary["dots"] = True
        return dictionary

    else:
        dots0 = 0
        dots1 = 0
    
    #BOTTOM LEFT =>

    mainRow = row
    mainColumn = column

    r = row + 3
    c = column - 3

    while(mainRow <= r and mainColumn >= c and mainRow < len(listOfCircles) and mainColumn>=0):
        element = connect4List[mainRow][mainColumn]

        if(element == 0):
            dots0 += 1

        elif(element == 1):
            dots1 += 1

        
        mainRow += 1
        mainColumn -= 1
    
    if(dots0 == 4):
        dictionary["player"] = 0
        dictionary["dots"] = True
        return dictionary
    
    elif(dots1 == 4):
        dictionary["player"] = 1
        dictionary["dots"] = True
        return dictionary

    else:
        dots0 = 0
        dots1 = 0

    #BOTTOM RIGHT =>

    mainRow = row
    mainColumn = column
    r = row + 3
    c = column + 3

    while(mainRow <= r and mainColumn <= c and mainRow < len(connect4List) and mainColumn < len(connect4List[0])):
        element = connect4List[mainRow][mainColumn]

        if(element == 0):
            dots0 += 1

        elif(element == 1):
            dots1 += 1

        mainRow += 1
        mainColumn += 1

    if(dots0 == 4):
        dictionary["player"] = 0
        dictionary["dots"] = True
        return dictionary
    
    elif(dots1 == 4):
        dictionary["player"] = 1
        dictionary["dots"] = True
        return dictionary

    else:
        dots0 = 0
        dots1 = 0

def startingScreen():
    
    startingFont = pygame.font.Font("freesansbold.ttf", 22)
    text = startingFont.render("Connect 4", True, red_color )
    surface.blit(text, (140, 20))

    
    rectangeStartGame = pygame.Rect(130,100, 140, 60)   # left(X), top(Y), width and height
    pygame.draw.rect(surface, black_color, rectangeStartGame)

    text = startingFont.render("Start Game", True, font_white)
    surface.blit(text, (140, 120))

    
    # FINDING VERTICES =>

    x1, y1 = 200 - 140 / 2 , 130 + 60 / 2
    x2, y2 = 200 + 140 / 2 , 130 - 60 / 2

    temp = False
    while True:

        for event in pygame.event.get():

           if event.type == pygame.MOUSEBUTTONDOWN:
               
               x, y = pygame.mouse.get_pos()

               if(isPointInsideRect(x1, y1, x2, y2, x, y)):
                   temp = True

           if event.type == pygame.QUIT:
                quit()
        
        if(temp):
            surface.fill(color)
            break

        pygame.display.flip()
        



startingScreen()




import socket
from threading import Thread
name = "player"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5555))
client.send(name.encode())

numbers = []
def send(data, client):

    client.send(str(data).encode())

def receive(client):
     global numbers 
     while True:
            try:
                data = client.recv(1024).decode()
                
                ans = ""
                for char in data:
                    if(char != "(" and char != ")"):
                        if(char == ","):
                            numbers.append(int(ans))
                            ans = ""
                        
                        else:
                            ans += char

                numbers.append(int(ans))

            except Exception as e:
                print(str(e))
                client.close()
                break

newRedColorXCoordinate = 0
newRedColorYCoordinate = 0
def main():
    global numbers, newRedColorYCoordinate, newRedColorXCoordinate
    thread2 = Thread(target=receive, args=(client, ))
    thread2.start() 
    
    while True:
    
        global isPlayerColor, playerWins  #these variables are considered as a local variable, and it's used before being set, thus the error.

        player_one = 0
        player_two = 1

        for event in pygame.event.get():
            
            if(isPlayerColor):
                player_color = (255,0,0)
            
            else:
                player_color = ((0,255,0))

            if event.type == pygame.MOUSEBUTTONUP:

                equation_x, equation_y = pygame.mouse.get_pos()

                isInsideTrue = False
                
                for i in listOfCircles:

                  for j in i:

                    equation_h, equation_k = j

                    if(isPointInsideCircle(equation_x, equation_y, equation_h, equation_k)):
                            
 
                            column = int(equation_h/60)  
                            row = len(listOfCircles)

                            redColorXCoordinate = 0
                            redColorYCoordinate = 0
                            
                            for x in reversed(range(len(connect4List))):
                                if(connect4List[x][column] == -1):
                                    
                                    if(isPlayerColor):  
                                        connect4List[x][column] = player_one
                                        redColorXCoordinate, redColorYCoordinate =listOfCircles[x][column]
                                    
                                    else:
                                        connect4List[x][column] = player_two
                                        redColorXCoordinate, redColorYCoordinate =listOfCircles[x][column]

                                    data = redColorXCoordinate, redColorYCoordinate

                                    # SOCKET =>

                                    thread1 = Thread(target=send, args=(data, client, ))
                                    thread1.start()


                                    dictionary = isFourdots0Connected(x,column,isPlayerColor)
                                    
                                    if(dictionary):
                                        if(dictionary["player"] == 0):
                                            print("Player 1 wins (Red Player)")

                                            text = font.render("Player 1 Wins", True, font_white, font_black)
                                            textRect = text.get_rect()
                                            surface.fill(font_black)
                                            textRect.center = (200, 150)
                                            surface.blit(text, textRect)
                                            playerWins = True

                                        
                                        elif(dictionary["player"] == 1):
                                            print("Player 2 Wins (Green Color)")
                                            text = font.render("Player 2 Wins", True, font_white, font_black)
                                            textRect = text.get_rect()
                                            surface.fill(font_black)
                                            textRect.center = (200, 150)
                                            surface.blit(text, textRect)
                                            playerWins = True
                                    
                                
                                    break

                            if(playerWins == True):
                                break    

                            
                            if(redColorYCoordinate == 0 and redColorYCoordinate == 0):
                                break
                            

                            pygame.draw.circle(surface, player_color, (redColorXCoordinate, redColorYCoordinate) , 20, 0)
                            if(isPlayerColor):
                                isPlayerColor = False
                            else:
                                isPlayerColor = True


                            isInsideTrue = True
                            break
                
                    else:    
                            pass

                if(isInsideTrue or playerWins):
                    break
                

            if event.type == pygame.QUIT:
                quit()


        pygame.display.flip()

createCircles()
main()

        