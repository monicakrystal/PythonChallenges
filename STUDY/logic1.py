
# You are driving a little too fast, and a police officer stops you.
# Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket.
# If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1.
# If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be
# 5 higher in all cases.


# caught_speeding(60, False) → 0
# caught_speeding(65, False) → 1
# caught_speeding(65, True) → 0

def caught_speeding(speed, is_birthday):
    # ticket currently is 0
    ticket = 0
    if not is_birthday:
        if speed in range(61, 81):
            ticket = 1
        elif speed >= 81:
            ticket = 2
        else:
            if speed in range(66,86):
                ticket = 1
            elif speed >= 86:
                ticket = 2
    print(ticket)


caught_speeding(60, False)

# When squirrels get together for a party, they like to have cigars.

# A squirrel party is successful when the number of cigars is between 40 and 60, inclusive.
# Unless it is the weekend, in which case there is no upper bound on the
# number of cigars. Return True if the party with the given values is successful, or
# False otherwise.

# cigar_party(30, False) → False
# cigar_party(50, False) → True
# cigar_party(70, True) → True


def cigar_party(cigars, is_weekend):
    if cigars in range(40,61) and not is_weekend: # why didn't you add and not is_weekend?
        print('True')
    elif is_weekend and cigars >= 40:
        print('True')
    else:
        print('False')


cigar_party(39, False)

# You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness
# of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result
# getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish,
# 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then
# the result is 0 (no). Otherwise, the result is 1 (maybe).

# date_fashion(5, 10) → 2
# date_fashion(5, 2) → 0
# date_fashion(5, 5) → 1

# def date_fashion(you, date):


if __name__ == "__main__":
    caught_speeding(60, False)