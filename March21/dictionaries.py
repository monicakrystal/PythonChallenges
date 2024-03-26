purse = dict()
purse['money'] = 12
purse['candy'] = 3

print(purse)

# lists have indexes as keys, dictionaries have keys and values

# What are dictionary literals? just not empty dictionaries?

# looping through a dict
counts2 = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts2:
    print(key, counts2[key])

# Retrieving lists of keys and values
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())

# Two Iteration Variables
# this is a better way than the one above?
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
for aaa,bbb in jjj.items():
    print(aaa,bbb)

# how do I enter a file here?
name = input('Enter file:')
handle = open(f'./HW/{name}')


counts = dict()
for line in handle:
    print(line)
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
        print(bigword, bigcount)


counts = dict()
line = input('Enter a line of text:')
words = line.split()

print('Words:', words)
print('Counting...')

for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)







if __name__ == "__main__":
    pass