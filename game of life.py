from random import randint
from pprint import pprint
from copy import deepcopy
import os
import time
#
# world_size = 16
# populations = 256
# world = [[] for _ in range(world_size)]
# for i in range(world_size):
#     for j in range(world_size):
#         world[i].append(randint(0, 1))
#
# new_world = deepcopy(world)
#
# for _ in range(populations):
#     for x in range(world_size):
#         for y in range(world_size):
#             alives_in_area = 0
#             for i in (-1, 0, 1):
#                 for j in (-1, 0, 1):
#                     if i != 0 and j != 0:
#                         if (
#                             world[(y - 1 + j + world_size) % world_size][
#                                 (x - 1 + i + world_size) % world_size
#                             ]
#                             == 1
#                         ):
#                             alives_in_area += 1
#             if alives_in_area == 3 or alives_in_area == 2:
#                 new_world[x][y] = 1
#             else:
#                 new_world[x][y] = 0
#     time.sleep(0.25)
#     os.system("cls")
#     for i in range(world_size):
#         for j in range(world_size):
#             if new_world[i][j] == 1:
#                 print(f"\N{MEDIUM BLACK CIRCLE}", end="")
#             else:
#                 print(f"\N{MEDIUM WHITE CIRCLE}", end="")
#         print("")
#     world = deepcopy(new_world)


import numpy as np
from tkinter import Tk, Canvas


class World:
    width = 0
    height = 0
    size = (width, height)
    alive_simbols = "\N{MEDIUM BLACK CIRCLE}"
    dead_simbols = "\N{MEDIUM WHITE CIRCLE}"
    states = 2
    cells = np.zeros(shape=size)
    new_cells = np.zeros(shape=size)

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = np.random.randint(low=0, high=self.states, size=(self.width, self.height))

    def __repr__(self):
        cells_repr = " " + str(self.cells).replace("[", "").replace("]", "").replace(".", "")
        return cells_repr.replace("1", self.alive_simbols).replace("0", self.dead_simbols)

    def check_rule(self, x, y):
        alives_in_area = 0
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if i != 0 and j != 0:
                    if (
                        self.cells[(y - 1 + j + self.width) % self.width][
                            (x - 1 + i + self.height) % self.height
                        ]
                        == 1
                    ):
                        alives_in_area += 1

        return 1 if alives_in_area == 3 or alives_in_area == 2 else 0

    def evaluate(self, iterations=1):
        new_cells = np.zeros_like(self.cells)
        for _ in range(iterations):
            for x in range(0, self.width):
                for y in range(0, self.height):
                    self.new_cells[x][y] = self.check_rule(x, y)
                self.cells = deepcopy(self.new_cells)
        del new_cells

    def get_data(self):
        """
        get_data [summary]
        размеры мира
        текущее поколение
        число живых клеток
        число мертвых клеток
        """
        cell_total = self.width*self.height
        alives_total = np.count_nonzero(self.crlls)
        dead_total = cells_total-alives_total
        alives_total_perc = alives_total/cell_total
        dead_total = 1.0 -alives_total_perc
        data = [stn(i) for i in (cell_total, alives_total, dead_total, alives_total_perc)]
        return "\n".join(data)

my_world = World(10, 10)
print(my_world)
my_world.evaluate()
print(my_world)
