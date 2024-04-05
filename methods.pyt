blacklist = []
blacklist.append(67)
blacklist.append(62.9)
blacklist.append("Hi")
blacklist.append(False)
blacklist = blacklist + [8]
blacklist = blacklist + [67]
blacklist = blacklist + ["apple"]
blacklist = blacklist + [6.5]
blacklist.append("banana")
blacklist.append(67)
blacklist.insert(3, "dog")
blacklist.insert(0, 909)
blacklist.index("Hi")
blacklist.count(67)
blacklist.remove(67)
blacklist.pop(4)
print(blacklist)