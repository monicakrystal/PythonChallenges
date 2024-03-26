def w_true():
    n = 0
    while True:
        if n == 3:
            break
        print(n)
        n = n + 1





def test_banana():
    for n in "banana":
        print(n)


def test_i_banana():
    for i in range(len("banana")):
        print(i)


def zork_test():
    zork = 0
    print(zork)
    for thing in [9, 41, 12, 3, 74, 15]:
        zork = zork + thing
        print(zork, thing)
    print('After', zork)


def find_food(s):
    food = s.find("pizza")
    print(food)


s = "I love pizza"

sent = "   Hello, World!   "
stripped_s = sent.strip()
print(stripped_s)

data = "from monica_krystal@gmail.com is my EMAIL"
start_position = data.find("@")
print(start_position)

end_position = data.find(" ", start_position)
print(end_position)

find_domain = data[start_position+1 : end_position]
print(find_domain)
if __name__ == "__main__":
    w_true()
    zork_test()
    test_banana()
    test_i_banana()
    find_food(s)


