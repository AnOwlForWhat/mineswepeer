import random
import pygame
from settings import*



class Tile:
	def __init__(self,x,y, image,type, revealed = False, flagged = False):
		self.x, self.y = x * TileSize, y *TileSize
		self.image = image
		self.type = type
		self.revealed = revealed
		self.flagged = flagged

	def draw(self,board_surf):
		if not self.flagged and self.revealed:
			board_surf.blit(self.image,(self.x,self.y))
		elif self.flagged and not self.revealed:
			board_surf.blit(TileFlag,(self.x,self.y))
		elif not self.revealed:
			board_surf.blit(TileUnknown,(self.x,self.y))
	def __repr__(self):
		return self.type



class Board:
	def __init__(self):
		self.board_surf = pygame.Surface((width,height))
		self.board_list  = [[Tile(col, row, TileEmpty, ".") for row in range(Rows)] for col in range(Cols)]
		self.place_mines()
		self.place_clues()
		self.dug = []

	def place_mines(self):
		for _ in range(mines):
			while True:	
				x = random.randint(0,Rows-1)
				y = random.randint(0,Cols-1)

				if self.board_list[x][y].type == ".":
					self.board_list[x][y].image = TileMine
					self.board_list[x][y].type = "X"
					break

	def place_clues(self):
		for x in range(Rows):
			for y in range(Cols):
				if self.board_list[x][y].type != "X":
					total_mines = self.check(x,y)
					if total_mines > 0:
						self.board_list[x][y].image = images[total_mines-1]
						self.board_list[x][y].type = "C"
	@staticmethod
	def is_inside(x,y):
		return 0 <= x < Rows and 0 <= y < Cols

	def check(self,x,y):
		total_mines = 0
		for x_offset in range(-1,2):
			for y_offset in range(-1,2):
				near_x = x + x_offset 
				near_y = y + y_offset 
				if self.is_inside(near_x, near_y) and self.board_list[near_x][near_y].type == "X":
					total_mines += 1

		return total_mines


	def draw(self, screen):
		for row in self.board_list:
			for tile in row:
				tile.draw(self.board_surf)
		screen.blit(self.board_surf, (0, 0))

	def dig(self, x ,y):
		self.dug.append((x, y))

		if self.board_list[x][y].type == "X":
			self.board_list[x][y].revealed = True
			self.board_list[x][y].image = TileExploded
			return False
		elif self.board_list[x][y].type == "C":
			self.board_list[x][y].revealed = True
			return True

		self.board_list[x][y].revealed = True

		for row in range(max(0, x-1), min(Rows-1, x+1)+1):
			for col in range(max(0, y-1), min(Cols-1, y+1)+1):
				if (row,col) not in self.dug:
					self.dig(row, col)
		return True
		


	def display(self):
		for row in self.board_list:
			print(row)
