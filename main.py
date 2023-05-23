import pygame
from settings import*
from sprites import* 

class GAME:

	def __init__(self):
		self.screen = pygame.display.set_mode((width,height))
		pygame.display.set_caption('minesweeper')
		self.clock = pygame.time.Clock()

	def update(self):
		self.board = Board()
		self.board.display()

	def run(self):
		self.playing = True
		while self.playing:
			self.clock.tick(60)
			self.events()
			self.draw()
		else:
			self.end_scr()

	def draw(self):
		self.screen.fill(BGcolor)
		self.board.draw(self.screen)
		pygame.display.flip()

	def check_win(self):
		for row in self.board.board_list:
			for tile in row:
				if tile.type !=  "X" and not tile.revealed:
					return False
		return True

	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				mx,my = pygame.mouse.get_pos()
				mx //= TileSize
				my //= TileSize
				if event.button == 1:
					if not self.board.board_list[mx][my].flagged:
						#dao , kiem tra neu no
						if not self.board.dig(mx, my):
							#no
							for row in self.board.board_list:
								for tile in row:
									if tile.flagged and tile.type != "X":
										tile.flagged = False
										tile.revealed = True
										tile.image = TileNotMine
									elif tile.type == "X":
										tile.revealed = True
							self.playing = False

				if event.button == 3:
					if not self.board.board_list[mx][my].revealed:
						self.board.board_list[mx][my].flagged = not self.board.board_list[mx][my].flagged

				if self.check_win():
					self.win = True
					self.playing = False
					for row in self.board.board_list:
						for tile in row:
							if not tile.revealed:
								tile.flagged = True

	def end_scr(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

				if event.type == pygame.MOUSEBUTTONDOWN:
					return


game = GAME()
while True:
	game.update()
	game.run()