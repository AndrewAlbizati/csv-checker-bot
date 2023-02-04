from checker import Checker

with open("sheets.txt", "r") as f:
    for line in f:
        link = line.strip()
        checker = Checker(link)
        checker.check()