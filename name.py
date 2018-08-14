from random import choice

STARTNAME = [" "," "]


f = open("starnames.csv")
w = f.read()
f.close()
wlist = w.split(",\n")
wlist.pop(-1)
w = [i.lower() for i in wlist if not " " in i]
mydictofw = {}
for i in w:
	listofchar = tuple(STARTNAME)
	for j in i:
		if mydictofw.get(listofchar) == None:
			mydictofw[listofchar] = []
		mydictofw[listofchar].append(j)
		listofcharlist = list(listofchar)
		listofcharlist.append(j)
		listofcharlist.pop(0)
		listofchar = tuple(listofcharlist)
	if mydictofw.get(listofchar) == None:
		mydictofw[listofchar] = []
	mydictofw[listofchar].append(None)


def randomname():
	listofchar = tuple(STARTNAME)
	w = ""
	while True:
		j = choice(mydictofw[listofchar])
		if j == None:
			break
		else:
			w += j
		listofcharlist = list(listofchar)
		listofcharlist.append(j)
		listofcharlist.pop(0)
		listofchar = tuple(listofcharlist)

	return w

def manynames(n):
	i = 0
	listofnames = set()
	while i<n:
		a = randomname()
		if len(a)>4 and len(a)<11 and not a in listofnames:
			i += 1
			listofnames.add(a)
	return list(listofnames)


