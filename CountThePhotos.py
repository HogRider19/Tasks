"""
In a string we describe a road. There are cars that move to the right
and we denote them with ">" and cars that move to the left and
we denote them with "<". There are also cameras that are indicated by: ".".
A camera takes a photo of a car if it moves to the direction of the camera.
Your task is to write a function such that,
for the input string that represents a road as described,
returns the total number of photos that were taken by the cameras.
The complexity should be strictly O(N) in order to pass all the tests.
"""


def count_photos(road):
    return count_photo_once('<', road) + count_photo_once('>', road[::-1])

def count_photo_once(direction, road):
    photo = 0
    cameras = 0
    for letter in road:
        if letter == '.':
            cameras += 1
        elif letter == direction:
            photo += cameras
    return photo


print(count_photos(">.>..<"), 8)
print(count_photos(".><.>>.<<"), 11)
print(count_photos(".>>>"), 0)
print(count_photos(">..<<.>.<."), 15)
print(count_photos(".<>>..><.<<<<<."), 34)
print(count_photos("<..>>..>>.><.<.><..<"), 57)
print(count_photos("..<>.>>.><>>.<<<.<>>.>.>>>>>..><<.>.>>..>.>>><><>."), 248)


