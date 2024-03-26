def multi_print(str):
    # This is what our expected output needs to look like:
    # if str = '12345'
    # 1      - needs to go through 1 index of str
    # 12     - needs to go through 2 indices of str
    # 123    - needs to go through 3 indices of str
    # ...
    # 12345  - needs to go through len(str) (5) indices of str

    # go through each index in str - this is called a for loop
    # i goes through [0, 1, 2, 3, 4]
    for i in range(len(str)): # i < len(str) (5)
        # the for loop of j
        for j in range(i+1):
            # j in the first iteration goes through:   [0]            because i is: 0   result: "1"
            # j in the second iteration goes through:  [0, 1]         because i is: 1   result: "12"
            # j in the third iteration goes through:   [0, 1, 2]      because i is: 2   result: "123"
            # j in the fourth iteration goes through:  [0, 1, 2, 3]   because i is: 3   result: "1234"
            print(str[j], end="")
        # After we go through every j index, we print a new line to separate each result
        print()

    # go through each element in str - this is called a for-each loop
    # for char in str:
    #    print(char)

 # Homework:
    # Problem 1: Draw me a (width x height) rectangle of "*"

def draw_rectangle(width, height):
    # ******
    # ******
    # ******
    # ******
    # ******
    for i in range(height): # first loop is height?
        for j in range(width):
            print("*", end="")
        print()

# Problem 2: draw an upside down triangle of base b of stars

def draw_upside_down_triangle(base):
    # *****
    # ****
    # ***
    # **
    # *
    for i in range(base, 0, -1):
        for j in range(i):
            print("*", end="")
        print()

def make_triangle(x):
    # * - 1
    # ** - 2
    # *** - 3
    # **** - 4
    # ***** - 5
    # range(starting point(inclusive)(default 0), ending point (exclusive), increments (by default 1) )
    # this loop goes through the height of the right triangle
    for i in range(x+1):
        # this loop goes through the number of stars in each row of the right triangle
        for j in range(i):
            print("*", end="")
        print()

if __name__ == "__main__":


    draw_rectangle(5, 6)

    multi_print("123456")  # why doesnt this have the last number? why does this have a space before?
    # why dont the others have this problem?

    draw_upside_down_triangle(5)
    make_triangle(5)




