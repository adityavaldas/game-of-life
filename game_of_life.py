import os
import time
import random

class ConwaysGameOfLife:
	def __init__(self):
		os.system('clear')
		N = 50
		self.LIFE_PROBABILITY = 30
		self.KILL_PROBABILITY = 90
		self.generation_number = 0
		self.map_x_length = N*4
		self.map_y_length = N
		self.total_points = self.map_x_length * self.map_y_length
		self.map_size = [self.map_x_length, self.map_y_length]
		self.current_plot = [[0] * self.map_y_length for _ in range(self.map_x_length)]
		self.next_gen_plot = [[0] * self.map_y_length for _ in range(self.map_x_length)]

	def run(self):
		self.initialize_map()
		self.print_map()
		while True:
			self.update_map()
			self.print_map()
			# input()
			time.sleep(0.01)

	def print_map(self):
		# print('Print map')
		os.system('clear')
		for y in range(self.map_y_length):
			for x in range(self.map_x_length):
				if(self.current_plot[x][y] == 1):
					print('0', end = '')
				else:
					print(' ', end = '')
			print()
		print(f'Generation {self.generation_number}')

	def initialize_map(self):
		# print()
		# print('Init map')
		for i in range(self.map_x_length):
			for j in range(self.map_y_length):
				a = random.randint(1, 100)
				if(a > self.LIFE_PROBABILITY):
					self.current_plot[i][j] = 1
				else:
					self.current_plot[i][j] = 0
	
	def update_map(self):
		# print()
		# print('Update map')
		self.generation_number += 1
		for i in range(self.map_x_length):
			for j in range(self.map_y_length):
				sum = 0
				for x in range(-1, 2):
					for y in range(-1, 2):
						#Avoid out of bounds points
						if(i+x >= 0 and i+x < self.map_x_length and j+y >= 0 and j+y < self.map_y_length):
							#Avoid reading the existing block
							if not(x == 0 and y == 0):
								if(self.current_plot[i+x][j+y] == 1):
									sum += 1
				#If it is a live cell
				if(self.current_plot[i][j] == 1):
					if(sum in [2, 3]):
						# print(f'Alive continue cell {i} {j}')
						self.next_gen_plot[i][j] = 1
					else:
						# print(f'Kill cell {i} {j}')
						self.next_gen_plot[i][j] = 0
				#If it is a dead cell
				else:
					if(sum == 3):
						# print(f'Alive cell {i} {j}')
						self.next_gen_plot[i][j] = 1
		
		self.kill_random_points()
		self.current_plot = self.next_gen_plot.copy()

	def kill_random_points(self):
		killed = 0
		kill_threshold = 0.03
		if(self.generation_number % 100 == 0):
			q = random.randint(1, 100)
			if(q < 10):
				kill_threshold = 0.5
			else:
				kill_threshold = 0.09
		while True:
			if(killed > self.total_points*kill_threshold):
				return
			a = random.randint(1, 100)
			if(a < self.KILL_PROBABILITY):
				i = random.randint(1, self.map_x_length-1)
				j = random.randint(1, self.map_y_length-1)
				self.current_plot[i][j] = 0
				killed += 1

ConwaysGameOfLife().run()