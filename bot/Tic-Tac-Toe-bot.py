import pygame
from random import choice

pygame.init()#initialising
pygame.display.set_caption('Tac-Tic-Toe')

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,155,0)

disp = 600

smallfont = pygame.font.SysFont("comicsansms", 20)
medfont = pygame.font.SysFont("comicsansms",35)
largefont = pygame.font.SysFont("comicsansms", 50)

ximg = pygame.image.load('x200.png')
oimg = pygame.image.load('o200.png')

possible_pos = [(0,0),(disp/3,0),(disp*2/3,0),(0,disp/3),(disp/3,disp/3),(disp*2/3,disp/3),(0,disp*2/3),(disp/3,disp*2/3),(disp*2/3,disp*2/3)]
winList = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]#possible win combinarions
turn = -1
usedXPos = []#contains positions of x
usedOPos = []#contains positions of o
empPos = [1,2,3,4,5,6,7,8,9]
corners = [1,3,7,9]

win = False
draw = False

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((disp, disp))

def text_objects(text,color, size):
	if size == "small":
		textSurface = smallfont.render(text, True,color)
	elif size == "medium":
		textSurface = medfont.render(text, True,color)
	elif size == "large":
		textSurface = largefont.render(text, True,color)
	return textSurface, textSurface.get_rect()

def msg_to_screen(msg, color, y_displace = 0, size="small"):
	textSurf, textRect = text_objects(msg,color, size)
	textRect.center = (disp/2), (disp /2)+y_displace
	gameDisplay.blit(textSurf,textRect)

def draw(pos):#drawing x or o
        global turn
        global usedXPos
        global usedOPos
        
        
        if pos in empPos:
                #not in usedXPos and pos not in usedOPos:#if input is not aldready used then
                empPos.remove(pos)
                turn += 1
                if turn % 2 == 0:
                        dX(pos)
                        
                if turn % 2 == 1:
                        dO(pos)

        
def Check(list):#checks if draw or win or nothing
	global winList
	global win
	global draw
	
	for i in range(8):
		if all(x in list for x in winList[i]):#if used list is a superlist of any one element of win list then
			win = True
			#msg_to_screen("press q to quit",black, 50, "large")
			clock.tick(5)
			
		if len(usedXPos+usedOPos) == 9:#if the length of used lists is 9 then its a draw
			draw = True
			#msg_to_screen("press q to quit", black, 50,"large")
			clock.tick(5)
	#these if statements are to handle the situation where a player wins and the all the boxes are filled
	if win == True:
		msg_to_screen("player "+str(turn%2+1)+" has won", red, size="large")
		
	elif draw == True and win == False:
		msg_to_screen("Its a Draw", red, size="large")		

def dO(pos):#draws o
	
	gameDisplay.blit(oimg, (possible_pos[pos - 1][0], possible_pos[pos-1][1]))
	
	usedOPos.append(pos)
	Check(usedOPos)
	
	pygame.display.update()#updates screen

def dX(pos):#draws x
	
	gameDisplay.blit(ximg, (possible_pos[pos - 1][0], possible_pos[pos-1][1]))
	
	usedXPos.append(pos)
	Check(usedXPos)
	
	pygame.display.update()

def Grid():#draws grid with the numbers
	
	pygame.draw.line(gameDisplay, black, (disp/3,0),(disp/3,1000))
	pygame.draw.line(gameDisplay, black,(disp*(2/3),0),(disp*(2/3),1000))
	pygame.draw.line(gameDisplay, black, (0,disp/3),(1000, disp/3))
	pygame.draw.line(gameDisplay, black, (0, disp*(2/3)), (1000,disp*(2/3)))
	for i in range(9):
		text = medfont.render(str(i+1),True,black)
		gameDisplay.blit(text,(possible_pos[i][0],possible_pos[i][1]))

def gameIntro():
	
	intro = True
	while intro:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:#if input is q
					pygame.quit()
					quit()
				elif event.key == pygame.K_p:
					intro = False
					
		gameDisplay.fill(white)
		msg_to_screen("Welcome to Tic-Tac-Toe",green, y_displace=-50,size="large")
		msg_to_screen("Press p to play q to quit",black,y_displace = 0, size="medium")
		msg_to_screen("Enter the number corresponding to",black, y_displace = 50, size="medium")
		msg_to_screen("the box to add x or o",black, y_displace = 100, size="medium")
		msg_to_screen("1  2  3",black,y_displace=150,size="small")
		msg_to_screen("4  5  6",black,y_displace=200,size="small")
		msg_to_screen("7  8  9",black,y_displace=250,size="small")
		
		pygame.display.update()
		clock.tick(5)
		
