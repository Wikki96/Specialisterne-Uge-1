import string
with open("opgave_1/Navne_liste.txt", "r") as f:
    navne = f.read()
navneliste = navne.split(sep=",")
navneliste = sorted(navneliste, key = str.casefold)
letterFrequency = {}
for letter in string.ascii_lowercase:
    letterFrequency[letter] = 0
for name in navneliste:
    for letter in name:
        letterFrequency[letter.lower()] += 1
print(letterFrequency)