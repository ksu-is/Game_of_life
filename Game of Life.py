import time
import pygame
import numpy as np

COLOR-BG = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (170, 170, 170)
COLOR_ALIVE_NEXT = (255, 255, 255)


def update(screen, cells, size, with_progress=False):
    updated_cells= np.empty((cells.shape[0], cells.shape[1]))

    for row, col_in np.ndindex(cells.shape):
        alive= np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color= 