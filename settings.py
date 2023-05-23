import pygame
import os 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
DARKGREEN = (0, 200, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BGcolor = DARKGREY

TileSize = 32
Rows = 15
Cols = 15
mines = 25
width = TileSize * Rows
height = TileSize * Cols

images = []
for i in range(1, 9):
	images.append(pygame.transform.scale(pygame.image.load
	(f"E:/Project/minesweeper/assets/Tile{i}.png"),(TileSize,TileSize)))

TileEmpty = pygame.transform.scale(pygame.image.load("E:/Project/minesweeper/assets/TileEmpty.png"),(TileSize,TileSize))
TileExploded = pygame.transform.scale(pygame.image.load("E:/Project/minesweeper/assets/TileExploded.png"),(TileSize,TileSize))
TileFlag = pygame.transform.scale(pygame.image.load("E:/Project/minesweeper/assets/TileFlag.png"),(TileSize,TileSize))
TileMine = pygame.transform.scale(pygame.image.load("E:/Project/minesweeper/assets/TileMine.png"),(TileSize,TileSize))
TileNotMine = pygame.transform.scale(pygame.image.load("E:/Project/minesweeper/assets/TileNotMine.png"),(TileSize,TileSize))
TileUnknown = pygame.transform.scale(pygame.image.load("E:/Project/minesweeper/assets/TileUnknown.png"),(TileSize,TileSize))