# unlike a list, tuples cant be changed, like strings
z = (5,4,3)
# this line would error because it cant change
#z[2] = 0

# cant sort(), .append(), reverse()

# can put tuples on left hand side of an assignment
(x,y) = (4, 'fred')
print(y)

# tuples are just lists with parenthesis ?
# just more simple, and efficient in terms of
# memory use and performance than lists
# best used when making temporary variables?

# confused here
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k, v)

tup = d.items()
print(tup)

# Tuples are Comparable ? how to test this?

(0, 1, 2) < (5, 1, 2)

('Jones', 'Sally') < ('Jones', 'Sam')

('Jones', 'Sally') > ('Adams' > 'Sam')

if __name__ == "__main__":
    pass