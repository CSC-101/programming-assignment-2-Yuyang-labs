import data
import hw2
import unittest
from data import Point
from data import Rectangle
from data import Duration
from data import Song
# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle(self):
        point1 = Point(3, 5)
        point2 = Point(9, 4)
        result = hw2.create_rectangle(point1, point2)
        expected = Rectangle(Point(3,5),Point(9,4) )
        self.assertEqual(expected, result)

    def test_create_rectangle(self):
        point1 = Point(2, 2)
        point2 = Point(10, 10)
        result = hw2.create_rectangle(point1, point2)
        expected = Rectangle(Point(2,10),Point(10,2) )
        self.assertEqual(expected, result)


    # Part 2
    def test_shorter_duration(self):
        duration1 = Duration(5, 59)
        duration2 = Duration(5, 10)
        result = hw2.shorter_duration_than(duration1, duration2)
        expected = False
        self.assertEqual(expected, result)

    def test_shorter_duration(self):
        duration1 = Duration(5, 100)
        duration2 = Duration(6, 41)
        result = hw2.shorter_duration_than(duration1, duration2)
        expected = True
        self.assertEqual(expected, result)

    # Part 3
    def test_song_shorter_than(self):
        song1 = Song('Polo G', 'Martin and Gina', Duration(3,20))
        song2 = Song('Calvin Harris', 'Outside', Duration(2,59))
        song3 = Song('Lil Tecca', '500 lbs', Duration(2,51))
        list_songs = [song1, song2, song3]
        result = hw2.song_shorter_than(list_songs, Duration(2,57))
        expected = [song3]
        self.assertEqual(result, expected)

    def test_song_shorter_than(self):
        song1 = Song('Polo G', 'Martin and Gina', Duration(3, 20))
        song2 = Song('Calvin Harris', 'Outside', Duration(2, 59))
        song3 = Song('Lil Tecca', '500 lbs', Duration(2, 51))
        list_songs = [song1, song2, song3]
        result = hw2.song_shorter_than(list_songs, Duration(3, 0))
        expected = [song2, song3]
        self.assertEqual(result, expected)
    # Part 4
    def test_running_time(self):
        playlist = [0,1,2]
        song1 = Song('Polo G', 'Martin and Gina', Duration(3, 20))
        song2 = Song('Calvin Harris', 'Outside', Duration(2, 59))
        song3 = Song('Lil Tecca', '500 lbs', Duration(2, 51))
        song_list = [song1, song2, song3]
        result = hw2.running_time(song_list, playlist)
        expected = Duration(9, 10)
        self.assertEqual(expected, result)

    def test_running_time(self):
        playlist = [0,1,2,0,2]
        song1 = Song('Polo G', 'Martin and Gina', Duration(3, 20))
        song2 = Song('Calvin Harris', 'Outside', Duration(2, 59))
        song3 = Song('Lil Tecca', '500 lbs', Duration(2, 51))
        song_list = [song1, song2, song3]
        result = hw2.running_time(song_list, playlist)
        expected = Duration(15, 21)
        self.assertEqual(expected, result)

    # Part 5
    def test_validate_route(self):
        result = hw2.validate_route([["San Diego", "Los Angeles"], ["Los Angeles", "San Luis Obispo"], ["Los Angeles", "Irvine"]],["San Diego", "Los Angeles", "San Luis Obispo"])
        expected = True
        self.assertEqual(expected, result)

    def test_validate_route(self):
        result = hw2.validate_route(
            [["San Diego", "Los Angeles"], ["San Diego", "San Luis Obispo"],
             ["Los Angeles", "Irvine"]], ["Los Angeles", "San Luis Obispo"])
        expected = False
        self.assertEqual(expected, result)


    # Part 6

    def test_longest_repetition(self):
        result = hw2.longest_repetition([2,2,1,1,1,2,2])
        expected = 2
        self.assertEqual(expected,result)

    def test_longest_repetition(self):
        result = hw2.longest_repetition([])
        expected = None
        self.assertEqual(expected,result)




if __name__ == '__main__':
    unittest.main()
