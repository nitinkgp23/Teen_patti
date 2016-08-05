num = int(input("Enter number of players "))
dict={}
for i in range(1,num+1):
	dict.update({i:input("Enter name of player "+str(i))})
for x in dict.items():
	print (x)
