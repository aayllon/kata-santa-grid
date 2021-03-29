from unittest import TestCase

from santa_grid import SantaGrid


class TestSantaGrid(TestCase):
    def test_turn_on_all_lights(self):
        santa_grid = SantaGrid(1000, 1000)
        initial_coordinates = (0, 0)
        end_coordinates = (999, 999)

        santa_grid.turn_on(initial_coordinates, end_coordinates)

        for row in range(initial_coordinates[0], end_coordinates[0]):
            for column in range(initial_coordinates[1], end_coordinates[1]):
                assert santa_grid.is_on((row, column))


    def test_toggle_should_turn_on_light_when_is_off(self):
        santa_grid = SantaGrid(1000, 1000)
        initial_coordinates = (0, 0)
        end_coordinates = (999, 0)

        santa_grid.toggle(initial_coordinates, end_coordinates)

        for row in range(initial_coordinates[0], end_coordinates[0]):
            for column in range(initial_coordinates[1], end_coordinates[1]):
                assert santa_grid.is_on((row, column))


    def test_toggle_should_turn_off_light_when_is_on(self):
        santa_grid = SantaGrid(1000, 1000)
        initial_coordinates = (0, 0)
        end_coordinates = (999, 0)
        santa_grid.turn_on(initial_coordinates, end_coordinates)

        santa_grid.toggle(initial_coordinates, end_coordinates)

        for row in range(initial_coordinates[0], end_coordinates[0]):
            for column in range(initial_coordinates[1], end_coordinates[1]):
                assert not santa_grid.is_on((row, column))


    def test_turn_off_lights(self):
        santa_grid = SantaGrid(1000, 1000)
        initial_coordinates = (0, 0)
        end_coordinates = (999, 0)
        santa_grid.turn_on(initial_coordinates, end_coordinates)

        santa_grid.turn_off(initial_coordinates, end_coordinates)

        for row in range(initial_coordinates[0], end_coordinates[0]):
            for column in range(initial_coordinates[1], end_coordinates[1]):
                assert not santa_grid.is_on((row, column))


    def test_follow_santa_instructions(self):
        santa_grid = SantaGrid(1000, 1000)

        santa_grid.turn_on((887, 9), (959, 629))
        santa_grid.turn_on((454, 398), (844, 448))
        santa_grid.turn_off((539, 243), (559, 965))
        santa_grid.turn_off((370, 819), (676, 868))
        santa_grid.turn_off((145, 40), (370, 997))
        santa_grid.turn_off((301, 3), (808, 453))
        santa_grid.turn_on((351, 678), (951, 908))
        santa_grid.toggle((720, 196), (897, 994))
        santa_grid.toggle((831, 394), (904, 860))

        print(santa_grid)
