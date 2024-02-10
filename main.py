
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

n = 1
result = console.log(diff21(n))