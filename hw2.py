import data
from data import Rectangle
from data import Point
from data import Duration
from data import Song
from typing import List, Optional
# Write your functions for each part in the space below.

# Part 1
def create_rectangle(point1:Point, point2:Point)-> Rectangle:
    top_left_x = min(point1.x, point2.x)
    top_left_y = max(point1.y, point2.y)
    bottom_left_x = max(point1.x, point2.x)
    bottom_left_y = min(point1.y, point2.y)

    top_left = Point(top_left_x, top_left_y)
    bottom_right = Point(bottom_left_x, bottom_left_y)

    return Rectangle((top_left), (bottom_right))

#The function's purpose is to return a rectangle with two points.
#The input are two points and the outputs are also two points the top left point of the rectangle and the top right of the rectangle.
#The parameters are point:Point and point2:Point. The return type is Rectangle. This contains the top left and bottom right points.

# Part 2
def shorter_duration_than(duration1:Duration, duration2:Duration)-> bool:
    total_duration1 = duration1.minutes + duration1.seconds// 60 + (duration1.seconds % 60 / 60)
    total_duration2 = duration2.minutes + duration2.seconds // 60 + (duration2.seconds % 60 / 60)
    if total_duration1<total_duration2:
        return True
    else:
        return False

#The function's purpose is to see which duration is longer or shorter. The input are two durations which includes minutes and seconds.
#The parameters are duration1:Duration and duration2:Duration. The return type is a bool.

# Part 3
def song_shorter_than(song_list:list[Song], max_duration: Duration)->list[Song]:
    max_duration = max_duration.minutes + max_duration.seconds // 60 + (max_duration.seconds % 60 / 60)
    return [song for song in song_list if (song.duration.minutes + song.duration.seconds // 60 + (song.duration.seconds % 60 / 60)<max_duration)]
#The function's purpose is to return a list of all the songs in the inputted list of songs where the duration is less than the inputted duration (duration parameter)
#The inputs are a list of songs and the max duration. The output is a list fo songs.
#The parameters are song_list:list[Song], max_duration: Duration, these are a list of songs and the max duration.
#The return type is a list of all songs that have a duration less than the max duration.

# Part 4
def running_time(song_list:list[Song], playlist:list[int])-> Duration:
    total_seconds = 0
    total_minutes = 0

    for index in playlist:
            total_minutes = total_minutes + song_list[index].duration.minutes
            total_seconds = total_seconds + song_list[index].duration.seconds

    total_minutes = total_minutes + total_seconds // 60
    total_seconds = total_seconds % 60
    return Duration(total_minutes, total_seconds)

#The function's purpose is is to add the duration of all the songs that are in the list of integers. The list of integers correspond to the songs' indexes in the list of songs.
#The inputs are a list of songs and a list integers. The output is a duration consists of minutes and seconds.
#The parameters are song_list:list[Song] and playlist:list[int]. The return type is Duration.

# Part 5
def validate_route(city_links:list[list[str]], route:list[str])-> bool:
    if route == []:
        return True

    for i in range(len(route)-1):
        city_a = route[i]
        city_b = route[i+1]

        if [city_a, city_b] not in city_links and [city_b, city_a] not in city_links:
            return False
    return True

#The functions purpose is to see if there is a link between the cities in the list to see if the routes are valid.
#The inputs are a list of list of strings that contain cities and a list of cities. The output is a bool that depends on whether there is a link between the cities.
#The parameters are city_links:list[list[str]] and route:list[str]. The return type is a bool.


# Part 6
def longest_repetition(list_integers:[list[int]])-> Optional[int]:
    if not list_integers:
        return None
    current_length= 1
    max_length = 1
    start_index = 0
    best_start_index = 0
    for i in range(1, len(list_integers)):
        if list_integers[i] == list_integers[i-1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 1
            start_index = i
    if current_length > max_length:
        best_start_index = start_index
    return best_start_index if max_length > 1 else None

#The function's purpose is to find the longest contiguous repetition in a list and to return the index where the repetition starts.
#The input is a list if integers. The output is an integer(index) or None.
#The parameter is list_integers:[list[int]. The return type is Optional[int].
