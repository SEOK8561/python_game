import pygame
import sys
import time
from UserString import MutableString

pygame.init()
pixelX = 60
pixelY = 60

tileX = 10
tileY = 8

displayX = tileX*pixelX
displayY = tileY*pixelY

iot_caption = "iotsokoban"
pygame.display.set_caption(iot_caption)
DISPLAYSURF = pygame.display.set_mode((displayX, displayY), 0, 32)

WHITE = (255, 255, 255)
ImgWall = pygame.image.load('iot_wall.png')
ImgManF = pygame.image.load('man_front.png')
ImgManB = pygame.image.load('man_back.png')
ImgManR = pygame.image.load('man_right.png')
ImgManL = pygame.image.load('man_left.png')
ImgDot = pygame.image.load('dot.png')
ImgBox = pygame.image.load('box.png')
ImgClear = pygame.image.load('stage_clear.png')
ImgMan = ImgManF
manx = 0
many = 0

iot_Stage = [
	[MutableString("##########"),
	MutableString("#        #"),
	MutableString("######## #"),
	MutableString("#   #### #"),
	MutableString("#   #### #"),
	MutableString("# .B@ #  #"),
	MutableString("#        #"),
	MutableString("##########")],
	
	[MutableString("##########"),
	MutableString("#      @ #"),
	MutableString("#######B #"),
	MutableString("##   # . #"),
	MutableString("#  #   ###"),
	MutableString("# ########"),
	MutableString("#    #   #"),
	MutableString("##########")]
	]
stage_Num = 0
iot_caption = "iotsokoban [stage:%d]" % (stage_Num+1)
pygame.display.set_caption(iot_caption)
iot_Map = []
for iStage in range(tileY):
	iot_Map.append(iot_Stage[stage_Num][iStage][:])

while True: # the main game loop
	stage_End = True
	DISPLAYSURF.fill(WHITE)
	for ix in range(tileX):
		for iy in range(tileY):
			if '#' == iot_Map[iy][ix]:	
				DISPLAYSURF.blit(ImgWall, (ix*pixelX, iy*pixelY))
			elif '@' == iot_Map[iy][ix]:
				DISPLAYSURF.blit(ImgMan, (ix*pixelX, iy*pixelY))
				manx = ix
				many = iy
			elif 'B' == iot_Map[iy][ix]:	
				DISPLAYSURF.blit(ImgBox, (ix*pixelX, iy*pixelY))
				if '.' != iot_Stage[stage_Num][iy][ix]:
					stage_End = False
			elif '.' == iot_Map[iy][ix]:	
				DISPLAYSURF.blit(ImgDot, (ix*pixelX, iy*pixelY))
	pygame.display.update()

	if True == stage_End:		
		DISPLAYSURF.blit(ImgClear, (120, 0))
		pygame.display.update()
		keyinput = False
		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					keyinput = True
					break
			if True == keyinput:
				break
			time.sleep(0.1)
			continue
		stage_Num = stage_Num + 1
		iot_Map = []
		for iStage in range(tileY):
			iot_Map.append(iot_Stage[stage_Num][iStage][:])
		iot_caption = "iotsokoban [stage:%d]" % (stage_Num+1)
		pygame.display.set_caption(iot_caption)
		continue
		
#raw_input()		

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			TempX = manx
			TempY = many
			if event.key == pygame.K_DOWN:
				ImgMan = ImgManF
				many = many + 1
			elif event.key == pygame.K_UP:
				ImgMan = ImgManB
				many = many - 1
			elif event.key == pygame.K_RIGHT:
				ImgMan = ImgManR
				manx = manx + 1
			elif event.key == pygame.K_LEFT:
				ImgMan = ImgManL
				manx = manx - 1
			else: 
				continue
#if ' ' == iot_Map[many][manx]or'.' == iot_Map[many][manx]:
			if '#' != iot_Map[many][manx]:
				if 'B' == iot_Map[many][manx]:
					if ' ' == iot_Map[2*many-TempY][2*manx-TempX]or'.' == iot_Map[2*many-TempY][2*manx-TempX]:
						iot_Map[2*many-TempY][2*manx-TempX] = 'B'
					else:
						many = TempY
						manx = TempX
				if '.' == iot_Stage[stage_Num][TempY][TempX]:
					iot_Map[TempY][TempX] = '.'
				else:
					iot_Map[TempY][TempX] = ' '
				iot_Map[many][manx] = '@'
			else:
				many = TempY
				manx = TempX
		elif event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