def gameLoop():
	global pos
	
	gameDisplay.fill(white)
	Grid()

	pygame.draw.rect(gameDisplay, black, [disp,0,5,disp])#border
	pygame.draw.rect(gameDisplay, black,[0,disp,disp,5])#border
	pygame.display.update()
	
	while True:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if turn % 2 == 1:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						pygame.quit()
						quit()
					elif event.key == pygame.K_1:#ie if the input is 1
						draw(1)
					elif event.key == pygame.K_2:#if input is 2
						draw(2)
					elif event.key == pygame.K_3:
						draw(3)
					elif event.key == pygame.K_4:
						draw(4)
					elif event.key == pygame.K_5:
						draw(5)
					elif event.key == pygame.K_6:
						draw(6)
					elif event.key == pygame.K_7:
						draw(7)
					elif event.key == pygame.K_8:
						draw(8)
					elif event.key == pygame.K_9:
						draw(9)
						
			elif turn % 2 == 0:
                                
                                #attack
                                #1,2,3
                                if 1 in usedOPos and 2 in usedOPos and 3 in empPos:
                                        draw(3)
                                elif 1 in usedOPos and 3 in usedOPos and 2 in empPos:
                                        draw(2)
                                elif 3 in usedOPos and 2 in usedOPos and 1 in empPos:
                                        draw(1)
                                #4,5,6
                                elif 4 in usedOPos and 5 in usedOPos and 6 in empPos:
                                        draw(6)
                                elif 4 in usedOPos and 6 in usedOPos and 5 in empPos:
                                        draw(5)
                                elif 6 in usedOPos and 5 in usedOPos and 4 in empPos:
                                        draw(4)
                                #7,8,9
                                elif 7 in usedOPos and 8 in usedOPos and 9 in empPos:
                                        draw(9)
                                elif 7 in usedOPos and 9 in usedOPos and 8 in empPos:
                                        draw(8)
                                elif 9 in usedOPos and 8 in usedOPos and 7 in empPos:
                                        draw(7)
                                #1,4,7
                                elif 1 in usedOPos and 4 in usedOPos and 7 in empPos:
                                        draw(7)
                                elif 1 in usedOPos and 7 in usedOPos and 4 in empPos:
                                        draw(4)
                                elif 7 in usedOPos and 4 in usedOPos and 1 in empPos:
                                        draw(1)
                                #2,5,8
                                elif 2 in usedOPos and 5 in usedOPos and 8 in empPos:
                                        draw(8)
                                elif 8 in usedOPos and 5 in usedOPos and 2 in empPos:
                                        draw(2)
                                elif 2 in usedOPos and 8 in usedOPos and 5 in empPos:
                                        draw(5)
                                #3,6,9
                                elif 3 in usedOPos and 6 in usedOPos and 9 in empPos:
                                        draw(9)
                                elif 3 in usedOPos and 9 in usedOPos and 6 in empPos:
                                        draw(6)
                                elif 9 in usedOPos and 6 in usedOPos and 3 in empPos:
                                        draw(3)
                                #1,5,9
                                elif 1 in usedOPos and 5 in usedOPos and 9 in empPos:
                                        draw(9)
                                elif 1 in usedOPos and 9 in usedOPos and 5 in empPos:
                                        draw(5)
                                elif 9 in usedOPos and 5 in usedOPos and 1 in empPos:
                                        draw(1)
                                #3,5,7
                                elif 3 in usedOPos and 5 in usedOPos and 7 in empPos:
                                        draw(7)
                                elif 3 in usedOPos and 7 in usedOPos and 5 in empPos:
                                        draw(5)
                                elif 7 in usedOPos and 5 in usedOPos and 3 in empPos:
                                        draw(3)

                                #defense
                                #1,2,3
                                elif 1 in usedXPos and 2 in usedXPos and 3 in empPos:
                                        draw(3)
                                elif 1 in usedXPos and 3 in usedXPos and 2 in empPos:
                                        draw(2)
                                elif 3 in usedXPos and 2 in usedXPos and 1 in empPos:
                                        draw(1)
                                #4,5,6
                                elif 4 in usedXPos and 5 in usedXPos and 6 in empPos:
                                        draw(6)
                                elif 4 in usedXPos and 6 in usedXPos and 5 in empPos:
                                        draw(5)
                                elif 6 in usedXPos and 5 in usedXPos and 4 in empPos:
                                        draw(4)
                                #7,8,9
                                elif 7 in usedXPos and 8 in usedXPos and 9 in empPos:
                                        draw(9)
                                elif 7 in usedXPos and 9 in usedXPos and 8 in empPos:
                                        draw(8)
                                elif 9 in usedXPos and 8 in usedXPos and 7 in empPos:
                                        draw(7)
                                #1,4,7
                                elif 1 in usedXPos and 4 in usedXPos and 7 in empPos:
                                        draw(7)
                                elif 1 in usedXPos and 7 in usedXPos and 4 in empPos:
                                        draw(4)
                                elif 7 in usedXPos and 4 in usedXPos and 1 in empPos:
                                        draw(1)
                                #2,5,8
                                elif 2 in usedXPos and 5 in usedXPos and 8 in empPos:
                                        draw(8)
                                elif 8 in usedXPos and 5 in usedXPos and 2 in empPos:
                                        draw(2)
                                elif 2 in usedXPos and 8 in usedXPos and 5 in empPos:
                                        draw(5)
                                #3,6,9
                                elif 3 in usedXPos and 6 in usedXPos and 9 in empPos:
                                        draw(9)
                                elif 3 in usedXPos and 9 in usedXPos and 6 in empPos:
                                        draw(6)
                                elif 9 in usedXPos and 6 in usedXPos and 3 in empPos:
                                        draw(3)
                                #1,5,9
                                elif 1 in usedXPos and 5 in usedXPos and 9 in empPos:
                                        draw(9)
                                elif 1 in usedXPos and 9 in usedXPos and 5 in empPos:
                                        draw(5)
                                elif 9 in usedXPos and 5 in usedXPos and 1 in empPos:
                                        draw(1)
                                #3,5,7
                                elif 3 in usedXPos and 5 in usedXPos and 7 in empPos:
                                        draw(7)
                                elif 3 in usedXPos and 7 in usedXPos and 5 in empPos:
                                        draw(5)
                                elif 7 in usedXPos and 5 in usedXPos and 3 in empPos:
                                        draw(3)

                                #double attacks
                                #1,5,9 and 3,5,7
                                elif (1 in usedXPos and 9 in usedXPos and 5 in usedOPos) or (3 in usedXPos and 7 in usedXPos and 5 in usedOPos):
                                        if 2 in empPos:
                                                draw(2)
                                        elif 4 in empPos:
                                                draw(4)
                                        elif 6 in empPos:
                                                draw(6)
                                        elif 8 in empPos:
                                                draw(8)

                                elif turn == 0 and 5 in usedXPos:
                                        draw(choice(corners))
                                elif turn == 0 and 5 in empPos:
                                        draw(5)
        
                                #xxo(cross)
                                elif 9 in usedXPos and 5 in usedXPos and 1 in usedOPos and 3 in empPos:
                                        draw(3)
                                elif 1 in usedXPos and 5 in usedXPos and 9 in usedOPos and 7 in empPos:
                                        draw(7)
                                elif 7 in usedXPos and 5 in usedXPos and 3 in usedOPos and 1 in empPos:
                                        draw(1)
                                elif 3 in usedXPos and 5 in usedXPos and 7 in usedOPos and 9 in empPos:
                                        draw(9)

                                #1,4,3(L shaped double attacks)
                                elif 1 in usedXPos and 6 in usedXPos and 3 in empPos:
                                        draw(3)
                                elif 2 in usedXPos and 9 in usedXPos and 3 in empPos:
                                        draw(3)
                                elif 3 in usedXPos and 8 in usedXPos and 9 in empPos:
                                        draw(9)
                                elif 4 in usedXPos and 3 in usedXPos and 1 in empPos:
                                        draw(1)
                                elif 6 in usedXPos and 7 in usedXPos and 9 in empPos:
                                        draw(9)
                                elif 7 in usedXPos and 2 in usedXPos and 1 in empPos:
                                        draw(1)
                                elif 8 in usedXPos and 1 in usedXPos and 7 in empPos:
                                        draw(7)
                                elif 9 in usedXPos and 4 in usedXPos and 7 in empPos:
                                        draw(7)

                                else:
                                        draw(choice(empPos))
                                        
		pygame.display.update()
		clock.tick(5)
		
gameIntro()
gameLoop()
