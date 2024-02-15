
# The parameter weekday is True if it is a weekday,
# and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday, or we're on vacation.
# Return True if we sleep in.

# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True


def sleep_in(weekday, vacation):
    # return True; if it is not a weekday (= False) OR we're on vacation (= True)
    # return False if weekday == True, vacation False
    if weekday == False or vacation == True:
        return True
    return False


weekday = False
vacation = True

result = sleep_in(weekday, vacation)
print(result)

# second way to solve

# False, False returns True
# True, True returns True
# False, True returns True
# True, False returns False

'''
if weekday == True and vacation == False:
  return False;
elif weekday == False and vacation == False:
  return True;
elif weekday == False and vacation == True:
  return True;
elif weekday == True and vacation == True:
  return True;
'''


# Given an int n, return the absolute difference between n and 21,
# except return double the absolute difference if n is over 21.

# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0

def diff21(n):
    if n > 21:
        return (n - 21) * 2
    elif n < 21:
        return 21 - n

result = diff21(23)
print(result)


#   Given 2 ints, a and b, return True if
#   one of them is 10 or if their sum is 10.

# makes10(9, 10) → True
# makes10(9, 9) → False
# makes10(1, 9) → True

def makes10(a, b):
    if (a == 10 or b == 10) or (a + b == 10):
        return True
    return False

a = 5
b = 5
print(makes10(a, b))


# create a function that checks if a string begins with "saucy" & returns string
# if it doesn't, add "saucy" and then return it

def addSauce(str):
    return str if str.startswith("saucy") else "saucy " + str

print(addSauce("pizza"))

def addSauceTrue(str):
    return str.startswith("pizza", 6)

print(addSauceTrue("saucy pizza"))


# make a function that capitalizes the first letter in a string
def test_word(str):
    return str.capitalize();

print(test_word("there"))


# Given a string of even length,
# return the first half. So the string "WooHoo" yields "Woo".

# first_half('WooHoo') → 'Woo'
# first_half('HelloThere') → 'Hello'
# first_half('abcdef') → 'abc'

def first_half(str):
  first = len(str) // 2
  print(first)
  return str[:first]

print(first_half("WooHoo"))

# second way

def first_part(str):
    return str[:len(str)//2]

print(first_part("YeeHah"))


# Given 2 strings, return their concatenation, except omit
# the first char of each. The strings will be at least length 1.

# non_start('Hello', 'There') → 'ellohere'
# non_start('java', 'code') → 'avaode'
# non_start('shotl', 'java') → 'hotlava'

def non_start(a, b):
    return a[0::2] + b[1:]

print(non_start("Code", "there"))



# Given a string, return a new string made of 3 copies
# of the last 2 chars of the original string.
# The string length will be at least 2.

# extra_end('Hello') → 'lololo'
# extra_end('ab') → 'ababab'
# extra_end('Hi') → 'HiHiHi'

def extra_end(str):
    return str[-2:] + str[-2:] + str[-2:]


print(extra_end("hello"))


# The web is built with HTML strings like "<i>Yay</i>"
# which draws Yay as italic text. In this example, the "i"
# tag makes <i> and </i> which surround the word "Yay". Given
# tag and word strings, create the HTML string with tags around
# the word, e.g. "<i>Yay</i>".

# make_tags('i', 'Yay') → '<i>Yay</i>'
# make_tags('i', 'Hello') → '<i>Hello</i>'
# make_tags('cite', 'Yay') → '<cite>Yay</cite>'

def make_tags(tag, word):
  return "<" + tag + ">" + word + "<" + "/" + tag + ">"

print(make_tags("i", "hello"))