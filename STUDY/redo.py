# This is what our expected output needs to look like:
# if str = '12345'
# 1      - needs to go through 1 index of str
# 12     - needs to go through 2 indices of str
# 123    - needs to go through 3 indices of str
# ...
# 12345  - needs to go through len(str) (5) indices of str

# go through each index in str - this is called a for loop
# i goes through [0, 1, 2, 3, 4]

def number_tri(s):
    for i in range(len(s)):
        print("When i is " + str(i))
        for j in range(i + 1):
            print(s[j], end="")
        print()

# number_tri('12345')

# Problem 1: Draw me a (width x height) rectangle of "*"

def draw_rec(width, height):
    for i in range(height):
        for j in range(width):
            print("*",end="")
        print()

# draw_rec(6,5)

# Problem 2: draw an upside down triangle of base b of stars
def draw_upside_down_triangle(base):
    # *****
    # ****
    # ***
    # **
    # *
    # [5,4,3,2,1]
    for i in range(base, 0, -1):
        for j in range(i):
            print("*", end="")
        print()

# draw_upside_down_triangle(5)

def make_triangle(x):
    # * - 1
    # ** - 2
    # *** - 3
    # **** - 4
    # ***** - 5
    # range(starting point(inclusive)(default 0), ending point (exclusive), increments (by default 1) )
    # this loop goes through the height of the right triangle
    # [0,1,2,3,4] +1 [1,2,3,4,5]
    for i in range(x+1): # why x + 1 because its excluded?
        for j in range(i):
            print("*", end="")
        print()

# make_triangle(5)

# Given a string, return a new string made of every other
# char starting with the first, so "Hello" yields "Hlo".

# string_bits('Hello') → 'Hlo'
# string_bits('Hi') → 'H'
# string_bits('Heeololeo') → 'Hello

def new_string(str):
    result = ""
    for i in range(0,len(str),2):
        result = result + str[i]
    print(result)

# new_string("Hello")

# Given a non-empty string like "Code" return a string like "CCoCodCode".

# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'

def string_splosion(str):
    result = ""
    for i in range(len(str)):
        for j in range(i + 1):  # why i + 1 instead of i
            result = result + str[j]  # what does this mean?
    print(result)


golf = {
    "Banff Springs": {"Address": "405 Spray Avenue, Banff, AB T1L 1J4, Canada",
                      "Ratings": ["Beautiful Scenery", "Well-maintained"]},
    "Coeur d'Alene": {"Address": "900 S Floating Green Dr, Coeur d'Alene, ID 83814",
                      "Ratings": ["Floating Green", "Great Condition"]},
    "Wolf Creek": {"Address": "403 Paradise Pkwy, Mesquite, NV 89027", "Ratings": ["Tough course", "Unique Landscape"]}}


def course_info():
    for course in golf:
        print("Golf Course Name: " + course)
        print("Address: " + golf[course]['Address'])
        print("Ratings: ")
        for rating in golf[course]["Ratings"]:
            print(rating)
        print()


# dict.items() returns tuples
# tuple = (key, value)
# when we assign a tuple to two variables like we did with (course, info) is known as "unpacking" on 85
def get_courses():
    for (course, info) in golf.items():
        address = info["Address"]
        ratings = ", ".join(info["Ratings"])
        print(f"{course}: {address}, Ratings: {ratings}")


if __name__ == "__main__":
    pass

# step 1 make a txt.file with 5 names.py
# step 2 fill txt file with names.py or values, seperated by commas,
# step 3 read and process the file in python
# step 3b store every name inside of a list as long as that name doesnt start with the letter A
# step 4 print the finalized list of names.py
