#-------------------------------------------------------------------------------
# Name:        Conway's Game of Life
# Purpose:     Conway's Game of Life in console display with stop
#              between step
#
# Author:      Oazin
#
# Created:     13/12/2020
# Copyright:   (c) Oazin 2020
# Version:     Python 3.4
#-------------------------------------------------------------------------------

from random import randint

class Cell :

    def __init__(self):
        """Constructive of the cell class"""
        self.current = False
        self.future = False
        self.neighbours = None

    def is_alive(self):
        """Returns the current state (boolean)"""
        if self.current is True:
            return True
        else:
            return False

    def set_neighbours(self, liste):
        """Allows to assign as neighbours the list passed in parameter"""
        self.neighbours = liste

    def get_neighbours(self):
        """Returns the length of the list of neighbours of the cell"""
        return len(self.neighbours)

    def born(self):
        """Sets the futuree state of the cell to True"""
        if self.current is False:
            self.future = True
            return self.future

    def die(self):
        """Reverse operation"""
        if self.current is True:
            self.future = False
            return self.future

    def switch_state(self):
        """Changes the futuree state of the cell to the current state"""
        self.current = self.future
        return self.current

    def __str__(self):
        """Displays an X if the cell is alive and a - otherwise"""
        if self.current is True:
            return "X"
        else:
            return "-"

    def calculate_future_state(self):
        """Implementing the evolutionary rules of the game of life by preparing the future state for its new value"""
        if self.is_alive():
            if self.get_neighbours() <= 3 and self.get_neighbours() >= 2:
                self.future = self.current
                return self.future
            else:
                self.die()
        else:
            if self.get_neighbours() == 3:
                self.born()
            else:
                self.future = self.current
                return self.future


class Grid:

    def __init__(self, W, H):
        """Constructice of the Grid class"""
        self.widht = W
        self.height = H
        self.matrix = [[Cell() for i in range(H)] for j in range (W)]

    def in_grid(self, i, j):
        """Indicates whether a point with coordinates i and j is in the grid"""
        if 0 <= i < self.widht and 0 <= j < self.height:
            return True
        else:
            return False

    def setXY(self, i, j, v):
        """Assigns a new value to the coordinate (i,j) in the grid"""
        if self.in_grid(i, j):
            self.matrix[i][j].current = v
        else:
            raise IndexError

    def getXY(self, i, j):
        """Retrieves the cell located to the coordinate(i,j) of the grid"""
        if self.in_grid(i, j):
            return self.matrix[i][j]
        else:
            raise IndexError

    def get_widht(self):
        """Retrieves the widht of the grid"""
        return self.widht

    def get_height(self):
        """Retrieves the height of the grid"""
        return self.height

    @staticmethod
    def est_voisin(i, j, x, y):
        """Check whether the cells (i,j) and (x,y) are neighbours in the grid"""
        return max(abs(x-i),abs(y-j))==1

    def get_neighbours(self, x, y):
        """Returns the list of neighbours of a cell"""
        v = []
        for i in range(x-2, x+2):
            for j in range(y-2, y+2):
                if self.in_grid(i,j) and Grid.est_voisin(x, y, i, j) and self.getXY(i, j).is_alive():
                    v.append(self.getXY(x, y))
        return v

    def assign_neighbours(self):
        """Assigns to each cell in the grid the list of its neighbours"""
        for x in range(self.get_widht()):
            for y in range(self.get_height()):
                self.getXY(x, y).set_neighbours(self.get_neighbours(x, y))

    def __str__(self):
        """display the grid in the console"""
        grid = ""
        for W in range(self.get_widht()):
            for H in range(self.get_height()):
                grid += str(self.getXY(W, H))
            grid+= "\n"
        return grid

    def fill_rand(self, rate):
        """Fills in the grid according to the rate of cells that must be alive"""
        for W in range(self.get_widht()):
            for H in range(self.get_height()):
                x = randint(0,100)
                if x < rate:
                    self.setXY(W, H, True)
                else:
                    self.setXY(W, H, False)

    def game(self):
        """Calculates the future state of each cell in the grid"""
        for W in range(self.get_widht()):
            for H in range(self.get_height()):
                self.getXY(W,H).calculate_future_state()

    def update(self):
        """switches the entire grid to its future state"""
        for W in range(self.get_widht()):
            for H in range(self.get_height()):
                self.getXY(W,H).switch_state()

def main():
    g = Grid(20,40) # Define widht and height of the grid
    g.fill_rand(20) # Define the starting occurrence rate
    while True:
        g.assign_neighbours()
        print(g)
        g.game()
        key = input("Press Enter to move to the next state and q to exit")
        if key == 'q':
            break
        elif key == "":
            g.update()


main()