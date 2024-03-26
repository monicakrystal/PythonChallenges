
# Given a string, return a new string made of every other
# char starting with the first, so "Hello" yields "Hlo".

# string_bits('Hello') → 'Hlo'
# string_bits('Hi') → 'H'
# string_bits('Heeololeo') → 'Hello

def string_bits(str):
    result = ""
    for i in range(0, len(str), 2):
        result = result + str[i]
    print(result)



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


def string_splosion2(str):
    result = ""
    for i in range(len(str)):
        result = result + str[:i + 1]
    print(result)


golf = {
    "Banff Springs": {"Address": "405 Spray Avenue, Banff, AB T1L 1J4, Canada",
                      "Ratings": ["Beautiful Scenery", "Well-maintained"]},
    "Coeur d'Alene": {"Address": "900 S Floating Green Dr, Coeur d'Alene, ID 83814",
                      "Ratings": ["Floating Green", "Great Condition"]},
    "Wolf Creek": {"Address": "403 Paradise Pkwy, Mesquite, NV 89027", "Ratings": ["Tough course", "Unique Landscape"]}}


def course_info_reg():
    for i in range(len(golf)):
        print("Golf Course Name: " + list(golf)[i])
        print()


def course_info():
    for course in golf:
        print("Golf Course Name: " + course)
        print("Address: " + golf[course]['Address'])
        print("Ratings: ")
        for rating in golf[course]["Ratings"]:
            print(rating)
        print()

    # for course in golf:
        # for info in golf:
            # result = golf[course] + golf[course]['Address']
        # print(result)


def nested_get():
    for course in golf:
        print(course)
        for info in golf:
            print(golf[course]['Address'])


def nested_get_one():
    for course in golf:
        print(course)
        print(golf[course]['Address'])

# dict.items() returns tuples
# tuple = (key, value)
# when we assign a tuple to two variables like we did with (course, info) is known as "unpacking" on 85
def get_courses():
    for (course, info) in golf.items():
        address = info["Address"]
        ratings = ", ".join(info["Ratings"])
        print(f"{course}: {address}, Ratings: {ratings}")

get_courses()

def nested_get_try():
    for course in golf:
        print(course)
        for key in golf[course]:
            print(f"  {key}: {golf[course][key]}")


def nested_get2():
    for course, info in golf.items():
        print(course)
        for address, value in info.items():
            if address == "Address":
                print(f"  {address}: {value}")


# course 1 address:,ratings:

# course 2 ratings:

# make a function that prints the name, address, ratings
# use nested loop
# golf['Course1']["Address"] add address to all
# use nested for each loop
# how to unpack a json in python  -----  the import JSON at the top?


# Given an array of ints, return the number of 9's in the array.

# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3

def array_count(nums):
    count = 0
    for num in nums:
        if num == 9:
            count = count + 1
    print(count)


if __name__ == "__main__":
    pass
