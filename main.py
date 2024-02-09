'''
The parameter weekday is True if it is a weekday,
and the parameter vacation is True if we are on vacation.
We sleep in if it is not a weekday or we're on vacation.
Return True if we sleep in.

sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
'''

def sleep_in(weekday, vacation):
    # False False return True
    # True True return True
    # False True true
    # True False false

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

  # return True; if it is not a weekday (= False) OR we're on vacation (= True)
  # return False if weekday == True, vacation False
  if weekday == False or vacation == True:
    return True
  return False

Saturday = False
vacation = True

result = sleep_in(Saturday, vacation)
print(result)