import string
import os
with open(os.path.join("opgave_1","Navne_liste.txt"), "r") as f:
    navne = f.read()
navneliste = navne.split(sep=",")
navneliste = sorted(navneliste, key = str.casefold)
letterFrequency = {}
for letter in string.ascii_lowercase:
    letterFrequency[letter] = 0
for name in navneliste:
    for letter in name:
        letterFrequency[letter.lower()] += 1
with open(os.path.join("opgave_1","sorted_list.txt"), "w") as f:
    for navn in navneliste:
        f.write(navn + ",")
with open(os.path.join("opgave_1","letterFrequency.txt"), "w") as f:
    for letter in string.ascii_lowercase:
        f.write(letter + ":" + str(letterFrequency[letter]) + ",")