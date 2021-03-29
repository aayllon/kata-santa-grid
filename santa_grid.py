class SantaGrid:
    def __init__(self, size_x, size_y):
        self.grid = [[0] * size_y for i in range(size_x)]


    def __str__(self) -> str:
        to_string = ""
        for row in range(len(self.grid)):
            to_string += "| "
            for column in range(len(self.grid[row])):
                to_string += str(self.grid[row][column]) + " "
            to_string += "|\n"
        return to_string


    def turn_on(self, initial_coordinates, end_coordinates):
        for row in range(initial_coordinates[0], end_coordinates[0]):
            for column in range(initial_coordinates[1], end_coordinates[1]):
                self.grid[row][column] = 1


    def is_on(self, coordinate):
        return self.grid[coordinate[0]][coordinate[1]] == 1


    def toggle(self, initial_coordinates, end_coordinates):
        for row in range(initial_coordinates[0], end_coordinates[0]):
            for column in range(initial_coordinates[1], end_coordinates[1]):
                self.grid[row][column] = 1 if self.grid[row][column] == 0 else 0


    def turn_off(self, initial_coordinates, end_coordinates):
        for row in range(initial_coordinates[0], end_coordinates[0]):
            for column in range(initial_coordinates[1], end_coordinates[1]):
                self.grid[row][column] = 0
