import pygame
import socket

pygame.init()#initialising
pygame.display.set_caption('Tac-Tic-Toe')

#colors
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green = (0,155,0)

#sets size of window and creates it
disp = 600
gameDisplay = pygame.display.set_mode((disp, disp))

#fonts
smallfont = pygame.font.SysFont("comicsansms", 20)
medfont = pygame.font.SysFont("comicsansms", 35)
largefont = pygame.font.SysFont("comicsansms", 50)

#images
ximg = pygame.image.load('x200.png')
oimg = pygame.image.load('o200.png')

#possible coordinates of x and o
possible_pos = [(0,0),(disp/3,0),(disp*2/3,0),(0,disp/3),(disp/3,disp/3),(disp*2/3,disp/3),(0,disp*2/3),(disp/3,disp*2/3),(disp*2/3,disp*2/3)]#coordinates in the form of (x,y)
winList = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]#possible win combinarions
turn = -1
usedXPos = []#contains positions of x as we play
usedOPos = []#contains positions of o as we play

clock = pygame.time.Clock()# for setting frames per second

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "127.0.0.1"#Your local IP Address
port = 1234#PORT to be used for serving
s.bind((host,port))#opens port for connection
s.listen(1)#listens for connection from ONE device
clientsocket, address = s.accept()#gets address of client and stores in variables

def text_objects(text,color, size):#creating text surfaces on which text will be written to
	if size == "small":
		textSurface = smallfont.render(text, True, color)#the text is rendered to an image and then put to screen
	elif size == "medium":
		textSurface = medfont.render(text, True, color)
	elif size == "large":
		textSurface = largefont.render(text, True, color)
	return textSurface, textSurface.get_rect()#creating rectangular object for the text surface object

def msg_to_screen(msg, color, y_displace = 0, size="small"):
	textSurf, textRect = text_objects(msg, color, size)
	textRect.center = (disp/2), (disp /2)+y_displace#getting the centre of the rectangular object
	gameDisplay.blit(textSurf,textRect)#putting them to the screen

def draw(pos):#drawing x or o
	global turn
	global usedXPos
	global usedOPos
	
	if not pos in usedXPos and not pos in usedOPos:#if input is not aldready used then
		turn += 1
		if turn % 2 == 0:
			dX(pos)
			
		if turn % 2 == 1:
			dO(pos)

def Check(list):#checks if draw or win or game to be continued
	global winList
	win = False
	draw = False
	
	for i in range(8):
		if all(x in list for x in winList[i]):#if given list is a superlist of any one element of win list
			win = True
			msg_to_screen("press q to quit",black, 50, "large")
			clock.tick(5)
			
		if len(usedXPos+usedOPos) == 9:#if the length of used lists is 9 then its a draw
			draw = True
			msg_to_screen("press q to quit", black, 50,"large")
			clock.tick(5)
	#these if statements are to handle the situation where a player wins and the all the boxes are filled
	if win == True:
		msg_to_screen("player "+str(turn%2+1)+" has won", red, size="large")
		
	elif draw == True and win == False:
		msg_to_screen("Its a Draw", red, size="large")		

def dO(pos):#draws o
	
	gameDisplay.blit(oimg, (possible_pos[pos - 1][0], possible_pos[pos-1][1]))#according to input the coordinates of the respective box is taken from a predefined list and then put to screen
	
	usedOPos.append(pos)#since the box is used, its appended to used positions' list
	Check(usedOPos)#checks for any event
	
	pygame.display.update()#updates screen

def dX(pos):#draws x
	
	gameDisplay.blit(ximg, (possible_pos[pos - 1][0], possible_pos[pos-1][1]))
	
	usedXPos.append(pos)
	Check(usedXPos)
	
	pygame.display.update()

def Grid():#draws grid with the numbers
	
	pygame.draw.line(gameDisplay, black, (disp/3,0),(disp/3,1000))#since the board is a 3x3 type
	pygame.draw.line(gameDisplay, black,(disp*(2/3),0),(disp*(2/3),1000))
	pygame.draw.line(gameDisplay, black, (0,disp/3),(1000, disp/3))
	pygame.draw.line(gameDisplay, black, (0, disp*(2/3)), (1000,disp*(2/3)))
	for i in range(9):#for rendering the number of the respective boxes to screen
		text = medfont.render(str(i+1), True, black)
		gameDisplay.blit(text, (possible_pos[i][0], possible_pos[i][1]))

def gameIntro():
	
	intro = True
	while intro:
		
		for event in pygame.event.get():#logs events
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				s.close()
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:#if input is q
					pygame.quit()
					quit()
					s.close()
				elif event.key == pygame.K_p:#if input is p
					intro = False
					
		gameDisplay.fill(white)
		msg_to_screen("Welcome to Tic-Tac-Toe",green, y_displace=-50,size="large")
		msg_to_screen("Press p to play q to quit",black,y_displace = 0, size="medium")
		msg_to_screen("Enter the number corresponding to ",black, y_displace = 50, size="medium")
		msg_to_screen("the box to add x or o", black, y_displace = 100, size="medium")
		msg_to_screen("1  2  3", black,y_displace=150,size="small")
		msg_to_screen("4  5  6", black,y_displace=200,size="small")
		msg_to_screen("7  8  9", black,y_displace=250,size="small")
		
		pygame.display.update()
		clock.tick(5)#Determines frames per second
		
def gameLoop():
	global pos
	
	gameDisplay.fill(white)
	Grid()
	
	pygame.display.update()
	
	while True:

		for event in pygame.event.get():#logs events
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				s.close()
			if turn % 2 == 1:#if its your turn
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						pygame.quit()
						quit()
						s.close()
					elif event.key == pygame.K_1:#if the input is 1
						draw(1)
						clientsocket.send(bytes("1",'utf-8'))
					elif event.key == pygame.K_2:#if input is 2
						draw(2)
						clientsocket.send(bytes("2",'utf-8'))
					elif event.key == pygame.K_3:
						draw(3)
						clientsocket.send(bytes("3",'utf-8'))
					elif event.key == pygame.K_4:
						draw(4)
						clientsocket.send(bytes("4",'utf-8'))
					elif event.key == pygame.K_5:
						draw(5)
						clientsocket.send(bytes("5",'utf-8'))
					elif event.key == pygame.K_6:
						draw(6)
						clientsocket.send(bytes("6",'utf-8'))
					elif event.key == pygame.K_7:
						draw(7)
						clientsocket.send(bytes("7",'utf-8'))
					elif event.key == pygame.K_8:
						draw(8)
						clientsocket.send(bytes("8",'utf-8'))
					elif event.key == pygame.K_9:
						draw(9)
						clientsocket.send(bytes("9",'utf-8'))
			elif turn % 2 == 0:#if its other person's turn we wait for input from them
				position = int(str(clientsocket.recv(1024)).replace("b","").replace("'",""))#receives input from other player and removes unwanted data
				draw(position)#draws their play
				
		pygame.display.update()
		clock.tick(3)
		
gameIntro()
gameLoop()
