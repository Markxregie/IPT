flist = [8, 9, 10]
print(flist)

flist.pop(1)
flist.insert(1, 17)
print(flist)

flist.append(4)
flist.append(5)
flist.append(6)
print(flist)

flist.pop(0)
print(flist)

flist.sort()
print(flist) 

doublelist = flist * 2
doublelist.insert(3, 25)
print(doublelist)