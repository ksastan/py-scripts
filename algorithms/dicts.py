s = [1, 2, 3, 1, 2]
letters = dict()
for c in s:
    if c not in letters:
        letters[c] = 0
    letters[c] += 1
for c in letters:
    print(c, letters[c])
